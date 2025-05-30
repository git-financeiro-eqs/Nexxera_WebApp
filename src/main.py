import os
import utils
import shutil
import easyocr
import zipfile
import pyautogui
import numpy as np
from time import sleep
from pathlib import Path
from datetime import datetime
from pyperclip import paste
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
 
 
pyautogui.FAILSAFE = True
 
 
def automacao(periodo):
    """
    Função principal. Nela está o fluxo da tarefa que esse programa realiza.
    """

    reader = easyocr.Reader(['pt'])
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)
    driver.get("https://webedi.nexxera.io/login")
    driver.maximize_window()
 
    driver.find_element(By.ID, "mailbox").send_keys("************")
    driver.find_element(By.ID, "password").send_keys("********")
    driver.find_element(By.ID, "submit").click()
 
    aux = 0
    while True:
        try:
            sair_alerta = driver.find_element(By.XPATH, "/html/body/div[4]/div/button")
            sleep(1.6)
            sair_alerta.click()
            break
        except:
            sleep(1)
            aux+=1
            if aux == 10:
                break
 
    while True:
        try:
            elemento_select = driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/skyline-table-pagination/table/thead/tr/th/select")
            select = Select(elemento_select)
            select.select_by_index(7)
            break
        except:
            sleep(1)
 
 
    data1 = periodo.split(" até ")[0].strip()
    data2 = periodo.split(" até ")[1].strip()
 
 
    while True:
        driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[1]/div/div[2]/ul/ng2-flatpickr/div/input[2]").clear()
        driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[1]/div/div[2]/ul/ng2-flatpickr/div/input[2]").send_keys(periodo)
 
        sleep(1.5)
        driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[1]/div/div[2]/ul/button").click()
 
        sleep(1.5)
        data_no_portal = driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[1]/div/div[2]/ul/ng2-flatpickr/div/input[2]").get_attribute("value")
        data_no_portal = str(data_no_portal)[:10]
 
        if data_no_portal in [data1, data2]:
            break

 
    sleep(5)
    if driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/thead/tr[1]/th[1]/input").is_selected():
        driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/thead/tr[1]/th[1]/input").click()
        if driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[1]/td[1]/input").is_selected():
            while driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[1]/td[1]/input").is_selected():
                sleep(1)
 
    driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/thead/tr[1]/th[1]/input").click()
    while not driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[2]/div/cdk-virtual-scroll-viewport/div[1]/table/tbody/tr[1]/td[1]/input").is_selected():
        sleep(1)
 
 
    sleep(5)
    driver.find_element(By.XPATH, "/html/body/app-root/app-shell/div/skyline-communication/div/div/div[2]/div/skyline-mailbox-table/div[3]/div/div/button[1]").click()
 
    sleep(15)
 
    pyautogui.hotkey("ctrl", "j", interval=2)
 
    pyautogui.press(["tab"]*4)
    pyautogui.press("enter", interval=3)
    pyautogui.press("f2", interval=0.5)
    pyautogui.hotkey('ctrl', 'c', interval=0.5)
       
    nome_do_arquivo = paste() + ".zip"
    pasta_downloads = Path.home() / "Downloads"
    caminho_completo = pasta_downloads / nome_do_arquivo
 
 
    pasta_destino = "C:\\Nex"
 
    try:
        os.mkdir(pasta_destino)
    except FileExistsError:
        shutil.rmtree(pasta_destino)
        os.mkdir(pasta_destino)
    except PermissionError:
        pass
 
 
    with zipfile.ZipFile(caminho_completo, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)
 
    os.remove(caminho_completo)
 
    pyautogui.press("esc", interval=0.5)
    pyautogui.hotkey("ctrl", "w", interval=0.6)
 
    driver.quit()
 
    agora = datetime.now()
    data_formatada = agora.strftime("%d/%m/%y")
    data_formatada2 = agora.strftime("%d/%m/%Y")
 
    arquivos = [arquivo for arquivo in os.listdir(pasta_destino) if not arquivo.endswith(".protocolo") and arquivo[:3] == "PAG" and arquivo.split("_")[1] != "422"]
 
    if arquivos:

        driver_siga = webdriver.Chrome(service=servico)
        driver_siga.get("https://totvs.eqsengenharia.com.br:8880/webapp/?E=servicos&P=sigamdi")
        sleep(15)
        driver_siga.maximize_window()
        actions = ActionChains(driver_siga)

 
        while True:
            try:
                driver_siga.find_element(By.CSS_SELECTOR, "#COMP4603")
                break
            except:
                pass
            sleep(1)

 
        for arq in arquivos:
 
            def lancar_CNAB(arq):
                """
                Função recursiva devido a possibilidade imprevisível do sistema alterar a Data Base voluntariosamente.
                Usando a tecnologia OCR como muleta de verificação a cada novo lançamento,
                faz-se uma conferência prévia da Data Base imediata no sistema 
                confrontando-a com a data extraída do computador através do método datetime.now()
                antes de se iniciar um novo lançamento.
                Em caso de inconformidade entre as datas, a automação reinicia o processo de lançamento.
                """
                sleep(2.5)

                esperar = utils.encontrar_imagem2(r'Imagens\ReferenciaAguarde.png')
                while type(esperar) == tuple:
                    esperar = utils.encontrar_imagem2(r'Imagens\ReferenciaAguarde.png')


                while True:
                    try:
                        referencia = utils.encontrar_referencia(r'Imagens\ReferenciaMatriz.png')
                        x, y = referencia
                        break
                    except:
                        try:
                            referencia = utils.encontrar_referencia(r'Imagens\ReferenciaMatriz2.png')
                            x, y = referencia
                            break
                        except:
                            pass
                   
                x = x - 75
                largura, altura = 76, 29
 
                screenshot = pyautogui.screenshot(region=(int(x), int(y), largura, altura))
 
                screenshot_np = np.array(screenshot)

                data_extraida = reader.readtext(screenshot_np, detail=0) 

                try:
                    if data_extraida[0] != data_formatada and data_extraida[0] != data_formatada2:
                        if utils.reabrir_rotina_siga():
                            return lancar_CNAB(arq)
                except:
                    if utils.reabrir_rotina_siga():
                        return lancar_CNAB(arq)
  
                sleep(1)
                pyautogui.hotkey("alt", "o", interval=1)
                pyautogui.press("n", interval=1)
                pyautogui.press("right", interval=1)
                pyautogui.press("down", interval=1)
                pyautogui.press("enter", interval=1)
 

                aux = 0
                while True:
                    esperar = utils.encontrar_imagem(r'Imagens\Referencia.png')
                    if type(esperar) == tuple:
                        break
                    aux+=1
                    if aux == 7:
                        pyautogui.hotkey("alt", "o", interval=1)
                        pyautogui.press("n", interval=1)
                        pyautogui.press("right", interval=1)
                        pyautogui.press("down", interval=1)
                        pyautogui.press("enter", interval=1)
                    sleep(1)

 
                sleep(0.5)
                pyautogui.press("enter", interval=0.2)
 
                while True:
                    clicar = utils.encontrar_imagem(r'Imagens\BotaoPerguntas.png')
                    if type(clicar) == tuple:
                        x, y = clicar
                        pyautogui.click(x, y)
                        abriu = utils.encontrar_imagem(r'Imagens\ReferenciaAbriuPerguntas.png')
                        if type(abriu) == tuple:
                            break
 
 
                sleep(1)

                utils.mover_seta(3, "tab", actions)
 
                caminho_absoluto = pasta_destino + "\\" + arq

                banco, dados_banco = utils.retornar_objeto_banco(arq)

                sleep(0.5)
                pyautogui.hotkey('ctrl', 'c', interval=0.8)
                verificacao = paste().strip()
                if not "PAG" in verificacao:
                    while not "PAG" in verificacao:
                        utils.mover_seta(1, "tab", actions)
                        pyautogui.hotkey('ctrl', 'c', interval=0.8)
                        verificacao = paste().strip()

 
                utils.colar_dado_no_campo(caminho_absoluto, actions)

                pyautogui.hotkey('ctrl', 'c', interval=0.8)
                atalho = paste().strip()

                if atalho != dados_banco["arquivo de config"]:

                    utils.colar_dado_no_campo(dados_banco["arquivo de config"], actions)
    
                    utils.colar_dado_no_campo(banco, actions)
    
                    utils.colar_dado_no_campo(dados_banco["agencia"], actions)

                    utils.colar_dado_no_campo(dados_banco["conta"], actions)
    
                    utils.colar_dado_no_campo(dados_banco["subconta"], actions)
    
                    pyautogui.press("space", interval=0.2)
                    pyautogui.press("up", interval=0.2)
                    pyautogui.press("enter", interval=0.2)


                while True:
                    clicar = utils.encontrar_imagem(r'Imagens\BotaoInformacoes.png')
                    if type(clicar) == tuple:
                        x, y = clicar
                        pyautogui.click(x, y)
                        abriu = utils.encontrar_imagem(r'Imagens\ReferenciaAbriuInformacoes.png')
                        if type(abriu) == tuple:
                            break
                        
                clicar = utils.encontrar_imagem(r'Imagens\BotaoExecutar.png')
                while type(clicar) != tuple:
                    clicar = utils.encontrar_imagem(r'Imagens\BotaoExecutar.png')
                x, y = clicar
                pyautogui.click(x, y)
                abriu = utils.encontrar_imagem(r'Imagens\ReferenciaAbriuInformacoes.png')
                while type(abriu) == tuple:
                    pyautogui.click(x, y)
                    abriu = utils.encontrar_imagem(r'Imagens\ReferenciaAbriuInformacoes.png')
                    
 
                sleep(1.5)
 
                while True:
                    esperar = utils.encontrar_imagem2(r'Imagens\ReferenciaAguarde.png')
                    if type(esperar) != tuple:
                        ignorar = utils.encontrar_imagem(r'Imagens\ReferenciaIgnorar.png')
                        ignorar2 = utils.encontrar_imagem(r'Imagens\ReferenciaIgnorar2.png')
                        ignorar3 = utils.encontrar_imagem(r'Imagens\ReferenciaIgnorar3.png')
                        ignorar4 = utils.encontrar_imagem(r'Imagens\ReferenciaIgnorar4.png')
                        ignorar5 = utils.encontrar_imagem(r'Imagens\ReferenciaIgnorar6.png')
                        erro_datab = utils.encontrar_imagem(r'Imagens\ErroDataBase.png')
                        arq_corromp = utils.encontrar_imagem(r'Imagens\ArqCorrompido.png')
                        if type(arq_corromp) == tuple:
                            pyautogui.press("enter", interval=0.2)
                        if type(erro_datab) == tuple:
                            pyautogui.press("enter", interval=1)
                            if utils.reabrir_rotina_siga():
                                return lancar_CNAB(arq)
                        if type(ignorar2) == tuple or type(ignorar3) == tuple or type(ignorar4) == tuple or type(ignorar5) == tuple:
                            pyautogui.press("enter", interval=0.2)
                        if type(ignorar) == tuple:
                            pyautogui.press("enter", interval=0.2)
                            while True:
                                negar = utils.encontrar_imagem(r'Imagens\BotaoNao.png')
                                if type(negar) == tuple:
                                    negar = utils.encontrar_imagem(r'Imagens\BotaoNao.png')
                                    while type(negar) != tuple:
                                        negar = utils.encontrar_imagem(r'Imagens\BotaoNao.png')
                                    x, y = negar
                                    pyautogui.click(x, y, interval=0.5)
                                    negar = utils.encontrar_imagem(r'Imagens\BotaoNao.png')
                                    while type(negar) == tuple:
                                        x, y = negar
                                        pyautogui.click(x, y)
                                        negar = utils.encontrar_imagem(r'Imagens\BotaoNao.png')
                                    break

                        if type(arq_corromp) != tuple and type(erro_datab) != tuple and type(ignorar) != tuple and type(ignorar2) != tuple and type(ignorar3) != tuple and type(ignorar4) != tuple and type(ignorar5) != tuple:
                            esperar = utils.encontrar_imagem2(r'Imagens\ReferenciaAguarde.png')
                            if type(esperar) != tuple:
                                return
 
            lancar_CNAB(arq)
 
            sleep(1)
 
      