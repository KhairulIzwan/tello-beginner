# tello-beginner

```

tello-beginner
├── images
│   └── Tello Aircraft Diagram.png
├── README.md
├── tello-command.py
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
