""""
Write a program that receives a positive integer and displays on the screen the 
number of digits it has.
You cannot convert number to string, nor use string functions. Arithmetic 
operators only.
"""
import math

num = int(input("Digite un numero entero: "))

if num < 0:
    num *= -1

cantDig = math.floor(math.log10(num)) + 1

print("La cantidad de digitos es: ", cantDig)
