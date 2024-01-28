# son mutables
# sin indices, llaves.
# equivalente a un json.
import json

with open('matches.json') as user_file:
  parsed_json = json.load(user_file)

print(parsed_json)

diccionario = {}

diccionario['tema'] = 'Do not cry'

print(diccionario)
print(len(diccionario))

diccionario2 = {'total': 55, 10: 'Curso python', (1,2,3): True, 'total': 9.99}
# diccionario2['total'] = 12
print(diccionario2)

another_dicc = {'a': 1, 'b':2, 'c':3, 'd':4}
print(another_dicc.get('d'))
print(another_dicc.get('z'))
print(another_dicc.get('z', 'No existe'))
print(another_dicc.get('z', False))
print(another_dicc.get('z', {'none': 'None value from diccionarie'}))
print(another_dicc.setdefault('z', {'none': 'None value from diccionarie'})) # Almacenar llave en diccionario

print(another_dicc)