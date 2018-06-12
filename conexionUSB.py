#!/usr/bin/python


import commands

comando = "ls -l /dev/tty* | grep 'dialout' | rev | cut -d ' ' -f1 | rev | grep -e USB -e ACM"
status, output = commands.getstatusoutput(comando)

def devconn():
	if status == 0:
		salida = output.split('\n')
		return ' '.join(salida)

	else:
		return 'empty'

if __name__ == '__main__':
	print devconn()