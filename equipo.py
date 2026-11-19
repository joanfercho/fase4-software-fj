from servicio import Servicio  # Clase abstracta de la que hereda este servicio


class AlquilerEquipo(Servicio):  # Servicio de alquiler de equipos, cobrado por día

    def __init__(self, codigo, nombre, valor_dia):  # Constructor: código, nombre y valor por día
        super().__init__(codigo, nombre)  # Inicializa y valida los datos comunes en la clase padre
        self.valor_dia = valor_dia  # Usa el setter, que valida la tarifa

    @property  # Permite leer el valor por día como si fuera un atributo
    def valor_dia(self):  # Getter del valor por día
        return self.__valor_dia  # Devuelve el atributo privado

    @valor_dia.setter  # Se ejecuta cada vez que se asigna el valor por día
    def valor_dia(self, valor):  # Setter del valor por día
        self.__valor_dia = self._validar_positivo(  # Guarda el valor solo si es válido
            valor, "El valor por día"  # Valor a validar y nombre del campo para el mensaje de error
        )

    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):  # Costo del alquiler según los días
        cantidad = self._validar_positivo(cantidad, "La cantidad de días")  # Los días deben ser mayores que 0
        subtotal = self.valor_dia * cantidad  # Subtotal: valor por día por número de días
        return self._aplicar_ajustes(subtotal, impuesto, descuento)  # Aplica descuento e impuesto opcionales

    def describir_servicio(self):  # Descripción del servicio
        return f"Alquiler de equipo: {self.nombre}"  