# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima
# por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y 
# minúsculas.

def run():
    password = input("Genere una contraseña: ")
    password = password.lower()
    password_repeat = input("Repita su contraseña: ")
    password_repeat = password_repeat.lower()
    if password == password_repeat:
        print("Su contraseña coincide con la guardada")
    else:
        print("Su contraseña es incorrecta.")


if __name__ == "__main__":
    run()