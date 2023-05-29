import matplotlib.pyplot as plt
import numpy as np
import os
from ..model import model
from ..ode import ode


def show(ODE, show_potential=False, show_phi=False,show_phi_dot=False,show_phi_dot_dot=False, show_energy=False, save=False, save_path="", savedpi=300):
    Model = model.Modeltype(ODE.Model)
    y = np.array(ODE.y)
    a_ln = ODE.a_ln
    t = ODE.t

    if show_potential:
        phi = np.linspace(0, ODE.y0 , 100)
        V = Model.potential(phi)
        plt.plot(phi, V, label="Potential")
        plt.xlabel("$\phi$")
        plt.ylabel("V($\phi$)")
        plt.legend()
        plt.show()

    if show_phi:
        plt.plot(t,y[0], label="$\phi$")
        plt.xlabel("Time")
        plt.ylabel("$\phi$")
        plt.legend()
        plt.show()

    if show_phi_dot:
        plt.plot(t,y[1], label="$\dot{\phi}$")
        plt.xlabel("Time")
        plt.ylabel("$\dot\phi$")
        plt.legend()
        plt.show()

    if show_phi_dot_dot:
        plt.plot(t,y[2], label="$\dot{\phi_t}$")
        plt.xlabel("Time")
        plt.ylabel("$\dot\phi_t$")
        plt.legend()
        plt.show()

    if show_energy:
        plt.plot(t, y[1]**2/2 ,color='b' ,label="Kinetic Energy")
        plt.plot(t, Model.potential(y[0]),color='r', label="Potential Energy")
        plt.xlabel("Time")
        plt.ylabel("Energy")
        plt.legend()
        plt.show()

    plt.plot(t, a_ln[0], label="Inflation")
    plt.xlabel("Time")
    plt.ylabel("$ln(a)$")
    plt.legend()
    if save:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            plt.savefig(os.path.join(save_path, Model + ".png"), dpi = savedpi)
            print("Save figure to " + save_path)
        else:
            if not os.path.exists(os.path.join(save_path, ODE.Model + ".png")):
                plt.savefig(os.path.join(save_path, ODE.Model + ".png"), dpi = savedpi)
                print("Save figure to " + save_path)
            else:
                os.remove(os.path.join(save_path, ODE.Model + ".png"))
                print("Remove old figure in " + save_path)
                plt.savefig(os.path.join(save_path, ODE.Model + ".png"), dpi = savedpi)
                print("Save figure to " + save_path)
    plt.show()
