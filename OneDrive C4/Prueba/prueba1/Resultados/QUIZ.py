def leerValHoraEmpl():
    while True:
        try:
            n = int(input("Ingrese el valor del producto: "))
            if n < 1000 or n > 150000:
                print("Valor de la Hora inválida. Debe estar en el rango de [1000, 150000]")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor del producto.")

def leerHoraTrabEmpl():
    while True:
        try:
            n = int(input("Ingrese la cantidad del producto: "))
            if n < 1 or n > 160:
                print("Cantidad inválidas. Debe estar en el rango de [1, 160]")
                continue
            return n
        except ValueError:
            print("Error al ingresar la cantidad del producto.")

def leerNombreEmpl():
    while True:
        try:
            nom = input("Ingrese el nombre del Producto:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalpha():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el producto.", e)

def leerIDEmpl():
    while True:
        try:
            n = int(input("Ingrese el ID del Producto: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")
            
def buscarEmpleado(bodega, idEmpl):
    for i in range(len(bodega)):
        if (bodega[i][0] == idEmpl):
            return i
    return -1

def eliminarProducto(bodega):
    eliminar = int(input("Que producto desea eliminar?:(1,2,3,4 o 5)"))
    if eliminar == 1:
        print("Producto eliminado correctamente")
        bodega.pop() 
        print(bodega)
    elif eliminar == 2:
        print("Producto eliminado correctamente")
        bodega.pop(1) 
        print(bodega)
    elif eliminar == 3:
        print("Producto eliminado correctamente")
        bodega.pop(2) 
        print(bodega)
    elif eliminar == 4:
        print("Producto eliminado correctamente")
        bodega.pop(3) 
        print(bodega)
    elif eliminar == 5:
        print("Producto eliminado correctamente")
        bodega.pop(4) 
        print(bodega)
    
def listaproductos(bodega):
    bodega.sort()
    print(bodega)
    

def listamayoramenor(bodega):
    lista=sorted(bodega)
    print(lista)
    

def modificarproducto(bodega):
    print("\n\n2. Modificar Producto\n")
    
    idEmpl = leerIDEmpl()
    posEmpl = buscarEmpleado(bodega, idEmpl)
    if posEmpl == -1:
        print("El código del producto no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Cantidad del producto\n3. Valor del producto\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreEmpl()
        bodega[posEmpl][1] = nombre
    elif op == 2:
        cantHoras = leerHoraTrabEmpl()
        bodega[posEmpl][2] = cantHoras
    elif op == 3:
        valHora = leerValHoraEmpl()
        bodega[posEmpl][3] = valHora

def agregarproducto(bodega):
    print("\n\n*** 1. Agregar empleado\n")
    lstDatos = []
    id = leerIDEmpl()
    if buscarEmpleado(bodega, id) != -1:
        print("El id ya existe en la lista")
        input()
        return
    
    lstDatos.append(id)
    lstDatos.append(leerNombreEmpl())
    lstDatos.append(leerHoraTrabEmpl())
    lstDatos.append(leerValHoraEmpl())
    
    bodega.append(lstDatos)

def menu():
    while True:
        try:
            print("*** PRODUCTOS ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. ELiminar producto")
            print("4. Listar varios productos")
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

## PROGRAMA PRINCIPAL
bodega= []
while True:
    op = menu()
    if op == 1:
        agregarproducto(bodega)
        print(bodega)
        input()
    elif op == 2:
        modificarproducto(bodega)
    elif op == 3:
        eliminarProducto(bodega)
    elif op == 4:
        listaproductos(bodega)
    elif op == 5:
        listamayoramenor(bodega)
    elif op == 6:
        print("\n\nGracias por usar el software. Adios")
        break