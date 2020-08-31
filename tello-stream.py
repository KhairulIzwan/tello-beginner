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
from time import sleep
import cv2
from imutils import resize

## create a UDP socket -- for sending command and receiving response
#print("[INFO]: Create a UDP socket...")
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#tello_ip = '192.168.10.1'
#tello_port = 8889
#tello_address = (tello_ip, tello_port)

## receiving command response configuration
#local_ip = ''
#local_port = 8889

#sock.bind((local_ip, local_port))

## initiate SDK mode
#print("[INFO]: Initiate SDK mode...")
#msg = "command"
#msg = msg.encode(encoding="utf-8")

#"""
#send "command" to the Tello via UDP PORT 8889 to initiate SDK mode
#"""
## sending command
#print("[SEND]: Sending [{}] command...".format(colored(msg, 'yellow')))
#sent = sock.sendto(msg, tello_address)

## receiving response
#data, server = sock.recvfrom(1024)
#data = data.decode(encoding="utf-8")
#print("[RECV]: Recieving [{}] response".format(colored(data, 'green')))

#"""
#send "stream" to the Tello via UDP PORT 8889 to enable video stream
#"""
## sending command
#msg = "streamon"
#msg = msg.encode(encoding="utf-8")
#print("[SEND]: Sending [{}] command...".format(colored(msg, 'yellow')))
#sent = sock.sendto(msg, tello_address)

## receiving response
#data, server = sock.recvfrom(1024)
#data = data.decode(encoding="utf-8")
#print("[RECV]: Recieving [{}] response".format(colored(data, 'green')))

tello_video = cv2.VideoCapture("udp://@0.0.0.0:11111")

while True:
	try:		
		# receiving video-stream
		ret, frame = tello_video.read()
		if ret:
			cv2.imshow('Tello', resize(frame, width=320))
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		
	except Exception as err:
		print("{}".format(colored(err, 'red')))
		# close a UDP socket -- for sending command
		print("[INFO]: Close a UDP socket...")
		sock.close()
		break
		
tello_video.release()
cv2.destroyAllWindows()
