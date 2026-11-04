from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):

        if self.estado == "Cancelada":
            raise ReservaError(
                "No se puede procesar una reserva cancelada."
            )

        costo = self.servicio.calcular_costo(self.duracion)

        self.estado = "Procesada"

        return costo