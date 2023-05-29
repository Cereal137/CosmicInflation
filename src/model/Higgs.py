import numpy as np
"""parameters for Higgs model"""
V0 = 1e-120 #potential parameter
mu = 1
def potential(phi):
    return V0 * (1-(phi/mu)**2)**2

def nabla_potential(phi):
    return -4 * V0 * phi * (1-(phi/mu)**2)

def hubble(phi, phi_t):
    return np.sqrt( 1 / 3 * (potential(phi)  + 1/2 * phi_t**2 ) )