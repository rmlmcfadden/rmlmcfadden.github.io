#!/usr/bin/python3

import os
import numpy as np
import matplotlib.pyplot as plt
from srim import TRIM, Ion, Layer, Target
from srim.output import Results, Range


# implantation energies (eV)
Energy_eV = 1e3 * np.array([1.0, 3.0, 5.0, 7.0])

# simulated ions
N_Ions = 1e3

# mass of 8Li (amu)
m_8Li = 8.02248625

# Specify the directory of SRIM.exe
# For windows users the path will include C://...
srim_executable_directory = "/home/rmlm/software/srim-2013"

# create a heterostructure consisting of alternating layers of LaNiO3 and LaAlO3
layers = []
for i in range(3):
    # 2 u.c. lanthanum nickelate layer
    LaNiO3 = Layer(
        {"La": {"stoich": 1.0}, "Ni": {"stoich": 1.0}, "O": {"stoich": 3.0},},
        density=7.11,
        width=2 * 3.857,
        name="LaNiO3(%d)" % i,
    )
    layers.append(LaNiO3)

    # 4 u.c. lanthanum aluminate layer
    LaAlO3 = Layer(
        {"La": {"stoich": 1.0}, "Al": {"stoich": 1.0}, "O": {"stoich": 3.0},},
        density=6.52,
        width=4 * 3.787,
        name="LaAlO3(%d)" % i,
    )
    layers.append(LaAlO3)

# 0.5 mm sapphire substrate
Al2O3 = Layer(
    {"Al": {"stoich": 2.0}, "O": {"stoich": 3.0},},
    density=3.95,
    width=50000.0,
    name="Al2O3",
)
layers.append(Al2O3)
# print(layers)

# loop over implantation energies
for E_eV in Energy_eV:
    # Construct a the implanted 8Li ion
    ion = Ion("Li", energy=E_eV, mass=m_8Li)

    # Construct a target of a single layer of Nickel
    target = Target(layers)

    # Initialize a TRIM calculation with given target and ion
    trim = TRIM(
        target,
        ion,
        calculation=2,
        number_ions=N_Ions,
        description="%.0f eV 8Li implanted in heterostructure" % E_eV,
        # reminders="",
        # autosave=1000,
        plot_mode=5,
        # plot_xmin=0,
        # plot_xmax=0,
        ranges=True,
        backscattered=True,
        transmit=True,
        sputtered=True,
        collisions=True,
        angle_ions=0,
    )

    # run the trim calculation (my take a few seconds to start)
    # if all went well, a TRIM window will pop up!
    results = trim.run(srim_executable_directory)

    # move all the results to a new directory
    output_directory = "results/heterostructure/%.0f_eV" % E_eV
    os.makedirs(output_directory, exist_ok=True)
    TRIM.copy_output_files(srim_executable_directory, output_directory)
