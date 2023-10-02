print("/" * 40, "Punto 1", "/" * 40, "\n", "\tComision de vendedores, ingresar los siguientes datos: ", "\n")
total_ventas = 0
total_comisiones = 0
comision_porcentaje = {1: 0.20,  2: 0.15,  3: 0.25}

while True:
    cedula = input("Ingrese la cédula de ciudadanía (o -1 para salir): ")
    if cedula == "-1":
        break
    
    nombre = input("Ingrese el nombre del vendedor: ")
    tipo_vendedor = int(input("Ingrese el tipo de vendedor (1: Puerta a Puerta, 2: Telemercadeo, 3: Ejecutivo de Ventas): "))
    ventas_mes = float(input("Ingrese el valor de ventas realizadas en el mes: "))
    
    # Calculamos la comisión para este vendedor.
    comision = ventas_mes * comision_porcentaje.get(tipo_vendedor, 0)
    
    # Actualizamos los valores totales.
    total_ventas += ventas_mes
    total_comisiones += comision
    
    # Mostramos la comisión para este vendedor.
    print(f"El vendedor {nombre} con cédula {cedula} tiene una comisión de: ${comision:.2f}")

# Mostramos los valores totales.
print(f"\nValor total de ventas del mes: ${total_ventas:.2f}")
print(f"Valor total a pagar por comisiones: ${total_comisiones:.2f}")
