#!/usr/bin/python3

import numpy as np


# Demagnetization factor N/4π for a rectangular prism with semi-axes a, b, and c.
#
# A. Aharoni.
# "Demagnetizing factors for rectangular ferromagnetic prisms".
# J. Appl. Phys. 83, 3422 (1998).
# https://doi.org/10.1063/1.367113
#
# Eq. (1) - see Fig. 1 for_abc coordinate system
# see also the online version of calculator
# http://www.magpar.net/static/magpar/doc/html/demagcalc.html
def N_prism(a, b, c):
    # the expression takes input as half of the semi-axes
    a = 0.5 * a
    b = 0.5 * b
    c = 0.5 * c
    # define some convenience terms
    a2 = a * a
    b2 = b * b
    c2 = c * c
    abc = a * b * c
    ab = a * b
    ac = a * c
    bc = b * c
    r_abc = np.sqrt(a2 + b2 + c2)
    r_ab = np.sqrt(a2 + b2)
    r_bc = np.sqrt(b2 + c2)
    r_ac = np.sqrt(a2 + c2)
    # compute the factor
    pi_N = (
        ((b2 - c2) / (2 * bc)) * np.log((r_abc - a) / (r_abc + a))
        + ((a2 - c2) / (2 * ac)) * np.log((r_abc - b) / (r_abc + b))
        + (b / (2 * c)) * np.log((r_ab + a) / (r_ab - a))
        + (a / (2 * c)) * np.log((r_ab + b) / (r_ab - b))
        + (c / (2 * a)) * np.log((r_bc - b) / (r_bc + b))
        + (c / (2 * b)) * np.log((r_ac - a) / (r_ac + a))
        + 2 * np.arctan2(ab, c * r_abc)
        + (a2 * a + b2 * b - 2 * c2 * c) / (3 * abc)
        + ((a2 + b2 - 2 * c2) / (3 * abc)) * r_abc
        + (c / ab) * (r_ac + r_bc)
        - (r_ab * r_ab * r_ab + r_bc * r_bc * r_bc + r_ac * r_ac * r_ac) / (3 * abc)
    )
    # divide out the factor of pi
    return pi_N / np.pi
