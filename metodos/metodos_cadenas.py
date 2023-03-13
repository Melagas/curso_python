#cadenas

cadena1 = "hola soy Gaston"
cadena2 = 'a'
cadena = 'chau'

#dir devuelve los atributos validos del objeto pasado
#print(dir(cadena1)) FUNCTION

#DATO.METODO()

#mayusculas
resultado0 = cadena1.upper()
#minusculas
resultado1 = cadena1.lower()
#mayuscula primer letra
resultado2 = cadena1.capitalize()


#buscamos cadena en otra cadena, sino -1
resultado3 = cadena1.find('r')
#buscamos cadena en otra cadena, sino exepcion
resultado4 = cadena1.index('a')

#si es numerico True sino False
resultado5 = cadena2.isnumeric()

#si es alfanumerico
resultado6 = cadena2.isalpha()

#contar coincidenacias
resultado7 = cadena1.count("a")

#contar caracteres de una cadena //FUNCTION
resultado8 = len(cadena1)

#verificar si una cadena empieza con otra cadena dada
resultado9 = cadena1.startswith("hola")

#verificar si una cadena termina con otra cadena
resultado10 = cadena1.endswith("n")

#remplaza un pedazo de la cadena dada por otro
resultado11 = cadena1.replace("Gaston", "Pedro")

#separar la cedena con la cadena que le pasamos
resultado12 = cadena1.split(" ")

 
print(resultado12[2])
