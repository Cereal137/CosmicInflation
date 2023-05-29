import numpy as np
"""
parameters for Coleman-Weinberg model
"""
mu = 5  #determine the coupling strength
V0 = 1e71 #potential parameter

def potential(phi):
    return V0 * ((phi/mu)**4 * (np.log(phi/mu) - 1/4) +1/4)

def nabla_potential(phi):
    return 4 * V0 * (phi/mu)**3 * np.log(phi/mu) / mu

def hubble(phi, phi_t):
    return np.sqrt( 1 / 3 * (potential(phi)  + 1/2 * phi_t**2 ) )