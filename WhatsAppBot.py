import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import logging

logging.basicConfig(filename='whatsapp_log.txt', level=logging.INFO, format='%(asctime)s %(message)s')

webbrowser.open('https://web.whatsapp.com/')
sleep(30)


workbook = openpyxl.load_workbook('Send.xlsx')
contatos = workbook['Plan1']

for linha in contatos.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    mensagem = linha[2].value
    texto = f'Oi {nome}! {mensagem}'

    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(texto)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(20)

        seta = pyautogui.locateCenterOnScreen('seta.png')
        if seta is None:
            raise Exception('Botão de enviar não encontrado')
        sleep(20)
        pyautogui.click(seta.x, seta.y)
        sleep(20)

        pyautogui.hotkey('ctrl', 'w')
        sleep(20)

        logging.info(f'Mensagem enviada para {nome} no número {telefone}')
    except Exception as erro:
        logging.error(f'Não foi possível enviar a mensagem para {nome} no número {telefone}: {erro}')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}\n')
