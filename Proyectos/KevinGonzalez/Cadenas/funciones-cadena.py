# Ejemplo de como imprimir los caracteres de una cada en cada linea, siempre y cuando el valor de la banderilla sea menor a la longitud de la cadena
# s = input("Ingrese string: ")
# j = 0
# while j < len(s):
#     print(s[j])
#     j += 1

# ejercicio 1
telefono = input("////////Ingrese telefono con el formato +34-XXXXXXXXX-XX////////\n")

prefijo = telefono.find("-")
extencion = telefono.rfind("-")
numeroPuro = telefono[prefijo+1:extencion]

print("Su numero telefonico es: ", numeroPuro,".")
