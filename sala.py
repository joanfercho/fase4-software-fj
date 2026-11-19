from servicio import Servicio  # Clase abstracta de la que hereda este servicio


class ReservaSala(Servicio):  # Servicio de reserva de salas, cobrado por hora

    def __init__(self, codigo, nombre, valor_hora):  # Constructor: código, nombre y valor por hora
        super().__init__(codigo, nombre)  # Inicializa y valida los datos comunes en la clase padre
        self.valor_hora = valor_hora  # Usa el setter, que valida la tarifa

    @property  # Permite leer el valor por hora como si fuera un atributo
    def valor_hora(self):  # Getter del valor por hora
        return self.__valor_hora  # Devuelve el atributo privado

    @valor_hora.setter  # Se ejecuta cada vez que se asigna el valor por hora
    def valor_hora(self, valor):  # Setter del valor por hora
        self.__valor_hora = self._validar_positivo(  # Guarda el valor solo si es válido
            valor, "El valor por hora"  # Valor a validar y nombre del campo para el mensaje de error
        )

    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):  # Costo de la sala según las horas reservadas
        cantidad = self._validar_positivo(cantidad, "La cantidad de horas")  # Las horas deben ser mayores que 0
        subtotal = self.valor_hora * cantidad  # Subtotal: valor por hora por número de horas
        return self._aplicar_ajustes(subtotal, impuesto, descuento)  # Aplica descuento e impuesto opcionales

    def describir_servicio(self):  # Descripción del servicio
        return f"Reserva de sala: {self.nombre}"  