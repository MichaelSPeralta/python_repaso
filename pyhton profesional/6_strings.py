lenguajes = 'Python  Ruby Java C++ JS'
lenguajesDash = 'Python-Ruby-Java-C++-JS'

listado_lenguajes = lenguajes.split()
listado_lenguajes2 = lenguajesDash.split('-')

print(listado_lenguajes)
print(listado_lenguajes2)

langJoinList = '-'.join(listado_lenguajes)

print(langJoinList)