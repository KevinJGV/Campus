while True:
    try:
        nombre = input("Nombre de usuario: ")
        nombre = nombre.strip()
        if len(nombre) == 0 or nombre.isalnum() == False:
            print("Nombre inválido. Vuelva a ingresarlo.")
            continue
        break
    except Exception as k:
        print("Errror al ingresar el nombre.\n", k)
        

while True:
    try:
        estrato = int(input("Estrato del usuario [1-5]: "))
        if estrato < 1 or estrato > 5:
            print("Estrato inválido. Vuelva a ingresarlo.")
            continue
        break
    except ValueError:
        print("Error.")
    
if estrato == 1:
    tbas = 10000
elif estrato == 2:
    tbas = 15000
elif estrato == 3:
    tbas = 30000
elif estrato == 4:
    tbas = 50000
else:
    tbas = 60000

print(f"Usuario {nombre}, su tarifa basica es {tbas}")