# tello-beginner

```

tello-beginner
├── images
│   ├── Tello Aircraft Diagram.png
│   ├── Tello App.png
│   ├── Tello Architecture.png
│   ├── Tello EDU App.png
│   ├── WhatsApp Image 2020-09-11 at 10.54.52 PM.jpeg
│   ├── WhatsApp Image 2020-09-11 at 10.54.53 PM (1).jpeg
│   ├── WhatsApp Image 2020-09-11 at 10.54.53 PM.jpeg
│   ├── WhatsApp Image 2020-09-11 at 10.54.54 PM (1).jpeg
│   ├── WhatsApp Image 2020-09-11 at 10.54.54 PM.jpeg
│   ├── WhatsApp Image 2020-09-11 at 10.54.55 PM (1).jpeg
│   ├── WhatsApp Image 2020-09-11 at 10.54.55 PM.jpeg
│   ├── WhatsApp Image 2020-09-11 at 10.54.56 PM.jpeg
│   └── WhatsApp Video 2020-09-11 at 10.58.41 PM.mp4
├── README.md
├── reference
│   └── TelloDoc
│       ├── FIRA-AIR
│       │   ├── FIRA Air 2019 - Emergency Service (Outdoor).pdf
│       │   ├── FIRA Air - Autonomous Race - Google Docs.pdf
│       │   ├── FIRA Air - Autonomous Race (U19) - 2019.pdf
│       │   └── FIRA Air - Emergency Service Indoor - 2019.pdf
│       ├── Official Documents
│       │   ├── Tello Mission Pad User Guide.pdf
│       │   ├── Tello.pdf
│       │   ├── Tello+Quick+Start+Guide_V1.2+multi.pdf
│       │   ├── Tello SDK 2.0 User Guide.pdf
│       │   ├── Tello SDK Documentation EN_1.3_1122.pdf
│       │   └── Tello_User_Manual_V1.2_EN.pdf
│       ├── Tello2.py
│       ├── Tello3.py
│       └── Tentatives
│           ├── Tello Programme Tentative.doc
│           ├── Tello Programme Tentative.docx
│           └── Tello Programme Tentative.odt
└── scripts
    ├── tello-command.py
    ├── tello-command-swarm.py
    ├── tello-state.py
    └── tello-stream.py

```

## Introduction

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/Tello%20Aircraft%20Diagram.png)

**Tello** is a **small quadcopter that features a Vision Positioning System and an 
onboard camera**. Using its **Vision Positioning System and advanced flight 
controller, it can hover in place and is suitable for flying indoors**. Advanced 
features like **Bounce mode, 8D Flips, and EZ Shots** make using Tello fun. Tello 
**captures 5 megapixel photos and streams 720p live video** to the Tello app on a 
mobile device. Its maximum **flight time is approximately 13 minutes***, and its 
**maximum flight distance is 328 ft (100 m)**. Failsafe Protection enables Tello to 
land safely even if you lose connection and its propeller guards can be used to 
enhance safety.

Aircraft | Description
------------ | -------------
Weight | Approximately 80 g (Propellers and Battery Included)
Dimensions | 98×92.5×41 mm
Propeller | 3 inches
Built-in Functions | Range Finder, Barometer, LED, Vision System, 2.4 GHz 802.11n Wi-Fi, 720p Live View
Port | Micro USB Charging Port


Flight Performance | Description
------------ | -------------
Max Flight Distance | 100m
Max Speed | 8m/s
Max Flight Time | 13min
Max Flight Height | 30m

Battery | Description
------------ | -------------
Detachable Battery | 1.1Ah/3.8V

Camera | Description
------------ | -------------
Photo | 5MP (2592x1936)
FOV | 82.6°
Video | HD720P30
Format | JPG(Photo); MP4(Video)
EIS | Yes

## Download the Tello App

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/Tello%20App.png)

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/Tello%20EDU%20App.png)

# Program the Ryze Tello
## Tello EDU App

*Please download Tello EDU apps before proceed with these steps*

**Steps**
1. Check the **wifi address** inside the drone:

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/WhatsApp%20Image%202020-09-11%20at%2010.54.56%20PM.jpeg)

2. Insert the batteries and **turn on** the drone:

![[Tello] Beginners Guide: Turn ON the drones](https://youtu.be/tgb-I981q9g)

3. **Connect** the drone to the phone, tablet etc.

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/WhatsApp%20Image%202020-09-11%20at%2010.54.52%20PM.jpeg)

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/WhatsApp%20Image%202020-09-11%20at%2010.54.54%20PM.jpeg)

4. Open **Tello EDU** App:

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/WhatsApp%20Image%202020-09-11%20at%2010.54.53%20PM.jpeg)

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/WhatsApp%20Image%202020-09-11%20at%2010.54.54%20PM%20(1).jpeg)

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/WhatsApp%20Image%202020-09-11%20at%2010.54.55%20PM.jpeg)

4. **Drag and drop the blocks**, and ready to fly!

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/WhatsApp%20Image%202020-09-11%20at%2010.54.55%20PM%20(1).jpeg)

### Examples
1. Takeoff and land

## Python Codes

## Important Notes
```
"""
The Tello SDK connects to the aircraft through a Wi-Fi UDP port, allowing users 
to control the aircraft with text commands.

By establish a UPD communication port, which can implement simple interaction 
with Tello, including sending SDK instructions to Tello and receiving Tello 
information.
"""
```

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/Tello%20Architecture.png)

### tello-command.py

```python
#!/usr/bin/python

"""
#!/usr/bin/python

"""
The Tello SDK connects to the aircraft through a Wi-Fi UDP port, allowing users 
to control the aircraft with text commands.

By establish a UPD communication port, which can implement simple interaction 
with Tello, including sending SDK instructions to Tello and receiving Tello 
information.
"""

#!/usr/bin/python

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
local_port = 9000

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
		msg = raw_input('') # change raw_input --> input for Python 3
		if not msg:
			break
		if 'end' in msg:
			sock.close()
			break
		# sending command
		print("[SEND]: Sending [{}] command...".format(colored(msg, 'yellow')))
		sent = sock.sendto(msg, tello_address)

	except Exception as err:
		print(err)
		sock.close()
		break
```

#### Commands

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/Screenshot%202020-09-12%2000:16:19.png)

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/Screenshot%202020-09-12%2000:16:57.png)

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/Screenshot%202020-09-12%2000:17:27.png)

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/Screenshot%202020-09-12%2000:18:07.png)

### tello-state.py

```python
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
```

### tello-stream.py

```python
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
```
