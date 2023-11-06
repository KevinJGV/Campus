#Funcion ID con gestion de errores
def leerId():
    while True:
        try:
            id = int(input("Ingrese el ID del producto: "))
            if id < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return id
        except ValueError:
            print("Error al ingresar el ID.")

#Funcion para nombre del producto
def leerNomProducto():
    while True:
        try:
            nomProducto = input("Ingrese el nombre del producto: ")
            nomProducto = nomProducto.strip()
            if len(nomProducto) == 0 or nomProducto.isalnum() == False:
                print("Nombre del producto invalido ")
            return nomProducto
        except Exception as e:
            print("Error al ingresar el nombre del producto.", e)

# Funcion para ingresar la cantidad productos
def cantProducto():
    while True:
        try:
            cantPr = int(input("Ingrese la cantidad de productos: "))
            if cantPr < 1:
                print("Datos de cantidad de productos invalido. Debe ser mayor a cero.")
                continue
            return cantPr
        except ValueError:
            print("Error al ingresar cantidad de productos")

#Funcion para ingresar el valor del producto
def precProducto():
    while True:
        try:
            precPr = int(input("Ingrese el precio del producto: "))
            if precPr < 1:
                print("Datos de precio del producto invalido. Debe ser mayor a cero.")
                continue
            return precPr
        except ValueError:
            print("Error al ingresar el precio del producto")

# Funcion buscar producto
def buscarProducto(dicProducto, idProd):
    return idProd in dicProducto


def agregarProducto(dicProducto):
    print("\n\n1. Agregar Producto\n")
    dicDatos = {}
    id = leerId()
    if buscarProducto(dicProducto, id) == True:
        print("El id ya existe en la lista de productos")
        input()
        return
    
    dicDatos["nombre"] = leerNomProducto()
    dicDatos["cantidad"] = cantProducto()
    dicDatos["precio"] = precProducto()
    
    dicProducto[id] = dicDatos
    # print(id)



def modificarProducto(dicProducto):
    print("\n\n2. Modificar Producto\n")
    
    id = leerId()
    productoExist = buscarProducto(dicProducto, id)
    if productoExist == False:
        print("El ID del producto no existe.")
        input()
        return
    
    print("\n")
    while True:
        opcion = int(input("\n1. Nombre Producto\n2. Cantidad Producto\n3. Precio Producto\nElige una opción "))
        if opcion < 1 or opcion > 3:
            print("Opción inválida")
            input()
            continue
        break
    if opcion == 1:
        nombrePr = leerNomProducto()
        dicProducto[id]["nombre"] = nombrePr
    elif opcion == 2:
        cantPr = cantProducto()
        dicProducto[id]["cantidad"] = cantPr
        
    elif opcion == 3:
        precPr = precProducto()
        dicProducto[id]["precio"] = precPr
        
def eliminarProducto(dicProducto):
    print("\n\n3. Eliminar Producto\n")
    id = leerId()
    dicDatos = dicProducto
    productoExist = buscarProducto(dicProducto, id)
    if productoExist == False:
        print("El ID del producto no existe.")
        input()
        return
    del dicDatos[id]

def listarProducto(dicProducto):
    print("\n\n4. Listar Productos\n")
    dicDatos = dicProducto
    # id = leerId()
    # productoExist = buscarProducto(dicProducto, id)
    # print(productoExist)

    # dicProducto[id] = dicDatos
    # print(id)
    print(dicDatos)

    # for i in range(dicProducto.index):

    #     nombrePr = []
    #     dicProducto[id]["nombre"] = nombrePr
    input("\n Presione cualquier tecla para volver al menu...")

    
def estrategiaMercadeo():
    pass
    

def menu():
    while True:
        try:
            print("\n", "=" * 29)
            print("PRODUCTOS ACME")
            print("=" * 30)
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. Eliminar producto")
            print("4. Listar varios productos")
            print("5. Estrategia mercadeo")
            print("6. Salir")
            opcion = int(input("¿Opción [1, 6]? "))
            if opcion < 1 or opcion > 8:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return opcion
        except ValueError:
            print("Opción no válida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...")


# PROGRAMA PRINCIPAL
dicProducto= {}
while True:
    opcion = menu()
    if opcion == 1:
        agregarProducto(dicProducto)
        print(dicProducto.items())
        input()
    elif opcion == 2:
        modificarProducto(dicProducto)
        print(dicProducto)
        input()
    elif opcion == 3:
        eliminarProducto(dicProducto)
        print("Datos de empleado eliminados con exito")
        input()
    elif opcion == 4:
        listarProducto(dicProducto)
    elif opcion == 6:
        print("\n\nGracias por usar el software. Hasta luego!")
        break