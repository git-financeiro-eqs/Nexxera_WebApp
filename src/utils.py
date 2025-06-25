import pyautogui
from time import sleep
import pyperclip
from selenium.webdriver.common.keys import Keys
 

pyautogui.FAILSAFE = True
 
def encontrar_referencia(imagem):
    cont = 0
    while True:
        try:
            x, y, a, b = pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.89)    
            return (x, y)
        except:
            sleep(0.8)
            cont += 1
            if cont == 2:
                break
            pass
 
 
def encontrar_imagem(imagem):
    cont = 0
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(imagem, grayscale=True, confidence=0.89)    
            return (x, y)
        except:
            sleep(0.4)
            cont += 1
            if cont == 2:
                break
            pass



def encontrar_imagem2(imagem):
    cont = 0
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(imagem, grayscale=True, confidence=0.8)    
            return (x, y)
        except:
            sleep(0.4)
            cont += 1
            if cont == 2:
                break
            pass


    
def mover_seta(passos, direcao, actions):
    match direcao:
        case "Direita":
            direcao = Keys.ARROW_RIGHT
        case "Esquerda":
            direcao = Keys.ARROW_LEFT
        case "Cima":
            direcao = Keys.ARROW_UP
        case "Baixo":
            direcao = Keys.ARROW_DOWN
        case "tab":
            direcao = Keys.TAB

    for _ in range(passos):
        sleep(1)
        actions.send_keys(direcao).perform()
 
 
def retornar_objeto_banco(arquivo):
    banco = arquivo.split("_")[1]
    if banco == "396881":
        banco = "104"
    bancos = {
        "341": {
            "arquivo de config":"itaupag.2pr",
            "agencia": "6243",
            "conta": "15755",
            "subconta": "0"
            },
        "001": {
            "arquivo de config":"bbpg.2pr",
            "agencia": "3013",
            "conta": "3506150",
            "subconta": "0"
            },
        "237": {
            "arquivo de config":"bradesco.2pr",
            "agencia": "1472",
            "conta": "80900",
            "subconta": "001"
            },
        "033": {
            "arquivo de config":"stdpag.2pr",
            "agencia": "1512",
            "conta": "13001503",
            "subconta": "0"
            },
        "104": {
            "arquivo de config":"caixapg.2pr",
            "agencia": "04270",
            "conta": "0300000012",
            "subconta": "0"
            },
    }
    return banco, bancos[banco]
 
 
def colar_dado_no_campo(dado, actions):
    sleep(0.8)
    pyperclip.copy(dado)
    pyautogui.hotkey("ctrl", "v")
    sleep(1)
    if dado in ["001", "04270", "341", "104", "237", "033", "bradesco.2pr", "0300000012"]:
        pass
    else:
        mover_seta(1, "tab", actions)
 
 
def reabrir_rotina_siga():
    pyautogui.press("esc", interval=1)
    func_cta_pag = encontrar_imagem(r'Imagens\RotinaFuncoesCtasPag.png')
    x,y = func_cta_pag
    pyautogui.doubleClick(x, y)
    while True:
        clicar = encontrar_imagem(r'Imagens\BotaoConfirmar.png')
        if type(clicar) == tuple:
            x, y = clicar
            pyautogui.click(x, y)
            clicar2 = encontrar_imagem(r'Imagens\BotaoConfirmar.png')
            while type(clicar2) == tuple:
                x, y = clicar2
                pyautogui.click(x, y)
                clicar2 = encontrar_imagem(r'Imagens\BotaoConfirmar.png')
            break
    while True:
        abriu = encontrar_imagem(r'Imagens\ReferenciaAbriuRotina.png')
        if type(abriu) == tuple:
            return True
            
