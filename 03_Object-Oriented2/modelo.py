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
    def nome(self, nome):
        self._nome = nome.title()

    def imprime(self):
        return f'Nome: {self._nome} - Ano: {self.ano} Likes: {self._likes}'

class Filme(Programa):  # Filme herda de Programa
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # chama da classe Mãe para evitar repetição de código
        self.duracao = duracao
    
    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} Duração - {self.duracao} min | Likes: {self._likes}'
     
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
         # Objeto a ser mostrado como string
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas - {self.temporadas} | Likes: {self._likes}'

#########################

godzilla = Filme('godzilla - rei dos mosntros', 2018, 127)
godzilla.adicionar_like()
print(f'Nome: {godzilla.nome} - Ano {godzilla.nome} - Duração {godzilla.duracao} - | Likes {godzilla.likes}')

dark = Serie('dark', 2019, 3)
dark.adicionar_like()
dark.adicionar_like()
print(f'Nome: {dark.nome} - Ano: {dark.ano} - Temporadas: {dark.temporadas} - | Likes: {dark.likes}')

#######################

filmes_e_series = [godzilla, dark]

for programa in filmes_e_series:
   # programa.imprime() # pode ser o imprime da série ou filme
    print(programa)