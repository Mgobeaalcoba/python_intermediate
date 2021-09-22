# Tmb se pueden manejar errores con asser
# El esquema es el siguiente:
# afirmo que (assert) debe cumplirse tal condición (condition) sino (,) presento el sigueinte msj de error ("Mensaje de error" - sin los parentesis)

# def palindrome(string):
#     assert len(string) > 0, "No se puede ingresar una cadena vacia"
#     return string == string[::-1]

# print(palindrome(""))

def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Ingrese un número: ")
    # el metodo "isnumeric() Solo funciona para cadena de caracteres
    assert num.isnumeric(), "Debe introducir un numero entero positivo: "
    print(divisors(int(num)))
    print("Termino el programa")


if __name__ == '__main__':
    run()

# Desafio: manejar como error el ingreso de un numero negativo
# Los asserts son una alternativa al manejo de errores con el esquema try-except-raise-finally. Se recomienda combinarlos con los assert statements
