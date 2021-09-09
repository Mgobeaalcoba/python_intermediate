def run():
    my_list=[ "mariano" , "nicole" , "lisandro" , "lautaro" ]
    my_dic= { nombre : i for nombre , i in zip ( my_list , range (1,5) ) } # El zip ( donde recorer con cada variable ) se usa para armar un diccionario con dos variables independientes
    print(my_dic)


if __name__ == "__main__":
    run()
    
