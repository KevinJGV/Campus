"""""
while True:
    año = int(input("Ingrese año a juzgar: "))
    if año % 400 == 0:
        print("Es bisiesto")
    elif año % 4 == 0 and año % 100 != 0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")

"""
users = int(input("CONSULTOR - SERVICIO DE AGUA\nCuantos usuarios desea analizar:\n"))
valorCm3 = 200
valorNeto = 0

for k in range(users):
        cod = int(input("Codigo de usuario: "))
        nomb = input("Nombre de usuario: ")
        status = input("Estado de usuario (V:Vigente o S:Suspendido): ")
        estrato = int(input("Estrato (1-6):"))
        if estrato == 1:
                tarifa = 10000
        elif estrato == 2:
                tarifa = 20000
        elif estrato == 3:
                tarifa = 30000
        elif estrato == 4:
                tarifa = 45000
        elif estrato == 5:
                tarifa = 60000
        elif estrato == 6:
                tarifa = 70000
        else:
                print("///////////// Estrato invalido ///////////////")
        cons = int(input("Consumo (Cm3): "))
        valorCons = cons * valorCm3
        valorAcumulado = valorCons + tarifa
        valorNeto += valorAcumulado
        print("\n\t", "*" * 80, "\n")
        print("Usuario: ", nomb)
        print("Tarifa basica correspondiente: $", tarifa)
        print("Valor Consumo: $", valorCons)
        print("Valor total: $", valorAcumulado)
        
        if status == "S" or status == "s":
               print("\n\t", "*" * 40, "USUARIO SUSPENDIDO, NO ES POSIBLE LIQUIDAR", "*" * 40)
print(f"Valor Neto de todos los usuarios: $", valorNeto)