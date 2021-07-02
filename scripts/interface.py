#!/usr/bin/python3

from PySimpleGUI import PySimpleGUI as sg
import os
import time

# Window do menu principal
def menu():
    # Theme
    sg.theme('DarkAmber')
    # Layout
    layout = [  
            [sg.Image(r'images/Logo_Preto_Transparente.png', size = (250,250))],
            [sg.Button('Configurar server', size = (20 , 1))],
            [sg.Button('Entrar no server', size = (20 , 1))],
            [sg.Button('Buscar fotos', size = (20 , 1))],  
            [sg.Button('Instalar pre requisitos', size = (20 , 1))],
            [sg.Button('Sobre', size = (20 , 1))],
            [sg.Button('Sair', size = (20 , 1))]
        ]
    # Window
    return sg.Window('4G Base by Skyrats', layout, element_justification = 'c', finalize=True)

# Eventos do menu
def menuEvent(event):
    global janela1, janela2

    if (event == 'Configurar server'):
        janela2 = configurarServer()
        janela1.hide()
    if (event == 'Entrar no server'):
        janela2 = configurarClient()
        janela1.hide()
    if (event == 'Buscar fotos'):
        janela2 = buscarFotos()
        janela1.hide()
    if (event == 'Instalar pre requisitos'):
        janela2 = instalarprerequisitos()
        janela1.hide()
    if (event == 'Sobre'):
        janela2 = sobre()
        janela1.hide()

# Window de configurações do server
def configurarServer():
    sg.theme("DarkAmber")
    
    layout = [
                [sg.Text('Configurações do servidor')],
                [sg.Button('Iniciar', size = (20,1))],
                [sg.Button('Reiniciar', size = (20,1))],
                [sg.Button('Desligar', size = (20,1))],
                [sg.Button('Ver status', size = (20,1))],
                [sg.Button('Ver lista de conexões', size = (20,1))],
                [sg.Button('Voltar', size = (20,1))]
    ]

    return sg.Window('Configurar server', layout, finalize=True)

# Eventos da configuração do server
def configurarServerEvents(event):
    if (event == 'Iniciar'):
        os.system("sudo service ssh start")
    elif (event == 'Reiniciar'):
        os.system("sudo service ssh restart")
    elif (event == 'Desligar'):
        os.system("sudo service ssh stop")
    elif (event == 'Ver status'):
        os.system("sudo service ssh status")
    elif (event == 'Ver lista de conexões'):
        # Ainda não implementado
        pass
    return 0

# Window de configuração do client
def configurarClient():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Conectar ao servidor')],
        [sg.Button('Conectar',size = (20,1))],
        [sg.Button('Voltar',size = (20,1))]
        ]
    return sg.Window("Entrando no server", layout,finalize=True)

# Eventos do client
def configurarClientEvents(event):
    if event == 'Conectar':
        os.system("sudo service ssh start")

# Window do download de fotos
def buscarFotos():
    sg.theme("DarkAmber")
    layout = [
            [sg.Text('Descarregar fotos')],
            [sg.Text('Endereço do drone', size = (20,1)), sg.In(key='-IP-', size = (30, 1))],
            [sg.Text('Senha do drone', size = (20,1)), sg.In(key='-S-', size = (30, 1))],
            [sg.Text('Repositório remoto', size = (20,1)), sg.In(key='-RE-', size = (30, 1))],
            [sg.Text('Destino das fotos', size = (20,1)), sg.In(key='-RO-', size = (30, 1)), sg.FolderBrowse(target='-RO-')],
            [sg.Button('Fazer download')],
            [sg.Button('Voltar')]
            ]
    return sg.Window('Buscar Fotos',layout, finalize=True) 

# Eventos do download de fotos
def entrarServerEvents(event, values):
    ip, senha, pastaDrone, pastaGs = values[0], values[1], values[2], values[3]
    numeroFoto = 0

    if event == 'Fazer download':
        pass

def instalarprerequisitos(): #Falta implementar
    sg.theme("DarkAmber")
    layout = [
        [sg.Button('Instalar pre requisitos', size = (20 , 1))],
        [sg.Button('Voltar')]
    ]
    
    return sg.Window('Instalar pre requisitos', layout, finalize=True, element_justification = 'c')

# Eventos da instalação de pré requisitos
def entrarServerEvents(events):
    pass

def sobre():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Versão 0.5')],
        [sg.Button('Voltar',size=(20,1))]
    ]
    return sg.Window('Sobre', layout, element_justification = 'c', finalize=True)   

# Eventos do sobre
def entrarServerEvents(events):
    pass

def main():
    global janela1, janela2

    while True:
        window, event, values = sg.read_all_windows()
        if window == janela1:
            menuEvent(event)
        if window.TKroot.title == 'Configurar server':
            configurarServerEvents(event)
        if window.TKroot.title == 'Entrar no server':
            configurarServerEvents(event)
        if event in (None, 'Voltar'):
            janela1.un_hide()
            janela2.close()
        if event in (None, 'Sair'):
            break


# Variaveis globais
janela1, janela2 = menu(), None

if __name__ == "__main__":
    main()