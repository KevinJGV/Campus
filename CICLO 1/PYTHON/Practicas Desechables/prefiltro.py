import math
"""""
# def distancia(xt,yt,xs,ys):
#     d = math.sqrt((xt - xs)**2 + (yt - ys)**2)
#     return d
# x1 = 1
# x2 = 2
# y1 = 3
# y2 = 4

# dist = distancia(x1,y1,x2,y2)
# print(f"La distancia es {dist:.2f}")

def distancia(xt,yt,xs,ys):
    d = math.sqrt((xt - xs)**2 + (yt - ys)**2)
    return d
def perimetroT(xp,yp,xr,yr,xq,yq):
    perimetro = distancia(xp,yp,xr,yr) + distancia(xr,yr,xq,yq) + distancia(xq,yq,xp,yp)
    return perimetro

x1 = 1
y1 = 4
x2 = 3
y2 = 0
x3 = 5
y3 = 3

print(f"El perimetro del triangulo es {perimetroT(x1,y1,x2,y2,x3,y3):.2f}")

def descuento(valor):
    if valor > 150000:
        descuento = valor * 0.05
    else:
        descuento = 0
    return descuento

valor = int(input("Ingrese valor del producto: "))
print(f"El valor del descuento es {descuento(valor)}")




def estadoEstudiante(n1,n2,n3,n4,n5):
    promedio = (n1 + n2 + n3 + n4 + n5)/5
    if promedio > 3.5:
        return True
    else:
        return False
    
nt1 = float(input("Ingrese la nota del primer trabajo: "))
nt2 = float(input("Ingrese la nota del segundo trabajo: "))
nt3 = float(input("Ingrese la nota del tercer trabajo: "))
nt4 = float(input("Ingrese la nota del cuarto trabajo: "))
nt5 = float(input("Ingrese la nota del quinto trabajo: "))

if estadoEstudiante(nt1,nt2,nt3,nt4,nt5):
    print("Estudiante aprobado.")
else:
    print("Estudiante CACORRO.")
"""

import turtle

def drawLine(x1,y1,x2,y2):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)

def writeText(s,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(s)

def drawPoint(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)
    turtle.end_fill()

def drawCircle(x = 0, y = 0, radius = 10):
    turtle.penup()
    turtle.goto(x,y - radius)
    turtle.pendown()
    turtle.circle(radius)

def drawRectangle(x = 0, y = 0, width = 10, height = 10):
    turtle.penup()
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(height)
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

def drawRectangle(x = 0, y = 0, width = 10, height = 10):
    turtle.penup()
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(height)



























