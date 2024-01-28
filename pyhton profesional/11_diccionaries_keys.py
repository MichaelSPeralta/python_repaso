another_dicc = {'a': 1, 'b':2, 'c':3, 'd':4}

keys = tuple(another_dicc.keys())
print(keys)

values = tuple(another_dicc.values())
print(values)

elements = another_dicc.items()
print(elements)

del another_dicc['a']
print(another_dicc)
valor = another_dicc.pop('b')
print(valor)
print(another_dicc)
another_dicc.clear()
print(another_dicc)
# para eliminar elementos del diccionario, tenemos que serciorarnos de que existen
# Diccionarios implementados mediante tablas de hash