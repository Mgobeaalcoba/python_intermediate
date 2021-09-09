# Formula para apertura de archivo:
# with open("./ruta/del/archivo.txt", "r") as f 
# modos de apertura - segundo parametro: "r" para read, "w" para sobreescribir y "a" para sumar al final del documento

def read():
    numbers =[]
    with open("./archivos/numbers.txt  ", "r", encoding="utf-8") as f:  # El encoding se usa para no tener problemas con los signos propios del idioma
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["facundo", "Miguel", "Pepe", "Christian","Rocio"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name+"\n")
            #f.write("\n")
            #f.write(",")


def run():
    write()

if __name__ == '__main__':
    run()