#!/bin/bash

# ##################################################
# BASH script 
# Instalador Ardublock_IT10	
version="0.0.1"              
#
# HISTORY:
#
# * DATE 27/11/2018 - v0.0.1 First Creation
#
# ##################################################
echo -e "$0\t$(date)" >> scripts.log  # logger

hash arduino  &> /dev/null
if [ $? -eq 1 ]; then
    echo >&2 "Arduino no encontrado, instalando ..."
    sudo apt install arduino
    wget https://github.com/it10/ArdublockIT10/archive/master.zip
    unzip master.zip
    cd ArdublockIT10-master && cp -r ~/Arduino/
   


#    mkdir ~/$user/Arduino/ 
else
	echo "arduino instalado"
fi

