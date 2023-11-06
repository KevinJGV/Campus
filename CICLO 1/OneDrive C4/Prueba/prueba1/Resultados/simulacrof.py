

from datetime import datetime
from os import system
from time import sleep

##### CONSTANTES #####
CONTINUAR = '\n> ENTER < para continuar...'
RUTA_INVENTARIO = 'database/inventario.json'

def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

def leerString(msg):
    while True:
        try:
            sNom = input(msg)
            if sNom.strip() == "":
                print("\nPor favor ingrese un nombre valido")
                continue
            return sNom
        except Exception as e:
            print("\nError al ingresar un nombre" , e.message)

def menu():
    while True:
        print("_" * 50)
        print("\nMENU\n"
            "\n1. Agregar Productos\n"
            "2.Modificar producto\n"
            "3.Eliminar productos\n"
            "4.lista de Varios productos o inventario"
            "5.Extrategia de mercado"
            "6.Salir")
       
        print("_" * 50)
        opc = leerInt("\nIngrese el numero de la opción que desea -->")
        if opc < 1 or opc > 6:
            print("Ingrese un valor valido")
            continue
        return opc

def productos():
    produc = {}
    while True:
        print("_" * 50)
        print("\nBIENVENIDO AL MENU PARA AGREGAR PRODUCTOS")
        print("_" * 50)
        codPro = leerInt("Ingrese el codigo del producto: ")
        print("_" * 50)
        nomPro = leerString("Ingrese el nombre del producto: ")
        print("_" * 50)        
        valPro = leerInt("Ingrese el valor del producto: ")
        while True:
            print("_" * 50)
            print("Ingrese la categoria del producto")
          
            print("\nIngrese una opción valida")
            continue
            

def Modificar ():
 produc = {}

while True:
        print("_" * 50)
        print("\nBIENVENIDO AL MENU PARA AGREGAR MODIFICAR PRODUCTOS")
        print("_" * 50)
        codPro = leerInt("Ingrese el codigo  a cambiar: ")
        print("_" * 50)
        nomPro = leerString("Ingrese el nombre del que desea cambiar: ")
        print("_" * 50)        
        valPro = leerInt("Ingrese el valor que desea cambiar: ")
        while True:
            print("_" * 50)
            print("Ingrese la categoria del producto  que desea cambiar")
          
            print("\nIngrese una opción valida")
            continue
            
### Ver inventario ###
def verInventario():
    inventario = {}
    with open(RUTA_INVENTARIO) as inv:
        data = json.load(inv)
        for id in data.keys():
            inventario[id] = data[id]

    return inventario

### Mostrar inventario ###
def imprimirInventario(inv):
    system('clear')
    print('-' * 80)
    print('INVENTARIO'.center(80,' '))
    print('-' * 80)

    for id in inv.keys():
        print(f'\nId producto: {id}\nProducto: {inv[id]["nombre"]}\nPrecio: {inv[id]["precio"]}\nCantidad: {inv[id]["cantidad"]}',end='\n')
        print(f'Cantidad vendida: {inv[id]["cantidad_vendida"]}\n')
    
    print('-' * 80)
    input(CONTINUAR)

def calcularVlrProd(product,cantVendida,idProd):
    nombreProd = product['nombre']
    vlrProdUni = product['precio']
    vlrTotalProd = product['precio'] * cantVendida
    
    

    return {
            "id":idProd,
            "nombre":nombreProd,
            "cantidad":cantVendida,
            "vlrUnidad":vlrProdUni,
            "totalProd":vlrTotalProd, }


def Eliminar ():
 produc = {}

while True:
        print("_" * 50)
        print("\nBIENVENIDO AL MENU PARA ELIMINAR UN PRODUCTO")
        print("_" * 50)
        codPro = leerInt("Ingrese el codico a eliminar: ")
        print("_" * 50)
        nomPro = leerString("Ingrese el nombre del que desea eliminar: ")
        print("_" * 50)        
        valPro = leerInt("Ingrese el valor que desea eliminar: ")
        while True:
            print("_" * 50)
            print("Ingrese la categoria del producto  que desea eliminar")
          
            print("\nIngrese una opción valida")
            continue
            

with open("Productos.json", "w") as archivo:
            json.dump(produc, archivo)
            print("Se ha escrito en disco")
desSeg = leerInt("¿Desea ingresar algun otro producto (1 para si) (2 para no)?")
if desSeg == 1:

  def estrategia ():
    while True:
        with open("Clientes.json", "r", encoding = "utf-8") as archivo:
            clientes = json.load(archivo)
        with open("Productos.json", "r", encoding = "utf-8") as archivo:
            produc = json.load(archivo)
        print("_" * 50)
        print("\nBIENVENIDO AL MENU PARA RECOMENDACIONES O SUJERENCIAS DE LOS CLIENTES ")
        cedCli = leerInt("Ingrese el numero del producto: ")
        if str(cedCli) in clientes:
            
        

while True:
    op = menu()
    if op == 1:
        productos()
        input("\nOprima cualquier letra para dirigirse al menu principal")
    elif op ==2:
        ventas()
        input("\nOprima cualquier letra para dirigirse al menu principal")
    elif op ==3:
        input("\nOprima cualquier letra para dirigirse al menu principal")
    elif op == 4:
          input("\nOprima cualquier letra para dirigirse al menu principal")
    elif op==5:    
          input("\nOprima cualquier letra para dirigirse al menu principal")
    elif op==6:   
          input("\nOprima cualquier letra para dirigirse al menu principal")
        
    else:   
        print("\nFin del programa")
        break