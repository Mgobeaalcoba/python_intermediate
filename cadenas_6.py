# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
#  y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.


def run():
    phrase = input("Introduzca una frase: ")
    vocal = input("Ahora introduzca la vocal que desea convertir en mayuscula: ")
    vocal = vocal.lower()
    vocales =["a","e","i","o","u"]
    while vocal not in vocales:
        vocal = input("No introdujo una vocal. Introduzca la vocal que desea convertir en mayuscula: ")
        vocal = vocal.lower()
    new_phrase = phrase.replace(vocal , vocal.upper())
    print(phrase)
    print(new_phrase)


if __name__ == "__main__":
    run()