#%%
import numpy as np
from matplotlib import pyplot as plt
from src.ode import ode
from src.plot import show
from src.save import datasave

logspace = [2,4,6,8,10,12,14]
for i in range(len(logspace)):
    y_t0 = 10**logspace[i]
    ODE = ode.ODE(Model='Simple', 
              y0=1e46, 
              y_t0=y_t0, 
              step=1e-37, 
              maximum=1e-33)
    ODE.solve()
    plt.plot(ODE.t,np.log10(ODE.y[1]))

plt.show()

# %%
