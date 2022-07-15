print("*"* 33) 
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 5


for rodada in range(1, total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou ", chute)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if(acertou):
        print("Acertou")
    else:
        if(maior):
            print("Você errou, seu chute foi maior")
        if(menor):
            print("Você errou, seu chute foi menor")
    rodada += 1
print("Fim do jogo!")