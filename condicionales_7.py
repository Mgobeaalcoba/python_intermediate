# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

def run():
    rent = float(input("Ingrese su renta anual: "))
    if rent < 10000:
        print("Debe pagar el 5 % de impuestos")
    elif rent >= 10000 and rent < 20000:
        print("Debe pagar el 15 % de impuestos")
    elif rent >=20000 and rent < 35000:
        print("Debe pagar el 20 % de impuestos")
    elif rent >=35000 and rent < 60000:
        print("Debe pagar el 30 % de impuestos")
    else:
        print("Debe pagar el 45 % de impuestos")


if __name__ == "__main__":
    run()