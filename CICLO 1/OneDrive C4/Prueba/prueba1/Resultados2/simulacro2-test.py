
def miFuncion(email):
    return len(email)

def leerNombre(msj): 
    while True:
        try:
            nom = input(msj)
            nom = nom.strip()
            if len(nom) == 0 :
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def principal():
    nombreArchivo = leerNombre("Ingrese el nombre del archivo: ")
    try:
        fd = open(''+nombreArchivo, 'r')
        setSpam = []
        for linea in fd:
            if linea.startswith('X-DSPAM-Confidence:'):
                setSpam.append(linea.split()[1])
    except Exception as e:
        print("Error el archivo al que intento acceder no existe", e)
        return None
    fd.close()

    cont = 0
    acum = 0

    for spam in sorted(setSpam, reverse = False, key = miFuncion):
        cont += 1
        acum += float(spam)
        # print(spam)
    promedioSpam = acum / cont
    print("\nEl promedio de spam confidence es:")
    print(promedioSpam)

principal()
