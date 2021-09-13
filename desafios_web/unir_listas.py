# Generar primero una lista con los números entre 0 y 10, 
# luego generar otra lista con los números del 11 al 20. Unir ambas lista e imprimir el resultado.

def run():
    lista1=[i for i in range(1,11)]
    lista2=[i for i in range(11,21)]
    lista3=lista1+lista2
    print(lista3)


if __name__ == '__main__':
    run()