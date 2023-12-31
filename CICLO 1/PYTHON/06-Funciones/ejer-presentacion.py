def facturaciones(Strat,Impulse):
    if Strat == 1:
        tarifa = 10000
    elif Strat == 2:
        tarifa = 15000
    elif Strat == 3:
        tarifa = 20000
    elif Strat == 4:
        tarifa = 25000
    else:
        tarifa = 30000
    ImpulseValue = Impulse * 100
    subsValue = tarifa + ImpulseValue
    return subsValue, tarifa, ImpulseValue


def ValidarImpInt(dato):
    while True:
        try:
            Impulse = int(input(dato))
            break
        except ValueError:
            print("Error. Ingrese un numero entero.")
    return Impulse


def ValidarStrat(dato):
    while True:
        try:
            Strat = int(input(dato))
            if Strat > 5 or Strat < 1:
                print("Ingrese un dato valido solicitado.")
                continue
            break
        except ValueError:
            print("Error. Ingrese un numero entero.")
        except:
            print("Error. Ingrese un numero.")
    return Strat

N = int(input("Cantidad de abonados: "))
TotalPaySubs = 0
for k in range(N):
    Name = input("Nombre del usuario: ")
    Strat = ValidarStrat("Dé su estrato (1-5): ")
    Impulse = ValidarImpInt("Impulsos del mes: ")
    subsValue, tarifa, ImpulseValue = facturaciones(Strat,Impulse)
    TotalPaySubs += subsValue
    print("*" * 80,"\nUsuario: ", Name,"\n Tarifa: ", tarifa, "\nTotal a pagar: ", subsValue)
print("*" * 80,"\nTotal a pagar de todos los abonados: ", TotalPaySubs)