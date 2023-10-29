# definiciones
def jugadores(nombre,ficha):
    return {"nombre":nombre,"ficha":ficha}

def ficha(valor):
    return {"valor":valor}

def tablero():
    return {"fila0": [["" for i in range(3)] for i2 in range(3)],
            "fila1": [["" for i in range(3)] for i2 in range(3)],
            "fila2": [["" for i in range(3)] for i2 in range(3)],}

