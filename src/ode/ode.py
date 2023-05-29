import numpy as np
from ..model import model

class ODE:
    def __init__(self, Model:str, y0, y_t0, step, maximum):
        self.Model = Model
        self.step = step
        self.maximum = maximum
        self.max_iteration = maximum/step
        self.y0 = y0
        self.y_t0 = y_t0
        self.y = [[y0],[y_t0],[]] #y, y_t, y_tt
        self.a_ln  = [[1],[]] #ln(a)
        self.t = [0] #time epoch

    def solve(self):
        Model = model.Modeltype(self.Model)
        step = self.step
        maximum = self.maximum
        max_iteration = self.max_iteration

        i = 0
        while ( Model.potential(self.y[0][i]) > 0.5* self.y[1][i]**2 and i < max_iteration):
            self.y[2].append( -Model.nabla_potential(self.y[0][i]) -3 * Model.hubble(self.y[0][i], self.y[1][i]) * self.y[1][i])
            self.y[1].append( self.y[1][i] + self.y[2][i]*step )
            self.y[0].append( self.y[0][i] + self.y[1][i]*step )
            self.t.append(self.t[i] + step)

            self.a_ln[1].append( Model.hubble(self.y[0][i], self.y[1][i]) )
            self.a_ln[0].append( self.a_ln[0][i] + self.a_ln[1][i]*step )
            i += 1
        
        self.y[2].append( -Model.nabla_potential(self.y[0][i]) -3 * Model.hubble(self.y[0][i], self.y[1][i]) * self.y[1][i])
        self.a_ln[1].append( Model.hubble(self.y[0][i], self.y[1][i]) )

        return self
    