from time import sleep
from picamera import PiCamera

import grovepi

x = 0

camera = PiCamera()
camera.resolution = (2592, 1944)

#Überprüfe ob schon Bild mit Namen besteht
def check_for_existing_pic():
    global x
    global camera
    FileNotFound = True
    while FileNotFound:
        try:  
            open('Bilder/Foto'+str(x)+'.jpg')
            print('File already exits')
            x+=1
        except FileNotFoundError:
            FileNotFound = False
            camera.capture('Bilder/Foto'+str(x)+'.jpg')


# Foto machen
def take_pic():

    buttonPort= 3
    run = True

    grovepi.pinMode(buttonPort, "INPUT")
    button_pushed = False
    camera.start_preview()
    sleep(.5)

    while run:
        digitalInput = grovepi.digitalRead(buttonPort)

        if digitalInput == 1 and button_pushed == False:
            button_pushed = True
            sleep(.5)
            check_for_existing_pic()
            camera.stop_preview()
            run = False

        if digitalInput == 0 and button_pushed == True:
            button_pushed = False
