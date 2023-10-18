# 4. Diseñe un algoritmo con funciones y procedimientos que indique si un estudiante ganó o perdió un curso después de presentar los cinco trabajos asociados al curso (Notas entre 0.0 y 5.0). Los trabajos tienen igual peso sobre la nota final y se gana el curso si la nota definitivaes superior a 3.5

def ing_nota(msj):
    while True:
        try:
            #cantNotas = 6
            #Notas = []
            nota = float(input(msj))
            
               
            if nota < 0 or nota > 5:
                print("Ingrese un valor en el rango indicado.")
                continue

            return nota
            
            
        except ValueError:
            print("Ingrese una nota correcta.")

def cant_notas(msj):
        while True:
            try:
                #cantNotas = 6
                #Notas = []
                cant_notas = int(input(msj))
                
                
                if cant_notas < 0:
                    print("La cantidad no puede ser negativa.")
                    continue

                return cant_notas
                
                
            except ValueError:
                print("Ingrese un numero.")

cant_notas = cant_notas("Ingrese la cantidad de notas:")
#ing_nota("Ingrese la nota (0-5): ")

for i in range(1, cant_notas+1):
    nota= ing_nota(f"Ingrese la nota #{i}: ")
    print(f"nota {i}: {nota}")


