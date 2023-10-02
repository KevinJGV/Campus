print("Sin importar su valor \n")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)

"""
elif num2 >= num1 and num2 >= num3:
    Orden = num2

elif num3 >= num1 and num3 >= num2:
    Orden = num3
if num1 < num2 and num1 < num3:
    Orden2 = num1
elif num2 < num1 and num2 < num3:
    Orden2 = num2
elif num3 < num1 and num3 < num2:
    Orden2 = num3


print("Primer numero: ", Orden)
print("Segundo numero: ", Orden2)
print("Tercer numero: ", Orden3)

"""