usuarios = ['usuario1','usuario2','usuario3','usuario4','usuario5',]

for usuario in usuarios:
    print(usuario)
    
# Break, Continue
titulo_curso = 'Curso Profesional Python'

for caracter in titulo_curso:
    
    if caracter == ' ':
        continue
    elif caracter == 'y':
        break
    print(caracter)