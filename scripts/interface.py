#!/usr/bin/python3

from PySimpleGUI import PySimpleGUI as sg

def configurarServer():
    sg.theme("DarkAmber")
    
    layout = [
                [sg.Button('Configurar server', size = (20 , 1))]
    ]

    return sg.Window('Configurar server', Layout = layout,finalize=True)


def entrarServer():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('O IP do drone em comunicação: ')],
        [sg.Text('Saida do terminal...')],
        [sg.Button('Cancelar entrada',size = (20,1))]
        ]
    return sg.Window("Entrando no server", layout,finalize=True)


def instalarprerequisitos():
    sg.theme("DarkAmber")
    layout =[sg.Button('Instalar pre requisitos', size = (20 , 1))]
    return sg.Window('Instalar pre requisitos',Layout = layout) 


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
            [sg.Button('Instalar pre requisitos', size = (20 , 1))],
            [sg.Button('Sobre', size = (20 , 1))],
            [sg.Button('Sair', size = (20 , 1))]
        ]

    return sg.Window('4G Base by Skyrats', layout, element_justification = 'c', finalize=True)


def main():
    janela1, janela2, janela3, janela4 = menu(), None, None, None
    while True:
        window, event, values = sg.read_all_windows()
        if window == janela1 and (event == sg.WIN_CLOSED or event == 'Sair'):
            break
        if window == janela1 and (event == 'Entrar no server'):
            janela2 = entrarServer()
            janela1.hide()
        if window == janela2 and (event == 'Cancelar entrada'):
            janela1.un_hide()
            janela2.close()

if __name__ == "__main__":
    main()