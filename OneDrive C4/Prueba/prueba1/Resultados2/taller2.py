nombre = input("Indique el nombre del archivo con su extension: ")
ruta = "" + nombre

fd = open(ruta, "r")
# tomo las lineas que inician con X-DSPAM-Confidence.
bandera = 0
dato = 0
for linea in fd:
    if linea.startswith("X-DSPAM-Confidence:"):
        linea.strip
        dato += float(linea.split()[1])
        bandera += 1
promedio = dato / bandera
print(f"Average SPAM confidence: {promedio}")

        
