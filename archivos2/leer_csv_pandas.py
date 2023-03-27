import pandas as pd
df = pd.read_csv("archivos2\\datos.csv")
df2 = pd.read_csv("archivos2\\datos.csv")

#,names=["Name","Lastname","Age"]

#nombres = (df["nombre"])

print(df)
#jupiter ctrl+shift+p
#df dataframe

#slice
# cadena = "hola gaston"
# print(cadena[0:10])

#ordenar de menor a mayor
df_ordenado = df.sort_values("edad")
print(df_ordenado)

#ordenar de mayor a menor
df_por_edad_mas = df.sort_values("edad",ascending=False)
print(df_por_edad_mas)

#concat
df_concat = pd.concat([df,df2])
print(df_concat)

#acceder a las prmeras filas
primer_fila = df.head(2)
print(primer_fila)

#acceder a las ultimas filas
ultima_fila = df.tail(2)
print(ultima_fila)


#cantidad de filas y columnas
filas_columnas = df.shape
print(filas_columnas)

#info matc estadistica
df_info = df.describe()
print(df_info)

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]
print(elemento_especifico_loc)

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]
print(apellidos_loc)

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]
print(elemento_especifico_iloc)

#accediendo a todos los apellidos con iloc
apellidos = df.iloc[:,1]
print(apellidos)

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]
print(fila_3)

fila_2 = df.iloc[3,:]
print(fila_2)

#filas mayor que
mayor_que = df.loc[df["edad"]>25,:]
print(mayor_que)
