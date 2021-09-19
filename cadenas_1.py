def print_name(names, numbers):
    for i in range(numbers):
        print(names)


def run():
    name = input("Introduzca su nombre: ")
    number = int(input("Introduzca la cantidad de veces que desea ver su nombre: "))
    print_name(name, number)

if __name__ == '__main__':
    run()