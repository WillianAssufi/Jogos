import pandas as pd
import win32com.client as win32
import Forca
import Adivinhacao

def escolhe_jogo():

    print("*********************************")
    print("*******Escolha o seu jogo********")
    print("*********************************")

    print("(1) Forca\n(2) Adivinhação")

    jogo = int(input("Qual Jogo quer jogar?: "))

    if(jogo == 1):
        print("\nJogando Forca\n")
        Forca.jogar()
    elif(jogo == 2):
        print("\nJogando Adivinhação\n")
        Adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()