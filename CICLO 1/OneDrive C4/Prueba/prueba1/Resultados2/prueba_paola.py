#EJERCICIO
#Calcular promedio de todo  el servidor 

def calcularSpam(archivo):
    try:
        with open("mbox.txt", 'r') as file:
            totalSpam = 0
            totalEmails = 0
            for linea in file:
                if linea.startswith("X-DSPAM-Confidence:"):
                    confSpam = float(linea.split(":")[1])
                    totalSpam += confSpam
                    totalEmails += 1

            if totalEmails > 0:
                promedioSpam = totalSpam / totalEmails
                return promedioSpam
            else:
                return 0

    except ValueError:
        return None

nombreArchivo = input("Ingrese el nombre del archivo: ")


promedio = calcularSpam(nombreArchivo)

if promedio is not None:
    print(f"El promedio de SPAM en el servidor es: {promedio:.8f}")
else:
    print("No se encontró el archivo.")
