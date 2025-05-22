from selenium import webdriver
import time

#Abrir o navegador 
navegador = webdriver.Chrome()

#Acessar o site
navegador.get('https://www.saucedemo.com/')

#Abrir o site em tela cheia
navegador.maximize_window()

#preencher o usuário
campo_nome = navegador.find_element("id", "user-name")
campo_nome.send_keys("standard_user")

#preencher a senha
campo_senha = navegador.find_element("id", "password")
campo_senha.send_keys("secret_sauce")

#Definindo um tempo para o navegador ficar aberto
time.sleep(10)



