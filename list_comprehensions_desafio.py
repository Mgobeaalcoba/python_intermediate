# Crear, con un list comprehension, una lista de todos los multiplos de 4 que a la vez tambien son multiplos de 6 y de 9, hasta 5 digitos
def run():
    multiples=[i for i in range (10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(multiples)

if __name__ == '__main__':
    run()