

ruta = input("Ingrese la ruta del archivo: ")
fd  = open(""+ruta, "r")
    

def calcularPromSpam(lstSpam):
    sumatoria = 0
    for i in lstSpam:
        sumatoria += i
    promedio = sumatoria / len(lstSpam)
    return promedio 



lstSpam = []
for linea in fd:
    if linea.startswith("X-DSPAM-Confidence:"):
        spam = float(linea.split()[1]) 
        lstSpam.append(spam)


print("Average spam confidence", calcularPromSpam(lstSpam))



fd.close()
    