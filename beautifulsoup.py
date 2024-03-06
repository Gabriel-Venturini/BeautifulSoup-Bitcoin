from datetime import datetime
import requests
from bs4 import BeautifulSoup as soup


url = 'https://www.google.com/search?q=cota%C3%A7%C3%A3o+bitcoin'
# site desejado
# valor atualizado de 30 em 30 minutos

header = {"User-Agent":'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'} 
# garante que o navegador utilize a versão de usuário e não a de bot

request = requests.get(url, headers=header) 
# request do url com o parametro headers para garantir a versao do navegador

site = soup(request.text, "html.parser") # funcao .text para transformar .json em .txt
# parser para analisar e manipular o documento html criado pelo request

horarioAtual = datetime.now()
valorMoeda = site.find("span", class_="pclqee")
valorDiferenca = site.find("span", jsname="SwWl3d")
valorPorcentagemDif = site.find("span", jsname="rfaVEf")
# procura os elementos desejados da página passando como parâmetros a tag e a classe escolhida

print(f'Horário atual: {horarioAtual}')
print(f'Bitcoin agora: {valorMoeda.get_text()}')
print(f'Diferenca agora: {valorDiferenca.get_text()}{valorPorcentagemDif.get_text()}')


# Resumo: Soup serve APENAS para paginas estaticas
# então para conseguir acessar informacoes dinamicas
# usarei o Selenium futuramente
# ja valeu a experiencia