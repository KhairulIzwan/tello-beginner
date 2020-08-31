#
# Tello Python2 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time
import os


host = '0.0.0.0'
# port should be an integer from 1-65535 (0 is reserved). It's the TCP port 
# number to accept connections on from clients. Some systems may require 
# superuser privileges if the port is < 1024.
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
	count = 0
	while True: 
		try:
			data, server = sock.recvfrom(1518)
			print(data.decode(encoding="utf-8"))
		except Exception:
			print ('\nExit . . .\n')
			break


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 

	try:
		# TODO: Python2 use raw_input; Python3 use input
		msg = raw_input("");

		if not msg:
			break  

		if 'end' in msg:
#			print ('\n . . .\n')
			sock.close()  
			# Clear the screen.
#			os.system('clear')
			break

		# Send data
		msg = msg.encode(encoding="utf-8") 
		sent = sock.sendto(msg, tello_address)

	except KeyboardInterrupt:
		print ('\n . . .\n')
		sock.close()  
		# Clear the screen.
		os.system('clear')
		break
		
#	finally:
#		# Clear the screen.
#		os.system('clear')
#		break
