# Diseñe un algoritmo con funciones y procedimientos que indique el valor del descuento de un artículo el cual es del 5% solo si el artículo tiene un costo superior al $150.000.



def funcion(valorDcto):
    valorStr = input("Ingrese el costo de su compra: ")
    valor = int(valorStr)
    while valorStr.isdigit():
        if valor > 150000:
            valorDcto = valor * 0.05
            return print(f"El descuento correspondiente a su compra es de {valorDcto}")
        else:
            return print("No corresponde al descuento del 5%")

valorDcto = ()
funcion(valorDcto)
