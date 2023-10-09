# def prepararCafe(insumo1, insumo2):
#     if insumo1.lower() == "cafe" and insumo2.lower() == "agua":
#         salida = "tinto"
#     else:
#         salida = "Daño la cafetera."
#     return salida

# vaso = prepararCafe("agua", "cafe")

# print(vaso)
# print(longString(vaso))

# def casa(direccion, edad):
#     return f"La direccion de tu casa es: {direccion}\n Tiene {edad} años de edad."


# a = casa("Carrera 3", "65")
# print(casa(a, "1"))

def nospaces(palabra):
    texto = ""
    for char in palabra:
        if char != " ":
            texto += char
    return texto

def reverse(palabra):
    textoReverse = ""
    for char in palabra:
        textoReverse = char + textoReverse
    return textoReverse

def palindromo(palabra):
    palabra = nospaces(palabra)
    palabraReverse = reverse(palabra)
    return palabra.lower() == palabraReverse.lower()

print("amo la ploma", palindromo("Amo la paloma"))
