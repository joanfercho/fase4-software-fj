from datetime import datetime


def registrar_log(mensaje):

    with open("logs/eventos.log", "a", encoding="utf-8") as archivo:
        archivo.write(
            f"[{datetime.now()}] {mensaje}\n"
        )