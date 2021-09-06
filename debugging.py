def divisors(num):
    divisors =[]
    for i in range(1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("Ingrese un número: "))
        if num < 0:
            raise TypeError("Debe ingresar un numero positivo")
        print(divisors(num))
        print("Termino el programa")
    except ValueError:
        print("Debe introducir un numero.")
    except TypeError as te:
        print(te)

if __name__ == '__main__':
    run()

# Desafio: manejar como error el ingreso de un numero negativo

