from cliente import Cliente
from servicios.sala import ReservaSala
from reserva import Reserva

try:

    cliente = Cliente(
        "12345678",
        "Joan Prieto",
        "joan@gmail.com"
    )

    sala = ReservaSala(
        "S01",
        "Sala Principal",
        50000
    )

    reserva = Reserva(
        cliente,
        sala,
        3
    )

    reserva.confirmar()

    costo = reserva.procesar()

    print("Costo total:", costo)

except Exception as e:
    print("Error:", e)