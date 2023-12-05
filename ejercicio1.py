def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return (f"F{n} = {b}")

def fib_eval(n):
    a = 0
    b = 1
    numeros = []
    rango = n/2
    for i in range(round(rango)):
        c = a + b
        a = b
        b = c
        numeros.append(b)
    if n in numeros:
        return print(f"{n} si es numero de Fibonacci")
    else:
        return print(f"{n} no es numero de Fibonacci")

def fibo_numbers(n):
    a = 0
    b = 1
    print("0")
    print("1")
    for i in range(n-2):
        c = a + b
        a = b
        b = c
        print(c)

print("===================================================================")
print("\t\t\t| Menu |\n\n\t1.1 ver numero fibonacci por posicion\n\t1.2 validar numero fibonacci\n\t1.3 mostrar los primeros n numeros de fibonacci\n")
print("===================================================================")
opcion = input("Ingrese una opcion: ")
if opcion == "1.1":
    numero = int(input("Ingrese el numero n: "))
    print(fibonacci(numero))
elif opcion == "1.2":
    numero = int(input("Ingrese el numero a validar: "))
    print(fib_eval(numero))
elif opcion == "1.3":
    numero = int(input("Ingrese el numero m: "))
    print(f"los {numero} primeros numeros de Fibonacci son: ")
    fibo_numbers(numero)
else:
    print("ingrese una opcion valida.")
