def leerCantidad():
    while True:
        try:
            n = int(input("Ingrese las cantidades del producto: "))
            if n < 0:
                print("cantidad de producto invalidos debe ser mayor a 1 ")
                continue
            return n
        except ValueError:
            print("Error al ingresar la cantidad de productos.")

def leerPrecioProd():
    while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if leerPrecioProd < 0:
                    print("ingrese solo precios existentes ")
                    continue
                break
            except Exception as e:
                    print("Error. precio invalido\n", e)
def leerNombreProd():
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

def leerIDProd():
    while True:
        try:
            n = int(input("Ingrese el ID del producto: "))
            if n < 1:
                print("ID inválido.")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")
            
        
        idProd = leerIDProd()
        if existProd == False:
            print("El nombre no ha sido ingresado.")
            input()
            return
    
        print("\n", "=" * 30)
        print("Nombre:", dicProducto[idProd]["nombre"])
        print("cantidad producto:", dicProducto[idProd]["cantidadProducto"])
        print("Valor precio:", dicProducto[idProd]["Valorprecio"])
        print(f"precio: ${dicProducto[idProd]['precio']:,.2f}")
        input("\n Presione cualquier tecla para volver al menu...")


def eliminarProducto(dicProducto):
    print("\n\n4. eliminar producto\n")
    
    idProd = leerIDProd()
    existEmpl = buscarEmpleado(dicProducto, idProd)
    if existEmpl == False:
        print("El producto con ese código no ha sido eliminado.")
        input()
        return
    
    dicProducto.pop(idProd)
    print(" el Producto ha sido eliminado")
    input()

def modificarProducto(dicProducto):
    print("\n\n2. Modificar producto\n")
    
    idProd = leerIDProd()
    existProd = (dicProducto, idProd)
    if existProd == False:
        print("El nombre del producto no existe.")
        input()
        return
    
    print("\n")

    while True:
        op = int(input("\n1. Nombre\n2.cantidad\n3. precio\nOpcion? "))
    
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue

        if op == 1:
         nombre = leerNombreProd()
         dicProducto[idProd]["nombre"] = nombre
        
        elif op == 2:
            cantProd = leerCantidad()
            dicProducto[idProd]["cantidad de producto"] = cantProd
        
        elif op == 3:
            valPrecio = leerPrecioProd()
            dicProducto[idProd]["ValorPrecio"] = valPrecio
        
        dicProducto[idProd]["precio"] = dicProducto[idProd]["ValorPrecio"] * dicProducto[idProd]["cantidad de producto"]
 

def agregarProducto(dicProducto):
    print("\n\n*** 1. Agregar producto\n")
    dicDatos = {}
    id = leerIDProd()
    if (dicProducto, id) == True:
        print("El id ya existe en la lista")
        input()
        return
    
    dicDatos["nombre"] = leerNombreProd()
    dicDatos["cantidad"] = leerCantidad()
    dicDatos["Valorprecio"] = leerPrecioProd()
    dicDatos["precio"] = dicDatos["valorPrecio"] * dicDatos["cantidad de producto"]
    
   
    dicProducto[id] = dicDatos


def menu():
    while True:
        try:
            print("*** PRODUCTOS ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. Eliminar producto")
            print("4. listar varios productos")
            print("5. estrategia de mercadeo")
            print("6. salir")
            op = int(input(">>> Opción (1-6)? "))
            if op < 1 or op > 6:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a .")
            input("Presione cualquier tecla para continuar...")

dicProducto= {}
while True:
    op = menu()
    if op == 1:
        agregarProducto(dicProducto)
        # print(dicEmpleados)
        # input()
    elif op == 2:
        modificarProducto(dicProducto)
        # print(dicEmpleados)
        # input()
        pass
    elif op == 3:
        eliminarProducto(dicProducto)
        #print(dicEmpleados)
        #input()
        
    elif op == 4:
        ListarVariosProductos(dicProducto)
        pass
    elif op == 5:
      pass
        #print(dicEmpleados)
        #input()
    elif op == 6:
        #listarEmpleado(dicEmpleados)
        pass
    elif op == 7:
        pass
    elif op == 8:
        print("\n\nGracias por usar el software. Adios")
        break



#valor hora = precio
#horas trabajadas = cantidad