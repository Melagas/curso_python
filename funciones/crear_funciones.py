def saludar():
    print("Hola Gaston")
    
#ejecutar funcion simple
saludar()

#funcion con parametros
def saludos(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
       adj = "reina"
    elif (sexo == "hombre"):
       adj = "rey"
    else:
       adj = "amor"
    print(f"Hola {nombre}, mi {adj}, como andas?")
    
saludos("Gaston","Hombre")
saludos("Lola","Mujer")
saludos("Agus","no binario")


#crear un a funcion que nos retorne valores

def password_random(num):
    chars = "asdfghjkl"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contra = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return (contra)

password = password_random(2)
frase = f"Tu contra nueva es: {password}"
print(frase)

    
    