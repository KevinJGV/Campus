fd = open("Proyectos/KevinGonzalez/Archivos/nombres.txt", "r")

fd2 = open("Proyectos/KevinGonzalez/Archivos/nombresBak.txt", "w")

#for linea in fd:
#    print(linea)

for linea in fd:
    fd2.write(linea)

fd2.close()
fd.close()


print("PROCESO TERMINADO.")