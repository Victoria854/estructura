# # #EJERCICIO_1. Cree un programa que le pida al usuario una serie de numeros cualquiera y que solo dejaremos de hacerlo cuando el usuario ingrese un numero igual a cero
# print("EJERCICIO 1")
while True:
    try:
        number = int(input("Ingrese un numero: "))
        if number == 0:
            print("Fin... ingreso el numero 0")
            break
    except ValueError:
        print("No ingreso un numero, Ingrese nuevamente: ")
print("--------------------------------------")

# # EJERCICIO_2. Ingrese un numero positivo y muestrelo, caso contrario solicite nuevamente  el numero
print("EJERCICIO 2")
while True:
    try:
        number = int(input("Ingrese un numero: "))
        if number <= 0:
            print("El número es negativo. Ingrese un nuevamente: ")
        else:
            print("El numero ",number," es positivo")
            break
    except ValueError:
        print("No ingreso un numero. Ingrese nuevamante")

print("--------------------------------------")
#
# #EJERCICIO_3. Leer numeros enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los numeros ingresados
print("EJERCICIO 3")
counter = 0
while True:
    try:
        number = int(input("Ingrese un numero: "))
        counter = counter + number
        if number == 0:
            print("La suma de los numeros ingresados es: ", counter)
            print("Fin... ingreso el numero 0")
            break
    except ValueError:
        print("No ingreso un numero. Ingrese nuevamente: ")
print("--------------------------------------")

# #EJERCICIO_4. Leer un numero entero positivo desde teclado e imprimir la suma de los digitos que lo componen
# print("EJERCICIO 4")
while True:
    try:
        number = int(input("Ingrese un numero: "))
        if number <= 0:
            print("Ingreso un numero negativo. intente otra vez: ")
        else:
            addition = 0
            while number > 0:
                addition = addition + (number % 10)
                number = number // 10
            print("La suma de los digitos que componen el numero es: ",addition)
            break
    except ValueError:
        print("No ingreso un numero. Ingrese nuevamente: ")
print("--------------------------------------")

# #EJERCICIO_5. Solicitar al usuario que ingrese numeros enteros positivos y, por cada uno imprimir la suma de los digitos
# # que lo componen. la condicion de corte sera al ingresar el numero -1. Al finalizar mostrar cuantos de los numros ingresados por el usuario fueron pares.
print("EJERCICIO 5")
counter = 0
addition = 0
numbers = 0
while numbers > -1:
    try:
        numbers = int(input("Ingrese un numero: "))
        if numbers % 2 == 0:
            counter = counter + 1
        while numbers > 0:
            addition = addition + (numbers % 10)
            numbers = numbers // 10
        print("La suma de los digitos que componen el numero es: ",addition)
        addition = 0
    except ValueError:
        print("No ingreso un numero. Ingrese nuevamente: ")
print("Hay ", counter, "numeros pares")
print("--------------------------------------")

#EJERCICIO_6. Mostrar un menu con tres opciones: 1. comenzar programa, 2.imprimir listado, 3. finalizar programa.
#a continuacon, el usuario debe poder seleccionar una opcion (1,2 o 3). Si elige uan opcion incorrecta, informarle el error.
#El menu se debe volver a mostrar luego de ejecutada cada opcion, permitiendo volver a elegir. Si las opciones 1 o 2 se imprimira un texto. Si elige la opcion 3, se interrumpira la impresion del menu y el programa finalizara.
print("EJERCICIO 6")
while True:
    print("Menu de opciones: ")
    print("1. Comenzar programa")
    print("2. Imprimir listado")
    print("3. Finaliazar programa")
    try:
        option = int(input("Elija una opcion: "))

        if option == 1:
            print("Bienvenido al programa")
        elif option == 2:
            print("Listado de alumnos de software A1:")
            print("Aguilar Jefferson")
            print("Penafiel Miguel")
            print("Rodriguez Eduardo")
            print("Sagnay Victoria")
            print("Zeas Christopher")
        elif option == 3:
            print("Finalizando el programa...")
            break
        else:
            print("Opcion invalida, vuelva a seleccionar otra opcion")
    except ValueError:
        print("La opcion esta representada por un numero. Ingrese nuevamente: ")
print("--------------------------------------")

