"""
ACME 
MISMO EJERCICIO PERO CON DICTS  
"""
productosACME={}

def menu():
    """menu de la aplicacion"""
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. Eliminar producto")
            print("4. Listar vairos productos")
            print("5. Estrategia de mercadeo")
            print("6. Salir")
            op = int(input(">>> Opción (1-6)? "))
            if op < 1 or op > 6:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...")
def leerPrecio():
    while True:
        try:
            n = int(input("Ingrese el valor del producto en $COP: "))
            if n < 0:
                print("Valor no válido; debe ser mayor o igual a $000.")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor del producto.")

def leerCantidad():
    while True:
        try:
            n = int(input("Ingrese el numero de existencias del producto"))
            if n < 0:
                print("Número inválido, debe ser un numero entero positivo.")
                continue
            return n
        except ValueError:
            print("Error al ingresar la cantidad de productos.")

def leerNombre():
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

def leerID():
    while True:
        try:
            n = int(input("Ingrese el ID del producto: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")
            
def estrategia(productosACME):
    listado=listarProductos(productosACME)
    listPrecios=[]
    keys=list(productosACME.keys())
    for k in keys:
        listPrecios.append(productosACME[k]["precio"])
    listPrecios.sort()
    for k in keys:
        for e in listPrecios:
            if listPrecios[listPrecios.index(e)] == productosACME[k]["precio"]:
                print(listado[listado.index(productosACME[k])])           
def listarProductos(productosACME):
    listado=[]
    keys=list(productosACME.keys())
    listComplete=[]
    listF=[]
    for k in keys:
        listado.append(productosACME[k])
    return listado
def eliminarProducto(productosACME,id):
    try: 
        del productosACME[id]
        print(productosACME)
    except KeyError:
        print("El ID no existe.")
    input()
def buscarProducto(productosACME,id):
    producto=productosACME.get(id,-1)
    return producto
    
def modificarProducto(productosACME,id):
    print("\n\n2. Modificar Producto\n")
    
    producto = buscarProducto(productosACME, id)
    if producto == -1:
        print("El producto no ha sido registrado.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Precio del producto\n3. Número de existencias\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombre()
        productosACME[id]["nombre"] = nombre
    elif op == 2:
        precio = leerPrecio()
        productosACME[id]["precio"] = precio
    elif op == 3:
        cantidad = leerCantidad()
        productosACME[id]["cant"] = cantidad
    print(f"Se modificó el empleado {id} correctamente.\n{productosACME[id]}")
    
def agregarProducto(productosACME:dict):
    print("\n\n*** 1. Agregar producto\n")
    producto = {}
    id = leerID()
    if buscarProducto(productosACME, id) != -1:
        print("El id ya existe en la lista")
        input()
        return

    producto["nombre"]=leerNombre()
    producto["precio"]=leerPrecio()
    producto["cant"]=leerCantidad()
    productosACME[id]=producto
#PROGRAMA PRINCIPAL
while True:
    op = menu()
    if op == 1:
        agregarProducto(productosACME)
        input()
    elif op == 2:
        id=leerID()
        modificarProducto(productosACME,id)
        input()
    elif op == 3:
        id=leerID()
        rslt=eliminarProducto(productosACME,id)
        if rslt == -1:
            print("El usuario no se ha registrado. ")
        else:print(rslt)
        input()
    elif op == 4:
        print(listarProductos(productosACME))
        input()
    elif op == 5:
        estrategia(productosACME)
        input()
    elif op == 6:
        print("\n\nGracias por usar el software. Adios")
        break
