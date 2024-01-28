# Las tuplas son inmutables.
tupla = ('String', 10, 3.14, True, [1, 2, 3], (4, 5, 6))

print(tupla)

ultimo = tupla[-1] 
print(ultimo)

segundo = tupla[1] 
print(segundo)

tercero = tupla[:]
print(tercero)

# tuple , list
lista_tupla = list(tupla)
print(type(lista_tupla))
print(lista_tupla)

tuple_list = tuple(lista_tupla)
print(type(tuple_list))
print(tuple_list)

# descomprimir 
# *
# omitir valor _

numeros = (1,2,3,4,5,6,7,8,9,10)
uno, _, *_, ultimo = numeros

print(uno)
print(ultimo)

# comprimir zip
list_1 = [1,2,3,4]
tuple_1 = (10,20,30,40)
list_2 = [100,200,300,400]
tuple_2 = (1000,2000,3000,4000)

result = zip(list_1, tuple_1, list_2, tuple_2)
result = tuple(result)
print(result)