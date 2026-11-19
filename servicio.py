import math  # Permite comprobar que un número no sea infinito ni NaN
from abc import ABC, abstractmethod  # Herramientas para crear clases abstractas
from excepciones import ServicioInvalidoError, ServicioNoDisponibleError  # Excepciones propias del sistema


class Servicio(ABC):  # Clase abstracta: define lo que deben tener todos los servicios  

    def __init__(self, codigo, nombre):  # Constructor: recibe código y nombre del servicio
        self.codigo = codigo  
        self.nombre = nombre  
        self.disponible = True  

    @property  # Permite leer el código como si fuera un atributo
    def codigo(self):  # Getter del código
        return self.__codigo  # Devuelve el atributo privado

    @codigo.setter  # Se ejecuta cada vez que se asigna un código
    def codigo(self, valor):  # Setter del código
        if not isinstance(valor, str) or not valor.strip():  # Debe ser texto y no estar vacío
            raise ServicioInvalidoError(  # Lanza la excepción propia del servicio
                "El código del servicio no debe estar vacío."  # Mensaje claro para el usuario
            )
        self.__codigo = valor.strip()  # Guarda el código sin espacios sobrantes

    @property  # Permite leer el nombre como si fuera un atributo
    def nombre(self):  # Getter del nombre
        return self.__nombre  # Devuelve el atributo privado

    @nombre.setter  # Se ejecuta cada vez que se asigna un nombre
    def nombre(self, valor):  # Setter del nombre
        if not isinstance(valor, str) or not valor.strip():  # Debe ser texto y no estar vacío
            raise ServicioInvalidoError(  # Lanza la excepción propia del servicio
                "El nombre del servicio no debe estar vacío."  # Mensaje claro para el usuario
            )
        self.__nombre = valor.strip()  # Guarda el nombre sin espacios sobrantes

    @property  # Permite leer si el servicio está disponible
    def disponible(self):  # Getter de disponibilidad
        return self.__disponible  # Devuelve el atributo privado

    @disponible.setter  # Se ejecuta cada vez que se cambia la disponibilidad
    def disponible(self, valor):  # Setter de disponibilidad
        if not isinstance(valor, bool):  # Solo se acepta True o False
            raise ServicioInvalidoError(  # Lanza la excepción propia del servicio
                "La disponibilidad debe ser True o False."  # Mensaje claro para el usuario
            )
        self.__disponible = valor  # Guarda el nuevo estado

    def verificar_disponibilidad(self):  # Comprueba que el servicio se pueda reservar
        if not self.disponible:  # Si el servicio no está disponible
            raise ServicioNoDisponibleError(  # Lanza la excepción de servicio no disponible
                f"El servicio '{self.nombre}' no está disponible."  # Mensaje con el nombre del servicio
            )

    @staticmethod  # No necesita acceso al objeto, solo recibe datos
    def _es_numero(valor):  # Indica si el valor es un número real y finito
        return (  # Devuelve True solo si se cumplen las tres condiciones
            isinstance(valor, (int, float))  # Debe ser entero o decimal
            and not isinstance(valor, bool)  # True y False cuentan como int en Python, se descartan
            and math.isfinite(valor)  # Se descartan infinito y NaN
        )

    @staticmethod  # No necesita acceso al objeto, solo recibe datos
    def _validar_positivo(valor, campo):  # Valida que un número sea mayor que 0
        if not Servicio._es_numero(valor) or valor <= 0:  # Debe ser número y mayor que cero
            raise ServicioInvalidoError(  # Lanza la excepción propia del servicio
                f"{campo} debe ser un número mayor que 0."  # Mensaje que indica qué campo falló
            )
        return valor  # Devuelve el valor ya validado

    @staticmethod  # No necesita acceso al objeto, solo recibe datos
    def _validar_porcentaje(valor, campo):  # Valida que un porcentaje esté entre 0 y 100
        if not Servicio._es_numero(valor) or not 0 <= valor <= 100:  # Debe ser número entre 0 y 100
            raise ServicioInvalidoError(  # Lanza la excepción propia del servicio
                f"{campo} debe ser un número entre 0 y 100."  # Mensaje que indica qué campo falló
            )
        return valor  # Devuelve el valor ya validado

    def _aplicar_ajustes(self, subtotal, impuesto, descuento):  # Aplica descuento e impuesto al subtotal
        descuento = self._validar_porcentaje(descuento, "El descuento")  # Valida el descuento (0 a 100)
        impuesto = self._validar_porcentaje(impuesto, "El impuesto")  # Valida el impuesto (0 a 100)
        con_descuento = subtotal * (1 - descuento / 100)  # Primero se resta el descuento
        total = round(con_descuento * (1 + impuesto / 100), 2)  # Luego se suma el impuesto y se redondea
        return int(total) if total == int(total) else total  # Si no hay decimales, devuelve un entero

    @abstractmethod  # Obliga a las clases hijas a implementar este método
    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):  # Cálculo del costo con parámetros opcionales
        pass  # Cada servicio define su propia fórmula

    @abstractmethod  # Obliga a las clases hijas a implementar este método
    def describir_servicio(self):  # Descripción del servicio en texto
        pass  # Cada servicio define su propia descripción