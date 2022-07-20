#!/usr/bin/env python

# uma class é como uma receita
class Conta: 
    
    def __init__(self, numero, titular, saldo, limite): #atributos #função construtora da classe, recebendo uma referência do próprio objeto como argumento
        print("Construindo o objeto .. {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

#>>> from conta import Conta
#>>> Conta()
#<conta.Conta object at 0x7f181716bc10>
# valores dos atributos da classe: numero, titular, saldo e limite.
#>>> conta.extrato() / dentro do objeto conta acessar o extrato()