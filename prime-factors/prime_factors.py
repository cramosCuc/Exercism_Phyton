def factors(valor):
    factores = []
    divisor = 2
    while valor > 1:
        while valor % divisor == 0:
            factores.append(divisor)
            valor /= divisor
            
        divisor = divisor + 1
        
    return factores