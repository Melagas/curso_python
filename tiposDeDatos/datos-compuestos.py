#creando una lista, se puede modificar (list)
#lista = ["Gaston Mela", "Mendiolaza", True, 1.65]

#creando una tumpla, no se puede modificar (tuple)
#tupla = ("Gaston Mela", "Mendiolaza", True, 1.65)

#esto es valido
#lista[3]= 1.64

#esto no es valido
#tupla[3]= 1.64


# print(tupla)
#print(lista[3])


#creando un conjunto (set) no se puede acceder a un indice sin un bucle, no modificar(si ampliar como el tuple), no duplicar datos

conjunto = {"Gaston Mela", "Mendiolaza", True, 1.65}

#crear un diccionario (dict)

diccionario = {
    'nombre': "Gaston",
    'edad': 26,
    'esta_emocionado': True,
    'altura': 1.65
}

print(diccionario['altura'])
