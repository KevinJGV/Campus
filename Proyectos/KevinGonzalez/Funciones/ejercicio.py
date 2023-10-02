print("*" * 40, "Punto 1", "*" * 40)
def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def calcular_salario(horas_trabajadas, salario_por_hora):
    if horas_trabajadas <= 40:
        salario_total = horas_trabajadas * salario_por_hora
    else:
        horas_regulares = 40
        horas_extra = horas_trabajadas - 40
        salario_regular = horas_regulares * salario_por_hora
        salario_extra = horas_extra * (salario_por_hora * 1.5)
        salario_total = salario_regular + salario_extra
    return salario_total


horas_trabajadas = 45
salario_por_hora = 10
ganancias_totales = calcular_salario(horas_trabajadas, salario_por_hora)
print(f"Ganancias totales por {horas_trabajadas} horas a ${salario_por_hora}/hora: ${ganancias_totales}")

def calcular_salario():
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
    salario = horas_trabajadas * tarifa_por_hora
    print(f"El salario del empleado es: ${salario:.2f}")


def contar_palabras(parrafo):
    palabras = parrafo.split()
    return len(palabras)


while True:
    print("\nMENU")
    print("1- Factorial de un número")
    print("2- Calcular Salario de un empleado")
    print("3- Calcular palabras en un párrafo")
    print("4- Salir")
    opcion = input("Escoja una opción (1-4): ")

    if opcion == '1':
        numero = int(input("Ingrese un número para calcular su factorial: "))
        resultado = calcular_factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
    elif opcion == '2':
        calcular_salario()
    elif opcion == '3':
        parrafo = input("Ingrese un párrafo: ")
        cantidad_palabras = contar_palabras(parrafo)
        print(f"El número de palabras en el párrafo es: {cantidad_palabras}")
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1-4).")


print("*" * 40, "Punto 3", "*" * 40)

def calcular_salario(horas_trabajadas, salario_por_hora):
    if horas_trabajadas <= 40:
        salario_total = horas_trabajadas * salario_por_hora
    else:
        horas_regulares = 40
        horas_extra = horas_trabajadas - 40
        salario_regular = horas_regulares * salario_por_hora
        salario_extra = horas_extra * (salario_por_hora * 1.5)
        salario_total = salario_regular + salario_extra
    return salario_total


horas_trabajadas = 45
salario_por_hora = 10
ganancias_totales = calcular_salario(horas_trabajadas, salario_por_hora)
print(f"Ganancias totales por {horas_trabajadas} horas a ${salario_por_hora}/hora: ${ganancias_totales}")
