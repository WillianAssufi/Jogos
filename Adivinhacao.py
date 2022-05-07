print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
tentativas = 3
contador = 1

while(contador <= tentativas):
    print("Tentativa {} de {}".format(contador, tentativas))
    chute_str = input("Digite o seu número: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    if(numero_secreto == chute):
        print("Voce acertou")
    elif(chute > numero_secreto):
        print("Voce errou! O seu chute foi maior que o numero secreto")
    else:
        print("Voce errou! O seu chute foi menor que o numero secreto")

    contador += 1

print("Fim do jogo")