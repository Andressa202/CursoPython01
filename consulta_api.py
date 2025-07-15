import json, requests
# Importar do site do dados do site do IBGE
pesquisa = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/derek")

dados_json = json.loads(pesquisa.text)

print(dados_json [0]['res'][0])