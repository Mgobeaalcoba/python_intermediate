import numpy as np

def run():
    # # Función np.arange(start, stop (no inclusivo), step) es para crear array diciendo de donde empieza y donde termina y cada cuanto fijar una step. El Stop es no inclusivo como en las listas
    # vector = np.arange(1,6,0.1) # Así se crea un array o arreglo que es mas liviano que una lista, es iterable pero solo puede contener un único tipo de dato.
    # # Pueso hacer vectores(unidimensionales) como aquí arriba, matrices (bidimensionales) o tensores (enedimensionales)
    # print(vector)

    # matriz = np.arange(1,6,0.1).reshape(25,2) # El primer numero del reshape me indica la cantidad de arreglos dentro del arreglo madre que quiero. El segundo la cantidad de escalares que va a tener cada arreglo
    # print(matriz)

    # tensor = np.arange(1,6,0.1).reshape(5,2,5)
    # print(tensor) 

    # Otras funciones de Numpy para crear listas son:
    # np.array([tu_lista])
    vector2 = np.array([1,2,3,4,5,6,7,8,9,0])
    #Los arrays tmb se pueden recorrer, recortar o transformar como las listas.
    dato3vector2 = vector2[2]
    print(vector2)
    print(dato3vector2)
    suma_vector2 = 0
    for num in vector2:
        suma_vector2 += num
    print(suma_vector2)
    vector2_invertido = vector2[::-1]
    print(vector2_invertido)

    # Otra función de Numpy para crear arreglos es np.linspace(start, stop, num= ) A diferencia del arange el stop es inclusivo
    # y el numero muestra la cantidad de steps que queremos. No el delta entre step y step como cuando usamos el arange
    muestra = 10
    vector3 = np.linspace(20,100,muestra)
    print(vector3)
    # vector3.append(999999) El metodo append no funciona para los arreglos.
    # print(vector3)

    # Arreglos vacios y predefinidos: 

    vector4 = np.zeros(10)
    print(vector4)
    vector5 = np.ones(10)
    print(vector5)
    vector6 = np.full((1,10),True) # Como parametros debo darle en una tupla cant de columnas y cant de filas y luego el valor que quiero repetir en la misma
    print(vector6)
    matriz2 = np.full((5,10),"Hola")
    print(matriz2)

    # np.full_like() sirve si ya tienes un array creado y quieres tomarlo como base para crear otro con el mismo tamaño, pero con un mismo
    # valor.

    matriz3 = np.full_like(matriz2,"Chau")
    print(matriz3)
    

if __name__ == "__main__":
    run()