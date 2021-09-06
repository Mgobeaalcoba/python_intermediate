# Realizar un juego del ahorcado o hangman game
# usar comprehensions (lists o dict o ambos), manejo de errores y manejo de archivos (data.txt)
# ayudas: investigar la función "enumerate", el metodo get de los diccionarios puede servirnos
# ayuda adicional: la sentencia os.system("cls") servirá para limpiar pantalla
# mejoras para el juego: Añade un sistema de puntos, dibuja el "ahorcado" en cada jugada con codigo ASCII (investigar) y mejorar la interfaz

import random
import os

def word():
    with open("./archivos/data.txt", "r" , encoding="utf-8") as f:
        words=[line for line in f] #List comprehensions
    wordrandom=(random.choice(words)).upper()
    return wordrandom


def lenword(word):
    len_word=len(word)-1
    presentation=["_ "]*len_word
    return presentation


def changelarge(hiddenword,letter,index):
    # print(index)
    # print(hiddenword)
    hiddenword[index]=letter
    # print(hiddenword)
    return hiddenword


def play():
    #Comienzo del juego
    selectword=word()
    large=lenword(selectword)
    # print(" ".join(large))
    # print(*large, sep=" ")

    hits=0
    objective=len(selectword)-1
    lifes=7
    usedletters=[]
    # print(objective)

    while lifes > 0 and hits < objective:
        # print("")
        # print(selectword)
        # print("")
        # print("".join(large)) #Usar el asterisco mas la "," y sep=" " sirve para que la imprima sin los corchetes
        print(*large, sep=" ")
        print("")

        letter=input("Ingrese una letra: ").upper()
        
        assert letter.isalpha(), "Debe introducir una letra. No numeros"
        while len(letter) != 1:
            letter=input("Ingreso mas de un dígito. Ingrese solo un digito: ").upper()
            assert letter.isalpha(), "Debe introducir una letra. No numeros"
        while letter in usedletters:
            letter=input("Ingresó una letra repetida. Ingrese otra que no haya usado: ").upper()
        usedletters.append(letter)
        print("Las letras usadas hasta aquí son: ")
        print(*usedletters, sep=" ")
        
        hitsbefore=hits
        for i in range(0,len(selectword)-1): 
            # print("i vale ",i,"y el len de selectword es: ",len(selectword))
            if selectword[i] == letter:
                hits += 1
                print("Excelente. Ha acertado! Ha sumado 1 punto. Quedan "+str(objective-hits)+" letras por encontrar.")
                large=changelarge(large,letter,i)

        if hitsbefore == hits:
            lifes -= 1
            print("No se encontró la letra elegida. Usted ha perdido una vida. Le quedan: "+str(lifes)+" vidas.")
        
        input("Presiones Enter para continuar: ")
        os.system("cls") 

    if hits == objective:
        print("¡¡¡Felictaciones!!! Usted ha ganado el juego.")
    if lifes == 0:
        print("Game Over. Vuelva a intentarlo mas tarde")

    # print(hits)
    # print(lifes)
        


if __name__ == '__main__':
    play()