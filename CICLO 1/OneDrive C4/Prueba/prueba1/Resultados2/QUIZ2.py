#Hacer un progama con el que un administrador pueda revisar
#el indice de SPAM.

#sabemos que el indice del spam es el X-DSAPAM Confidence
#entonces abria que sumar cada uno de los resultados para
#luego dividirlos.


#Creando la entrada del usuario

def miFun(email):
    return email

fd = open("mbox.txt", "r")

cl = 0
setEmail = set()
for linea in fd:
    if linea.startswith("X-DSPAM-Confidence:"):
        #cl += 1
        #email = linea.split()[1]
        #print(email)
        setEmail.add(linea.split()[1])

fd.close()
contarlineas = len(setEmail)


for email in sorted(setEmail, reverse=False, key=miFun):


    while True:
        try:
            archivo = input("Ingrese el archivo: ")
            if archivo == ("mbox.txt"):
                abrir = open("mbox.txt","r")
            print("Este archivo que abriste tiene un total de spam de: ", email)
        except ValueError:
            print("Hubo un error")
            continue
        break
            
