#Resuelto por el profesor

#Inicializamos la lista sin valores
pila=[]

while True:
    op = input("Introduzca una operación: A-Añadir, E-Eliminar, S-Salir" ).upper()

    if op not in ("A","E","S"):
        continue
    elif op == "S":
        break
    elif op == "A":
        valor = int(input("Introduce el valor: "))
        pila.append(valor)

    else:
        if len(pila) > 0:
            valor = pila[-1]
            del pila[-1]
            print(valor)
        else:
            print("Pila vacía!!")
            continue
    print("Tamaño de la pila: " + str(len(pila)))
            
