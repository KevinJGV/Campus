
# numPar = 0
# numImpar = 0

# while True:
#     numero = int(input("Ingresa numero entero a juzgar: "))
#     if numero % 2 == 0:
#         print("Éste numero es par.")
#         numPar += 1 
#     else:
#         print("Éste numero es impar.")
#         numImpar += 1
#     if numero == -1:
#         break
# print(f"Cantidad total de N pares: {numPar}")
# print(f"Cantidad total de N impares: {numImpar}")


# while True:
#     Nombre = input("***************¿CUAL ES SU TARIFA DE SERVICIO ELECTRICO?***************\nNombre del usuario: ")
#     Estrato = int(input("Estrato del usuario (1-5): "))
#     if Estrato == 1:
#         Tarifa = 10000
#     elif Estrato == 2:
#         Tarifa = 15000
#     elif Estrato == 3:
#         Tarifa = 30000
#     elif Estrato == 4:
#         Tarifa = 50000
#     elif Estrato == 5:
#         Tarifa = 65000
#     else:
#         print("Información incorrecta.")
#         continue
#     print(f"Sr. / Sra. {Nombre} su tarifa basica de energia electrica es ${Tarifa}")
#     continuar = input("¿Desea continuar con la operación nuevamente? (y/n): ")
#     if continuar == "n" or continuar == "N":
#         break
#     else:
#         continue


AcumMatriculas = 0

while True:
        CodUser = int(input("Suministre el codigo del estudiante [-1 para salir del programa]: "))
        if CodUser == -1:
                break
        Name = input("Suministre nombre del estudiante: ")
        Program = int(input("Indique su programa academico de la siguiente manera\n      1 - Técnico en Sistemas\n      2 - Técnico en Desarrollo de videojuegos\n      3 - Técnico en Animación Digital\n"))
        if Program == 1:
                Matricula = 800_00
                AcumMatriculas += Matricula
        elif Program == 2:
                Matricula = 1_000_000
                AcumMatriculas += Matricula
        elif Program == 3:
                Matricula = 1_200_000
                AcumMatriculas += Matricula
        else:
                print("OPERACIÓN ABORTADA")
                continue
        Beca = int(input("Indicador de Beca, puede ser:\n   1 - Beca por rendimiento académico. Descuento del 50% sobre el valor matricula.\n   2 - Beca Cultural/Deportes. Descuento del 40% sobre el valor matrícula.\n   3 - Sin Beca.\n"))
        if Beca == 1:
                Dcto = 0.5
        elif Beca == 2:
                Dcto = 0.4
        elif Beca == 3:
                Dcto = 0
        else:
                print("OPERACIÓN ABORTADA")
                continue
        ValorNeto = Matricula * Dcto
        print("*" * 30, " RESULTADO ", "*" * 30,"\n")
        print(f"Estudiante: {Name}\nCoste de matricula: {Matricula}\nValor Neto a pagar: {ValorNeto}")
        continue

print("Valor de la totalidad en matriculas operada (sin Dcto de becas): ", AcumMatriculas)
