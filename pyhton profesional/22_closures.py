# nonlocal
 # Closure, funciones que retornan funciones, a su vez estas funciones pueden acceder a variables locales, "tienen memoria"
def saludar(username):
    mensaje = f'Hola {username}'
    
    def mostrar_mensaje():
        print(mensaje)
    
    return mostrar_mensaje

username = 'Buzz Lightgear Comando Estelar'
respuesta = saludar(username)
username = 'Peppa Pig'
respuesta()
respuesta()
respuesta()
