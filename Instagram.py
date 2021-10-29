from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#abrir navegador
navegador = webdriver.Edge('C:\\Users\\wesle\\OneDrive\\Área de Trabalho\\Wesley\\python\\MeusProjetos\\Instagram\\msedgedriver.exe')

#Entrar no insta
navegador.get("https://www.instagram.com/")

#fazer login
time.sleep(3)
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("seu login") #login
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("sua senha") #senha
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click() #entrar
time.sleep(5)

#clicar em não salvar
navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(2)

#Desativar notifiação
navegador.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
time.sleep(1)

#clicar na barra de pesquisa
navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div').click()

#Escrever na barra de pesquisa
navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys("perfil que deseja seguir")
time.sleep(0.5)

#clicar no perfil 
navegador.find_element_by_class_name('-qQT3').click()
time.sleep(3)

#Seguir perfil
navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click()
