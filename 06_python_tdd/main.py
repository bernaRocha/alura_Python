from codigo.bytebank import Funcionario

def teste_idade():
    funcionario_teste0 = Funcionario('Fulano', '06/03/1980', 2000)
    print(f'Teste = {funcionario_teste0.idade()}')

    funcionario_teste1 = Funcionario('Beltrano', '16/09/1995', 2500)
    print(f'Teste = {funcionario_teste1.idade()}')

    funcionario_teste2 = Funcionario('Ciclano', '27/05/2005', 3500)
    print(f'Teste = {funcionario_teste2.idade()}')

teste_idade()


bernardo = Funcionario("Bernardo", '07/03/1988', 2000)

print(bernardo)

"""
Teste = 42
Teste = 27
Teste = 17
Funcionário(Bernardo, 07/03/1988, 2000)
"""