import json

while True:
    try:
        archivo = input("Digite el nombre del archivo, ejemplo: datos.txt\n")
        archivo = archivo
        fd = open(archivo,"r")
        break
    except Exception as e:
        print("Error al intentar abrir el archivo, intente de nuevo...")
        continue


c = 0
promedio_total = 0
suma = 0
lstEmails = []
lst_spam = []
for linea in fd:
    if linea.startswith("From:"):
        email = linea.split()[1]
        lstEmails.append(email)
    if linea.startswith("X-DSPAM-Confidence:"):
        spam = linea.split()[1]
        spam = float(spam)
        lst_spam.append(spam)
        c += 1
b = input("Si desea imprimir el spam por cada correo digite S, de lo contrario digite cualquier tecla:\n")
for i in range(c):
    msj = f"Del email from:{lstEmails[i]} \nHubo {lst_spam[i]:.6f} spam"
    if b == "S":
        print(msj)
    suma += lst_spam[i]

promedio_total = suma/c

print(f"La sumatoria del spam fué de: {suma:.6f} \nY el promedio total de spam fué de: {promedio_total:.6f}")


fd.close()
