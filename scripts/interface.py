#!/usr/bin/python3

from PySimpleGUI import PySimpleGUI as sg

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


def entrarServer():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Conectar ao servidor')],
        [sg.Text('O IP do drone em comunicação: '), sg.In(key='-IP')],
        [sg.Button('Conectar',size = (20,1))],
        [sg.Button('Voltar',size = (20,1))]
        ]
    return sg.Window("Entrando no server", layout,finalize=True)

def buscarFotos():
    sg.theme("DarkAmber")
    layout = [
            [sg.Text('Descarregar fotos', size = (20 , 1))],
            [sg.Text('Endereço do drone'), sg.In(key='-IP-')],
            [sg.Text('Senha'), sg.In(key='-S-')],
            [sg.Text('Repositório remoto'), sg.In(key='-RE-')],
            [sg.Text('Destino das fotos'), sg.In(key='-RO-'), sg.FolderBrowse(target='-RO-')],
            [sg.Button('Fazer download')],
            [sg.Button('Voltar')]
            ]
    return sg.Window('Buscar Fotos',layout, finalize=True) 

def instalarprerequisitos(): #Falta implementar
    sg.theme("DarkAmber")
    layout = [
        [sg.Button('Instalar pre requisitos', size = (20 , 1))],
        [sg.Button('Voltar')]
        ]
    return sg.Window('Instalar pre requisitos', layout, finalize=True)


def sobre():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Versão 0.5')],
        [sg.Button('Voltar',size=(20,1))]
    ]
    return sg.Window('Sobre', layout, finalize=True)   

def menu():
    sg.theme('DarkAmber')

    layout = [  
            [sg.Image(r'./Logo_Preto_Transparente.png', size = (250,250))],
            [sg.Button('Configurar server', size = (20 , 1))],
            [sg.Button('Entrar no server', size = (20 , 1))],
            [sg.Button('Buscar fotos', size = (20 , 1))],  
            [sg.Button('Instalar pre requisitos', size = (20 , 1))],
            [sg.Button('Sobre', size = (20 , 1))],
            [sg.Button('Sair', size = (20 , 1))]
        ]

    return sg.Window('4G Base by Skyrats', layout, element_justification = 'c', finalize=True)


def main():
    janela1, janela2 = menu(), None
    while True:
        window, event, values = sg.read_all_windows()
        if window == janela1:
            if (event == 'Configurar server'):
                janela2 = configurarServer()
                janela1.hide()
            if (event == 'Entrar no server'):
                janela2 = entrarServer()
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
        if event in (None, 'Voltar'):
            janela1.un_hide()
            janela2.close()
        if event in (None, 'Sair'):
            break
if __name__ == "__main__":
    main()