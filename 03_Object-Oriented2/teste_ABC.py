from collections.abc import MutableSequence

class MinhaListinhaMutavel(MutableSequence):
    pass

# A classe MinhaListinhaMutavel herda de MutableSequence, 
# ou seja, é desejável que o Python avise que tem que implementar todos os métodos abstratos de uma MutableSequence

objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)

"""
File "teste_ABC.py", line 9, in <module>
objetoValidado = MinhaListinhaMutavel()
TypeError: Can't instantiate abstract class MinhaListinhaMutavel with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert
bernardo@bernardo:~/Documentos/dev/Cursos_Alura/Alura_Python/03_Object-Oriented2$ 

"""