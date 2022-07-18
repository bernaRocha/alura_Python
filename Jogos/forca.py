from operator import le


def jogar_forca():

    print("*" * 40)
    print("*********Bem vindo ao jogo da forca!*************")
    print("*" * 40)

    palavra_secreta = "python".upper()
    letras_acertadas = [] #lista
#
    for letra in palavra_secreta:
        letras_acertadas.append("_")
#   ou letras_acertadas = ["_" for letra in palavra_secreta]    
#   List comprehension    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                    #print("Encontrou a letra {} na posição {}".format(letra, index + 1))
                index += 1
        else:
            erros += 1
        
        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou! parabéns!")

    print("Fim de jogo! Tente novamente!")

if(__name__== "__main__"):
    jogar_forca()
