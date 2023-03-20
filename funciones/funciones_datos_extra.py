#creando funciones de 3 parametros

def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos un {adjetivo}"

frase_resultante = frase("Gaston","Mela","genio")
print (frase_resultante)

#utilizando keywords arguments
frase_resultante = frase(nombre = "Gaston", adjetivo= "genio", apellido = "Mela")

#keywords en la fuction
def frase(nombre,apellido,adjetivo = "genio"):
    return f"Hola {nombre} {apellido}, sos un {adjetivo}"

frase_resultante = frase("Gaston","Mela")
print (frase_resultante)
