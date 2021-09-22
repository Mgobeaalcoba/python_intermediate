# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario
# su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def run():
    age = int(input("Ingrese su edad: "))
    ingresos = int(input("¿Cuales son sus ingresos: ?"))
    if age > 16 and ingresos > 1000:
        print("Usted debe tributar")
    else:
        print("Usted no debe tributar aún.")


if __name__ == "__main__":
    run()