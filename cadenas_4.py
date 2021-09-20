def clearing(phone):
    my_list = phone.split(sep="-")
    clean_number = my_list[1]
    return clean_number


def run():
    phone_number = input("Introduzca su número de telefono con prefijo y extensión. Ej: +34-913724710-56: ")
    clear_phone = clearing(phone_number)
    print(phone_number)
    print("Su numero sin prefijo y extensión es "+str(clear_phone))


if __name__ == '__main__':
    run()