import os
from datetime import datetime

# Ruta común utilizada para guardar los eventos registrados por la aplicación.
RUTA_LOG = "logs/eventos.log"


def registrar_log(mensaje):
    """Agrega un mensaje con fecha y hora al archivo de eventos."""

    # Crea el directorio de registros si todavía no existe.
    os.makedirs("logs", exist_ok=True)

    # Abre el archivo en modo anexar para conservar los registros anteriores.
    with open(RUTA_LOG, "a", encoding="utf-8") as archivo:
        # Guarda cada entrada con su marca temporal y el mensaje recibido.
        archivo.write(
            f"[{datetime.now()}] {mensaje}\n"
        )