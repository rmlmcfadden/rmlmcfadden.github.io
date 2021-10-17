#!/usr/bin/python3

import numpy as np
from scipy.special import ellipeinc


# Demagnetization factor N/4π for an ellipsoid with semi-axes a, b, and c.
#
# J. A. Osborn.
# "Demagnetizing factors of the general ellipsoid".
# Phys. Rev. 67, 351 (1945).
# https://doi.org/10.1103/PhysRev.67.351
#
# General ellipsoid
# Equation (2.3) [a >= b >= c >= 0]
def N_ellipsoid(a, b, c):
    # Equation (2.4) - amplitude
    theta = np.arccos(c / a)
    # Equation (2.5)
    phi = np.arccos(b / a)
    # Equation (2.6) - modulus
    k = np.sin(phi) / np.sin(theta)
    alpha = np.arcsin(k)
    # convert to the notation used in SciPy
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ellipeinc.html
    m = np.power(k, 2)
    E = ellipeinc(theta, m)
    # Equation (2.3) - demagnetization factor for the general ellipsoid
    return (
        (np.cos(phi) * np.cos(theta))
        / (np.power(np.sin(theta), 3) * np.power(np.cos(alpha), 2))
        * (((np.sin(theta) * np.cos(phi)) / np.cos(theta)) - E)
    )
