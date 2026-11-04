from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass