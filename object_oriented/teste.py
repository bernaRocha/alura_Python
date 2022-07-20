def cria_conta(numero, titular, saldo, limite): #encapsular a criação dentro de uma função
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}   
    return conta 

def deposita(conta, valor):
        conta["saldo"] += valor # conta["saldo"] = conta["saldo"] + valor  #

def saca(conta, valor):
        conta["saldo"] -= valor

def extrato(conta):
        print("Saldo é {}".format(conta["saldo"]))
