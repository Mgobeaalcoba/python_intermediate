# Listar los caracteres de la cadena ‘2001: A Space Odyssey’. Dejando solamente aquellos que no se repiten y que no son espacios

def run():
    cadena="2001: A Space Odyssey"
    my_list=[]
    for letter in cadena:
        if letter != " " and letter not in my_list:
            my_list.append(letter)
    print(my_list)
    print(cadena)


if __name__ == '__main__':
    run()