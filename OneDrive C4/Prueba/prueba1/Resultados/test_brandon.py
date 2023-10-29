def agregarProducto():  
    print(f"\n", "=" * 25, "\n")
    print("\n1. DATOS PRODUCTO") 
    datProducto = {} 
    datProducto['id']= leerId("ID: ") 
    datProducto['nombre'] = leerNombre("Nombre: ")
    datProducto['precio'] =  leerPrecio("Precio: ")
    datProducto['cantidad'] = leerCantidad("Cantidad: ")
    print(f"\n", "=" * 25, "\n")

    lstProductos.append(datProducto)


def leerId(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 1 or num == "":
                print("Numero invalido digite de nuevo")
                continue
            return num
        except ValueError:
            print("Error al ingresar el número.")
            input("Presione cualquier tecla para continuar...")

def leerNombre(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip("")
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e) 

def leerPrecio(msj):
    while True:
        try:
            num = float(input(msj))
            if num < 0 or num == "":
                print("Precio Invalido.")
                continue
            return num
        except ValueError:
            print("Error al ingresar el número.")
            input("Presione cualquier tecla para continuar...")  

def leerCantidad(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 0 or num == "":
                print("Cantidad Invalida.")
                continue
            return num
        except ValueError:
            print("Error al ingresar el número.")
            input("Presione cualquier tecla para continuar...") 

def buscarProducto(lstProductos , idProd):
    for i in range(len(lstProductos)): 
        if(lstProductos[i]['id'] == idProd): 
            return i 
    return -1

def eliminarProducto(pos):  
    lstProductos.remove(lstProductos[pos]) 
    print("El Producto ha sido eliminado")

def modificarProducto(lstProductos): 
    print("\n2. Modificar Producto\n") 
    idProd = leerId("ID: ") 
    posProd = buscarProducto(lstProductos , idProd) 
    if posProd == -1:
        print("El ID del Producto no existe.")
        input()
        return 

    print("\n") 
    while True:
        try:
            op = int(input("\n1. Nombre\n2. Precio\n3. Cantidad\nOpcion: "))
            if op < 1 or op > 3:
                print("Opción inválida")
                input()
                continue
            break 
        except ValueError: 
            print("Error al digitar la opcion...")

    
    if op == 1: 
        print(f"\n", "=" * 25, "\n")
        nombre = leerNombre("Nombre:") 
        lstProductos[posProd]['nombre'] = nombre

    elif op == 2: 
        print(f"\n", "=" * 25, "\n")
        precio = leerPrecio("Precio: ") 
        lstProductos[posProd['precio']] = precio

    elif op == 3: 
        print(f"\n", "=" * 25, "\n")
        cantidad = leerCantidad("Cantidad: ")
        lstProductos[posProd]['cantidad'] = cantidad  

        

def imprimirProductos(lst): 

   for i in range(len(lst)): 
        print(f"Nombre: {lst[i]['nombre']}\n Id: {lst[i]['id']}\n Precio: {lst[i]['precio']}\n Cantidad: {lst[i]['cantidad']}") 


def menu ():  
    while True: 
        try: 
            print(f"\n", "=" * 25, "\n")
            print("===_PRODUCTOS ACME_===")
            print("")
            print("1. Agreagar un Producto") 
            print("2. Modificar Producto") 
            print("3. Eliminar Producto") 
            print("4. Listar Varios Productos") 
            print("5. Estrategia de Mercadeo")
            print("6. Salir")
            print(f"\n", "=" * 25, "\n")
            op = int(input(">>>>>> Opcion (1-6): ")) 
            if op <1 or op > 6: 
                print("Opcion no valida. Escoja de 1 a 6.")  
                input("Presione cualquier tecla para continuar: ")
                continue 
            return op  
        except ValueError:  
            print("Opcion no valida. Escoja de (1-8 )") 
            input("Presione cualquier tecla para continuar: ")  


lstProductos = []

while True:  

    opcion = menu() 

    if opcion == 1:  
        agregarProducto()
        print("Producto agregado con exito")
        
    if opcion == 2:  
        modificarProducto(lstProductos) 

    if opcion == 3: 
        identificacion = leerId("Id: ")    
        eliminarProducto(buscarProducto(lstProductos , identificacion))

    if opcion == 4:  
        imprimirProductos(lstProductos) 

    if opcion == 6:
        print("Muchas gracias por usar el software")
        break 