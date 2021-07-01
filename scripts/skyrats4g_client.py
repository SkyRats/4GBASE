#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
# coding: latin-1

#Imports
import os
import time
#import PySimpleGUI as sg

def interfacePrincipal(): #Interface principal
  os.system("./src/bash/arte.sh")
  print("\t \t \t \t \t \t \t \t \t \t \t \t4G Base for Ubuntu 18.04")
  print("    1 - Configurar server")
  print("    2 - Configurar client")
  print("    3 - Buscar fotos do drone")
  print("    4 - Instalar pre-requisitos")
  print("    Outro - Encerrar programa")
  return int(input())

def configurarServer():
  while True:
    print("Escolha o que fazer agora...")
    print("1 - Iniciar server")
    print("2 - Reiniciar server")
    print("3 - Desligar server")
    print("4 - Ver status do server")
    print("5 - Ver lista de conexões")
    # Ir colocando opção aqui

    escolha = int(input())
    if escolha == 1:
      os.system("sudo service ssh start")
    elif escolha == 2:
      os.system("sudo service ssh restart")
    elif escolha == 3:
      os.system("sudo service ssh stop")
    elif escolha == 4:
      os.system("sudo service ssh status")
    elif escolha == 5:
      print("ainda nao fizemos essa parte")
    else:
      print("Opcao invalida...")
      return
  


def configurarClient():
  while True:
    print("Escolha o que fazer agora...")
    print("1 - Conectar ao servidor")

    escolha = int(input())
    if escolha == 1:
      os.system("sudo service ssh start")
    else:
      print("Opcao invalida...")
    
def buscarFotos():
  print("Qual o endereço de ip do drone? (USUARIO@IP")
  ip = str(input())
  print("Qual a senha do drone?")
  senha = str(input())
  print("Qual a pasta das fotos no drone?")
  pastaDrone = str(input())
  print("Qual a pasta das fotos no seu computador?")
  pastaGs = str(input())

  ultimoArqv = os.popen("ls -t " + pastaGs + " | tail -1").read() #Pegar o último arquivo colocado

  os.system("sshpass -p " + senha + " ssh " + ip + "'" + "scp " + ip + ":" + pastaDrone + "/" + ultimoArqv + " " + pastaGs + "'") #Copiar esse arquivo
  
  #Apagar ele

  os.system("sshpass -p " + senha + " ssh " + ip +"'" "ssh " + senha + "@" + ip +": 'rm " + pastaDrone + "/" + ultimoArqv + "'" + "'")

  pastaDrone + "/" + ultimoArqv

  print(ultimoArqv)

  #print(tmp)

  #Pegar primeiro arquivo
  #tmp = os.popen("ls").read()
  
  
  
  
  #Automação sem senha: sshpass -p SENHA  ssh USUARIO@IP 'COMANDO'
  #Puxar Arquivos: os.system("scp USUARIO@IP: LOCAL DO ARQUIVO")
  #Remover: os.system("ssh SENHA@IP: 'rm LOCAL ARQUIVO'")

def instalacao():
  print("Para de preguiça e entra ae: https://askubuntu.com/questions/759880/where-is-the-ubuntu-file-system-root-directory-in-windows-subsystem-for-linux-an")
  print("Mande algo para continuar...")
  return input("")
  #sudo apt install sshpass

def main():
  #root = Tk()
  #root.mainloop()
  while True:
    escolha = interfacePrincipal()
    if escolha == 1:
      configurarServer()
    elif escolha == 2:
      configurarClient()
    elif escolha == 3:
      buscarFotos()
    elif escolha == 4:
      instalacao()
    elif escolha == 5:
      return
    else:
      return

if __name__ == "__main__":
    main()