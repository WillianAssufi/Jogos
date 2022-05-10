import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
tentativas = 3

for contador in range(1, tentativas + 1):
    print("Tentativa {} de {}".format(contador, tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Voce deve digitar um número entre 1 e 100!")
        continue

    if(numero_secreto == chute):
        print("Voce acertou")
        break
    elif(chute > numero_secreto):
        print("Voce errou! O seu chute foi maior que o numero secreto")
    else:
        print("Voce errou! O seu chute foi menor que o numero secreto")

print("Fim do jogo")