import os
import configparser

#read configure file
config = configparser.ConfigParser()

config.read(os.path.join(os.path.dirname(__file__), "config.ini"))

#read model name
model_name = config["DEFAULT"]["model"]

#read initial value
y0 = float(config["DEFAULT"]["y0"])
y_t0 = float(config["DEFAULT"]["y_t0"])

#read step and maximum
step = float(config["ODE"]["step"])
maximum = float(config["ODE"]["maximum"])

#read plot option
show_potential = config["PLOT"].getboolean("show_potential")
show_phi = config["PLOT"].getboolean("show_phi")
show_phi_dot = config["PLOT"].getboolean("show_phi_dot")
show_phi_dot_dot = config["PLOT"].getboolean("show_phi_dot_dot")
Issave = config["PLOT"].getboolean("save")
Savepath = config["PLOT"]["save_path"]
#run
from src.ode import ode
from src.plot import show

ODE = ode.ODE(model_name, 
              y0, 
              y_t0, 
              step, 
              maximum)
ODE.solve()
show.show(ODE, 
          show_potential, 
          show_phi, 
          show_phi_dot, 
          show_phi_dot_dot, 
          Issave, 
          save_path=os.path.join(os.path.dirname(__file__),Savepath))
