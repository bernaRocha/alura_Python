#!/usr/bin/env python

# uma class é como uma receita
class Conta: 
    
    def __init__(self, numero, titular, saldo, limite): #atributos #função construtora da classe, recebendo uma referência do próprio objeto como argumento
        print("Construindo o objeto .. {}".format(self))
        self.__numero = numero   # __ torna o atributo privado
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

 ###### métodos  
 
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

#>>> from conta import Conta
#>>> Conta()
#<conta.Conta object at 0x7f181716bc10>
# valores dos atributos da classe: numero, titular, saldo e limite.
#>>> conta.extrato() / dentro do objeto conta acessar o extrato()

conta = Conta(34567, "Bernardo", 131.0, 2000.0)