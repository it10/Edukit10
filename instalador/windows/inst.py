
#! python
# ##################################################
# python script
# Instalador Ardublock_IT10
# version="0.0.1"
#
# HISTORY:
#
# * DATE 4/12/2018 - v0.0.1 First Creation
#
# ##################################################

import wget
import shutil
from zipfile import ZipFile
import os
import pathlib
path = os.getcwd()
zip_file_path = path    #"C:\AA\BB"
homepath = os.path.expanduser(os.getenv('USERPROFILE'))
ardufolder = "\\Documents\\Arduino\\"
print('Instalando Arduino IDE')
url = 'https://downloads.arduino.cc/arduino-1.6.5-r5-windows.exe'
uurl = 'https://github.com/it10/ArdublockIT10/archive/master.zip'
uuurl = 'http://www.wch.cn/downloads/file/65.html'
wget.download(url)
print(' ')#Ejecutar
print('Instalando Arduino')
os.system('arduino-1.6.5-r5-windows.exe')
print('Instalando Controlador')
wget.download(uuurl)
os.system('CH341SER.EXE')
print(' Instalando Ardublock')
wget.download(uurl)
zip = ZipFile('ArdublockIT10-master.zip')
zip.extractall()
zip.close()
dir_path = cwd = os.getcwd()
print('dir_path')
print ( homepath)
destFolder = homepath + ardufolder
print ( destFolder)
if  os.path.exists(os.path.dirname(destFolder)):
    try:
        shutil.rmtree(destFolder)
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
if os.path.exists("ArdublockIT10-master"):
    shutil.copytree('ArdublockIT10-master', destFolder) #copiar a carpeta de usuario
if os.path.exists("ArdublockIT10-master.zip"):
    os.remove('ArdublockIT10-master.zip') #limpiar
if os.path.exists("arduino-1.6.5-r5-windows.exe"):
    os.remove('arduino-1.6.5-r5-windows.exe')
if os.path.exists("CH341SER.EXE"):
    os.remove('CH341SER.EXE')
if os.path.exists("ArdublockIT10-master"):
    shutil.rmtree('ArdublockIT10-master')

print('Instalación terminada. Adiós')
