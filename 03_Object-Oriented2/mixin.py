class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    #def mostrar_tarefas(self):
    #    print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        return f'Hipster,  {self.nome}'        

# classes que herdam os comportamentos

class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass

fulano = Junior("Fulano")
fulano.busca_perguntas_sem_resposta()

luan = Pleno("Luan")
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()

print(luan)  ##  Hipster,  Luan

"""
        Antes de comenta as linhas 16 e 17
Mostrando perguntas não respondidas do fórum
Mostrando perguntas não respondidas do fórum
Mostrando cursos desse mês
Fez muita coisa, Alurete!
"""

# após comentar as linhas 16 e 17

"""
Mostrando perguntas não respondidas do fórum
Mostrando perguntas não respondidas do fórum
Mostrando cursos desse mês
Fez muita coisa, Caelumer
"""

