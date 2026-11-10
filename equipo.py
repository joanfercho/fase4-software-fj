from servicio import Servicio


class AlquilerEquipo(Servicio):

    def __init__(self, codigo, nombre, valor_dia):
        super().__init__(codigo, nombre)
        self.valor_dia = valor_dia

    def calcular_costo(self, dias=1):
        return self.valor_dia * dias

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}"