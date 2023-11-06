def leerCantProd():
    while True:
        try:
            n = int(input("Ingrese la cantidad del producto: "))
            if n < 0 or n == "":
                print("Cantidad invalida. por favor ingrese un valor mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor de la hora trabajada.")

def leerPrecProd():
    while True:
        try:
            n = int(input("Ingrese el precio del producto: "))
            if n < 0 or n == "":
                print("Valor de la precio inválido.")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor de la hora trabajada.")

def leerNombreProd():
    while True:
        try:
            nom = input("Ingrese el nombre del producto:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerIDProd():
    while True:
        try:
            n = int(input("Ingrese el ID del producto: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")

def buscarProducto(dicProductos, idProd):
    # return dicEmpleados.get(idEmpl) != None
    return idProd in dicProductos

def agregarProducto(dicProductos):  

    print("\n\n*** 1. Agregar producto ***\n")
    dicDatosProd = {}
    id = leerIDProd()
    if buscarProducto(dicProductos, id) == True:
        print("El id ya existe en la lista")
        input()
        return
    
    dicDatosProd["nombre"] = leerNombreProd()
    dicDatosProd["precio"] = leerPrecProd()
    dicDatosProd["cantidad"] = leerCantProd()

    
    dicProductos[id] = dicDatosProd

def modificarProducto(dicProductos):
    print("\n\n2. Modificar Producto\n")
    
    idProd = leerIDProd()
    existProd = buscarProducto(dicProductos, idProd)
    if existProd == False:
        print("El código del Producto no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Precio del producto\n3. Cantidad del producto\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreProd()
        dicProductos[idProd]["nombre"] = nombre
    elif op == 2:
        precio = leerPrecProd()
        dicProductos[idProd]["precio"] = precio
        
    elif op == 3:
        cantidad = leerCantProd()
        dicProductos[idProd]["cantidad"] = cantidad

def eliminarProducto(dicProductos): 
    print("\n\n2. Eliminar Producto\n")
    
    idProd = leerIDProd()  
    existProd = buscarProducto(dicProductos, idProd)
    if existProd == False:
        print("El código del empleado no existe.")
        input()
        return 
    
    del dicProductos[idProd]

def listaProductos(dicProductos): 
    for k , v in dicProductos.items(): 
        print(f"Codigo: {k} Nombre: {v['nombre']} Precio: {v['precio']:,.0f} Cantidad: {v['cantidad']}")
        return

def estratMerc(dicProductos):
    
    listaOrdenada = []

    for k , v in dicProductos.items():
        listaOrdenada.append(v["precio"])

    listaOrdenada.sort()

    for i in listaOrdenada:
        for key, value in dicProductos.items():
                id = key
                dicNuevoDatosProd = {}
                dicNuevoDatosProd["nombre"] = value["nombre"]
                dicNuevoDatosProd["precio"] = value["precio"]
                dicNuevoDatosProd["cantidad"] = value["cantidad"]

                dicProductosOrdenados[id] = dicNuevoDatosProd

def paginacion(dicProductosOrdenados):
    contador = 0
    for k, v in dicProductosOrdenados.items():
        print(f"Codigo: {k} Nombre: {v['nombre']} Precio: {v['precio']:,.0f} Cantidad: {v['cantidad']}")
        contador += 1
        if contador == 5:
            continuar = input("Desea ver los proximos 5 productos (S/N)?")
            input()
            if continuar.lower == "s":
                continue
            elif continuar.lower == "n":
                break



def menu ():  
    while True: 
        try: 
            print("\n*****PRODUCTOS ACME MENU******\n")  
            print("1. Agreagar un producto") 
            print("2. Modificar producto") 
            print("3. Eliminar producto") 
            print("4. Listar varios productos") 
            print("5. Estrategia de mercadeo")
            print("6. Salir") 
            op = int(input(">>>>>> Opcion (1-6): ")) 
            if op <1 or op > 6: 
                print("Opcion no valida. Escoja de 1 a 6. ")  
                input("Presione cualquier tecla para continuar: ")
                continue 
            return op 
        except ValueError:  
            print("Opcion no valida. Escoja de (1-6)") 
            input("Presione cualquier tecla para continuar: ")  

dicProductos = {}
dicProductosOrdenados = {}

while True:
    op = menu()
    if op == 1:
        agregarProducto(dicProductos)
        # print(dicEmpleados)
        # input()
    elif op == 2:
        modificarProducto(dicProductos)
        # print(dicEmpleados)
        # input()
    elif op == 3:
        eliminarProducto(dicProductos)
    elif op == 4:
        listaProductos(dicProductos)
    elif op == 5:
        estratMerc(dicProductos)
    elif op == 6: 
        print("\n\nGracias por usar el software. Adios")
        break