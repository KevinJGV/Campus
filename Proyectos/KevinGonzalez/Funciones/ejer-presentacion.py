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
    return subsValue   

N = int(input("Cantidad de abonados: "))
TotalPaySubs = 0
for k in range(N):
    Name = input("Nombre del usuario: ")
    Strat = int(input("De su estrato (1-5): "))
    Impulse = int(input("Impulsos del mes: "))
    subsValue = facturaciones(Strat,Impulse)
    TotalPaySubs += subsValue
    print("*" * 80,"\nUsuario: ", Name, "\nTotal a pagar: ", subsValue)
print("*" * 80,"\nTotal a pagar de todos los abonados: ", TotalPaySubs)

