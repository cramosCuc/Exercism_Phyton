def is_paired(input_string):
    simbolos = {')': '(', '}': '{', ']': '['}
    pila = []
    for char in input_string:
        if char in simbolos.values():
            pila.append(char)
        elif char in simbolos:
            if not pila:
                return False
            if pila.pop() != simbolos[char]:
                return False
    return not pila

