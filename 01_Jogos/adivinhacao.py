import random

def jogar_advinhacao():

    print("*"* 33) 
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # Game variables
    numero_secreto = random.randrange(0, 101) # Or round(random.random() * 100) 
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade? ")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute)

        if(chute < 1 or chute > 100): 
            print("Você deve digitar entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if(acertou):
            print("Acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, seu chute foi maior")
            if(menor):
                print("Você errou, seu chute foi menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        rodada += 1
    print("Fim do jogo!")

if(__name__== "__main__"):
    jogar_advinhacao()