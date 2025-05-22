from bs4 import BeautifulSoup
import requests

def coleta_dados():
    #criar as listas
    nome = []
    descrição = []
    preço = []

    #Acessa a página
    link = "https://www.saucedemo.com/inventory.html"
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
    site = requests.get(link, headers=headers)
    soup = BeautifulSoup(site.text, "html.parser")

    #Acessa os produtos
    conjunto_produtos = soup.find('div', id='inventory_list')
    produtos = conjunto_produtos.find_all('div')

    for produto in produtos:
        #Acessa o nome
        nome = produto.find('div', class_='inventory_item_name')
        v1 = nome.find('font')
        print(v1)
    