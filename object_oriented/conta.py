#!/usr/bin/env python

# uma class é como uma receita
class Conta: 
    
    def __init__(self, numero, titular, saldo, limite): #atributos #função construtora da classe, recebendo uma referência do próprio objeto como argumento
        print("Construindo o objeto .. {}".format(self))
        self.__numero = numero   # __ torna o atributo privado
        self.__titular = titular # o saldo da conta só deve ser modificado através dos métodos deposita e saca
        self.__saldo = saldo
        self.__limite = limite

 ###### métodos  
 
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor) #self serve para acessar atributo e chamar método
        destino.depositar(valor)
    
    #### métodos getter (sempre tem retorno)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property # troquei o get_ pelo property, com isso ao chamar o métod dispensa-se os ()
    def limite(self):
        return self.__limite

    #### métodos setter (altera valor)

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    

#>>> from conta import Conta
#>>> Conta()
#<conta.Conta object at 0x7f181716bc10>
# valores dos atributos da classe: numero, titular, saldo e limite.
#>>> conta.extrato() / dentro do objeto conta acessar o extrato()

#   conta = Conta(34567, "Bernardo", 131.0, 2000.0)
#   conta2 = Conta(567, "Fulano", 100.0, 1000.0)

#   >>> conta2.transferir(10.0, conta)
#   >>> conta2.extrato()
#   Saldo de 90.0 do titular Fulano
#   >>> 

# para getters
    # @property
    # def nome(self):
    #   return self.__nome

# para setters

    # @nome.setter
    # def nome(self, nome)
    #    self.__nome = nome
