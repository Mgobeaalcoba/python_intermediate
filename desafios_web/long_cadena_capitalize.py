# Crear una función que calcule la longitud de una cadena alfanumérica. Crear otra función que dada una
# cadena devuelva el primer caracter en mayúsculas y el resto en minúsculas. Pasar una palabra por ambas funciones y dar el resultado.
def long(cadena):
    # largo = len(cadena)
    largo=0
    for i in cadena:
        largo +=1
    return largo


def capi(cadena):
    # cadena = cadena.capitalize()
    mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    minusculas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","R","s","t","u","v","w","x","y","z"]
    for letter in cadena:
        indice=minusculas.index(letter)
        indice2=cadena.index(letter)
        cadena[indice2] = mayusculas[indice]
    print(cadena)
    return cadena


def run():
    palabra = input(
        "Escriba cualquier palabra que desee medir y poner su primera letra en mayuscula: ")
    largo = long(palabra)
    palabra = capi(palabra)
    print("El largo de su cadena es de "+str(largo)+" caracteres.")
    print(palabra)


if __name__ == '__main__':
    run()
