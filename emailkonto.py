import smtplib
import takepic


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#   Email Variabeln
SMTP_SERVER = 'smtp.gmail.com' #Email Server
SMTP_PORT = 587 #Server Port
GMAIL_USERNAME = 'senderadresse@gmail.com' #eigene Gmail Sender-Mailadresse
GMAIL_PASSWORD = 'geheimes Passwort'  #Gmail Passwort (extra für Anwendungen ausserhalb Gmail als Token generiert)

x=0

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
        imageData = MIMEImage(open(image, 'Bilder/Foto')+str(x)+ 'jpg')
        imageData.add_header('Content-Disposition', 'attachment; filename='Foto'+str(x)+'.jpg')
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


while True:

    image = 'Bilder/Foto'+str(x)+'.jpg'
    camera.capture(image)
    sendTo = 'Empfängeradresse@gmail.com'
    emailSubject = "Button wurde gedrückt &Bild wurde aufgenommen!"
    emailContent = "Button wurde gedrückt! Email öffnen, um zu sehen, wer es war...: "()
    sender.sendmail(sendTo, emailSubject, emailContent, image)
    print("Email gesendet")

    time.sleep(0.1)