#!/usr/bin/env python

conta = {"numero": 123,   #dicionário
        "titular": "Fulano",
        "saldo": 38.0,
        "limite": 1000.0
}
# atributos da classe: numero, titular, saldo, limite
def cria_conta(numero, titular, saldo, limite): #encapsular a criação dentro de uma função
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}   
    return conta 

def depositar(conta, valor):
        conta["saldo"] += valor # conta["saldo"] = conta["saldo"] + valor  #

def saca(conta, valor):
        conta["saldo"] -= valor

def extrato(conta):
        print("Saldo é {}".format(conta["saldo"]))
