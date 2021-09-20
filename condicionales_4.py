# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def run():
    whole_number = int(input("Introduzca un número entero: "))
    parity = whole_number % 2
    if parity == 0:
        print("El numero es par")
    else:
        print("El numero es impar")


if __name__ == "__main__":
    run()