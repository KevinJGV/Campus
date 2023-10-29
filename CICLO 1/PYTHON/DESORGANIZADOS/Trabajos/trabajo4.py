print("//// PUNTO 1 ////""\n")

Num = int(input("Ingresa un número: "))
Contador = 0

for k in range(1, Num):
    if Num % k == 0:
        Contador += k

if Contador == Num:
    print(f"{Num} es un número perfecto.")
else:
    print(f"{Num} no es un número perfecto.")
