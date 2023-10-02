"""""
Num = int(input("Ingrese un número""\n"))
pares = 0
impares = 0

while Num != -1:
    if Num % 2 == 0:
        print("Es par.")
        pares += 1
    else:
        print("Es impar.")
        impares += 1

    Num = int(input("Ingrese un número""\n"))

print("*" * 50)
print(f"")
"""""

#Ejercicio

inicial = True

Status1 = 10_000
Status2 = 15_000
Status3 = 30_000
Status4 = 50_000
Status5 = 65_000

while  inicial == True:
    User = input("Nombre del usuario""\n")
    Status = int(input("Estrato (1-5): "))

    if Status == 1:
        print("*" * 50)
        print(f"Sr./Sra. {User} su tarifa básica es de {Status1}, acorde al estrato {Status}")
    elif Status == 2:
        print("*" * 50)
        print(f"Sr./Sra. {User} su tarifa básica es de {Status2}, acorde al estrato {Status}")
    elif Status == 3:
        print("*" * 50)
        print(f"Sr./Sra. {User} su tarifa básica es de {Status3}, acorde al estrato {Status}")
    elif Status == 4:
        print("*" * 50)
        print(f"Sr./Sra. {User} su tarifa básica es de {Status4}, acorde al estrato {Status}")
    elif Status == 5:
        print("*" * 50)
        print(f"Sr./Sra. {User} su tarifa básica es de {Status5}, acorde al estrato {Status}")
    else:
        print("Datos no válidos.")
    inicial = input("¿DESEA CONTINUAR? [S/N]")
    if inicial == "s" or inicial == "S":
        inicial = True
    elif inicial == "n" or "N":
        inicial = False
