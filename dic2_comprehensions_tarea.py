# dic con llaves hasta 1000 y valores hasta 1000 a su raiz cuadrada
def run():
    my_dic = { i : round(i**(1/2),2) for i in range (1,1001)}
    print(my_dic)


if __name__ == '__main__':
    run()