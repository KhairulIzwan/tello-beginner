# tello-beginner

```

tello-beginner
├── images
│   ├── Tello Aircraft Diagram.png
│   ├── Tello App.png
│   ├── Tello Architecture.png
│   └── Tello EDU App.png
├── README.md
├── reference
│   └── TelloDoc
│       ├── FIRA-AIR
│       │   ├── FIRA Air 2019 - Emergency Service (Outdoor).pdf
│       │   ├── FIRA Air - Autonomous Race - Google Docs.pdf
│       │   ├── FIRA Air - Autonomous Race (U19) - 2019.pdf
│       │   └── FIRA Air - Emergency Service Indoor - 2019.pdf
│       ├── Tello2.py
│       ├── Tello3.py
│       ├── Tello Mission Pad User Guide.pdf
│       ├── Tello.pdf
│       ├── Tello Programme Tentative.doc
│       ├── Tello Programme Tentative.docx
│       ├── Tello Programme Tentative.odt
│       ├── Tello+Quick+Start+Guide_V1.2+multi.pdf
│       ├── Tello SDK 2.0 User Guide.pdf
│       ├── Tello SDK Documentation EN_1.3_1122.pdf
│       └── Tello_User_Manual_V1.2_EN.pdf
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

## Download the Tello App

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/Tello%20App.png)

![GitHub Logo](https://github.com/KhairulIzwan/tello-beginner/blob/master/images/Tello%20EDU%20App.png)

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
