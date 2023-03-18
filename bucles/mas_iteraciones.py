frutas = ["banana","pera","manzana","higo","ciruela","mandarina","limon"]
cadena = "HOLA MUNDO!"
numeros = [1,2,3,4,5]
#evitando que se coma la pera usando continue
# for fruta in frutas:
#     if fruta == "pera":
#         continue
#     print(f"me voy a comer una {fruta}")
    
#evitar que el bucle continue
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == "pera":
        break
    
print("Ya me llené")

for letra in cadena:
    print(letra)
    

#for en una linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

