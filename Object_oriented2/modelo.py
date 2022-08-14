class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0 

    @property
    def likes(self):
        return self._likes

    def adicionar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):  # Filme herda de Programa
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # chama da classe Mãe para evitar repetição de código
        self.duracao = duracao
     

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas





godzilla = Filme('godzilla - rei dos mosntros', 2018, 127)
godzilla.adicionar_like()
print(f'Nome: {godzilla.nome} - Ano {godzilla.nome} - Duração {godzilla.duracao} - Likes {godzilla.likes}')

dark = Serie('dark', 2019, 3)
dark.adicionar_like()
dark.adicionar_like()
print(f'Nome: {dark.nome} - Ano: {dark.ano} - Temporadas: {dark.temporadas} - Likes: {dark.likes}')