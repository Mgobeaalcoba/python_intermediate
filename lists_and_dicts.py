def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "Lastname": "Garcia"}

    super_list = [
        {"firstname": "Facundo", "Lastname": "Garcia"},
        {"firstname": "Mariano", "Lastname": "Gobea"},
        {"firstname": "Nicole", "Lastname": "Fernandez"},
        {"firstname": "Lautaro", "Lastname": "Gobea Fernandez"},
        {"firstname": "Lisandro", "Lastname": "Raccio Fernandez"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }
    for key, value in super_dict.items(): #Metodo items para recorrer el diccionari entero, es decir: llave y valor de conjunto
        print(key, "-", value)
    
    for x in super_list: 
        print(x) #Recorro la lista e imprimo el diccionario completo.
    


if __name__ == '__main__': #Entry Point de Python para que se ejecuto el codigo de la función run cuando iniciamos el programa. Truco para que se ejecute al iniciar el archivo
    run()