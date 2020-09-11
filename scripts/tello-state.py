#!/usr/bin/python

"""
The Tello SDK connects to the aircraft through a Wi-Fi UDP port, allowing users 
to control the aircraft with text commands.

By establish a UPD communication port, which can implement simple interaction 
with Tello, including sending SDK instructions to Tello and receiving Tello 
information.
"""

# import required libraries and packages
import socket
from termcolor import colored

# create a UDP socket -- for sending command and receiving state
print("[INFO]: Create a UDP socket...")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_ip = '192.168.10.1'
tello_port = 8889
tello_address = (tello_ip, tello_port)

# receiving tello-state configuration
local_ip = '0.0.0.0'
local_port = 8890

sock.bind((local_ip, local_port))

# initiate SDK mode
print("[INFO]: Initiate SDK mode...")
msg = "command"
msg = msg.encode(encoding="utf-8")

"""
send "command" to the Tello via UDP PORT 8889 to initiate SDK mode
"""
# sending command
print("[SEND]: Sending [{}] command...".format(colored(msg, 'yellow')))
sent = sock.sendto(msg, tello_address)

while True:
	try:		
		# receiving tello-sate
		data, server = sock.recvfrom(1024)
		data = data.decode(encoding="utf-8")
		print("[RECV]: Recieving [{}] command".format(colored(data, 'green')))
		
	except Exception as err:
		print("{}".format(colored(err, 'red')))
		# close a UDP socket -- for sending command
		print("[INFO]: Close a UDP socket...")
		sock.close()
		break
