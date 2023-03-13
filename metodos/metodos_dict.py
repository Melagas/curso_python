diccionario = {
    "nombre": 'Gaston',
    "apellido": 'Mela',
    "edad": 26
}
#keys devuelve un objeto dict_item
claves = diccionario.keys()

#get obtiene un elemento
claves1 = diccionario.get("nombre")

#clear borra todo el dict
#diccionario.clear()

#pop eliminar un elemento o mas
#diccionario.pop("apellido")

#obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)
