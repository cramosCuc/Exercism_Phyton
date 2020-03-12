def spiral_matrix(size):
    matriz = [[0]*size for row in range(size)]
    i, j, elemento = 0, -1, 1
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    for x in range(2*size - 1):
        for _ in range((2*size - x) // 2):
            i = i + di[x % 4]
            j = j + dj[x % 4]
            matriz[i][j] = elemento
            elemento = elemento + 1
    return matriz
