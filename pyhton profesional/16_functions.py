def suma():
    numero_a = int(input("ingresa un numero entero: "))
    numero_b = int(input("ingresa otro numero entero: "))

    resultado = numero_a + numero_b
    print(f'resultado suma: {resultado}')

# suma()

####

def suma_con_parametros(num_a, num_b):
    return num_a + num_b

numero_a = int(input("ingresa un numero entero: "))
numero_b = int(input("ingresa otro numero entero: "))

resultado = suma_con_parametros(numero_a, numero_b)
print(f'resultado: {resultado}')

