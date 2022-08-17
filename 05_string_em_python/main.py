# o método find tem a seguinte estrutura: str.find(sub[, start[, end]])
    #  sub == substring, end é opcional
# para fatiar uma string do início até um certo índice, ou a partir de um índice até o final. 
# Exemplo: str[a:] ou str[:b].

#url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
#url = 'https://bytebank.com/cambio?'

url = 'https://bytebank.com/cambio?moedaOrigem=real'
#print(url)

url = ""

## Sanitização da URL
url = url.replace(" ", "")  ## substitui espaço em branco por espaço vazio

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia") # retorna erro ao usuário

### Separa base e os parâmetros


indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]
print(f'Linha 18 {url_parametros}') # Linha 18 moedaOrigem=real

### Busca o valor de um parâmetro

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)