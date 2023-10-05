N = 0

Name = input("Nombre del usuario: ")
Strat = int(input("De su estrato (1-5): "))
Impulse = input("Impulsos del mes: ")

def facturaciones(Strat,Impulse):
    if Strat == 1:
        tarifa = 10000
    elif Strat == 2:
        tarifa = 15000
    elif Strat == 3:
        tarifa = 20000
    elif Strat == 4:
        tarifa = 25000
    elif Strat == 5:
        tarifa = 30000
    ImpulseValue = Impulse * 100
    subsValue = tarifa + ImpulseValue
    return subsValue
