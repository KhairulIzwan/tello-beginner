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

# close/clean streams		
tello_video.release()
cv2.destroyAllWindows()
