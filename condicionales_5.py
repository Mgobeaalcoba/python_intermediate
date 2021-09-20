# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un
# nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al 
# usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def run():
    name = input("Ingrese su nombre: ")
    sex = input ("Ingrese su sexo: ")
    group_a = "abcdefghijklm"
    group_b = "nopqrstuvwxyz"
    initial_letter=name[0]
    if (initial_letter in group_a and sex == "f") or (initial_letter in group_b and sex == "m"):
        print("Usted pertenece al grupo A.")
    else: 
        print("Usted pertenece al grupo B.")


if __name__ == "__main__":
    run()