#conjunto con set

conjunto = set(["Dato1","Dato2"])

#meter un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)

#teoria de conjuntos 

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificar subconjunto <=
resultado = conjunto2.issubset(conjunto1)
#verificar superconjunto > 
resultado = conjunto1.issuperset(conjunto2) 

#verificar si hay algun numero en comun //false si coinciden
resultado = conjunto2.isdisjoint(conjunto1)


print(resultado)