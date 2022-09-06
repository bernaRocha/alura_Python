from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_06_03_1980_retorna_42(self): # é um padrão começar com test_
        # contexto
        entrada = '06/03/1980'
        esperado = 42

        funcionario_teste = Funcionario('Teste', entrada, 2000)
        resultado = funcionario_teste.idade() # When - ação

        assert resultado == esperado

    def test_qaundo_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = '    Lucas Carvalho ' # Given || Contexto
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 2000)
        resultado = lucas.sobrenome() # When || ação

        assert resultado == esperado # Then

    def test_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 # Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # When
        resultado = funcionario_teste.salario 

        assert resultado == esperado # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 # Given
        
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000000 # given

            funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus() # when

            assert resultado # then

    def test_retorno_str(self):
        nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000 #given
        esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__() # When

        assert resultado == esperado # then
"""
Dado(contexto)....
Quando(Ação)...
Então(Desfecho)....

Testes devem possuir o nome mais verboso o possível
Utilizar o método ágil Given-When-Then para a construção de testes

pytest -v para rodar o teste

tests/test_bytebank.py::TestClass::test_quando_idade_recebe_06_03_1980_retorna_42 PASSED                                              [ 50%]
tests/test_bytebank.py::TestClass::test_qaundo_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho PASSED                          [100%]

"""
