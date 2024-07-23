#Ejercicio 2:
# Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. 
# El programa nos dará el siguiente menú:
# 
# * Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. 
# * Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# * Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# * Listar: Nos muestra todos los contactos de la agenda.

#Variables
diary = {}
choice = ''
name = ''
phone = ''
choice_modify = ''
find = ''

#Diccionario de prueba
#diary = {'Alberto':'123456', 'Angel':'89756', 'Elena':'456798' }

#Bucle principal
while True:
    choice = input("Introduce una opción: -A Añadir modificar, -B Buscar, -D Borrar, -L Listar, -S Salir --> ")
    if choice == 'S':
        break
    elif choice == 'A':
        name = input("Introduzca un nombre: ")
        if name in diary:
            print("Teléfono: ", diary[name])
            choice_modify = input("¿Desea modificar el teléfono? S-Si N-No")
            if choice_modify == "S":
                phone = input("Introduzca el nuevo número: ")
                diary[name] = phone
        else:
            print("Contacto no encontrado en la agenda. Se añadirá")
            phone = input("Introduzca el número del teléfono: ")
            diary[name] = phone
    elif choice == 'B':
        #Usar el método startwith para realizar una búsqueda
        """
        for nombre, numero in agenda.items():
            if nombre.tartswith(cadena):
            
        """
        name = input("Introduzca un nombre para buscar: ")
        if name in diary:
            print("El número de teléfono de: ", name, " es: ", diary[name])
        else:
            print("Contacto no enncontrado!")
    elif choice == 'D':
        name = input("Introduzca el nombre del contacto a borrar: ")
        if name in diary:
            choice_delete = ""
            choice_delete = input("¿Desea borrar el contacto ", name, "? S-Sí, N-No ")
            if choice_delete == 'S':
                del diary[name]
            else:
                continue
    elif choice == 'L':
        for i in diary.items():
            print(i)
    else:
        print("Introduzca una opción válida")
        continue