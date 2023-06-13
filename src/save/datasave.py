import os
import numpy as np
from ..ode import ode

class DataSave:
    def __init__(self, 
                 save_data=False, 
                 save_data_path=None, 
                 save_data_name=None, 
                 save_data_format=None,
                 ):
        self.save_data = save_data
        self.save_data_path = save_data_path
        self.save_data_name = save_data_name
        self.save_data_format = save_data_format

    def save(self, ODE: ode.ODE):
        if self.save_data:
            if self.save_data_format == "txt":
                self.save_txt(ODE)
            elif self.save_data_format == "csv":
                self.save_csv(ODE)
            elif self.save_data_format == "npy":
                self.save_npy(ODE)
            else:
                raise ValueError("save_data_format must be 'txt', 'csv' or 'npy'.")
            
    def save_txt(self, ODE: ode.ODE):
        if not os.path.exists(self.save_data_path):
            os.makedirs(self.save_data_path)
        self.save_data_name = self.save_data_name + str(format(ODE.y0,'.2e')) + "_" + str(format(ODE.y_t0,'.2e'))
        with open(os.path.join(self.save_data_path, self.save_data_name+".txt"), "w") as f:
            f.write("t,phi,phi_dot,phi_dot_dot\n")
            t = np.array(ODE.t)
            y = np.array(ODE.y)
            for i in range(len(ODE.t)):
                f.write(str(t[i])+" "+str(y[0][i])+" "+str(y[1][i])+" "+str(ODE.y[2][i])+"\n")
    
    def save_csv(self, ODE: ode.ODE):
        if not os.path.exists(self.save_data_path):
            os.makedirs(self.save_data_path)
        self.save_data_name = self.save_data_name + str(ODE.y0) + "_" + str(ODE.y_t0)
        with open(os.path.join(self.save_data_path, self.save_data_name+".csv"), "w") as f:
            f.write("t,phi,phi_dot,phi_dot_dot\n")
            t=np.array(ODE.t)
            y=np.array(ODE.y)
            for i in range(len(ODE.t)):
                f.write(str(t[i])+","+str(y[0][i])+","+str(y[1][i])+","+str(y[1][i])+"\n")

    def save_npy(self, ODE: ode.ODE):
        if not os.path.exists(self.save_data_path):
            os.makedirs(self.save_data_path)
        self.save_data_name = self.save_data_name + str(ODE.y0) + "_" + str(ODE.y_t0)
        t=np.array(ODE.t)
        y=np.array(ODE.y)
        np.save(os.path.join(self.save_data_path, self.save_data_name+".npy"), y)