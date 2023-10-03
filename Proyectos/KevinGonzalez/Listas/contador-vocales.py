letras = []
while True:
    letra = input("Ingrese una letra del abcdario: ")
    if not letra.isalpha():
        print(">>>  ERROR. LETRA NO VALIDA.\n")
        input()
        continue

    letras.append(letra)

    op = input("\nDesea continuar? (S/N): ")
    if op.lower() != "s":
        break

print("\n", "=" * 30)
vocales = ["a", "e", "i", "o", "u"]
canVocales = [0] * 5
for l in letras:
    if l.lower in vocales:
