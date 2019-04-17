#!/bin/bash
# ##################################################
# BASH script 
# Desinstalador Ardublock_IT10	
# version="0.0.1"              
#
# HISTORY:
#
# * DATE 17/04/2019 - v0.0.1 First Creation
# ##################################################
echo -e "$0\t$(date)" >> unistaller.log  # logger

rm -rf ~/.local/share/ArduinoIT10
read -p "Remover carpeta de usuario? (Respalde cualquier información Importante). Estas Seguro? Si=S    " REPLY
		if [[ $REPLY =~ ^[Ss]$ ]]
			then
		#do dangerous stuff
				rm -rf ~/Arduino/ 
        			echo "removiendo carpeta de usuario Arduino  ..."
		else
		exit
		fi
echo "Desinstalación completa"
