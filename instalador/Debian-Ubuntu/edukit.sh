#!/bin/bash
# ##################################################
# BASH script 
# Instalador Ardublock_IT10	
# version="0.0.1"              
#
# HISTORY:
#
# * DATE 27/11/2018 - v0.0.1 First Creation
#
# ##################################################
echo -e "$0\t$(date)" >> scripts.log  # logger
PKG="git unzip  wget xz-utils libncurses5 libreadline5" #Depencias gestionadas por el sistema

arduino_installer () {
	ARD="arduino"
	if  : dpkg-query -l $ARD > /dev/null ;
	read -p "La version de Arduino se va a reemplazar.(Respalde cualquier información Importante). Estas Seguro? Si=S    " REPLY
	then
		if [[ $REPLY =~ ^[Ss]$ ]]
			then
		#do dangerous stuff
				sudo apt remove $ARD -y
        			echo "removiendo Arduino antiguo ..."
		else 
		exit
		fi
		
	fi	
	
MACHINE_TYPE=`uname -m`
if [ ${MACHINE_TYPE} == 'x86_64' ]; then
	echo "64 bit Arduino"	
       	wget https://downloads.arduino.cc/arduino-1.6.5-r5-linux64.tar.xz
  	tar xf arduino-1.6.5-r5-linux64.tar.xz
	rm arduino-1.6.5-r5-linux64.tar.xz
	# 64-bit stuff here
else
	echo "32 bit Arduino"
	wget https://downloads.arduino.cc/arduino-1.6.5-r5-linux32.tar.xz
  	tar xf arduino-1.6.5-r5-linux32.tar.xz
	rm arduino-1.6.5-r5-linux32tar.xz
      	# 32-bit stuff here
fi
	cd arduino-1.6.5-r5
	echo "Scripts arduino"
	#./arduino-linux-setup.sh $user		#group handling
	sudo usermod -a -G dialout $USER
	sudo /bin/bash install.sh 			#Actual Installer
	cd ..
}

ArdublockIT10 () {

	wget https://github.com/it10/ArdublockIT10/archive/master.zip
	unzip master.zip
	cd ArdublockIT10-master	
	mkdir ~/Arduino/
	cp -r tools ~/Arduino/
	echo "Ardublock Instalado"
	cd ..
	rm -r ArdublockIT10-master -f
	rm master.zip 
}
if  dpkg-query -l $PKG > /dev/null ;
	then sudo apt install $PKG -y
	echo "instalando dependencias..."
	
	
else 
		echo "exiting ..."
fi
cd ~/.local/share/
mkdir ArduinoIT10 
cd ArduinoIT10
arduino_installer
ArdublockIT10

echo "nos vimos, bye bye, ciao,auf Wiedersehen, 侨, さようなら, Sayōnara, chauchis"

