def CrearMatrices(fila, colum):
    m = []
    for i in range(fila):
        fila = [0] * colum
        m.append(fila)
    return m

def PrintMatriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = input()