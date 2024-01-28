lista = ['Estring', 2, 2.4, False] # list()

print(lista)

lista_cursos = ['python', 'java', 'javascript', 'ruby']
lista_cursos_2 = ['k8s', 'docker', 'terraform', 'grafana']
primer_curso = lista_cursos[0]

print(primer_curso)

sub_lista = lista_cursos[0:3]
print(sub_lista)

lista_invertida = lista_cursos[::-1]
print(lista_invertida)

#  Modificar Lista
lista_cursos.append('MongoDB')
lista_cursos.append('C#')

lista_cursos.insert(1, 'Rails')

lista_cursos.extend(lista_cursos_2)
print(len(lista_cursos))
print(lista_cursos)

# Eliminar de lista
lista_cursos.remove('terraform')
print(lista_cursos)

del lista_cursos[-1]
print(lista_cursos)

lista_cursos.clear()
print(lista_cursos)