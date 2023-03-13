#usuario crea la frase por un input
frase = input("Decime una frase y te dig cuanto tardarias en decirla: ")

#creamos una lista con espacios
palabras_separadas = frase.split(" ")

#contamos la cantidad de palabras
cantidad_palabras = len(frase)

#si tarda mas de un minuto mostrar:
if cantidad_palabras > 120:
    print("no te pedi un testamento")
    
#calculamos cuanto tardaria la persona y cuanto tardaria dalto
print(f"dijiste {cantidad_palabras} palabras, tardarias {cantidad_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_palabras/2/1.3} segundos")
