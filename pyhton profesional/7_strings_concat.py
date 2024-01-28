name = 'Pedro Ismael'
lastname = 'Juarez Garrido'

fullname = name + ' ' + lastname

print(fullname)

fullname2 = 'Mr. %s %s.' %(name, lastname)

print(fullname2)

print('###############################################')
###############################################

nombre_completo = 'Mr. {} {} {}.'.format(name, lastname, '- ADMIN')
print(nombre_completo)

nombre_completo2 = 'Mr. {name} {lastname} {role}.'.format(name=name, lastname=lastname, role='- SUPERUSER')
print(nombre_completo2)

anothername = f'Mr. {name} {lastname} - EXTERNAL.' # interpolacion
print(anothername)