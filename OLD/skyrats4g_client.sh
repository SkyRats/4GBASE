#!/bin/bash
echo "                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                @@@@@@@@@@@ .@@    @@@&  @@@       @@( @@@@@@@@@@@*    @@@@@@@@@@  @@@@@@@@@  @@@@@@@@@@@               
               @@@          .@@ @@@@      @@@      @@. @@@       @@@ &@@@      @@     @@@     @@@                       
                .@@@@@@@@@    @@@@*        #@@@@@@@@@  @@@ #@@@@@@@  @@@       @@     @        @@@@@@@@@@               
         @              @@@ .@@  @@@@             @@@  @@@    ,@@@    @@@      @@     /@@             @@@    #@         
         @@@   @@@@@@@@@@   .@@    ,@@@  @@@@@@@@@@#   @@@      @@@     *@@@@  @@     @@@     @@@@@@@@@@   @@@@         
         @@@@@@                                                                                         ,@@@@@@         
         @@@@@@@@  @@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@               ,@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@( @@@@@@@@@         
         @@@@@@@@@@@ %@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@           @@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@,         
         & &@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@* @@@@@@@@@@@     *@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@/ @@@@@@@@@@@  @         
         @@@  @@@@@@@@@@@ %@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@ @@@@@@@@@@@ ,@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@/ @@@@         
         @@@@@# %@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@/ @@@@@@@@@@@  @@@@@@         
         @@@@@@@@                                    .@@@@@@@@@@@@                                    &@@@@@@@@         
         @@@@@@@@  &@@@@@@@@@@@@  @@@@@@@@@@@@@@@  @@@  @@@@@@@   @@  @@@@@@@@@@@@@@@  &@@@@@@@@@@@@  @@@@@@@@@         
           @@@@@@     @@@@@@@@@@@@, #@@@@@@@@@/    @@@@@  *@@  @@@@@     @@@@@@@@@@  @@@@@@@@@@@@&    @@@@@@            
              @@@       @@@@@@@@@@@@@  @@@@@       @@@@@@@@  @@@@@@@       &@@@@# /@@@@@@@@@@@@       @@@@              
                @          @@@@@@@@@@@@            @@@@@@@@@@@@@@@@@            @@@@@@@@@@@@@         @                 
                                                     @@@@@@@@@@@@@@                                                     
                                                       @@@@@@@@@                                                        
                                                         &@@@@                                                          
                                                                                                                        
                                                                                                                       "

echo "                                                                                         4G Base for Ubuntu 18.04"
echo " "
echo "Escolha a opção: "
echo "    1 - Iniciar server SFTP"
echo "    2 - Conectar ao server SFTP"
echo "    3 - Conectar ao server SFTP"
echo "    4 - Encerrar programa"
echo "    5 - Instalar pre-requisitos"

read SELECT

        #Configurações Arquivo 1
arquivoConfig1="/etc/ssh/sshd_config"
#arquivoConfig1="/alo.txt" # Debug line
Aq1L1="Match group sftp" 
Aq1L2="ChrootDirectory /home"
Aq1L3="X11Forwarding no"
Aq1L4="AllowTcpForwarding no"
Aq1L5="ForceCommand internal-sftp"

flagInstall=0

if  [[ $SELECT -eq "1" ]]
then
    echo "Selecionada a opcao 1"
    exit 0
elif [[ $SELECT -eq "2" ]]
then
    echo "Selecionada a opcao 2"
    exit 0
elif [[ $SELECT -eq "3" ]]
then
    echo "Selecionada a opcao 3"
    exit 0
elif [[ $SELECT -eq "4" ]]
then
    echo "Encerrando programa"
    exit 0
elif [[ $SELECT -eq "5" ]]
then
    echo "Iniciando instalações"

    #sudo apt-get install vsftpd

    #sudo mv /etc/vsftpd.conf /etc/vsftpd.conf_orig

    #sudo nano /etc/vsftpd.conf

    #https://linuxconfig.org/how-to-setup-ftp-server-on-ubuntu-18-04-bionic-beaver-with-vsftpd

    #sudo apt install ssh

    while read LREAD
    do
        if [[ $LREAD == ${Aq1L1} ]]
        then
            if [[ $flagInstall -eq "0" ]]
            then
                echo "Arquivo 1 ja configurado..."
            fi
            flagInstall=$"1";
        fi
        #echo ${LREAD} #Debug line
        #echo ${flagInstall} #Debug line two
    done < ${arquivoConfig1}

    if [[ $flagInstall -eq "0" ]]
    then
        echo "Escrevendo arquivo 1..."
        echo " " >> ${arquivoConfig1}
        echo ${Aq1L1} >> ${arquivoConfig1}
        echo ${Aq1L2} >> ${arquivoConfig1}
        echo ${Aq1L3} >> ${arquivoConfig1}
        echo ${Aq1L4} >> ${arquivoConfig1}
        echo ${Aq1L5} >> ${arquivoConfig1}
    fi

    exit 0
else
    echo "Opcao invalida!!!"
    exit 1
fi