import adivinhacao
import forca

def escolhe_jogo():
    print("*" * 40)
    print("***********Escolha seu jogo")
    print("*" * 40)

    print("(1) Forca (2) Advinhação")

    escolha = int(input("Qual o jogo que deseja jogar? "))

    if(escolha == 1):
        print("Jogando forca")
        forca.jogar_forca()
    elif(escolha == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar_advinhacao()

    if(__name__ == "__main__"):
        escolhe_jogo()