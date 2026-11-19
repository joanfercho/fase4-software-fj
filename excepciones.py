class ErrorSistema(Exception):  # Clase base: todas las excepciones del sistema heredan de aquí
    """Excepción base del sistema."""  
    pass  


class ClienteInvalidoError(ErrorSistema):  # Se lanza cuando los datos de un cliente no son válidos
    """Datos de cliente inválidos (identificación, nombre o correo)."""  
    pass  


class ServicioNoDisponibleError(ErrorSistema):  # Se lanza cuando se intenta usar un servicio que no está disponible
    """El servicio solicitado no está disponible."""  
    pass  


class ReservaError(ErrorSistema):  # Se lanza cuando una operación sobre una reserva no es permitida
    """Operación no permitida sobre una reserva."""  
    pass  


class ServicioInvalidoError(ErrorSistema):  # NUEVA: se lanza cuando los parámetros de un servicio son inválidos
    """Parámetros de servicio inválidos (código, nombre, tarifa o valores del costo)."""  
    pass  


class DuracionInvalidaError(ReservaError):  # NUEVA: hereda de ReservaError porque la duración pertenece a la reserva
    """La duración de la reserva no es válida (menor o igual a cero, o no numérica)."""  
    pass  