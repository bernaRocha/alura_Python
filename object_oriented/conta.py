#!/usr/bin/env python

# receita
class Conta: 
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto .. {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


#>>> from conta import Conta
#>>> Conta()
#<conta.Conta object at 0x7f181716bc10>