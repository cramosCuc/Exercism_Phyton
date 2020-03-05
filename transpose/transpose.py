def transpose(lines):
    filas = [fila.replace(' ', '_') for fila in lines.splitlines()]
    filas = [fila.ljust(len(max(filas, key=len))) for fila in filas]
    filas = [''.join(fila) for fila in zip(*filas)]
    filas = [fila.rstrip().replace('_', ' ') for fila in filas]
    return '\n'.join(filas)
