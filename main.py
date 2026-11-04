from cliente import Cliente

clientes = []

while True:

    print("\n=== SOFTWARE FJ ===")
    print("1. Registrar cliente")
    print("2. Ver clientes")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        cliente = Cliente(
            identificacion,
            nombre,
            correo
        )

        clientes.append(cliente)

        print("Cliente registrado correctamente")

    elif opcion == "2":

        for cliente in clientes:
            print(
                cliente.identificacion,
                cliente.nombre,
                cliente.correo
            )

    elif opcion == "3":
        print("Hasta luego")
        break

    else:
        print("Opción inválida")