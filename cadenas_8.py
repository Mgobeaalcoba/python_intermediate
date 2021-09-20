# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla
# el número de euros y el número de céntimos del precio introducido.

def run():
    price = round(float(input("Introduzca el precio del producto en euros: ")),2)
    euros = int(price)
    centimos = round(price % euros,2)
    print("El numero de euros es: "+str(euros))
    print("El numero de centavos es: "+str(centimos))

if __name__ == "__main__":
    run()