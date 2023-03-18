diccionario = {
    "nombre": "Gaston",
    "apellido": "Mela",
    "edad": 26   
}

for key in diccionario:
    print(key)

#recorriendo diccionario 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"Las keys son : {key} y los valores son {value}")