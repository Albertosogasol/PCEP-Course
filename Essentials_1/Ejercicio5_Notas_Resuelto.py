#Ejercicio 3 
# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase 
# y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. 
# Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 

alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guradar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    notas = []
    nota = 0
    while nota >= 0:
        nota = int(input("Introduce una nota (negativo para terminar)"))
        if nota >= 0: 
            notas.append(nota)
    alumnos[alumno] = notas

for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f " % (alumno, sum(notas)/len(notas)))