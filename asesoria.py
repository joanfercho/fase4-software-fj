from servicio import Servicio  # Clase abstracta de la que hereda este servicio


class AsesoriaEspecializada(Servicio):  # Servicio de asesoría, cobrado por hora

    def __init__(self, codigo, nombre, tarifa):  # Constructor: código, nombre y tarifa
        super().__init__(codigo, nombre)  # Inicializa y valida los datos comunes en la clase padre
        self.tarifa = tarifa  # Usa el setter, que valida la tarifa

    @property  # Permite leer la tarifa como si fuera un atributo
    def tarifa(self):  # Getter de la tarifa
        return self.__tarifa  # Devuelve el atributo privado

    @tarifa.setter  # Se ejecuta cada vez que se asigna la tarifa
    def tarifa(self, valor):  # Setter de la tarifa
        self.__tarifa = self._validar_positivo(  # Guarda el valor solo si es válido
            valor, "La tarifa"  # Valor a validar y nombre del campo para el mensaje de error
        )

    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):  # Costo de la asesoría según las horas
        cantidad = self._validar_positivo(cantidad, "La cantidad de horas")  # Las horas deben ser mayores que 0
        subtotal = self.tarifa * cantidad  # Subtotal: tarifa por número de horas
        return self._aplicar_ajustes(subtotal, impuesto, descuento)  # Aplica descuento e impuesto opcionales

    def describir_servicio(self):  # Descripción del servicio
        return f"Asesoría especializada: {self.nombre}" 