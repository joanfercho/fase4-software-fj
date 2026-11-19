
# Descripción: Punto de entrada principal del sistema SOFTWARE FJ: gestiona el menú de clientes y reservas.

from cliente import Cliente
from sala import ReservaSala
from equipo import AlquilerEquipo
from asesoria import AsesoriaEspecializada
from reserva import Reserva
from logger import registrar_log

# Datos almacenados durante la ejecución del programa.
clientes = []
reservas = []

# Catálogo de servicios disponibles para crear reservas.
servicios = [
    ReservaSala("S01", "Sala de Reuniones", 50000),
    AlquilerEquipo("E01", "Video Beam", 30000),
    AsesoriaEspecializada("A01", "Consultoría TI", 80000)
]

# Ciclo principal que mantiene activo el menú hasta elegir "Salir".
while True:

    # Encabezado y opciones principales del menú.
    print("\n==================================")
    print("         SOFTWARE FJ")
    print("==================================")
    print("1. Registrar cliente")
    print("2. Listar clientes")
    print("3. Crear reserva")
    print("4. Consultar reservas")
    print("5. Procesar reserva")
    print("6. Cancelar reserva")  
    print("7. Salir")

    opcion = input("\nSeleccione una opción: ")

    # Registrar un nuevo cliente y guardar la operación en el log.
    if opcion == "1":

        try:
            identificacion = input("Identificación: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")

            cliente = Cliente(
                identificacion,
                nombre,
                correo
            )

            clientes.append(cliente)
            registrar_log(
                f"Cliente registrado: {cliente.nombre}"
            )

            print("\n✅ Cliente registrado correctamente")

        except Exception as e:
            registrar_log(
                f"Error al registrar cliente: {e}"
            )
            
            print(f"\n❌ Error: {e}")

    # Mostrar todos los clientes registrados.
    elif opcion == "2":

        if not clientes:
            print("\nNo hay clientes registrados.")
        else:
            print("\n===== CLIENTES =====")

            for i, cliente in enumerate(clientes, start=1):
                print(
                    f"{i}. {cliente.identificacion} - "
                    f"{cliente.nombre} - "
                    f"{cliente.correo}"
                )

    # Crear una reserva seleccionando un cliente y un servicio.
    elif opcion == "3":
        try:
            if not clientes:
                print("\nNo existen clientes registrados.")
                continue

            print("\n===== CLIENTES =====")

            for i, cliente in enumerate(clientes):
                print(f"{i+1}. {cliente.nombre}")

            indice_cliente = int(
                input("Seleccione cliente: ")
            ) - 1

            cliente = clientes[indice_cliente]

            print("\n===== SERVICIOS =====")

            for i, servicio in enumerate(servicios):
                print(
                    f"{i+1}. {servicio.describir_servicio()}"
                )

            indice_servicio = int(
                input("Seleccione servicio: ")
            ) - 1

            servicio = servicios[indice_servicio]

            duracion = int(
                input("Ingrese duración: ")
            )

            reserva = Reserva(
                cliente,
                servicio,
                duracion
            )

            reservas.append(reserva)

            registrar_log(
                f"Reserva creada para {cliente.nombre}"
            )

            print("\n✅ Reserva registrada.")

        except Exception as e:
            registrar_log(
                f"Error al crear reserva: {e}"
            )

            print(f"\n❌ {e}")

    # Consultar el estado y los datos de las reservas existentes.
    elif opcion == "4":

        if not reservas:

            print("\nNo existen reservas.")

        else:

            print("\n===== RESERVAS =====")

            for i, reserva in enumerate(reservas):

                print(
                    f"{i+1}. "
                    f"{reserva.cliente.nombre} | "
                    f"{reserva.servicio.nombre} | "
                    f"{reserva.estado}"
                )

    # Procesar una reserva seleccionada y calcular su costo.
    elif opcion == "5":

        try:

            if not reservas:

                print("\nNo existen reservas.")
                continue

            for i, reserva in enumerate(reservas):

                print(
                    f"{i+1}. "
                    f"{reserva.cliente.nombre} - "
                    f"{reserva.estado}"
                )

            indice = int(
                input("Seleccione reserva: ")
            ) - 1

            costo = reservas[indice].procesar()

            registrar_log(
                f"Reserva procesada. Valor: {costo}"
            )

            print(
                f"\n✅ Reserva procesada."
            )

            print(
                f"Costo total: ${costo:,}"
            )

        except Exception as e:

            registrar_log(
                f"Error procesando reserva: {e}"
            )

            print(f"\n❌ {e}")

    # Cancelar una reserva seleccionada.
    elif opcion == "6":

        try:

            if not reservas:

                print("\nNo existen reservas.")
                continue

            for i, reserva in enumerate(reservas):

                print(
                    f"{i+1}. "
                    f"{reserva.cliente.nombre} - "
                    f"{reserva.estado}"
                )

            indice = int(
                input("Seleccione reserva: ")
            ) - 1

            reservas[indice].cancelar()
            registrar_log(
                f"Reserva cancelada por {reservas[indice].cliente.nombre}"
            )

            registrar_log(
                "Reserva cancelada"
            )

            print(
                "\n✅ Reserva cancelada."
            )

        except Exception as e:

            registrar_log(
                f"Error cancelando reserva: {e}"
            )

            print(f"\n❌ {e}")

    

    # Finalizar la ejecución del programa.
    elif opcion == "7":
        print("\nGracias por utilizar SOFTWARE FJ.")
        break

    # Informar cuando el usuario ingresa una opción no válida.
    else:
        print("\n❌ Opción inválida.")
