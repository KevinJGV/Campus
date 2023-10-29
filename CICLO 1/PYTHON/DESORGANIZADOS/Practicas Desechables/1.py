#Dado el nombre y salario de un empleado, calcular el subsidio de transporte, teniendo en cuenta que si el salario es menor o igual a $1.200.000 entonces tiene derecho a un subsidio de transporte por valor de $120.000, de lo contrario no tiene derecho al subsidio detransporte. Se debe visualizar el nombre, salario y subsidio de transporte 
""""
print("º" * 80)
nombre = input("Nombre del empleado: ")
salario = float(input("Salario del empleado: "))

if salario <= 1_200_000:
    subTrans = 120_000
else:
    subTrans = 0


salarioTotal = salario + subTrans
print("Empleado: ", nombre)
if subTrans == 120_000:
    print("Aux. Transporte: $", subTrans,"\nSalario: $", salario, "\nTotal: $", salarioTotal)

else:
    print("Total: $", salario,"\n No aplica a subsidio de transporte.")

##Dado el nombre del estudiante y la calificación cuantitativa de
# una evaluación (0-100), se pide hallar la calificación cualitativa,
# de acuerdo a la siguiente información
# Rango Evaluación Evaluación cualitativa
#  0 - 59 D
#  60 - 79 C 
#  80 - 89 B
#  90 - 100 A
# Se pide visualizar, nombre, calificación
# cuantitativa y cualitativa

print("º" * 80)
nombre = input("Nombre de estudiante: ")
califCuan = int(input("Calificación (0-100): "))

if califCuan > -1 and califCuan < 60:
    califCual = "D"
elif califCuan > 59 and califCuan < 80:
    califCual = "C"
elif califCuan > 79 and califCuan < 90:
    califCual = "B"
elif califCuan > 89 and califCuan < 101:
    califCual = "A"
else:
    califCual = "Rango incorrecto."

print(f"{nombre} su calificación {califCuan} corresponde a la nota {califCual}")

# Diseñe y escriba un programa que solicite tres números enteros
# (pueden ser positivos o negativos) y como salida los muestre en
# orden de mayor a menor

print("º" * 80)
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

numA = num1
numB = num2
numC = num3

if num2 > numA:
    numB = numA
    numA = num2
elif num2 > numB:
    numB = numA

if num3 > numA:
    numC = numB
    numB = numA
    numA = num3
elif num3 > numB:
    numC = numB
    numB = num3

print(F"El resultado es:\n 1er numero: {numA}\n 2do numero: {numB}\n 3er numero: {numC}")

"""
# Escribe un programa en Python que determine si un año
# ingresado por el usuario es bisiesto o no. Un año bisiesto es
# aquel que es divisible entre 4, excepto aquellos divisibles entre
# 100 pero no entre 400.
# El programa debe realizar lo siguiente:
# Solicitar al usuario que ingrese un año.
# Verificar si el año cumple con las condiciones para ser bisiesto.
# Mostrar un mensaje indicando si el año es bisiesto o no

Año = int(input("Año a juzgar: "))

if Año % 4 == 0 and Año % 100 == 0:
    Año = "Bisiesto."
elif Año % 100 == 0 and Año % 400 != 0:
    Año = "No bisiesto."
else:
    Año = "Bisiesto."

print("Su año es: ", Año)