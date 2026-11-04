import os
from datetime import datetime

RUTA_LOG = "logs/eventos.log"


def registrar_log(mensaje):

    os.makedirs("logs", exist_ok=True)

    with open(RUTA_LOG, "a", encoding="utf-8") as archivo:
        archivo.write(
            f"[{datetime.now()}] {mensaje}\n"
        )