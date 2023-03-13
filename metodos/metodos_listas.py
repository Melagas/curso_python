#creando una lista con list
lista = list([78, 6, 5, 26])

#cantidad de elementos de una lista
cantidad_de_elementos = len(lista)
print(cantidad_de_elementos)

#agregar elemento a la lista
lista.append(1)
#agregar un elemento a la lista en un indice especifico
lista.insert(4, 14)
#agregar varios elementos a la lista
lista.extend([23])

#eliminado un elemento de la lista por indice
lista.pop(0) #-1 para elimiar el ultimo o -2 el anteultimo
#removiendo un elemento de la lista por su valor
lista.remove(5)

#eliminar todos los elementos de la lista
#lista.clear()

#ordenarlos de mayor a menor o viseversa
lista.sort(reverse=False)

#buscar
buscador = lista.index(26)


print(lista)
print(buscador)



