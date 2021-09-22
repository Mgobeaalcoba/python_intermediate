# Arreglos aleatorios
# Si quieres generar una serie de números totalmente aleatoria, ¡lo puedes hacer! Pero no solo eso, sino que si quieres que esos números
# obedezcan una distribución, puedes indicarlo. Para ello deberás usar np.random. Veamos algunas funciones que te pueden ayudar.

# .rand(): números aleatorios en una distribución uniforme. Permite crear ndarrays.
# .uniform(): parecido a rand, pero permite ingresar los límites de la muestra.
# .randn(): números aleatorios en una distribución normal. Permite crear ndarrays.
# .normal(): parecido a randn, pero permite escalar los límites de la muestra.
# .randint(): números enteros aleatorios entre un rango dado.

import numpy as np
# import matplotlib.pyplot as plt


def run():
    vector = np.random.rand(10) #Selecciona de forma aleatoria la cantidad de datos indicada como argumento entre 0 y 1
    print(vector)
    vector2 = np.random.uniform(0,100,10) #Selecciona de forma aleatoria la cantidad de datos indicada en el ultimo argumento
    # entre el rango comprendido entre el primer argumento y el segundo.
    print(vector2)
    vector3 = np.random.randn(20) #Si separo con comas dentro de los argumentos puedo generar columnas y filas
    print(vector3)
    # print(plt.hist(vector3))
    vector4 = np.random.normal(loc=0,scale=1,size=10) #Loc marca el inicio del dato en el data set. Size marca el tamaño del arreglo, scale el rango de movimento del dataset
    print(vector4)
    vector5 = np.random.randint(1,100,10) #Igual que el .uniform pero con numeros enteros.
    print(vector5)

if __name__ == "__main__":
    run()