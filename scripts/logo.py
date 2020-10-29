#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import os

# load the data/fit from an old 8Li -NMR SLR measurement in BTS
data = np.genfromtxt(
    "2011-45886.dat", delimiter="\t", names=["time", "asymmetry", "asymmetry_error"]
)
fit = np.genfromtxt("2011-45886.fit", delimiter="\t", names=["time", "asymmetry"])

t_min = np.min(data["time"])
t_max = np.max(data["time"])

# ad hoc scale factor for fine tuning the figure size
scale = 0.4

# create the figure
fig, ax = plt.subplots(
    1, 1, figsize=(3.0 * scale, 3.0 * scale), constrained_layout=True
)

# ax.axhline(0, linestyle="--", color="grey", zorder=1)
# ax.axvspan(0, 4, color="lightgrey", zorder=0)

ax.errorbar(
    data["time"],
    data["asymmetry"],
    yerr=data["asymmetry_error"],
    fmt="o",
    color="black",
    # markerfacecolor="lightgrey",
    zorder=2,
    label="data",
)

ax.plot(fit["time"], fit["asymmetry"], "-", color="magenta", zorder=3, label="fit")

# ax.set_xlabel("Time (s)", color="black")
# ax.set_ylabel("Asymmetry", color="black")

ax.set_xlim(None, 13)
ax.set_ylim(None, fit["asymmetry"][0])

# ax.set_title("rmlmcfadden.github.io")
# fig.suptitle("rmlmcfadden.github.io", color="purple")
"""
ax.text(
    0.975,
    0.975,
    "rmlmcfadden.github.io",
    ha="right",
    va="top",
    color="purple",
    transform=ax.transAxes,
)
"""

# make the axis completely invisible
# ax.set_axis_off()

# make the spines thicker
for axis in ["top", "bottom", "left", "right"]:
    ax.spines[axis].set_linewidth(3)

# make the axis spines invisible
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

# turn off the axes labels/ticks
ax.tick_params(
    axis="both",
    which="both",
    left=False,
    bottom=False,
    right=False,
    top=False,
    labelleft=False,
    labelbottom=False,
)

# save the figure as a high resolution transparent png
fig.savefig("logo.png", dpi=900, transparent=True)

# use imagemagick to create the favicon from the rendered image
cmd = "convert logo.png -background none -resize 128x128 -density 128x128 favicon.ico"
os.system(cmd)

# plt.show()
