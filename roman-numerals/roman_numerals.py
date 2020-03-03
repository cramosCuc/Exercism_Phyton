Map_Romanos = ( (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
)
def roman(numero):
    resultado = ''
    for arabic, roman in Map_Romanos:
        while numero >= arabic:
            resultado = resultado + roman
            numero -= arabic
    return resultado
