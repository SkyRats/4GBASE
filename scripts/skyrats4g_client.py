#!/usr/bin/python
# coding=utf-8

#Imports
import os
import time
#import PySimpleGUI as sg

def interfacePrincipal(): #Interface principal
  os.system("./src/bash/arte.sh")
  print("\t \t \t \t \t \t \t \t \t \t \t \t4G Base for Ubuntu 18.04")
  print("    1 - Iniciar server SFTP")
  print("    2 - Conectar ao server SFTP")
  print("    3 - Instalar pre-requisitos")
  print("    Outro - Encerrar programa")
  return int(input())

def iniciarServer():
  print("Iniciando server...")

def conectarServer():
  print("Conectando ao server...")

def instalacao():
  print("Para de preguiça e entra ae: https://askubuntu.com/questions/759880/where-is-the-ubuntu-file-system-root-directory-in-windows-subsystem-for-linux-an")
  print("Mande algo para continuar...")
  return input("")

def main():
  #root = Tk()
  #root.mainloop()
  while True:
    escolha = interfacePrincipal()
    if escolha == 1:
      iniciarServer()
    elif escolha == 2:
      conectarServer()
    elif escolha == 3:
      instalacao()
    elif escolha == 4:
      instalacao()
    else:
      return

if __name__ == "__main__":
    main()