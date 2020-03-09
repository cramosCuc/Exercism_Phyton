def find(search_list, value):
    bajo = 0
    alto = len(search_list) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if search_list[medio] > value:
            alto = medio - 1
        elif search_list[medio] < value:
            bajo = medio + 1
        else:
            return medio
    raise ValueError("El valor no fue encontrado")
