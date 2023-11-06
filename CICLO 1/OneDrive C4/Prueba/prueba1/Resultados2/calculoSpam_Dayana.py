mbox = open("mbox.txt", "r")
# mbox_short = open("campus/archivos/mbox-short.txt", "r")

arcTxt = ""

lineas = mbox.readlines()


def leerNomArchivo():
    
    # arc = input("Ingrese el archivo de texto: ")
    while True:
        try:
            print("Archivos de Texto:")
            print("*mbox.txt")
            print("*mbox-short.txt")
            arch1 = "mbox.txt"
            arch2 = "mbox-short.txt"

            arcTxt = str(input("Ingrese el archivo de texto: "))
            # arc.append(arcTxt)
            if arcTxt != arch1 and arcTxt != arch2:
                print("Opción no válida. Ingrese nuevamente el archivo a ver.")
                input("Presione cualquier tecla para continuar...")
                continue
            return arcTxt

        except ValueError:
            print("Opción no válida.")
            input("Presione cualquier tecla para continuar...")

mensSpam = []   
cl = []     

while True:
    ver = leerNomArchivo()
    if ver == "mbox.txt":
        mbox = open("mbox.txt", "r")
        print("Este es el archivo 1")
        break
    else:
        mbox_short = open("mbox-short.txt", "r")
        for spam in lineas:
            if spam.startswith('X-DSPAM-Confidence'):
                mensSpam.append(spam.split()[1])
                if mensSpam not in cl:
                    cl.append(mensSpam)
                    print(cl)
        break



# mbox_short.close()
mbox.close()
