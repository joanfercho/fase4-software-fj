import math  # Permite comprobar que la duración no sea infinita ni NaN
from excepciones import ErrorSistema, ReservaError, DuracionInvalidaError  # Excepciones propias del sistema


class Reserva:  # Reserva que une un cliente, un servicio y una duración
    

    PENDIENTE = "Pendiente"  # Estado inicial de toda reserva
    CONFIRMADA = "Confirmada"  # La reserva fue confirmada antes de procesarse
    PROCESADA = "Procesada"  # La reserva ya se cobró (estado final)
    CANCELADA = "Cancelada"  # La reserva fue cancelada (estado final)

    def __init__(self, cliente, servicio, duracion):  # Constructor: cliente, servicio y duración
        if cliente is None:  # Una reserva no puede existir sin cliente
            raise ReservaError("La reserva necesita un cliente.")  # Error claro para el usuario
        if servicio is None:  # Una reserva no puede existir sin servicio
            raise ReservaError("La reserva necesita un servicio.")  # Error claro para el usuario
        self.duracion = duracion  # Usa el setter, que valida la duración
        servicio.verificar_disponibilidad()  # Lanza ServicioNoDisponibleError si no se puede reservar
        self.cliente = cliente  # Guarda el cliente de la reserva
        self.servicio = servicio  # Guarda el servicio reservado
        self.__estado = Reserva.PENDIENTE  # Toda reserva nueva empieza pendiente
        self.__intentos = 0  # Cuenta cuántas veces se intentó procesar la reserva

    @property  # Permite leer la duración como si fuera un atributo
    def duracion(self):  # Getter de la duración
        return self.__duracion  # Devuelve el atributo privado

    @duracion.setter  # Se ejecuta cada vez que se asigna la duración
    def duracion(self, valor):  # Setter de la duración
        es_numero = (  # Comprueba que el valor sea un número real y finito
            isinstance(valor, (int, float))  # Debe ser entero o decimal
            and not isinstance(valor, bool)  # True y False cuentan como int, se descartan
            and math.isfinite(valor)  # Se descartan infinito y NaN
        )
        if not es_numero or valor <= 0:  # Debe ser número y mayor que cero
            raise DuracionInvalidaError(  # Lanza la excepción propia de la duración
                "La duración debe ser un número mayor que 0."  # Mensaje claro para el usuario
            )
        self.__duracion = valor  # Guarda la duración ya validada

    @property  # Permite leer el estado como si fuera un atributo
    def estado(self):  # Getter del estado 
        return self.__estado  # Devuelve el atributo privado

    @property  # Permite leer los intentos como si fuera un atributo
    def intentos(self):  # Getter de los intentos de procesamiento
        return self.__intentos  # Devuelve el atributo privado

    def confirmar(self):  # Confirma una reserva pendiente
        if self.__estado != Reserva.PENDIENTE:  # Solo se confirma desde el estado pendiente
            raise ReservaError(  # Lanza la excepción propia de la reserva
                f"Solo se puede confirmar una reserva pendiente (estado actual: {self.__estado})."  # Indica el estado actual
            )
        self.__estado = Reserva.CONFIRMADA  # Pasa al estado confirmada

    def cancelar(self):  # Cancela una reserva que aún no se ha cobrado
        if self.__estado == Reserva.CANCELADA:  # No se puede cancelar dos veces
            raise ReservaError("La reserva ya está cancelada.")  # Error claro para el usuario
        if self.__estado == Reserva.PROCESADA:  # Una reserva cobrada no se puede cancelar
            raise ReservaError("No se puede cancelar una reserva ya procesada.")  # Error claro para el usuario
        self.__estado = Reserva.CANCELADA  # Pasa al estado cancelada

    def procesar(self):  # Calcula el costo y deja la reserva como procesada
        if self.__estado == Reserva.CANCELADA:  # Una reserva cancelada no se procesa
            raise ReservaError("No se puede procesar una reserva cancelada.")  # Error claro para el usuario
        if self.__estado == Reserva.PROCESADA:  # Una reserva ya procesada no se cobra dos veces
            raise ReservaError("La reserva ya fue procesada.")  # Error claro para el usuario
        try:  # Bloque donde pueden ocurrir errores del servicio
            self.servicio.verificar_disponibilidad()  # El servicio debe seguir disponible
            costo = self.servicio.calcular_costo(self.duracion)  # Calcula el costo según la duración
        except ErrorSistema as error:  # Errores conocidos del sistema (servicio inválido o no disponible)
            raise ReservaError(  # Encadenamiento: se lanza un error de reserva y se conserva el original
                f"No se pudo procesar la reserva: {error}"  # Mensaje que incluye la causa
            ) from error  # "from" guarda el error original como causa
        except Exception as error:  # Cualquier otro error inesperado
            raise ReservaError(  # Encadenamiento: se conserva el error original
                "Error inesperado al calcular el costo de la reserva."  # Mensaje genérico para el usuario
            ) from error  # "from" guarda el error original como causa
        else:  # Se ejecuta solo si el bloque try terminó sin errores
            self.__estado = Reserva.PROCESADA  # Marca la reserva como procesada
            return costo  # Devuelve el costo calculado
        finally:  # Se ejecuta siempre, haya o no errores
            self.__intentos += 1  # Cuenta el intento de procesamiento (exitoso o fallido)