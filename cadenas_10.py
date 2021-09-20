# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla
# cada uno de los productos en una línea distinta.

def run():
    products = input("Ingrese los productos que compró en el supermercado separados por comas: \",\": ")
    list_products = products.split(sep=",")
    for product in list_products:
        print(product)


if __name__ == "__main__":
    run()