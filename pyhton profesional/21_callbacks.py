promedio = lambda *args : sum(args) / len(args)
aprobatorio = lambda calificacion : calificacion >= 6

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)
    
    if func_aprobatorio(promedio):
        print(f'Felicitaciones aprobaste con {promedio}.')
    else:
        print(f'Lo siento, no aprobaste, tu calificacion es {promedio}.')

mostrar_mensaje(promedio, aprobatorio, 1,8,9,5,7,10)

