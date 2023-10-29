import io

def readNum(num):
    while True:
        try:
            n = int(input(num))
            if n < 1:
                print("Error: Ingreso invalido. Defina cuantos registros desea crear.")
                input()
                print("\n", "=" * 30, "\n")
                continue
            return n
        except ValueError:
            print("Error: Ingreso invalido. Debe ser un numero.")
            input()
            print("\n", "=" * 30, "\n")

def temp(msj):
    while True:
        temp = input(msj)
        if temp.isdigit():
            return temp
        elif temp == "" or temp.startswith("-") or temp.isalnum():
            print("////////////////////////////////////////////\nPara este ejercicio solo se valen temperaturas positivas y digitos.\nReingrese un valor correcto.")
            input()
            continue
def compare_temps(tempa,tempb):
    try:
        while True:
            tempa = int(tempa)
            tempb = int(tempb)
            if tempa = tempb:
                print("El ingreso de temperaturas es incorrecto, ingreselas nuevamente.")
                tempa = temp("Ingrese la temperatura minima registrada: ")
                tempb = temp("Ingrese la temperatura maxima registrada: ")
            else:
                return tempa, tempb
    except Exception as e:
        print("Se cometio un error en el ingreso de datos.")
        input()



def UI_Creador(main_storage):
    print("//" * 10, "CREADOR MANUAL DE REGISTROS METEREOLOGICOS".center(50), "//" * 10, "\n\n", "Para propositos del requerimiento del filtro y hacer interactivo la lectura de los archivos .csv usted mismo creara los registros que se evaluaran :)\n Se le solicitara:\n1-Código del observatorio\n2-Nombre del observatorio\n3-Fecha del registro (día, mes y año)\n4-Temperatura máxima y temperatura mínima.\n Esto segun la cantidad de archivos que especifique creara.\n")
    i = readNum("¿Cuantos registros desea crear? => ")
    
    for it in range(1, i+1):
        id = input(f"Defina el còdigo que identifica al observatorio #{it}: ")
        nom = input(f"Defina el nombre del observatorio #{it}: ")
        dia = input("Ahora especificara la fecha del registro suministrando dia, mes y año.\nDia del registro: ")
        mes = input("Mes del registro: ")
        año = input("Año del registro: ")
        fecha = dia + "/" + mes + "/" + año
        print(f"Fecha ingresada: {fecha}")
        temp_min = temp("Ingrese la temperatura minima registrada: ")
        temp_max = temp("Ingrese la temperatura maxima registrada: ")
        temp_min, temp_max = compare_temps(temp_min, temp_max)
        storage = [id,nom,fecha,temp_min,temp_max]
        main_storage.append(storage)
    print("=" * 50,"\nCon la informacion que suministro se creara el archivo \"Datos.csv\" a partir del cual se hara la siguiente parte del filtro.\n Su Lista de datos esta en la linea 3 de ese archivo.")
    return registro


f = open("Datos.csv", "w")
registro = []
UI_Creador(registro)
registro = str(registro)
start = "/////////////////////////////// REGISTROS METEOROLOGICOS SISTEMA SAPO ///////////////////////////////\n\n"
f.write(start)
f.write(registro)

f.close()