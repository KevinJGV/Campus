
print("Punto 1: ""\n""\n")

print("CALCULADOR TOTAL DE COSTO PARA VIAJE EN FERROCARRIL", "\n")
Distancia = float(input("Distancia aproximada: "))
Dias = int(input("Duración de estancia (Dias): "))

KmCosto = 0.63
Descuento = 70
PrecioSinDescuento = float(Distancia * KmCosto)

if Dias > 7 and Distancia > 800:
    PrecioConDescuento = (PrecioSinDescuento*2) * Descuento
    print(f"Costo de ida y vuelta (30% Dcto. aplicable): {PrecioConDescuento:,}")
else:
    PrecioConDescuento = PrecioSinDescuento
    print(f"Costo de ida y vuelta: {PrecioSinDescuento:,}")

print("\n""\n")
print("Punto 2: ""\n""\n")
print("CONSULTOR DE AÑO BISIESTO""\n")

try:
    Año = int(input("Digite un año: "))
except ValueError:
    print("Ingresar un año valido.")
    exit()

if (Año % 4 == 0 and Año % 100 != 0) or (Año % 400 == 0):
    print(f"{Año} es un año bisiesto.")
else:
    print(f"{Año} NO es un año bisiesto.")



    





