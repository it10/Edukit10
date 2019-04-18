#!/bin/bash
# ##################################################
# BASH script
# Instalador Ardublock_IT10
# version="0.0.1"
#
# HISTORY:
#
# * DATE 27/11/2018 - v0.0.1 First Creation
# * DATE 17/04/2019 - Add folder revision for older install
# * DATE 18/04/29 - Add symbolic link for libreadline
# ##################################################
echo -e "$0\t$(date)" >> scripts.log  # logger
DIRECTORY="ArduinoIT10"
ARDUINO_DIRECTORY="Arduino"
PKG="git unzip  wget xz-utils libncurses5 libreadline7" #Depencias gestionadas por el sistema

arduino_installer () {
	ARD="arduino"
	if  : dpkg-query -l $ARD > /dev/null ;
	read -p "La version de Arduino se va a reemplazar.(Respalde cualquier información Importante). Estas Seguro? Si=S    " REPLY
	then
		if [[ $REPLY =~ ^[Ss]$ ]]
			then
				#do dangerous stuff
				sudo apt remove $ARD -y
		else
		exit
		fi

	fi

MACHINE_TYPE=`uname -m`
if [ ${MACHINE_TYPE} == 'x86_64' ];
	then
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
		#./arduino-linux-setup.sh $user		#group handling
	sudo usermod -a -G dialout $USER
	sudo /bin/bash install.sh 			#Actual Installer
	echo "Parte 1: Instalacion IDE Arduino completa"
	cd ..
}

ArdublockIT10 () {

	wget https://github.com/it10/ArdublockIT10/archive/master.zip
	unzip master.zip
	cd ~/
	if [ ! -d "$ARDUINO_DIRECTORY" ];
		then  	# Control will enter here if $DIRECTORY does NOT exists.
			mkdir ~/Arduino/
	fi
	cd ~/.local/share/ArduinoIT10/ArdublockIT10-master
	cp -r tools ~/Arduino/
	echo "Ardublock Instalado"
	cd ..
	rm -r ArdublockIT10-master -f
	rm master.zip
}
##----------------------------------------------------
if  dpkg-query -l $PKG > /dev/null ;
	then
			sudo apt install $PKG -y
			echo "instalando dependencias..."
else
echo "exiting ..."
fi
cd ~/.local/share/
if [ -d "$DIRECTORY" ];
	then	# Control will enter here if $DIRECTORY exists.
		rm -rf $DIRECTORY
fi

mkdir $DIRECTORY
cd $DIRECTORY
arduino_installer
ArdublockIT10
FILE=/lib/x86_64-linux-gnu/libreadline.so.6
if test -f "$FILE";
	then
    echo "$FILE exist"
else
sudo ln -s /lib/x86_64-linux-gnu/libreadline.so.7 /lib/x86_64-linux-gnu/libreadline.so.6
fi



echo "nos vimos, bye bye, ciao,auf Wiedersehen, 侨, さようなら, Sayōnara, chauchis"
