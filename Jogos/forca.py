def jogar_forca():

    print("*" * 40)
    print("*********Bem vindo ao jogo da forca!*************")
    print("*" * 40)

    palavra_secreta = "python"
    
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrou a letra {} na posição {}".format(letra, index))
            index += 1
        print("jogando........")

    print("Fim de jogo!")

if(__name__== "__main__"):
    jogar_forca()