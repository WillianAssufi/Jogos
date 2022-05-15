import random
import Apresentacao

def jogar():

    Apresentacao.a_forca()

    with open("Frutas.txt", "r") as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = input("\nEscolha uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("\nVoce ganhou!")
    else:
        print("\nVoce perdeu!\nA palavra secreta era", palavra_secreta)
    print("\nFim de jogo!")

if(__name__ == "__main__"):
    jogar()