# Ejemplo de como imprimir los caracteres de una cada en cada linea, siempre y cuando el valor de la banderilla sea menor a la longitud de la cadena
# s = input("Ingrese string: ")
# j = 0
# while j < len(s):
#     print(s[j])
#     j += 1

# ejercicio 1
# telefono = input("////////Ingrese telefono con el formato +34-XXXXXXXXX-XX////////\n")

# prefijo = telefono.find("-")
# extencion = telefono.rfind("-")
# numeroPuro = telefono[prefijo+1:extencion]

# print("Su numero telefonico es: ", numeroPuro,".")

# ejercicio 2

# palindrome = input("Validemos si su palabra es palindrome.\nIngrese una palabra: ")
# verificar = palindrome[::-1]

# if palindrome == verificar:
#     print("Su palabra es palindrome.")
# else:
#     print("Su palabra NO es palindrome.")

# ejercicio 3

# fechaDia = input("Visualizador de fecha de nacimiento.\nIngrese su dia de nacimiento: ")
# fechaMes = input("Ingrese su mes de nacimiento: ")
# fechaAño = input("Ingrese su año de nacimiento: ")
# fechaDia = fechaDia.strip()
# fechaMes = fechaMes.strip()
# fechaAño = fechaAño.strip()

# if not fechaDia.startswith("0"):
#     fechaDia = "0" + fechaDia
# if not fechaMes.startswith("0"):
#     fechaMes = "0" + fechaMes
# if not fechaAño.startswith("0"):
#     fechaAño = "0" + fechaAño

# fechaNac = "/".join([fechaDia,fechaMes,fechaAño])

# print("Su fecha de nacimiento es: ", fechaNac)

# ejercicio 4

##METODO CHATGPT
# linea = str(input("Ingrese una linea con letras repetidas (o no) seguidas: "))
# linea = linea.lower()
# # Crear una lista (pila) para almacenar los caracteres
# pila = []

# # Recorrer la cadena
# for char in  linea:
#     if pila and pila[-1] == char:
#         # Si el último carácter en la pila coincide con el carácter actual, eliminarlo
#         pila.pop()
#     else:
#         # Si no coincide, agregar el carácter actual a la pila
#         pila.append(char)

# # Comprobar si la pila está vacía
# if not pila:
#     print("Empty String")
# else:
#     # Unir los caracteres restantes en la pila para obtener la cadena reducida
#     cadena_reducida = ''.join(pila)
#     print("Cadena reducida:", cadena_reducida)


# ##METODO DE CARLOS
# a = input("Ingrese secuencia: ")




# i = True
# f = 0
# new_sec = ""

# while i == True:
#     if new_sec == "":
#         if a[f] == a[f+1]:
#             new_sec = a[f+2:]
#             print(new_sec)
#             x = "check" 



#         else:
#             new_sec = a
#             print(new_sec)
#             x = "no-check"



#     if x == "check":
#         f = f

#     elif x == "no-check":
#         f += 1

#     if f < (len(new_sec)-1):
#         if new_sec[f] == new_sec[f+1]:
#             new_sec = new_sec[:f] + new_sec[f+2:]
#             #new_sec =  new_sec[f+2:]
#             print(new_sec)
#             x = "check"

#         elif new_sec[f] == new_sec[f - 1]:
#             new_sec = new_sec[:f-1] + new_sec[f+1:]
#             #new_sec =  new_sec[f+2:]
#             print(new_sec)
#             x = "check"

#         else:
#             new_sec = new_sec
#             print(new_sec)
#             x = "no-check"

#         if new_sec == "":
#             new_sec = "Secuencia vacia"

#     elif f == len(new_sec)-1:
#         if new_sec[f] == new_sec[f-1]:
#             new_sec = "Secuencia vacía"

#     else:
#         i = False


# print(f"secuencia: {a}")
# print (f"Nueva secuencia: {new_sec}")