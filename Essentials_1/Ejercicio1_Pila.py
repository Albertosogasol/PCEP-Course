"""
Construir una pila en la que se puedan añadir y quitar elementos.
Si se añaden, se añaden al final de la pila

Si se eliminan, se elimina el último que ha entrado. 

"""
option =''
stack = []

while option !='S':
    option = input("Seleccione la opcion a ejecutar: A-Añadir, E-Eliminar, S-Salir").upper()

    if option == 'A':
        value = int(input("Inserte el valor a añadir: "))
        stack.append(value)

    elif option == 'E':
        if len(stack):
            del stack[-1]
    print(stack)

print("Cerrando...")

#Se podría añadir la funcionalidad de eliminar la posición deseada y todas las que están por encima de ella para poder llegar hasta esa. 
