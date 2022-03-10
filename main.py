from random import randint

#Pedimos los datos al usuario
nombre_fichero = input("\n\tDame el nombre del fichero: ")
caracteristica1 = input("\n\tDame la primera característica: ")
caracteristica2 = input("\tDame la segunda característica: ")
caracteristica3 = input("\tDame la tercera característica: ")
caracteristica4 = input("\tDame la cuarta característica: ")
caracteristica5 = input("\tDame la quinta característica: ")
minimo1 = int(input("\n\tMínimo de "+caracteristica1+": "))
maximo1 = int(input("\tMáximo de "+caracteristica1+": "))
minimo2 = int(input("\n\tMínimo de "+caracteristica2+": "))
maximo2 = int(input("\tMáximo de "+caracteristica2+": "))
minimo3 = int(input("\n\tMínimo de "+caracteristica3+": "))
maximo3 = int(input("\tMáximo de "+caracteristica3+": "))
minimo4 = int(input("\n\tMínimo de "+caracteristica4+": "))
maximo4 = int(input("\tMáximo de "+caracteristica4+": "))
minimo5 = int(input("\n\tMínimo de "+caracteristica5+": "))
maximo5 = int(input("\tMáximo de "+caracteristica5+": "))

#Función que devuelve un array con valores aleatorios entre dos rangos dados
def calcularValor(min, max):
    array = []

    for i in range(1000):
        array.insert(i, randint(min, max))

    return array

#Función que escribe en un fichero dado el contenido de los arrays dados
def escribirCaracteristicas(fichero, array1, array2, array3, array4, array5):
    file = open(fichero, "a+")

    for i in range(len(array1)):
        cadena = f"{array1[i]:3} {array2[i]:10} {array3[i]:10} {array4[i]:10} {array5[i]:10}"
        file.write(cadena+"\n")

    file.close()

#Inicializamos los array de valores según los varemos del usuario
array1 = calcularValor(minimo1, maximo1)
array2 = calcularValor(minimo2, maximo2)
array3 = calcularValor(minimo3, maximo3)
array4 = calcularValor(minimo4, maximo4)
array5 = calcularValor(minimo5, maximo5)

#Inicializamos el fichero, y llamamos a la función que lo escribe
file = open(nombre_fichero, "w")
cadena = f" {caracteristica1:10} {caracteristica2:10} {caracteristica3:10} {caracteristica4:10} {caracteristica5:10}"
file.write(cadena+"\n")
file.close()
escribirCaracteristicas(nombre_fichero, array1, array2, array3, array4, array5)

print("\n\tFichero generado!!")