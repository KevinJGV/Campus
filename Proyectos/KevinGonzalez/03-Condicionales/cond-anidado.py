nombre = input("Nombre del Estudiante: ")
nota = int(input("Ingrese una nota [0-100]: "))

if nota >= 0 and nota <= 59:
    NotaCual = "D"
elif nota >= 60 and nota <= 79:
    NotaCual = "C"
elif nota >= 80 and nota <= 89:
    NotaCual = "B"
elif nota >= 90 and nota <= 100:
    NotaCual = "A"
else:
    NotaCual = ""
    print("No aprovò.")
print("\n", "-" * 30)
print("Estudiante: ", nombre)
print("Nota cuantitativa: ", nota)
print("Nota cualitativa: ", NotaCual)
