def rows(letter):
    lineas = ord(letter) - 64
    columnas = lineas * 2 - 1
    half = make_half(lineas, columnas)
    return half + half[-2::-1]


def make_half(lineas, columnas):
    diamond_half = []
    for number in range(lineas):
        fila = [' '] * columnas
        fila[lineas - 1 - number] = chr(number + 65)
        fila[lineas - 1 + number] = chr(number + 65)
        diamond_half.append(''.join(fila))
        
    return diamond_half
