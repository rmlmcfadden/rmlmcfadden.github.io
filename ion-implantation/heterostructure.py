#!/usr/bin/python3

import os
import numpy as np
import matplotlib.pyplot as plt
from srim import TRIM, Ion, Layer, Target
from srim.output import Results, Range


# desired implantation energies (eV)
Energy_eV = 1e3 * np.array([1.0, 3.0, 5.0, 7.0])

# number of simulated ions
N_Ions = 1e3

# mass of the implanted ion 8Li (amu)
m_8Li = 8.02248625

# specify the directory of SRIM.exe
# for Windows users the path will be of the form "C://..."
srim_executable_directory = "/path/to/srim-2013"

# create a heterostructure consisting of n_repetitions of alternating layers of
# the perovskites LaNiO3 and LaAlO3
# these have the (approximate) cubic lattice constants:
a_LaNiO3 = 3.857
a_LaAlO3 = 3.787

# use an empty list to hold each layer
layers = []

# number of layer repetitions
n_repetions = 3

# loop over the repetions to create the heterostructure!
for i in range(n_repetions):

    # 2 unit cell thick lanthanum nickelate layer
    LaNiO3 = Layer(
        {
            "La": {"stoich": 1.0},
            "Ni": {"stoich": 1.0},
            "O": {"stoich": 3.0},
        },
        density=7.11,
        width=2 * a_LaNiO3,
        name="LaNiO3(%d)" % i,
    )
    layers.append(LaNiO3)

    # 5 unit cell thick lanthanum aluminate layer
    LaAlO3 = Layer(
        {
            "La": {"stoich": 1.0},
            "Al": {"stoich": 1.0},
            "O": {"stoich": 3.0},
        },
        density=6.52,
        width=5 * a_LaAlO3,
        name="LaAlO3(%d)" % i,
    )
    layers.append(LaAlO3)

# use a 0.5 mm sapphire layer as the bottom "substrate"
Al2O3 = Layer(
    {
        "Al": {"stoich": 2.0},
        "O": {"stoich": 3.0},
    },
    density=3.95,
    width=50000.0,
    name="Al2O3",
)
layers.append(Al2O3)


# construct the mulitlayer target using the layers list
target = Target(layers)

# loop over implantation energies
for E_eV in Energy_eV:

    # Construct the implanted 8Li ion
    ion = Ion("Li", energy=E_eV, mass=m_8Li)

    # Initialize a TRIM calculation with the ion & target
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

    # run the TRIM calculation
    # - this may take a few seconds to start (especially using wine)
    # - if all went well, a TRIM window will pop up!
    results = trim.run(srim_executable_directory)

    # move all the results for each implantation energy to a new directory
    output_directory = "results/%.0f_eV" % E_eV
    os.makedirs(output_directory, exist_ok=True)
    TRIM.copy_output_files(srim_executable_directory, output_directory)
