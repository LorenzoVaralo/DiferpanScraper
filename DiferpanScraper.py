from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from datetime import datetime
import os
clear = lambda: os.system('clear')

lista_prod = []

with open("user.txt", 'r+') as f:
    contents = f.read()
    if contents:
        user = contents.split("\n")[0]
        senha = contents.split("\n")[1]
    else:
        user = input('Email: ')
        senha = input('Senha: ')
        f.write(f"{user}\n{senha}")
    f.close()


driver = webdriver.Chrome()
driver.get('https://b2b.diferpan.com.br/login')

def Inicialização(user, senha):
    email_input = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/form/div[1]/div/div[1]/div/input')
    email_input.send_keys(user)

    password_input = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/form/div[2]/div/div[1]/div/input')
    password_input.send_keys(senha)

    driver.find_element_by_css_selector('#root > div > div.login__limiter > form > div.login__form-group > button').click()

    driver.implicitly_wait(4)
    #Fechar Pop-up
    driver.find_element_by_xpath('/html/body/div[2]/div/footer/button[2]').click()
    #Abrir aba de orçamentos
    driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/ul/li[3]/a').click()
    driver.implicitly_wait(4)
    #Fechar Pop-up
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/footer/button').click()
    #Criar Orçamento
    driver.implicitly_wait(7)
    driver.find_element_by_css_selector('#root > div.jss539 > div.MuiPaper-root-686.jss685.MuiPaper-outlined-688.MuiPaper-rounded-687 > div.MuiCardContent-root-714.bg-white > div > div:nth-child(1) > button').click()
    #Fechar Pop-up
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/html/body/div[2]/div/footer/button[2]').click()

Inicialização(user, senha)


def Compras365():
    driver.find_element_by_xpath('//*[@id="MixVendas"]/button').click()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/button').click()
    driver.implicitly_wait(2)
    driver.find_element_by_css_selector('body > div:nth-child(6) > div > div:nth-child(1) > div > div > div.modal-content > div > div.xbox__content.border-top.pt-4.d-flex.flex-column.flex-md-row.align-items-center.justify-content-center.flew-wrap > button').click()
    driver.implicitly_wait(10)
    num_results = driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[3]/div/div/div[2]/div/div/form/div/div[2]/div/span/strong').text
    num_results = int(num_results)
#Compras365()

def pintura():
    driver.find_element_by_xpath('//*[@id="Dimensoes"]/button').click()
    driver.find_element_by_xpath('//*[@id="Dimensoes"]/div/div/div[2]/div[2]/ul/li[11]').click()
    driver.find_element_by_xpath('//*[@id="Dimensoes"]/button').click()
    driver.implicitly_wait(10)
    num_results = driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[3]/div/div/div[2]/div/div/form/div/div[2]/div/span/strong').text
    num_results = int(num_results)
    return num_results

num_results = pintura()




def PegarInfo(j):
    try:
        estoque = driver.find_element_by_xpath(f'//*[@id="root"]/div[3]/div[4]/div/div/div[1]/div[{j}]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/div/span').text
    except:
        estoque = 'ALTO'
    try:
        driver.find_element_by_xpath(f'//*[@id="root"]/div[3]/div[4]/div/div/div[1]/div[{j}]/div/div[1]').click()
    except:
        driver.find_element_by_xpath(f'//*[@id="root"]/div[3]/div[4]/div/div/div[1]/div[{j}]/div/div[1]/div').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[2]/ul/li[2]').click()
    Cod = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/ul/li[1]/div/span/strong').text
    Nome = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/h2/span').text
    CodFab = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/ul/li[2]/span/strong').text
    CodBar = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/table/tbody/tr[2]/td[2]').text
    CodNCM = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/table/tbody/tr[3]/td[2]').text
    Valor = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div[1]/div/span/strong').text
    Valor = float(Valor[2:].replace(',', '.'))
    PesoBruto = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/table/tbody/tr[4]/td[2]').text
    PCs = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/ul/li[2]').text
    PCs = int(PCs[10:-3])
    Desc = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[2]/div/div[3]/ul/li[4]/div').text
    lista_prod.append([Nome, Valor, Cod, CodFab, CodBar, CodNCM, PesoBruto, PCs, estoque, Desc])
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[1]/div/div/button').click()



num_items = int(num_results // 12)
rest = int(1 + (num_results % 12))


for i in range(num_items+1):
    if i==num_items:
        for c in range(1,rest):
            print(f'ITEM {c}')
            PegarInfo(c)
    else:
        for j in range(1,13):
            print(f'ITEM NUMERO {j}, pg: {i+1}')
            PegarInfo(j)

        driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[4]/div/div/div[2]/ul/li[12]/a').click()
    if i%1==0:
        df = pd.DataFrame(lista_prod)
        date = datetime.now()
        date = date.strftime('%d-%m-%Y_%H:%M')
        df.to_excel(f'Relatório_{date}.xlsx', index=False, header=["nome", "valor", "cod_dif", "cod_fab", "cod_bar", "cod_ncm", "peso", "peças", "estoque", "descrição"])

    

df = pd.DataFrame(lista_prod)
date = datetime.now()
date = date.strftime('%d-%m-%Y_%H:%M')
df.to_excel(f'Relatório_{date}.xlsx', index=False, header=["nome", "valor", "cod_dif", "cod_fab", "cod_bar", "cod_ncm", "peso", "peças", "estoque", "descrição"])
