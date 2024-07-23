"""
A partir de un input de una frase, contar cuantas veces aparece cada letra del abecedario. 
EL input es una ccadena de texto y se usan diccionarios para contar cuantas veces aparece cada letra

1ºEl usuario introduce una cadena de texto
2º Contar cuantas veces aparece cada letra del abecedario en esa cadena
3º Calcular el maximo
4º Sacar el valor del último elemento del diccioanrio

"""
#Contar la letra que aparece más veces
def max_freq(dictionary_input):
    max_letter = ''
    max_number = 0
    for i in dictionary_input:
        if dictionary_input[i]>max_number:
            max_number = dictionary_input[i]
            max_letter = i
    print("La letra que más aparece es la ", max_letter, " apareciendo ", max_number, " veces")

#User input
user_string = input("Introduzca una cadena de texto para contar cuantas veces aparece cada letra: ")

dictionary={}
counter = 0

#Recorremos todo la cadena
for i in user_string:
    #Si la letra ya está en el diccionario -> +1 al contador
    if i in dictionary:
        counter = dictionary[i] + 1
        dictionary[i] = counter
    #Si no está en el diccionario, añadimos la letra
    else:
        counter = 0
        dictionary[i] = counter + 1

#Llamamos a la función que cuenta la letra que aparece más veces
max_freq(dictionary)

