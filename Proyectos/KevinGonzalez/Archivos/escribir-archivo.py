archivo = open("Proyectos/KevinGonzalez/Archivos/salas.txt", "w")

archivo.write("sputnik\n\t")
archivo.write("apolo")

archivo.writelines(["houston\n", "artemis\n"])
archivo.close()