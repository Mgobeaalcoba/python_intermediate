# funcion de orden superior es cuando una función recibe de parametro a otra función

# def saludo(func):
#     func()

# def hola():
#     print("Hola!!!")

# def adios():
#     print("Adios!!!")

# saludo(hola)
# saludo(adios)

# Filter, Map y Reduce son las mas usadas de estas funciones
# de orden superior

# my_list = [1,4,5,6,9,13,19,21]
# odd=[i for i in my_list if i%2!=0]
# print(odd)  #Resolución con list comprehensions

# my_list = [1,4,5,6,9,13,19,21]

# odd = list(filter(lambda x: x%2 !=0, my_list))

# print(odd)

# my_list = [1,2,3,4,5]

# squares = list(map(lambda x : x**2, my_list))

# print(squares)

# squares = [i**2 for i in my_list]

# print(squares)

# Reduce se usa para reducir una lista a un unico componente 

from functools import reduce
my_list = [1,2,3,4,5]
# acum=1

# for i in my_list:
#     acum=acum*i

# print(acum)

all_multiplied = reduce(lambda a, b: a * b, my_list)
print(all_multiplied)

