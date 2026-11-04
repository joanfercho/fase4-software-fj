from entidad import Entidad
from excepciones import ClienteInvalidoError


class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        if not str(valor).isdigit():
            raise ClienteInvalidoError(
                "La identificación debe contener solo números."
            )
        self.__identificacion = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor.strip()) < 3:
            raise ClienteInvalidoError(
                "El nombre debe tener mínimo 3 caracteres."
            )
        self.__nombre = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if "@" not in valor:
            raise ClienteInvalidoError(
                "Correo electrónico inválido."
            )
        self.__correo = valor

    def mostrar_info(self):
        return f"{self.nombre} - {self.correo}"