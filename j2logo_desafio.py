# Ejercicio #1: Menú de la aplicación Kwranking


def cargar_keywords():
    my_list=[]
    with open ("./archivos/keywords.txt ", "r", encoding="utf-8") as f:
        for line in f:
            my_list.append(line)
    return my_list


def print_list(list):
    for index , word in enumerate(list):
        if index % 20 != 0 or index == 0:
            print(word)
        else:   
            print(word)
            input("Presione enter para continuar")


def run():
    continuar = True
    keywords = []
    while continuar:
        print("""
        Menu:
        [1] – Importar palabras clave
        [2] – Mostrar palabras clave
        [0] – Salir
        """)
        option = int(input("Seleccione el numero de opción que desea ejecutar: "))
        while option < 0 or option > 2:
            option = int(input("Opción invalida. Seleccione el numero de opción que desea ejecutar: "))
        if option == 1:
            keywords = cargar_keywords()
        elif option ==2:
            print_list(keywords)
        else: 
            continuar = False


if __name__ == '__main__':
    run()