def menu():
    while True:
        try:
            print("==================\n PRODUCTOS ACME\n==================")
            print("1. Agregar producto\n2. Modificar producto\n3. Eliminar producto\n4. Listar varios productos\n5. Estrategia de mercadeo\n6. Salir\n")
            op = int(input(">> Opción [1-6]? "))
            if op < 1 or op > 6:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...")

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

def agregarproducto(dic_productos):
    print("\n\n*** 1. Agregar producto\n")
    dicDatos = {}
    id = leerID()
    if id in dic_productos:
        print("El id ya existe en la lista")
        input()
        return
    
    dicDatos["nombre"] = leer_nombre_poducto()
    dicDatos["precio"] = leer_precio()
    dicDatos["existencias"] = leer_existencias()
    
    dic_productos[id] = dicDatos

def leer_nombre_poducto():
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

def leer_precio():
    while True:
        try:
            n = float(input("Ingrese el valor del producto: "))
            if n < 0:
                print("Valor inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor del producto.")

def leer_existencias():
    while True:
        try:
            n = int(input("Ingrese las existencias del producto: "))
            if n < 0:
                print("Existencias inválidas. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar las existencias.")

def modificarproducto(dic_productos):
    print("\n\n*** 2. Modificar producto\n\n")
    
    id = leerID()
    if not id in dic_productos:
        print("El código del producto no ha sido registrado.")
        input("Ingrese cualquier tecla para continuar")
        return
    
    while True:
        try:
            op = int(input("\nQue desea modificar? \n1. Nombre\n2. Precio\n3. Existencias\nOpcion? \n"))
            if op < 1 or op > 3:
                print("Opción inválida")
                input()
                continue
            break
        except ValueError:
            print("Valor inválido, intente de nuevo:")

    if op == 1:
        nombre = leer_nombre_poducto()
        dic_productos[id]["nombre"] = nombre
    elif op == 2:
        precio = leer_precio()
        dic_productos[id]["precio"] = precio   
    else:
        existencias = leer_existencias()
        dic_productos[id]["existencias"] = existencias    
    print("producto modificado exitosamente\n")
            
def eliminarproducto(dic_productos):
    # return dic_productos.get(idEmpl) != None
    print("\n\n*** 3. Eliminar producto\n")
    id = leerID()
    if id in dic_productos:
        del dic_productos[id]
        print("producto eliminado exitosamente")
        return
    else:
        print("El producto con ese código no ha sido registrado.")
        input("Ingrese cualquier tecla para continuar")
        return
    

def listar_all(dic_productos):
    print("\n\n*** 4. Listar productos\n")
    for k in dic_productos.keys():
        i += 1
        print(f"===============\n{dic_productos[k]}\n===============")

def estrategia_mercadeo(dic_productos):
    i = 0
    imprimir = dic_productos.copy()
    for k in dic_productos.keys():
        for ke in dic_productos.keys():
            if imprimir[k]["precio"] <= imprimir[ke]["precio"]:
                m = k
            else:
                m = ke
        i += 1
        print(dic_productos[m])
        imprimir[m] = dic_productos[m].copy()
        imprimir[m]["precio"] += 999999999999
        if i%5 == 0:
            while True:
                a = input("Desea continuar? \nSi:S\nNo:N\n")
                if a != "S" and a != "N":
                    print("Error, solo se admite S ó N")
                    continue
                elif a == "S":
                    break
                elif a == "N":
                    return



## PROGRAMA PRINCIPAL
dic_productos = {}
while True:
    op = menu()
    if op == 1:
        agregarproducto(dic_productos)
    elif op == 2:
        modificarproducto(dic_productos)
    elif op == 3:
        eliminarproducto(dic_productos)
    elif op == 4:
        listar_all(dic_productos)
        pass
    elif op == 5:
        estrategia_mercadeo(dic_productos)
        pass
    elif op == 6:
        print("\n\nGracias por usar el software. Adios")
        break