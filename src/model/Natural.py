"""
Natural Model
"""


import numpy as np

f = 1
V0 = 1e-11

def potential(phi):
    return V0*(1+np.cos(phi/f))

def nabla_potential(phi):
    return -V0/f*np.sin(phi/f)

def hubble(phi, phi_t):
    return np.sqrt( 1 / 3 * (potential(phi)  + 1/2 * phi_t**2 ) )