import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("\nQual o nível de dificuldade?")
    print("(1) Fácil \n(2) Médio\n(3) Difícil")

    nivel = int(input("Defina o nível: "))
    print()
    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for contador in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(contador, tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")

        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100!\n")
            continue

        if(numero_secreto == chute):
            print("\nVoce acertou e fez {} pontos!\n".format(pontos))
            break
        elif(chute > numero_secreto):
            print("Voce errou! O seu chute foi maior que o numero secreto\n")
        else:
            print("Voce errou! O seu chute foi menor que o numero secreto\n")

        if(chute != numero_secreto):
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
            continue

        if(contador == tentativas):
            print("O número secreto era {}".format(numero_secreto))
            break

    print("Fim do jogo")