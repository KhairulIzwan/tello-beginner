#!/usr/bin/python

"""
The Tello SDK connects to the aircraft through a Wi-Fi UDP port, allowing users 
to control the aircraft with text commands.

By establish a UPD communication port, which can implement simple interaction 
with Tello, including sending SDK instructions to Tello and receiving Tello 
information.
"""

import socket
import time

drone1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
drone1.setsockopt(socket.SOL_SOCKET, 2, 'wlp2s0')

drone2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
drone2.setsockopt(socket.SOL_SOCKET, 2, 'wlxe8de271db8bb')

drone1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
drone2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

drone1.sendto('takeoff'.encode(), 0, ('192.168.10.1', 8889))
drone2.sendto('takeoff'.encode(), 0, ('192.168.10.1', 8889))

time.sleep(5)

drone1.sendto('command'.encode(), 0, ('192.168.10.1', 8889))
drone2.sendto('command'.encode(), 0, ('192.168.10.1', 8889))

drone1.sendto('land'.encode(), 0, ('192.168.10.1', 8889))
drone2.sendto('land'.encode(), 0, ('192.168.10.1', 8889))
