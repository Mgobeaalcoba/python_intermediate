# Calcular cuantos granos de trigo tendríamos que utilizar si por cada casilla de un tablero 
# de ajedrez pusiéramos un grano en la primera casilla, dos en la segunda, cuatro en la tercera, y así doblando hasta la última.

def run():
    casillas=[i for i in range(1,65)]
    print(casillas)
    granos=[]
    for i in range(64):
        if i == 0:
            granos.append(casillas[i])
        else:
            granos.append(granos[i-1]*2)
    print(granos)
    


if __name__ == '__main__':
    run()

