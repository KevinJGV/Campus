# ******
# *    *
# *    *
# *    *
# ******

for k in range(9):
    print(k)

print("")

for k in range (6):
    print("*", end="")
print("")
for k in range (3):
    print("*    *")
for k in range (6):
    print("*", end="")
print("")

# El usuario decide el tamaño de la piramide:
# Ejem:
#     input: 4
#     output: 

usuario = int(input("Ingrese cantidad de filas deseadas que formen su piramide: "))

for k in range (usuario):
    print((1+k)*"*")


