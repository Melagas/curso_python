#AND &

#Opcion = True & True = True
#Opcion = True & False = False
#Opcion = False & False = False

#OR | 

#Opcion = True | True = True
#Opcion = True | False = True
#Opcion = False | False = False

#NOT

#Opcion = not True = False
#Opcion = not False = True

#print(Opcion)


a = 10 
b = 12
c = 13
d = 10

operacion = ((a<b)or(a<c))and((a!=c)or(a<b))

print(operacion)

