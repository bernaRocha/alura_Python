import re # Expressões regulares || RegEx

padrao = re.compile()

endereco = "Rua das Flores, apartamento 101, \
            Bairro Inexistente, Rio de Fevereiro, SJ, \
            23434-590"

# [-]? pode ter OU não o hífen

busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)