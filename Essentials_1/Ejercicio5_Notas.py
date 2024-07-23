#Ejercicio 3:

# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. 
# Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 

#Variables
school_class = {}

while True:
    choice = input("- A Añadir nota\n- L Listar notas\n- S Salir")
    if choice.upper == 'S':
        break
    elif choice.upper == 'A'
        name = input("Introduzca el nombre del alumno: ")
        if name in school_class:
            print("Notas: ",school_class[name])
            score = int(input("Introduzca la calificación del alumno: (0-10) ")) 
            



    
