#crear diccionario con dict
diccionario = dict(nombre = "gaston", apellido = "mela")
#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["mela","gaston"]):"hola"}
#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])
#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"],"no se")

print(diccionario)