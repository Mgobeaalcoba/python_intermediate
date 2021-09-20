# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def run():
    age = int(input("Introduzca su edad: "))
    if age >= 18:
        print("Es mayor de edad.")
    else:
        print("Es menor de edad.")


if __name__ == "__main__":
    run()