from servicio import Servicio


class ReservaSala(Servicio):

    def __init__(self, codigo, nombre, valor_hora):
        super().__init__(codigo, nombre)
        self.valor_hora = valor_hora

    def calcular_costo(self, horas=1):
        return self.valor_hora * horas

    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}"