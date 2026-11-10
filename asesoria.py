from servicio import Servicio


class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, nombre, tarifa):
        super().__init__(codigo, nombre)
        self.tarifa = tarifa

    def calcular_costo(self, horas=1):
        return self.tarifa * horas

    def describir_servicio(self):
        return f"Asesoría especializada: {self.nombre}"