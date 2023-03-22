numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]


#recreando funciones lambda(return automatico)
multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(3))
 
#funcion clasica
def multiplicar(x):
    return x*2
print(multiplicar(5))

#creando una funcion comun que diga si es par
def es_par(num):
    if (num%2==0):
        return True
    
#funcion numeros impares    
def es_impar(num):
    if (num%2==1):
        return True

#usando filter con una funcion comun
numeros_pares = filter(es_par,numeros)
numeros_impares = filter(es_impar,numeros)
print (list(numeros_pares))
print(list(numeros_impares))

#lo mismo pero con lambda 
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
numeros_impares = filter(lambda numero:numero%2 == 1, numeros)
print(list(numeros_pares))
print(list(numeros_impares))




