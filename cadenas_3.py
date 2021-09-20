def count_name(names):
    count = 0
    for letter in names:
        if letter != " ":
            count += 1
    return count 


def run():
    fullname = input("Introduzca su nombre completo: ")
    letters = count_name(fullname)
    print(fullname)
    print("Su nombre tiene "+str(letters)+" letras.")


if __name__ == '__main__':
    run()
