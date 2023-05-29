import os
from importlib import import_module

class Modeltype:
    """
    Model class
    """
    def __init__(self, name:str):
        self.name = name
        #check if exist
        if not os.path.isfile(os.path.join(os.path.dirname(__file__), name + ".py")):
            print(os.path.join(os.path.dirname(__file__), name + ".py"))
            raise FileNotFoundError("Model file not found")

    def potential(self, phi):
        imported = import_module("src.model." + self.name)
        return imported.potential(phi)
    
    def nabla_potential(self, phi):
        imported = import_module("src.model." + self.name)
        return imported.nabla_potential(phi)
    
    def hubble(self, phi, phi_t):
        imported = import_module("src.model." + self.name)
        return imported.hubble(phi, phi_t)
