# Capturar las notas de un curso y calcular el promedio de estas.
# Mostrar en pantalla el resultado del promedio

CantNotas = int(input("Cantidad de notas: "))

SumaNotas = 0
for k in range(1, CantNotas+1):
    Nota = float(input(f"Ingrese la nota #{k}: "))
    SumaNotas = SumaNotas + Nota
prom = SumaNotas / CantNotas

print(f"Promedio de notas: {prom:.1f}")