import Forca
import Adivinhacao

def escolhe_jogo():

    print("*********************************")
    print("*******Escolha o seu jogo********")
    print("*********************************")

    print("(1) Forca\n(2) Adivinhação")

    jogo = int(input("Qual Jogo quer jogar?: "))

    if(jogo == 1):
        print("Jogando Forca\n")
        Forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação\n")
        Adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()