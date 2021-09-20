# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar
# un error. Lo hago con manejo de errores en lugar de con condicionales. 

def run():
    number1 = round(float(input("Introduzca el dividendo: ")),2)
    number2 = round(float(input("Introduzca el divisor: ")),2)
    try:
        division = number1 / number2
        print("El resultado de su división es: "+str(division))
    except ZeroDivisionError:
        print("No se puede dividir por cero. Por favor introduzca un divisor distinto de cero.")


if __name__ == "__main__":
    run()