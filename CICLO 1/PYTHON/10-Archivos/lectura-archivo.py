archivo = open("Proyectos/KevinGonzalez/Archivos/nombres.txt", "r")

texto = archivo.read()
print(texto)

archivo.seek(0)
texto2 = archivo.readline()
print(texto2)

texto3 = archivo.readlines()
archivo.close()