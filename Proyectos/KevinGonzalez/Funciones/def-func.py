def longString(str):
    try:
        long = 0
        while str(long) != None:
            long += 1
    except:
        pass
    return long

# def prepararCafe(insumo1, insumo2):
#     if insumo1.lower() == "cafe" and insumo2.lower() == "agua":
#         salida = "tinto"
#     else:
#         salida = "Daño la cafetera."
#     return salida

# vaso = prepararCafe("agua", "cafe")

# print(vaso)
# print(longString(vaso))
