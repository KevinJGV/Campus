def leerValProducto():
    while True:
        try:
            n = int(input("Ingrese el valor del producto: "))
            if n < 0:
                print("Valor del producto Invalido")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor del producto.")

def leerCanProducto():
    while True:
        try:
            n = int(input("Ingrese la cantidad de productos existentes en bodega: "))
            if n < 0:
                print("Cantidad inválida")
                continue
            return n
        except ValueError:
            print("Error al ingresar cantidad.")

def leerNombreProducto():
    while True:
        try:
            nom = input("Ingrese el nombre del Producto:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el Nombre.", e)

def leerIDProducto():
    while True:
        try:
            n = int(input("Ingrese el ID del producto: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")

def buscarProducto(lstProducto, idProducto):
    for i in range(len(lstProducto)):
        if (lstProducto[i][0] == idProducto):
            return i
    return -1

def agregarProducto(lstProducto):
    print("\n\n*** 1. Agregar Producto\n")
    lstDatos = []
    id = leerIDProducto()
    lstDatos.append(id)
    lstDatos.append(leerNombreProducto())
    lstDatos.append(leerValProducto())
    lstDatos.append(leerCanProducto()) 
    lstProducto.append(lstDatos)   



def modificarProducto(lstProducto):
    print("\n\n2. Modificar Producto\n")

     
    idProducto = leerIDProducto()
    posProducto = buscarProducto(lstProducto, idProducto)
    if posProducto == -1:
        print("El código del producto no existe.")
        input()
        return
    
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Precio\n3. Cantidad de Productos en bodega\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break     
     
    if op == 1:
        nombre = leerNombreProducto()
        lstProducto[posProducto][1] = nombre
    elif op == 2:
        valorProducto = leerValProducto()
        lstProducto[posProducto][2] = valorProducto
    elif op == 3:
        canProducto = leerCanProducto()
        lstProducto[posProducto][3] = canProducto       

def eliminarProducto(lstProducto):
    pos = buscarProducto(lstProducto, leerIDProducto())
    if pos != -1:
        lstProducto.pop(pos)
        print("Producto Eliminado")
    else:
        print("El producto fue eliminado")

def listarProductos(lstProducto):
    bandera8 = 0
    while True:
        jabon = len(lstProducto)
        if jabon <= 5:
            for m in range(jabon):
                print(lstProducto[m])
            input()
            break
        elif jabon > 5:
            for l in range(5):
                if bandera8 < jabon:
                    print(lstProducto[bandera8])
                    bandera8 += 1
                else:
                    print("No hay mas producto.")
                    break
            bandera12 = input("Desea continuar? (S//N)")
            if  bandera12.lower() != "s":
                break   

# def  exitProducto(lstProducto): 
#        while True:
#            try:
#                produc = input(lstProducto)
#                break
#            except Exception:
        
#             return produc       
                


# def estrategiaMercadeo(lstProducto):
#     for i in range (0, N+1 ):
#         for j in range (i+1, N):
#             if lstProducto[i] > lstProducto[j]:
#                 t = lstProducto[i]
#                 lstProducto[i] = lstProducto[j]
#                 lstProducto[j] = t
#     return lstProducto            
    
       






def menu():
    while True:
        try:
            print("***PRODUCTOS ACME***")
            print("1. Agregar Producto ")
            print("2. Modificar Producto")
            print("3. Eliminar Producto")
            print("4. Listar Varios Productos")
            print("5. Estrategia de Mercadeo")
            print("6. Salir")
        
            op = int(input("Opcion (1-6): "))
            if op <1 or op > 6:
                print("Opcion invalida. Escoja de 1 a 6")
                input("Presione cualquier tecla para continuar...")
                continue
            return op 
        except ValueError:
            print("Opcion invalida. Escoja de 1 a ")
            input("Presione cualquier tecla para continuar... ")





#PROGRAMA PRINCIPAL
lstProducto = []
while True:
    op = menu()
    if op == 1:
        agregarProducto(lstProducto)
        print(lstProducto)
        input()
    elif op == 2:
        modificarProducto(lstProducto)
    elif op == 3:
        eliminarProducto(lstProducto)
    elif op == 4:
        listarProductos(lstProducto)
    elif op == 5:
        pass
    elif op == 6:
        print("\n\nGracias . Adios")

        # N = lstProducto 
        # productos = []
        # for i in range [N]:
        #     pro = exitProducto("Producto: ")
        #     lstProducto.append(pro)
        # print("Lista Productos: ")
        # lstProducto = estrategiaMercadeo
        # print("Lista Ordenada")