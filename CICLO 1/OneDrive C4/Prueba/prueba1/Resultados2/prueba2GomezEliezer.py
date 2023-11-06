import json
import io
def promedio(a, b):
    return (a * b)



#a = input("ingrese el nombre del archivo: ")
f = open("mbox.txt","r")
contSp = 0
ruta = "ACME.txt"
for line in f:
     list = []
     if line.startswith("X-DSPAM-Confidence: "):  
        line  = line.strip()
        numero = line.splitlines()
        #print(line)
        #ap =  lista_de_spam.append(line)
          #spamp = line. 
        contSp +=1

a = input("ingrese el nombre del archivo: ")
p = int(input("ingrese el codigo del spam que desea ver"))

print(f"este es el ususario: {a}, codigo : {p} -----> {numero}")
#print(contSp)
#print(line)
#print(ap)
#print(correos)




f.close()
