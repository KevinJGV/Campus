import math
def posT(Xt,Yt):
    return Xt,Yt

def posS(Xs,Ys):
    return Xs,Ys

def length(posT,posS):
    d = math.sqrt((posT[0] - posS[0] )**2 + (posT[1] - posS[1])**2)
    return f"La distancia entre estos puntos es: {d:.2f}"

print("\tCALCULADOR DE TEOREMA DE PITAGORAS\n")

Xt = float(input("Ingrese la posicion en (formato float) X de t: "))
Yt = float(input("Ingrese la posicion en (formato float) Y de t: "))
Xs = float(input("Ingrese la posicion en (formato float) X de s: "))
Ys = float(input("Ingrese la posicion en (formato float) Y de s: "))
posT(Xt,Yt)
posS(Xs,Ys)
d = length(posT(Xt, Yt), posS(Xs, Ys))
print(d)
