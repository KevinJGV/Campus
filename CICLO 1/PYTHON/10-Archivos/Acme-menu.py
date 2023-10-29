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


def readNumAbort(num):
    while True:
        try:
            n = int(input(num))
            return n
        except ValueError:
            print("Error: Ingreso invalido. Debe ser un numero.")
            input()

def readNum(num):
    while True:
        try:
            n = int(input(num))
            if n < 1:
                print("Error: Ingreso invalido.")
                input()
                continue
            return n
        except ValueError:
            print("Error: Ingreso invalido. Debe ser un numero.")
            input()
def readNumM1(num):
    while True:
        try:
            n = int(input(num))
            if n < 1 or n > 5:
                print("Error: Ingreso invalido. Debe ser un numero de la lista.")
                input()
                continue
            return n
        except ValueError:
            print("Error: Ingreso invalido. Debe ser un numero.")
            input()



def readNumM2(num):
    while True:
        try:
            n = int(input(num))
            if n == (1,2,3):
                return n
            else:
                n = 0
                return n
        except ValueError:
            print("Error: Ingreso invalido. Intentelo nuevamente.")
            input()


def readString(msj):
    while True:
        try:
            frase = input(msj)
            frase = frase.strip()
            if len(frase) == 0:
                print("Error: Entrada no válida, ingrese nuevamente")
                input()
                continue
            return frase
        except Exception as e:
            print(f"Error: Entrada no válida, debe ser una cadena\n{e}")
            input()


def yorn(msj):
    while True:
        op = input(msj)
        op = op.strip().lower()
        if len(op) == 0:
            print("Ingrese y ú n.")
            continue
        if op == "y":
            return op
        elif op == "n":
            return op
        else:
            print("Opcion incorrecta, intente de nuevo")
            input()
            continue


def validarAddId(msj,dic):
    while True:
        try:
            id = input(msj)
            id = id.strip()
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
            

def validarDelId(msj,dic):
    while True:
        try:
            id = input(msj)
            id = id.strip().lower()
            if id == "salir":
                return id
            if not id.isalnum() or len(id) == 0:
                print("Ingrese un id válido.")
                continue
            elif not id in dic:
                print("El id no existe.")
                continue
            elif id in dic:
                return id
        except Exception as e:
            print(f"Ocurrió un error. {e}")
            input()
    
def validarNombre(msj):
    while True:
        try:
            nombre = input(msj)
            nombre = nombre.strip()
            if len(nombre) == 0:
                print("Ingrese un nombre.")
                continue
            return nombre
        except Exception as e:
            print(f"Ocurrio un error.\n{e}")
            input()
            

def validarPrecio(msj):
    while True:
        try:
            Precio = input(msj)
            Precio = Precio.strip()
            if len(Precio) == 0:
                print("Ingrese un Precio.")
                input()
                continue
            if not Precio.isdigit():
                print("Solo se permiten valores numericos.")
                input()
                continue
            else:
                Precio = float(Precio)
                Precio = str(Precio)
                return Precio
        except Exception as e:
            print(f"Ocurrio un error.\n{e}")
            input()


def validarCant(msj):
    while True:
        try:
            Cant = input(msj)
            Cant = Cant.strip()
            if len(Cant) == 0:
                print("Ingrese una cantidad.")
                input()
                continue
            if not Cant.isdigit():
                print("Solo se permiten valores numericos.")
                input()
                continue
            return Cant
        except Exception as e:
            print(f"Ocurrio un error.\n{e}")
            input()


def verifyDel(dic,id, msj):
    while True:
        try:
            verificador = input(msj).lower().strip()
            if verificador == "borrar":
                dic = dic.pop(id)
                print(">>> Producto eliminado satisfactoriamente <<<")
                return dic
            else:
                print("Operacion abortada.")
                input()
                return False
        except Exception as e:
            print(f"Error inesperado > \"{e}\"\n////////////////// OPERACION ABORTADA //////////////////")
            return False

#Funcion del menu principal

def add_product(dic):
    print("●" * 10, "Registro de productos","●" * 10, "\n")
    cantidad_ingreso = readNumAbort("¿Cuantos productos desea agregar en ésta operación (Para abortar ingrese cero (0))? => ")
    for i in range(cantidad_ingreso):
        id = validarAddId("ID del producto => ", dic)
        nombre = validarNombre("Nombre del articulo => ")
        precio = validarPrecio("Precio del articulo => ")
        cantidad = validarCant("Cantidad del articulo => ")
        dic[id] = {"id" : id,"nombre" : nombre, "precio" : precio, "cantidad" : cantidad}
    return dic

