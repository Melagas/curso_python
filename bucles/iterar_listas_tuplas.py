#listas
animales =  ("perro","gato","loro","cocodrilo","pez") #[]listas / tuplas()
numeros = (2,3,5,6,9) #[]listas / tuplas()

#recorrer una lista
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")

#recorrer y multiplicar una lista  
for numero in numeros:
    resultado = numero * 2
    print(f"Los numeros son: {resultado}")
    
#recorrer dos listas juntas
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1:{numero}")
    print(f"recorriendo lista2:{animal}")
 
#recorrer una lista con su indice   
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"indice: {indice} valor: {valor}")
    
#usando el ELSE
for numero in numeros:
    print (f"Los numeros son:{numero}")
else:
    print("no hay mas numeros")
    