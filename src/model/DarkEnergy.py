import numpy as np
"""parameters for DarkEnergy model"""
m = 1e-11 #potential parameter
Lambda = 1e71 #dark energy term

def potential(phi):
    return 1/2*m**2*phi**2 + Lambda

def nabla_potential(phi):
    return m**2*phi

def hubble(phi, phi_t):
    return np.sqrt( 1 / 3 * (potential(phi)  + 1/2 * phi_t**2 ) )