from selenium import webdriver
import time

#Abrir o navegador 
navegador = webdriver.Chrome()

#Acessar o site
navegador.get('https://www.saucedemo.com/')

#Abrir o site em tela cheia
navegador.maximize_window()

#Definindo um tempo para o navegador ficar aberto
time.sleep(10)



