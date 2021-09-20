# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.


def inverter(text):
    my_list = text.split()
    my_list = my_list[::-1]
    inverter_text = " ".join(my_list)
    return inverter_text


def run():
    phrase = input("Introduzca una frase: ")
    inverter_phrase = inverter(phrase)
    print(inverter_phrase)


if __name__ == '__main__':
    run()
