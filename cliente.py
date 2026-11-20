from entidad import Entidad
from excepciones import ClienteInvalidoError


class Cliente(Entidad):
    """Representa a un cliente y valida los datos usados para identificarlo."""

    def __init__(self, identificacion, nombre, correo):
        # Los setters realizan las validaciones al asignar cada atributo.
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    @property
    def identificacion(self):
        """Devuelve la identificación numérica del cliente."""
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor):
        # La identificación debe contener únicamente dígitos.
        if not str(valor).isdigit():
            raise ClienteInvalidoError(
                "La identificación debe contener solo números."
            )
        self.__identificacion = valor

    @property
    def nombre(self):
        """Devuelve el nombre del cliente."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        # Se eliminan los espacios externos al comprobar la longitud mínima.
        if len(valor.strip()) < 3:
            raise ClienteInvalidoError(
                "El nombre debe tener mínimo 3 caracteres."
            )
        self.__nombre = valor

    @property
    def correo(self):
        """Devuelve el correo electrónico del cliente."""
        return self.__correo

    @correo.setter
    def correo(self, valor):
        # La validación básica exige que el correo incluya el símbolo @.
        if "@" not in valor:
            raise ClienteInvalidoError(
                "Correo electrónico inválido."
            )
        self.__correo = valor

    def mostrar_info(self):
        """Retorna el nombre y el correo en un formato legible."""
        return f"{self.nombre} - {self.correo}"