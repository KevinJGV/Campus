fd = open("Proyectos/KevinGonzalez/Archivos/mbox-short.txt", "r")

cn = 0
cp = 0
for linea in fd:
    linea = linea.strip()
    cp += len(linea.split())
    cn += 1

fd.close()

print("Cantidad lineas: ", cn)
print("Cantidad palabras: ", cp)