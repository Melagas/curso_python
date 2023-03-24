archivos = open("archivos\\lluvia.txt",encoding="UTF-8")
#archivo = archivos.read()
#print(archivo)

#leer por lineas
#lineas = archivos.readlines()
#print(lineas)

linea = archivos.readline()
print(linea)

#cerrar archivo
archivos.close()

