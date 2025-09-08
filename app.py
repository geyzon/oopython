from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
import requests
import json

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0,'grande')
prato_paozinho = Prato('Paozinho',2.00,'O melhor pão da cidade')

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

def main():
	if response.status_code == 200:
		dados_json = response.json()
		dados_restaurante = {}
		for item in dados_json:
			nome_restaurante = item['Company']
			if nome_restaurante not in dados_restaurante:
				dados_restaurante[nome_restaurante] = []
			dados_restaurante[nome_restaurante].append({
				"item": item['Item'],
				"price": item['price'],
				"description": item['description']
			})
	else:
		print(f'O erro foi {response.status_code} - {response.reason}')
		
	for nome_do_restaurante, dados in dados_restaurante.items():
		nome_do_arquivo = f'{nome_do_restaurante}.json'
		with open(nome_do_arquivo, 'w') as arquivo_restaurante:
			json.dump(dados, arquivo_restaurante, indent=4)
		

if __name__ == '__main__':
    main()