def modifyData(identifier, dic, number):
    if number == 1:
        name = readString("Nuevo nombre: ")
        dic[identifier]["nombre"] = name
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
    print("●" * 10, "Modificación de productos","●" * 10)
    while True:
        try:
            id = input("ID del articulo que va a modificar => ")
            
            if not id.isalnum() or len(id) == 0:
                print("Ingrese un id válido.")
                continue
            
            if id in dic:
                print("=" * 35, "\nID ", dic[id]["id"], "\nNOMBRE ", dic[id]["nombre"], "\nPRECIO ", dic[id]["precio"], "\nCANTIDAD ", dic[id]["cantidad"], "\n" + "=" * 35)
                op = readNumM2("Qué desea modificar?\n 1 - Modificar nombre del articulo\n 2 - Modificar precio del articulo\n 3 - Modificar cantidad del articulo\nPara abortar ingrese cualquier otro valor numerico.\n\n>>> ")
                if op == 1:
                    modifyData(id, productos, op)
                    print("=" * 5,"REGISTRO MODIFICADO".center(20), "=" * 5,"\nID ", dic[id]["id"], "\nNOMBRE ", dic[id]["nombre"], "\nPRECIO ", dic[id]["precio"], "\nCANTIDAD ", dic[id]["cantidad"], "\n" + "=" * 35)
                    loop = yorn("¿Desea modificar más productos? y/n\n>>> ")
                    if loop == "y":
                        modifyProduct(dic)
                    else:
                        return False
                elif op == 2:
                    modifyData(id, productos, op)
                    loop = yorn("¿Desea modificar más productos?")
                    if loop == "y":
                        modifyProduct(dic)
                    else:
                        return False
                elif op == 3:
                    modifyData(id, productos, op)
                    loop = yorn("¿Desea modificar más productos?")
                    if loop == "y":
                        modifyProduct(dic)
                    else:
                        return False
                else:
                    return False
            else:
                print("No se encontró el ID ingresado.\n Intentelo nuevamente.")
                input()
        except Exception as e:
            print(f"Ocurrió un error. {e}")
            input()


def delete_product(dic):
    print("●" * 10, "Eiminacion de productos","●" * 10)
    while True:
        try:
            id = validarDelId("ID del articulo que desea eliminar (Para cancelar ingrese \"Salir\") => ", productos)
            if id == "salir":
                return False
            else:
                print("=" * 35, "\nID ", dic[id]["id"], "\nNOMBRE ", dic[id]["nombre"], "\nPRECIO ", dic[id]["precio"], "\nCANTIDAD ", dic[id]["cantidad"], "\n" + "=" * 35)
                verifyDel(productos , id, f"Para confirmar la eliminacion del id {id} digite \"borrar\". ESTA OPERACION SERA ABORTADA SI INGRESA CUALQUIER OTRO MENSAJE.\n>>> ")
            return False
        except KeyError:
            print("\nEl ID no existe en la base de datos.\nIntentalo nuevamente.")
            input()
        except ValueError:
            print("\nPor favor, ingrese una respuesta valida.")
            input()
        except Exception as e:
            print(f"\nOcurrio un error. {e}\n")
            input()


def marketing_plan(dic):
    print("●"*10,"Plan de Marketing", "●"*10)
    while True:
        try:
            
def menu(dic):
    while True:
        print("●" * 40, "Menu Principal","●" * 40)
        print("\n1. Agregar Producto")
        print("2. Modificar Producto")
        print("3. Eliminar Producto")
        print("4. Estrategia de Mercadeo")
        print("5. Salir del Sistema\n")
        opcion = readNumM1("Ingrese una opcion: ")
        # Opcion para agregar producto
        if opcion == 1:
            add_product(dic)
        elif opcion == 2:
            modifyProduct(dic)
        elif opcion == 3:
            delete_product(dic)
        elif opcion == 4:
            marketing_plan(dic)
        else:
            print("Gracias por usar nuestro sistema!")
            input()
            return False

productos = {}

while True:
    menu(productos)
    break