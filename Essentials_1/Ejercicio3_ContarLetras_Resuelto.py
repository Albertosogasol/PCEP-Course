#Ejercicio contador caracteres en cadena
texto = input("Introduce una frase: ")
dicc = {}

for char in texto:
    #print(char)
    char = char.lower()
    if char in dicc:
        dicc[char] = dicc[char] + 1
        #dicc[char] += 1
    else:
        dicc[char] = 1

for key, value in sorted(dicc.items()):
    print(key, " : ", value)

key_value = ""
max_value = 0
for key, value in dicc.items():
    if value > max_value:
        key_value = key
        max_value = value

print("La letra", key_value, "es la que aparece mas veces: ", max_value)
print("El ultimo elemento del dicc es: ", [key for key in dicc.keys()][-1])
print("El ultimo elemento del dicc es: ", list(dicc.keys())[-1])
print("El ultimo elemento del dicc es: ", [(key,value) for key,value in dicc.items()][-1])


