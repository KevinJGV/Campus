"""
test - calculoSpam
"""
spamR="X-DSPAM-Confidence: "
def pedirRuta():
    rutaDir=""
    rutaInput=input("Ingrese el nombre del archivo sin la extensión: ")+".txt"
    ruta=rutaDir+rutaInput
    return ruta

def contarSpam():
    while True:
        try:
            r=pedirRuta()
            print(r)
            archivo=open(r,"r")
            lstSpam=[]
            for linea in archivo:
                if linea.startswith(spamR):
                    lstSpam.append(linea.split(" ")[1])
            archivo.close()
        except Exception:
            print("Hubo un error con la recuperación del archivo; intente de nuevo. ")
            continue
        break
    sumSpam=0
    for e in lstSpam:
        num=float(e.split("\n")[0])
        sumSpam+=num
    promSpam=(sumSpam)/len(lstSpam)
    return promSpam
#programa

print("\n" * 30)
print("*** CALCULO DE SPAM EN EL SERVIDOR DE CORREO ***".center(40))
print(f"Promedio de SPAM CONFIDENCE: {contarSpam()}")