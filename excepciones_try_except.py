def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")  # Se usa para forzar un error con la posibilidad de incorporarle un msj personalizado. Y luego ese error lo manejo desde el except.
        return string == string [::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindrome(""))
except TypeError:
    print("Solo se pueden ingresar strings")

# Finally Se usa al final de una estructura try - except para alguna de las siguientes tres cosas:
# cerrar un archivo dentro de python
# cerrar una conexion a una base de datos
# liberar recursos externos. Son buenas practicas 