#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from iminuit import Minuit
from iminuit.cost import LeastSquares
from bdata import bdata, life
from bfit import pulsed_strexp
import json
import os


# year/run numbers for a subset of the 8Li SLR data in a LaNiO3 single crystal
# see also: https://doi.org/10.1103/PhysRevB.100.165109
year = 2017
runs = np.concatenate(
    [
        range(40774, 40787 + 1),
        range(40789, 40802 + 1),
    ]
)
runs = np.arange(40774, 40780)

# empty dictionary for holding fit parameter initial guess
# (to be passed to the minimizer later)
initial_params = dict()

# empty list for each chi2 calculation
# (to be used to calculate the "global" chi2 later)
chi2_list = []

# add some binning to the data (to speed up the minimization)
BINNING = 20

# loop over each run in the runs list
for run in runs:
    # read data
    data = bdata(run, year)

    # calculcate asymmetry
    time, asymmetry, asymmetry_error = data.asym("c", rebin=BINNING)

    # find values w/ non-zero error
    has_nonzero_error = asymmetry_error > 0.0

    # create a generic pulsed stretched exponential functor
    pse = pulsed_strexp(life.Li8, data.pulse_s)

    # dynamically create a pulsed stretched exponential functor with run-specific parameter names
    # see e.g., https://stackoverflow.com/a/11291851
    fcn_txt = "def pse_run(x, lambda_s%d, beta%d, amp):\n" % (
        run,
        run,
    ) + "\treturn pse(x, lambda_s%d, beta%d, amp)" % (run, run)
    exec(fcn_txt)

    # create the run-specific chi2 object
    lsq = LeastSquares(
        time[has_nonzero_error],
        asymmetry[has_nonzero_error],
        asymmetry_error[has_nonzero_error],
        pse_run,
        verbose=1,  # optionally print minimization "steps" to terminal (default=0)
    )

    # append chi2 object to the list
    chi2_list.append(lsq)

    # create an initial guess for each fit parameter dynamically
    initial_params["amp"] = 0.1
    initial_params["lambda_s%d" % run] = 0.25
    initial_params["beta%d" % run] = 0.5


# calculate the "global" chi2 automagically
global_chi2 = sum(chi2_list)

# get the previous fit result (if it exists!)
OLD_FIT_RESULTS_EXIST = os.path.isfile("fit_results.json")
OLD_FIT_RESULTS_EXIST = False
if OLD_FIT_RESULTS_EXIST:
	# open them
	with open("fit_results.json", "r") as fh:
		# and put them in a dictionary!
		old_fit_results = json.load(fh)
		# overwrite the inital_params dictionary w/ the old fit results!
		# initial_params = old_fit_results["values"]
		for key, value in old_fit_results["values"].items():
			initial_params[key] = value


# set up the MINUIT2 minimizer
m = Minuit(
    global_chi2,
    **initial_params,  # see e.g., https://stackoverflow.com/a/21986301
)

# add some constraints to the run-specific fit parameters
for run in runs:
    m.limits["beta%d" % run] = (0, 1)
    m.limits["lambda_s%d" % run] = (0, None)


# give better error estimate using previous fit results
if OLD_FIT_RESULTS_EXIST:
	for key, value in old_fit_results["errors"].items():
		m.errors[key] = value

# do the fitting!
m.migrad()
m.hesse()
# m.minos()

# print the fit results to the terminal
print(m)
# print(m.covariance.to_table())

# save the fit results to a json file to be read from later
results_dict = {
	"values": m.values.to_dict(),
	"errors": m.errors.to_dict(),
	"covariance": m.covariance.to_table(),
}

with open("fit_results.json", "w") as fh:
	json.dump(results_dict, fh, indent="\t")
	# json.dump(results_dict, fh)


# plot the results
fig, ax = plt.subplots(1, 1, figsize=(4.8, 6.4), constrained_layout=True)

# maximum time range we wish to plot
TIME_RANGE = 12.0

# maximum operating temperature
MAX_TEMPERATURE = 320.0

# import a colormap (for "fancy" plotting)
# https://matplotlib.org/tutorials/colors/colormaps.html
cmap = matplotlib.cm.get_cmap("rainbow")

# create a list of runs sorted by temperature
sorted_runs = sorted(runs, key=lambda run: bdata(run, year).camp.smpl_read_A.mean)

# loop over every run
for run in sorted_runs:
    # read data
    data = bdata(run, year)
    # calculcate asymmetry
    time, asymmetry, asymmetry_error = data.asym("c", rebin=BINNING)
    # only plot data within the desired time range
    # (for better auto-deduced axes limis)
    is_within_range = time <= TIME_RANGE
    # extract one of the temperature readings
    temperature = data.camp.smpl_read_A.mean

    # plot the SLR data
    ax.errorbar(
        time[is_within_range],
        asymmetry[is_within_range],
        yerr=asymmetry_error[is_within_range],
        fmt="o",
        color=cmap(temperature / MAX_TEMPERATURE),
        zorder=2,
        label="%.1f K" % data.camp.smpl_read_A.mean,
    )

    # create the stretched exponential SLR functor
    pse = pulsed_strexp(life.Li8, data.pulse_s)
    # create some "dummy" time points
    t = np.linspace(0.001, TIME_RANGE)
    # "package" the correct run-specific fit parameters
    par = (m.values["lambda_s%d" % run], m.values["beta%d" % run], m.values["amp"])

    # plot the fit
    ax.plot(
        t,
        pse(t, *par),
        "-",
        color="black",
        zorder=3,
    )


# refine some of the plot's aesthetics
ax.axvspan(0.0, 4.0, color="lightgrey", zorder=0)
ax.axhline(0.0, linestyle=":", color="grey", zorder=1)
ax.set_xlim(0, TIME_RANGE)
ax.set_ylim(None, None)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Asymmetry")

# create the legend
ax.legend(
    title="$^{8}$Li SLR in LaNiO$_{3}$ @ 6.55 T:",
    bbox_to_anchor=(0.5, 1.025),
    loc="lower center",
    ncol=4,
    frameon=False,
    fontsize="small",
)

# display the plot
plt.show(block=True)
