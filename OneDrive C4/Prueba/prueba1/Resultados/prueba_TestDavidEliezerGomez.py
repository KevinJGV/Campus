#FUNCIONES HA UTILIZAR 

#ESTA FUNCION LEE EL NOMBRE DEL PRODUCTO
def leerNmProducto():
    while True:
        try:
            nom = input("Ingrese el nombre del producto:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el prodcuto nuevamente.", e)

#fUNCION LEE EL ID DEL PRODUCTO Y LO VERIFICA ASI MISMO 
def IDproducto():
    while True:
        try:
            n = int(input("Ingrese el ID del producto: "))
            if n <= 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")


#LEE EL VALOR DEL PRODUCTO SI NO ES NEGATIVO O ALGO POR EL ESTILO

def valProducto():
    while True:
        try:
            n = int(input("Ingrese el valor del Producto: "))
            if n < -1:
                print("Valor del producto invalido")
                continue
            return n
        except ValueError:
            print("Error al valor del producto")

#ESTA AÑADE LA CANTIDAD DE CADA PRODUCTO
def cantidadProducto():
    while True:
        try:
            n = int(input("Ingrese la Cantidad de Productos por Kilo: "))
            if n < -1:
                print("cantidad del producto invalida")
                continue
            return n
        except ValueError:
            print("Error digitar cantidad  del producto")

def buscarProducto(lstProductos, IDproducto):
    for i in range(len(lstProductos)):
        if (lstProductos[i][0] == IDproducto):
            return i
    return -1

def eliminarProducto(lstProductos):
    eliminar = int(input("Que ID desea remover de la lista"))
    if eliminar == IDproducto:
        b = lstProductos.sort(IDproducto)
    elif eliminar != IDproducto:
        b = print("id no encontrado")
    return b

#ME PERMITE BUSCAR EL PRODUCTO

def modificaProducto(lstProductos):
    print("\n\n2. Modificar Empleado\n")
    
    IDprod= IDproducto()
    posProducto = buscarProducto(lstProductos, IDprod)
    if posProducto == -1:
        print("El código del producto  no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Cantidad de productos\n3. Valor del producto\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
        
    if op == 1:
        nombre =  leerNmProducto()
        lstProductos[posProducto][1] = nombre
    elif op == 2:
        cantProducto = cantidadProducto()
        lstProductos[posProducto][2] = cantProducto
    elif op == 3:
        valproducto = valProducto()
        lstProductos[posProducto][3] = valproducto



def agregarProducto(lstProductos):
    print("\n\n*** 1. Agregar Producto\n")
    lstPro= []
    id = IDproducto()
    if buscarProducto(lstProductos, id) != -1:
        print("El id ya existe en la lista")
        input()
        return 
    lstPro.append(id)
    lstPro.append(leerNmProducto())
    lstPro.append(cantidadProducto())
    lstPro.append(valProducto())
    
    lstProductos.append(lstPro)
    


#MENU PRINCIPAL


def menu():
    while True:
        try:
            print("*** PRODUCTOS ***".center(40))
            print("MENU".center(40))
            print("1. Agregar producto ")
            print("2. Modificar producto ")
            print("3. Eliminar Producto ")
            print("4. Listar varios productos ")
            print("5. Estrategia del mercado")
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


#PROGRAMA PRINCIPAL 
lstProductos= []
while True:
    op = menu()
    if op == 1:
        agregarProducto(lstProductos)
        print(lstProductos)
        input()

    elif op == 2:
        modificaProducto(lstProductos)
    elif op == 3:
        eliminarProducto(lstProductos)
        
    elif op == 4:
       
        listarProducto = []
        lstProductos.append(listarProducto)
        print("=" * 30 )
        print("lista de los productos")
        print("=" * 30 )
        po = int(input("ingrese la cantidad de productos que desea listar"))
        for i in range(0,po):
            print("\n", lstProductos[i])

        
    elif op == 6:
        print("\n\nGracias por usar el software. Adios")
        break