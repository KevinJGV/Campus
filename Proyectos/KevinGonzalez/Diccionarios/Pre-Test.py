def leerCantProduc():
    while True:
        try:
            n = int(
                input("Ingrese cantidad (existencias disponibles) del Producto: "))
            return n
        except ValueError:
            print("Error al ingresar cantidad del producto.")


def leerPrecioProduc():
    while True:
        try:
            n = int(input("Ingrese precio del producto: "))
            return n
        except ValueError:
            print("Error al ingresar precio.")


def leerNombreProduc():
    while True:
        try:
            nom = input("Ingrese el nombre del Producto:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)


def leeridProd():
    while True:
        try:
            n = int(input("Ingrese el ID del Producto: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")


def buscarProducto(dicProductos, idProd):
    # return dicProductos.get(idProd) != None
    return idProd in dicProductos


def mnubuscarProducto(dicProductos):
    try:
        print("\n\n3. Buscar Producto\n")
        idProd = leeridProd()
        existProduc = buscarProducto(dicProductos, idProd)
        if existProduc == False:
            print("El Producto con ese código no ha sido ingresado.")
            input()
            return
    except ValueError:
        print("Error de ingreso.")

    print("\n", "=" * 30)
    print("Nombre:", dicProductos[idProd]["nombre"])
    print("Precio:", dicProductos[idProd]["Precio"])
    print("Cantidad disponible:", dicProductos[idProd]["CantProduc"])
    print(f"ValorTotal: ${dicProductos[idProd]['ValorTotal']:,.2f}")
    input("\n Presione cualquier tecla para volver al menu...")


def modificarProducto(dicProductos):
    try:
        print("\n\n2. Modificar Producto\n")
        idProd = leeridProd()
        existProd = buscarProducto(dicProductos, idProd)
        if existProd == False:
            print("El código del Producto no existe.")
            input()
            return
    except ValueError:
        print("Error de ingreso.")
    print("\n")
    while True:
        try:
            opc = int(
                input("\n1. Nombre\n2. Precio\n3. Cantidad disponible\nOpcion? "))
            if opc < 1 or opc > 3:
                print("Opción inválida")
                input()
                continue
            break
        except ValueError:
            print("Error de ingreso.")
    if opc == 1:
        nombre = leerNombreProduc()
        dicProductos[idProd]["nombre"] = nombre
    elif opc == 2:
        Precio = leerPrecioProduc()
        dicProductos[idProd]["Precio"] = Precio

    elif opc == 3:
        valHora = leerCantProduc()
        dicProductos[idProd]["CantProduc"] = valHora

    dicProductos[idProd]["ValorTotal"] = dicProductos[idProd]["CantProduc"] * \
        dicProductos[idProd]["Precio"]


def agregarProducto(dicProductos):
    try:
        print("\n\n*** 1. Agregar Producto\n")
        dicDatos = {}
        id = leeridProd()
        if buscarProducto(dicProductos, id) == True:
            print("El id ya existe en la lista")
            input()
            return

        dicDatos["nombre"] = leerNombreProduc()
        dicDatos["Precio"] = leerPrecioProduc()
        dicDatos["CantProduc"] = leerCantProduc()
        dicDatos["ValorTotal"] = dicDatos["CantProduc"] * dicDatos["Precio"]
        dicProductos[id] = dicDatos
    except ValueError:
        print("Error de ingreso.")


def elimProducto(dicProductos):
    try:
        print("\n\n4. Eliminar Producto\n")
        idProd = leeridProd()
        if idProd in dicProductos:
            del dicProductos[idProd]
            print("Producto eliminado satisfactoriamente.")
        else:
            print("El producto con ese ID no existe en la lista.")
        input()
    except ValueError:
        print("Error de ingreso.")


def menu():
    while True:
        try:
            print("*** PRODUCTOS ACMEE ***".center(40))
            print("MENU".center(40))
            print("1. Agregar Producto")
            print("2. Modificar Producto")
            print("3. Buscar Producto")
            print("4. Eliminar Producto")
            print("5. Listar Productos")
            print("6. Salir")
            opc = int(input(">>> Opción (1-6)? "))
            if opc < 1 or opc > 6:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return opc
        except ValueError:
            print("Opción no válida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...")


# PROGRAMA PRINCIPAL
dicProductos = {}
while True:
    try:
        opc = menu()
        if opc == 1:
            agregarProducto(dicProductos)
            # print(dicProductos)
            # input()
        elif opc == 2:
            modificarProducto(dicProductos)
            # print(dicProductos)
            # input()
        elif opc == 3:
            mnubuscarProducto(dicProductos)
        elif opc == 4:
            elimProducto(dicProductos)
        elif opc == 5:
            pass
        elif opc == 6:
            print("\n\nGracias por usar el software. Adios")
            break
    except ValueError:
        print("Error de ingreso.")
