import smtplib
import grovepi

from time import sleep
from picamera import PiCamera
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Einstellungen für Camera:
camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 15

#   Email Variabeln
SMTP_SERVER = 'smtp.gmail.com' #Email Server
SMTP_PORT = 587 #Server Port
GMAIL_USERNAME = 'senderadresse@gmail.com' #eigene Gmail Sender-Mailadresse
GMAIL_PASSWORD = 'supergeheimes Passwort'  #Gmail Passwort (extra für Anwendungen ausserhalb Gmail als Token generiert)



class Emailer:
    def sendmail(self, recipient, subject, content, image):

        #Create Headers
        emailData = MIMEMultipart()
        emailData['Subject'] = subject
        emailData['To'] = recipient
        emailData['From'] = GMAIL_USERNAME

        #Textdaten anhängen?
        emailData.attach(MIMEText(content))

        #Bilddaten von Bild erstellen
        imageData = MIMEImage(open(image, 'rb').read(), 'jpg')
        imageData.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
        emailData.attach(imageData)

        #Verbindung zu Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Email senden & Exit
        session.sendmail(GMAIL_USERNAME, recipient, emailData.as_string())
        session.quit

sender = Emailer()

# wenn button gedrückt --> Photo aufnehmen:
button = 3

while True:
    if grovepi.pinMode(button,"INPUT"):
        print(grovepi.digitalRead(button))
        image = '/home/pi/Desktop/image.jpg'
        camera.capture(image)
        sendTo = 'Empfängeradresse@gmail.com'
        emailSubject = "Button wurde gedrückt &Bild wurde aufgenommen!"
        emailContent = "Button wurde gedrückt! Email öffnen, um zu sehen, wer es war...: "()
        sender.sendmail(sendTo, emailSubject, emailContent, image)
        print("Email gesendet")

    time.sleep(0.1)