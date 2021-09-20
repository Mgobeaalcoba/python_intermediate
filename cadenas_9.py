# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes 
# y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

def run():
    birth = input("Ingrese su fecha de nacimiento con el siguiente esquema dd/mm/aaaa: ")
    birth_list = birth.split(sep="/")
    day = int(birth_list[0])
    month = int(birth_list[1])
    year = int(birth_list[2])
    month_list = ["_","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    month = month_list[month]
    print("Su día de nacimiento fue el: "+str(day))
    print("Su mes de nacimiento fue el: "+month)
    print("Su año de nacimiento fue el: "+str(year))

if __name__ == "__main__":
    run()