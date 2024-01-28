entrada = 10

if False:
    if entrada >= 10 and entrada < 20:
        print('Entro a zion.')
    else:
        print('No podes entrar.')


if False:
    entrada = 10
    if entrada == 10:
        print('Aprobaisimo!')
    elif entrada > 4 and entrada <= 9:
        print('Pase.')
    else:
        print('Sorry, te falto para llegar al Nirvana.')
        
# Ternario.
if True:
    calificacion = 7
    color = 'Verde' if calificacion >= 7 else 'Rojo'

    print(color)
    
    ##############
    
    listado = [] # False // See 12_type_none.py
    nombre = 'Cody'
    
    variable = listado or nombre
    
    print(variable)