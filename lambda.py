# Funciones anonimas o lambda functions
# utilizamos lambda en lugar de def. Se hacen en una sola
# linea de codigo. Es obligatorio que así se hagan en python
# es una función anonima, sin nombre, pero a la que se la llama
# mediante el nombre de una variable que la guarda
# no necesitas usar el return en las lambda. Ej abajo

palindrome = lambda string: string == string[::-1] 

#El primer "string" es el parametro de la función. Y retornara solo True o False en base a la comparación propuesta. 

print(palindrome("mariano"))