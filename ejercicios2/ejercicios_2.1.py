#falto el profesor y los chicos arman la clase

#obtener al profesor y asistente por edad
def obtener_compañeros(cantidad_de_compañeros):
    #creando lista 
    compañeros = []
    #ejecutamos un for para pedir info
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingresa tu nombre: ")
        edad = int(input("Ingresa tu edad: "))
        compañero = (nombre,edad)
        
        #agregando informacion a la lista
        compañeros.append(compañero)
    
    #ordenarlos de menor a mayor en la lista
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#mostrat el resultado
print(f"El profesor es {profesor} y su asistente es {asistente}")


    