### https://www.bytebank.com.br/cambio

## Utilizar () quando for achar exatamente o que estiver nos ()
## Pode ser http OU https

#
###  Mais RegEx https://docs.python.org/pt-br/3/howto/regex.html#regex-howto
#

import re

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida")

print("A URL é válida")