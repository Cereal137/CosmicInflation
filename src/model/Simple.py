"""
Simple Model
"""


import numpy as np

m = 1e-11

def potential(phi):
    return 0.5*m**2*phi**2

def nabla_potential(phi):
    return m**2*phi

def hubble(phi, phi_t):
    return np.sqrt( 1 / 3 * (potential(phi)  + 1/2 * phi_t**2 ) )