import re # Expressões regulares || RegEx

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

endereco = "Rua das Flores, apartamento 101, "\
            "Bairro Inexistente, Rio de Fevereiro, SJ, "\
            "23434-590"

# [-]? pode ter OU não o hífen

busca = padrao.search(endereco) # retorna True ou False

if busca:
    cep = busca.group() # retorna a string encontrada no padrão
    print(cep)

#### Como simplificar o 
###   "[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]"