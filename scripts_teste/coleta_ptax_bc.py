import requests 
import json
import re

url = r"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/codigo_recurso?$format=json"

recursos = {
    '1': "Moeda",
    '2': "CotacaoDolarDia",
    '3': "CotacaoDolarPeriodo",
    '4': "CotacaoMoedaDia",
    '5': "CotacaoMoedaPeriodo"
}

p = re.compile(r"codigo_recurso")
cod_recurso = re.sub(p, recursos["1"], url)

headers = {
    'connection': 'Keep-Alive',
    'content-language': 'en-US',
    'content-type': 'application/json;charset=UTF-8;odata.metadata=minimal',
    'date': 'Mon, 25 Apr 2022 00:50:45 GMT',
    'expires': '0',
    'keep-alive': 'timeout=10',
    'odata-version': '4.0',
    'pragma': 'no-cache',
    'strict-transport-security': 'max-age=16070400 ; includeSubDomains',
    'transfer-encoding': 'chunked',
    'x-content-type-options': 'nosniff',
    'x-frame-options': 'DENY',
    'x-xss-protection': '1 ; mode=block'
}

params = {
  "@odata.context": "string",
  "value": [
    {
      "simbolo": "string",
      "nomeFormatado": "string",
      "tipoMoeda": "string"
    }
  ]
}

request = requests.get(url, headers=headers).json()

print(request)