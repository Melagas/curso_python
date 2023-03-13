#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
curso_dalto = 1.5

#diferencias de duracion

diferencia_con_min = 100 - curso_dalto / otros_cursos_min * 100
diferencia_con_max = 100 - curso_dalto * 1000 // otros_cursos_max / 10
diferencia_con_prom = 100 - curso_dalto / otros_cursos_prom * 100
print("-------------------")
print("el curso de dalto dura:")
print(f"{diferencia_con_min}% menos que el mas rapido")      
print(f"{diferencia_con_max}% menos que el mas lento")      
print(f"{diferencia_con_prom}% menos que el promedio")
print("-------------------")
#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

tiempo_vacio_promedio = 100 - otros_cursos_prom * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - curso_dalto *1000 // crudo_dalto / 10

print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio")

#mostrando dif si los cursos duraran 10hs
print("-------------------")
print(f"ver 10 horas de este curso equivale a ver {otros_cursos_prom * 100 // curso_dalto / 10} horas de otrros cursos")
print(f"ver 10 horas de otro curso equivale a ver {curso_dalto *100 // otros_cursos_prom /10} horas de dalto")
