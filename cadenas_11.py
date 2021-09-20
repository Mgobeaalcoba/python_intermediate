# Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el
# nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste
# total con 8 dígitos enteros y 2 decimales.

def run():
    product = input('Introduce el nombre del producto: ')
    price = float(input('Introducde el precio unitario: '))
    units = int(input('Introduce el número de unidades: '))
    print('{product}: {units:3d} unidades x {price:9.2f}€ = {total:11.2f}€'.format(product = product, units = units, price = price, total = units * price))

if __name__ == "__main__":
    run()