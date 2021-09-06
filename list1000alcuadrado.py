def run():

    # squares=[]
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    # # for j in squares: 
    # #     print(j)
    # print(squares)

    #List comprehensions

    squares = [i**2 for i in range(1,101) if i %3 != 0]
    print(squares)
    

if __name__ == '__main__':
    run()

#Lista donde se guarden todos los cuadrados de los numeros del 1 a 100 que no sean divisibles entre 3. 

