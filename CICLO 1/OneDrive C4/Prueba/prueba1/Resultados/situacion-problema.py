#
productos = []

#
def agregar_producto():
    id_producto = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad en bodega: "))
    producto = {'id': id_producto, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    productos.append(producto)
    print("Producto agregado exitosamente.")

#
def modificar_producto():
    codigo = input("Ingrese el ID del producto que desea modificar: ")
    for producto in productos:
        if producto['id'] == codigo:
            producto['nombre'] = input("Nuevo nombre del producto: ")
            producto['precio'] = float(input("Nuevo precio del producto: "))
            producto['cantidad'] = int(input("Nueva cantidad en bodega: "))
            print("Producto modificado exitosamente.")
            return
    print("Producto no encontrado.")

# 
def eliminar_producto():
    codigo = input("Ingrese el ID del producto que desea eliminar: ")
    for producto in productos:
        if producto['id'] == codigo:
            productos.remove(producto)
            print("Producto eliminado exitosamente.")
            return
    print("Producto no encontrado.")

#
def listar_productos():
    print("Lista de productos:")
    for producto in productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad en bodega: {producto['cantidad']}")

#
def estrategia_mercadeo():
    productos_ordenados = sorted(productos, key=lambda x: x['precio'])
    pagina = 1
    productos_por_pagina = 5
    while pagina <= len(productos_ordenados):
        print(f"Página {pagina}:")
        for producto in productos_ordenados[pagina - 1:pagina - 1 + productos_por_pagina]:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}")
        pagina += 1
        input("Presione Enter para continuar...")

# 
while True:
    print("==================")
    print("PRODUCTOS ACME")
    print("==================")
    print("1. Agregar producto")
    print("2. Modificar producto")
    print("3. Eliminar producto")
    print("4. Listar varios productos")
    print("5. Estrategia de mercadeo")
    print("6. Salir")
    opcion = input(">> ¿Opción [1, 6]? ")

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        modificar_producto()
    elif opcion == '3':
        eliminar_producto()
    elif opcion == '4':
        listar_productos()
    elif opcion == '5':
        estrategia_mercadeo()
    elif opcion == '6':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
