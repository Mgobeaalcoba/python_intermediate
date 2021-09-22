# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.0
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la
#  puntuación del nivel.
# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

def run():
    points = float(input("Ingrese la puntuación obtenida: "))
    while points != 0.0 and points != 0.4 and points != 0.6 and points != 0.7 and points != 0.8 and points != 0.9 and points != 1.0:
        points = float(input("Dato invalido. Solo puede ingresar 0.0 , 0.4 , 0.6 , 0.7 , 0.8 , 0.9 o 1.0. Ingrese la puntuación obtenida: "))
    prime = 2400 * points
    if points == 0.0:
        print("Su performance es inaceptable y su premio es de {}".format(prime))
    elif points == 0.4:
        print("Su performance es aceptable y su premio es de {}".format(prime))
    else:
        print("Su performance es meritoria y su premio es de {}".format(prime))


if __name__ == "__main__":
    run()