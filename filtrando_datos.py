DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]  # Contendrá solo los nombres x list comprehensions

    all_python_devs = list(filter(lambda worker : worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker : worker["name"], all_python_devs))

    for worker in all_python_devs:
        print(worker)
    
    print()

    #Traer los nombres de todos los que trabajan en platzi

    # all_platzi_devs = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]

    all_platzi_devs = list(filter(lambda worker : worker["organization"] == "Platzi" , DATA))
    all_platzi_devs = list(map(lambda worker : worker["name"] , all_platzi_devs))

    for worker in all_platzi_devs:
        print(worker)

    print()

    # for worker in all_platzi_devs:
    #     print(worker)    #Explicación: DATA hace referencia a la list de diccionarios de arriba. Worker hace referencia a cada diccionario que lo compone en la recorrida. Lo que está entre corchetes al lado de worker hace referencia a la key del diccionario que quiero traer. Si no pusiera nada, me traeria todo el diccionario que cumple el requisito que está despues del if
    
    # # print(all_python_devs)

    # adults = list(filter(lambda worker : worker["age"] > 18, DATA))
    # adults = list(map(lambda worker: worker["name"], adults))

    adults = [worker["name"] for worker in DATA if worker["age"] > 18]

    for worker in adults:
        print(worker)

    print()

    #Explicación: En la primera high order function - filter, sobre mi lista de diccionarios inicial, armo una lista de diccionarios donde solo me voy a quedar con aquellos diccionarios donde la edad del trabajador sea mayor a 18 años. Esto me va a traer una nueva lista de diccionarios pero con todas las key y values dentro. No solo el nombre
    #Explicación: En la segunda high order function - map, sobre mi lista "adults" ya conformada y filtrada, yo voy transformarla mediante un maps para que solo quede una unica key y value y la misma sea "name".

    old_people = list(map(lambda worker : {**worker , **{"old": worker["age"] > 70}}, DATA))  # Solo funciona en python 3.9.1 usando el "|". En python 3.8 se hace como lo hice recien
    
    # for worker in old_people:
    #     print(worker)

    # old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]

    for worker in old_people:
        print(worker)

    print("fin")

if __name__ == '__main__':
    run()