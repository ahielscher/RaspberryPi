import smtplib
import grovepi

from time import sleep
from picamera import PiCamera
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import emailkonto #Datei "Emailkonto"importieren
import takepic #Datei "takepic"importieren

while True: 
    takepic.take_pic()
    emailkonto.Emailer()
    image = 'Foto'+str(x)+ 'jpg'
    takepic.take_pic(image)
    sendTo = 'Empfängeradresse@gmail.com'
    emailSubject = "Button wurde gedrückt &Bild wurde aufgenommen!"
    emailContent = "Button wurde gedrückt! Email öffnen, um zu sehen, wer es war...: "()
    emailkonto.Emailer(sendTo, emailSubject, emailContent, image)
    print("Email gesendet")
    
