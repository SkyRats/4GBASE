#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
# coding: latin-1

#Imports
import os
import time

class uavPhotosTranfer:
    def __init__(self):
        os.system("sudo apt-get install sshpass")

    def buscarFotos(self):
        print("Qual o endereço de ip do drone? (USUARIO@IP)")
        ip = str(input())
        print("Qual a senha do drone?")
        senha = str(input())
        print("Qual a pasta das fotos no drone?")
        pastaDrone = str(input())
        print("Qual a pasta das fotos no seu computador?")
        pastaGs = str(input())

        numeroFoto = 0
        while True:
            ultimoArqv = os.popen("sshpass -p " + senha + " ssh " + ip + " '" + "ls -t " + pastaDrone + " | tail -1" + "'").read() #Pegar o último arquivo colocado
            print("Copiando o " + ultimoArqv)
            os.system("sshpass -p " + senha + " scp -r " + ip + ":" + pastaDrone + "/" + ultimoArqv[:-1] + " " + pastaGs) #Copiar esse arquivo
            os.system("sshpass -p " + senha + " ssh " + ip +" 'rm " + pastaDrone + "/" + ultimoArqv[:-1] + "'")
            numeroFoto = numeroFoto + 1
            os.system("mv " + pastaGs + "/" + ultimoArqv[:-1] + " " + pastaGs + "/" + "FOTO" + str(numeroFoto) + ".png")

def main():
    photos = uavPhotosTranfer()
    photos.buscarFotos()

if __name__ == "__main__":
    main()