from cliente import Cliente

clientes = []
reservas = []

while True:

    print("\n==================================")
    print("         SOFTWARE FJ")
    print("==================================")
    print("1. Registrar cliente")
    print("2. Listar clientes")
    print("3. Crear reserva")
    print("4. Consultar reservas")
    print("5. Procesar reserva")
    print("6. Cancelar reserva")
    print("7. Ver servicios")
    print("8. Salir")

    opcion = input("\nSeleccione una opción: ")

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

            print("\n✅ Cliente registrado correctamente")

        except Exception as e:
            print(f"\n❌ Error: {e}")

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

    elif opcion == "3":
        print("\nFunción pendiente: Crear reserva")

    elif opcion == "4":
        print("\nFunción pendiente: Consultar reservas")

    elif opcion == "5":
        print("\nFunción pendiente: Procesar reserva")

    elif opcion == "6":
        print("\nFunción pendiente: Cancelar reserva")

    elif opcion == "7":
        print("\n===== SERVICIOS =====")
        print("1. Reserva de Sala")
        print("2. Alquiler de Equipo")
        print("3. Asesoría Especializada")

    elif opcion == "8":
        print("\nGracias por utilizar SOFTWARE FJ.")
        break

    else:
        print("\n❌ Opción inválida.")