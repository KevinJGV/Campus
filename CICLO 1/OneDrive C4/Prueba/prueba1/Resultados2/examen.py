# Este programa calcula el promedio de SPAM en un servidor de correo interactuando con el usuario por medio de la simulacion de una barra de busqueda:

def promedio_spam(archivo):
    try:
        archivo = open("mbox.txt", "r")
    except FileNotFoundError:
        print("El archivo no existe o no se puede leer.")
        exit()
    contenido = archivo.read()
    archivo.close()
    indicador_spam = []

    for linea in contenido.splitlines():
        if "X-DSPAM-Confidence:" in linea:
            try:
                indicador_spam.append(float(linea.split(":")[1]))
            except ValueError:
                print("No se pudo convertir el indicador de SPAM a un número.")
                exit()
    promedio_spam = sum(indicador_spam) / len(indicador_spam)
    return promedio_spam

archivo = input("Introduzca el nombre del archivo: ")
promedio_spam = promedio_spam(archivo)
print("Promedio de SPAM:", promedio_spam)
