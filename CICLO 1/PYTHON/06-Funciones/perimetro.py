import math
def posTSR(Xt,Yt,Xs,Ys,Xr,Yr):
    # Xt = float(input("CALCULADOR DE PERIMETRO\nDebe ingresar los valores posicionales (X,Y) de cada vertice, inicie ingresando el valor Xt: "))
    # Yt = float(input("Valor Yt: "))
    # Xs = float(input("Valor Xs: "))
    # Ys = float(input("Valor Ys: "))
    # Xr = float(input("Valor Xr: "))
    # Yr = float(input("Valor Yr: "))
    return Xt,Yt,Xs,Ys,Xr,Yr

def lenTS(posTSR):
    l1 = math.sqrt((posTSR[0] - posTSR[2] )**2 + (posTSR[1] - posTSR[3])**2)
    return l1

def lenSR(posTSR):
    l2 = math.sqrt((posTSR[2] - posTSR[4] )**2 + (posTSR[3] - posTSR[5])**2)
    return l2

def lenRT(posTSR):
    l3 = math.sqrt((posTSR[4] - posTSR[0] )**2 + (posTSR[5] - posTSR[1])**2)
    return l3

def calc(a,b,c):
    calc = a + b + c
    return print(f"El perimetro de su triangulo es {calc:.2f}")


Xt = float(input("CALCULADOR DE PERIMETRO\nDebe ingresar los valores posicionales (X,Y) de cada vertice, inicie ingresando el valor Xt: "))
Yt = float(input("Valor Yt: "))
Xs = float(input("Valor Xs: "))
Ys = float(input("Valor Ys: "))
Xr = float(input("Valor Xr: "))
Yr = float(input("Valor Yr: "))

calc(lenTS(posTSR(Xt,Yt,Xs,Ys,Xr,Yr)),lenSR(posTSR(Xt,Yt,Xs,Ys,Xr,Yr)),lenRT(posTSR(Xt,Yt,Xs,Ys,Xr,Yr)))



