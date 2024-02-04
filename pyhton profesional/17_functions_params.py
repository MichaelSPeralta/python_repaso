def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2) 

resultado = area_circulo(10, 3.141592654)
print(resultado)

##### PARAMETROS #####

def promedio(*args):
    return sum(args) / len(args)

promedio(1,2,5,8,9,7,10,10)

def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)
    
combinacion(10,20,30,40,50,60,70,100,200,300,1000,2000,8000,p4=1503548)

##### ARGUMENTOS #####

def comb(*args, **kwargs):
    print(args)
    print(kwargs)

comb(1,2,3,4,5, cody=True, eduardo=[10,10,8], fernando=[4,8,7])