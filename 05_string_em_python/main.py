# o método find tem a seguinte estrutura: str.find(sub[, start[, end]])
    #  sub == substring, end é opcional


#url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
#url = 'https://bytebank.com/cambio?'

url = 'https://bytebank.com/cambio?moedaOrigem=real'
#print(url)

indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
#print(url_base)


url_parametros = url[indice_interrogacao+1:]
print(f'Linha 12 {url_parametros}') # Linha 12 moedaOrigem=real

url_base = url[0:20]

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]