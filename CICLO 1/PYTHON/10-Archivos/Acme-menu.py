"""desarrollo de menu interactivo con las siguientes caracteristicas:
1. Agregar producto. Este opción permite agregar un producto al sistema. El producto consta de
un id, nombre, precio y cantidad (existencias en bodega)
2. Modificar producto. Esta opción permite modificar los datos de un producto ingresando el
código.
3. Eliminar producto. Esta opción permite modificar un producto a partir del código.
4. Estrategia de mercadeo. Esta opción ordena y lista ascendentemente por precio todos los
dic que hay en bodega y los muestre sus datos en pantalla. Se listan de a 5 dic
usando paginación.
5. Salir del sistema"""

# Funciones de validacion
def readNum(num):
    while True:
        try:
            n = int(input(num))
            if n < 1:
                print("Error: Ingreso invalido. Debe ser un numero de la lista.")
                input()
                print("\n", "=" * 30, "\n")
                continue
            return n
        except ValueError:
            print("Error: Ingreso invalido. Debe ser un numero.")
            input()
            print("\n", "=" * 30, "\n")


def readNumM(num):
    while True:
        try:
            n = int(input(num))
            if n < 1 or n > 3:
                print("Error: Ingreso invalido. Debe ser un numero de la lista.")
                input()
                print("\n", "=" * 30, "\n")
                continue
            return n
        except ValueError:
            print("Error: Ingreso invalido. Debe ser un numero.")
            input()
            print("\n", "=" * 30, "\n")

def readTitle(msj):
    while True:
        try:
            frase = input(msj)
            frase = frase.strip()
            if len(frase) == 0 or frase.isdigit() == True:
                print("Error: Entrada no válida, debe ser una cadena")
                input("Presiona cualquier tecla para continuar ... ")
                print("\n", "=" * 30, "\n")
                continue
            return frase
        except Exception as e:
            print(f"Error: Entrada no válida, debe ser una cadena\n{e}")
            input()
            print("\n", "=" * 30, "\n")

def readString(msj):
    while True:
        try:
            frase = input(msj)
            frase = frase.strip()
            if len(frase) == 0:
                print("Error: Entrada no válida, ingrese nuevamente")
                input("Presiona cualquier tecla para continuar ... ")
                print("\n", "=" * 30, "\n")
                continue
            return frase
        except Exception as e:
            print(f"Error: Entrada no válida, debe ser una cadena\n{e}")
            input()
            print("\n", "=" * 30, "\n")
def validarId(msj,dic):
    while True:
        try:
            id = input(msj)
            
            if not id.isalnum() or len(id) == 0:
                print("Ingrese un id válido.")
                continue
            
            if id in dic:
                print("El id ya existe.")
                continue
            return id
        
        except Exception as e:
            print(f"Ocurrió un error. {e}")
            input()
    



#Funcion del menu principal
def menu(dic):
    while True:
        print("●" * 40, "\nMenu Principal","●" * 40)
        print("\n1. Agregar Producto")
        print("2. Modificar Producto")
        print("3. Eliminar Producto")
        print("4. Estrategia de Mercadeo")
        print("5. Salir del Sistema\n")
        opcion = readNum("Ingrese una opcion: ")
        # Opcion para agregar producto
        if opcion == 1:
            add_product(dic)
        elif opcion == 2:
            modifyProduct(dic)
        elif opcion == 3:
            delete_product()
        elif opcion == 4:
            marketing_plan()
        else:
            print("Gracias por usar nuestro sistema!")
            input()
            return False
        



# Funcion para agregar producto
# def add_product():
#     dic = {}
#     cantidad_ingreso = readNum("Cuantos dic desea agregar en ésta operación? => ")
#     for i in range(cantidad_ingreso):
#         id = int(input("Ingrese el id del articulo => "))
#         nombre = input("Nombre del articulo => ")
#         precio = input("Precio del articulo => ")
#         cantidad = input("Cantidad del articulo => ")
        
#         dic[id] = {"nombre" : nombre, "precio" : precio, "cantidad" : cantidad}
        

def add_product(dic):
    cantidad_ingreso = readNum("Cuantos productos desea agregar en ésta operación? => ")
    for i in range(cantidad_ingreso):
        id = validarId("ID del producto => ", dic)
        nombre = input("Nombre del articulo => ")
        precio = input("Precio del articulo => ")
        cantidad = input("Cantidad del articulo => ")
        dic[id] = {"nombre" : nombre, "precio" : precio, "cantidad" : cantidad}
    return dic

def modifyName(identifier, dic, number):
    if number == 1:
        name = readTitle("Nuevo nombre: ")
        dic[identifier]["nombre"] = readString(name)
        return dic
    if number == 2:
        price = readNum("Nuevo precio: ")
        dic[identifier]["precio"] = price
        return dic
    if number == 3:
        quantity = readNum("Nueva cantidad: ")
        dic[identifier]["cantidad"] = quantity
        return dic

    
    


def modifyProduct(dic):
    while True:
        try:
            id = input("ID del articulo que va a modificar => ")
            
            if not id.isalnum() or len(id) == 0:
                print("Ingrese un id válido.")
                continue
            
            if id in dic:
                op = readNumM("Qué desea modificar?\n 1 - Modificar nombre del articulo\n 2 - Modificar precio del articulo\n 3 - Modificar cantidad del articulo")
                if op == 1:
                    modifyName(id, productos, op)
                    return False
                if op == 2:
                    modifyName(id, productos, op)
                    return False
                else:
                    modifyName(id, productos, 3)
                    return False
                
        except Exception as e:
            print(f"Ocurrió un error. {e}")
            input()


#             opc = int(
#                 input("\n1. Nombre\n2. Precio\n3. Cantidad disponible\nOpcion? "))
#             if opc < 1 or opc > 3:
#                 print("Opción inválida")
#                 input()
#                 continue
#             break
#         except ValueError:
#             print("Error de ingreso.")
#     if opc == 1:
#         nombre = leerNombreProduc()
#         dicdic[idProd]["nombre"] = nombre
#     elif opc == 2:
#         Precio = leerPrecioProduc()
#         dicdic[idProd]["Precio"] = Precio

#     elif opc == 3:
#         valHora = leerCantProduc()
#         dicdic[idProd]["CantProduc"] = valHora

#     dicdic[idProd]["ValorTotal"] = dicdic[idProd]["CantProduc"] * \
#         dicdic[idProd]["Precio"]

productos = {}

while True:
    menu(productos)
    break