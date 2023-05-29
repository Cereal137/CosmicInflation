import matplotlib.pyplot as plt
import numpy as np
import os
from ..model import model
from ..ode import ode


def show(ODE, show_potential=False, show_hubble=False,show_phi=False,show_phi_dot=False,show_phi_dot_dot=False, save=False, save_path="", savedpi=300):
    Model = ODE.Model
    y = ODE.y
    a_ln = ODE.a_ln
    t = ODE.t

    if show_potential:
        phi = np.linspace(min(y[0]), max(y[0]), 100)
        V = Model.potential(Model, phi)
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
        plt.plot(t,y[1], label="\dot{\phi}")
        plt.xlabel("Time")
        plt.ylabel("$\dot\phi$")
        plt.legend()
        plt.show()

    if show_phi_dot_dot:
        plt.plot(t,y[2], label="\ddot{\phi}")
        plt.xlabel("Time")
        plt.ylabel("$\dot\phi_t$")
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
            import shutil
            shutil.rmtree(save_path)
            print("Remove old figure in " + save_path)
            os.makedirs(save_path)
            plt.savefig(os.path.join(save_path, Model + ".png"), dpi = savedpi)
            print("Save figure to " + save_path)
    plt.show()
