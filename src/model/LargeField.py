import numpy as np
"""
parameters for large-field model
y0 = 1e47  40
y_t0 can be free
V0= = 1e-118 -90
p = 4  can be a good choice
y0 = 1e30
y_t0 = -1e6 can be the best choice
V0 = 1e-50
p = 4
"""
V0 = 1e-50 #potential parameter
p = 4 #power of the potential

def potential(phi):
    return V0 * phi**p

def nabla_potential(phi):
    return p * V0 * phi**(p-1)

def hubble(phi, phi_t):
    return np.sqrt( 1 / 3 * (potential(phi)  + 1/2 * phi_t**2 ) )