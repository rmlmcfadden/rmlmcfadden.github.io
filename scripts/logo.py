#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import os

data = np.genfromtxt(
    "2011-45886.dat", delimiter="\t", names=["time", "asymmetry", "asymmetry_error"]
)

fit = np.genfromtxt("2011-45886.fit", delimiter="\t", names=["time", "asymmetry"])

t_min = np.min(data["time"])
t_max = np.max(data["time"])

scale = 0.4

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

ax.set_xlabel("Time (s)", color="black")
ax.set_ylabel("Asymmetry", color="black")

ax.set_xlim(None, 13)
ax.set_ylim(None, None)

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

ax.set_axis_off()

fig.savefig("logo.png", dpi=900, transparent=True)

cmd = "convert logo.png -background none -resize 128x128 -density 128x128 favicon.ico"
os.system(cmd)

# plt.show()
