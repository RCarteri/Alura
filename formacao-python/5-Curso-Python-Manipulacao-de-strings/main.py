# url = "https://cursos.alura.com.br/course/python-manipulando-strings/task/52588"
#
# #printa cursos
# teste1 = url[8:14]
# print(teste1)
#
# #printa do início até o indice 13
# teste2 = url[:14]
# print(teste2)
#
# #printa do índice 50 em diante
# teste3 = url[50:]
# print(teste3)
#
# #printa o índice do valor pesquisado
# teste4 = url.find(":")
# print(teste4)
# print(url[teste4:10
#       ])
#
# #printa um vetor oncde cada elemento é o valor que estava entre o valor informado
# teste5 = url.split("-")
# print(teste5)

from strings import ExtratorArgumentoURL
url ="https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150"
cambio = ExtratorArgumentoURL(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)

url ="https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"
cambio = ExtratorArgumentoURL(url)
moedaOrigem,moedaDestino=cambio.retornaMoedas()
valor = cambio.retornaValor()
print(moedaOrigem,moedaDestino,valor)

import re
padrao = "[0-9]{4,5}-?[0-9]{4}" #retorna 4 ou 5 digitos de 0 a 9 com ou sem - e mais 4 digitos de 0 a 9
texto =  "Meu número para contato é 2633-5723"
retorno = re.findall(padrao,texto)
print(retorno)
