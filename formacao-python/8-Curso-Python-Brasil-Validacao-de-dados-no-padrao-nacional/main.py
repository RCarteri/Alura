from telefone import TelefonesBr
from documento import Documento
from validate_docbr import CNPJ

cpf_um = '15316264754'
#print(cpf_um)

#exemplo_cnpj = "35379838000112"
#exemplo_cpf = "11111111112"

#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
documento = Documento.cria_documento(cpf_um)
print(documento)

telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

import requests
from endereco import BuscaEndereco
cep = "97250000"
objeto_cep = BuscaEndereco(cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r.text)

logradouro, bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(logradouro, bairro, cidade, uf)
print(telefone_objeto)