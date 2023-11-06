#La empresa ACME desea saber cual es su indice promedio de SPAM en su servidor de correo.
#Para calcular se le pide construir un programa que lea el archivo y calcule el promedio de SPAM
#de todo el servidor. El indicador de SPAM por cada correo se encuentra en el parámetro X-
#DSPAM-Confidence. Este programa será ejecutado por el administrador de infraestructura por lo
#tanto el programa debe pedir el nombre del archivo que se va a leer.

# inicio
fd = open("mBox2.txt","r")

fd = input("por favor ingrese el nombre del archivo que contiene los correos: ")

try:
    archivo = open(fd, "r")
    cantidadCorreos = 0
    sumaSpam = 0
    
    for linea in archivo:
        if linea.startswith("x-DSPAM-Confidence: "):
            try:
                spamConfidence = float(linea.split(":")[1])
                sumaSpam += spamConfidence
                cantidadCorreos += 1
            except ValueError:
                print("Error al procesar una linea, se pasa")
                    
            
    if cantidadCorreos > 0:
        promedioSpam = sumaSpam / cantidadCorreos
        print(f"El promedio de spam es: {promedioSpam}",)
    else:
        print("No se encontraron correos con SPAM")
        
        archivo.close()

except FileNotFoundError:
    print("El archivo no existe")
except Exception as e:
    print(f"ocurrio un error: {str(e)}")
    
    
    
