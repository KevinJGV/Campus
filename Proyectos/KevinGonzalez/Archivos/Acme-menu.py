"""desarrollo de menu interactivo con las siguientes caracteristicas:
1. Agregar producto. Este opción permite agregar un producto al sistema. El producto consta de
un id, nombre, precio y cantidad (existencias en bodega)
2. Modificar producto. Esta opción permite modificar los datos de un producto ingresando el
código.
3. Eliminar producto. Esta opción permite modificar un producto a partir del código.
4. Estrategia de mercadeo. Esta opción ordena y lista ascendentemente por precio todos los
productos que hay en bodega y los muestre sus datos en pantalla. Se listan de a 5 productos
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


#Funcion del menu principal
def menu():
    print("●" * 40, "\nMenu Principal","●" * 40)
    print("\n1. Agregar Producto")
    print("2. Modificar Producto")
    print("3. Eliminar Producto")
    print("4. Estrategia de Mercadeo")
    print("5. Salir del Sistema\n")
    # Opcion para agregar producto
    if input("Ingrese una opcion: ") == "1":
        add_product()
    elif input("Ingrese una opcion: ") == "2":
        modify_product()
    elif input("Ingrese una opcion: ") == "3":
        delete_product()
    elif input("Ingrese una opcion: ") == "4":
        marketing_plan()
    else:
        print("Gracias por usar nuestro sistema!")
        input()


productos = {}
# Funcion para agregar producto
def add_product():
    productos = {}
    cantidad_ingreso = readNum("Cuantos productos desea agregar en ésta operación? => ")
    for i in range(cantidad_ingreso):
        id = int(input("Ingrese el id del articulo => "))
