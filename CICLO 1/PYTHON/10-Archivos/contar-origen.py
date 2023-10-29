def miFun(email):
    return len(email)

fd = open("Proyectos/KevinGonzalez/Archivos/mbox-short.txt", "r")

cl = 0
setEmail = set()
for linea in fd:
    if linea.startswith("From:"):
    # cl += 1
    # email = linea.split()[1]
    # print(email)
        setEmail.add(linea.split()[1])

fd.close()
cl = len(setEmail)
print("La cantidad de correos de origen distintos: ", cl)
for email in sorted(setEmail, key=miFun):
    print(email)