# # #EJERCICIO_7. Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada,
# # #En cada iteracion, solicitar al usuario que ingrese un numero. Al finalizar, mostrar la suma de todos los numeros ingresados.
print("EJERCICIO 7")
counter = 1
while True:
    try:
        limit = int(input("Ingrese cuantos numeros desea sumar: "))
        addition = 0
        while counter <= limit:
            try:
                numbers = int(input(f'Ingrese el {counter}° numero: '))
                addition = addition + numbers
                counter = counter + 1
            except ValueError:
                print("No ingreso un numero. Ingrese nuevamente: ")
        print("La suma de todos los numeros es: ", addition)
        break
    except ValueError:
        print("No ingreso un numero. Ingrese nuevamente: ")
#
print("--------------------------------------")
#
# #EJERCICIO_8. Solicitar al usuario que ingrese una frase y luego imprimir las vocales que se encuentran en dicha frase
print("EJERCICIO 8")
vowels = "aeiouAEIOU"
phrase = str(input("Ingrese una frase: "))
for vowel in phrase:
    if vowel in vowels:
        print(vowel)
print("--------------------------------------")

# # #EJERCICIO_9. Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en diche frase
print("EJERCICIO 9")
vowels = "aeiouAEIOU"
counter = 0
phrase = str(input("Ingrese una frase: "))
for vowel in phrase:
    if vowel in vowels:
        counter = counter + 1
print("Hay", counter, "vocales en su frase")
print("--------------------------------------")
#
# # #EJERCICIO_10. Escribir un programa que le permita al usuario ingresar 6 numeros enteros, que puedan ser positivos o negativos. Al finalizar, mostrar
# # #la sumatoria de los numeros negativos y el promedio de los positivos. No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa
# #arroje un error si no se ingresaron numeros positivos
print("EJERCICIO 10")
positive_counter = 0
counter = 0
limit = 6
addition = 0
negative_sum = 0
average= 1

print("Ingrese 6 numeros positivos o negativos")
while counter < limit:
    numbers = int(input(f"Ingrese el {counter + 1}° numero: "))
    if numbers > 0:
        addition = addition + numbers
        positive_counter = positive_counter + 1
    else:
        negative_sum = negative_sum + numbers
    counter = counter + 1

if positive_counter > 0:
    average = addition / positive_counter
    print(f"El promedio de los numeros positivos es: {average:.2f}")
elif positive_counter == 0:
    print("No hay ingreso numeros positivos")
else:
    print("No se puede calcular el promedio porque no a ingresado numros positivos")

if negative_sum == 0:
    print("No se han ingresado numeros negativos")
else:
    print("La suma de los negativos es: ", negative_sum)
print("--------------------------------------")

# # #EJERCICIO_11. Realizar un programa que solicite por teclado al usuario su  cedula, nombre, edad, direccion y telefono
# # #Esos datos deben ser guardados en un diccionario. Mostrar el resultado
print("EJERCICIO 11")
User_data = {}
name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))
identification_card = int(input("Ingrese su numero de cedula: "))
address = input("Ingrese su direccion: ")
phone_number = int(input("Ingrese su numero de telefono: "))

User_data["Nombre"] = name
User_data["Edad"] = age
User_data["Cedula"] = identification_card
User_data["Direccion"] = address
User_data["Telefono"]  = phone_number

print(User_data)
print("--------------------------------------")

# # #EJERCICIO_12. Realizar un programa que guarde en un diccionario los precios unitarios de los productos de un mercado,
# # #pregunte al usuario por el producto y el numero de kilos y muestre por pontalla el precio de ese numero de kilo. Si el producto no consta en la lista indique al cliente queno hay stock
# #precios por kilo, tomate = 2.35 , pimiento = 1.5, zanahoria = 2, arroz = 2.5
# print("EJERCICIO 12")
Product = {
    "tomate": 2.35,
    "pimiento": 1.5,
    "zanahoria": 2,
    "arroz": 2.5,
}
product = input("Ingrese su producto: ").lower()
if product in Product:
    unit_price = Product[product]
    while True:
        try:
            print(f"Precio por kilo: ${unit_price}")
            kilos = float(input(f"Ingrese cuantos kilos de {product} desea: "))
            total_price= unit_price * kilos
            print(f"Precio total por {kilos} kilos: ${total_price:.2f}")
            break        
        except ValueError:
            print(f"No ha ingresado cuantos kilos de {product} desea. Ingrese nuevamenete: ")
else:
    print(f"El producto {product}, no esta en stock")
