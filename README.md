# RaspberryPi
Bei Drücken eines Buttons wird ein Foto gemacht, welches per Mail verschickt wird.
Das Projekt wurde in Grundanforderung und Erweiterungen gegliedert.

------------------------

Material:
- RaspberryPi
- Button v1.2
- Camera v2.1

------------------------
________________________
*Version 1: "Abgaberaspberrypi.py"*

Als Grundfunktion gelten:
  - Eine durch das Drücken des Buttons ausgelöste Aktion.
  - Eine Kamera, welche mit einem Auslöser ein Bild macht.
  
  --> dafür wurden beide Funktionen einzeln programmiert und getestet.
  
________________________

1. Erweiterung:
  - Wenn der Button gedrückt wird, macht die Kamera ein Bild.
  
  --> für diese Verknüpfung wurden die vorher getesteten Funktionen gebraucht. 
  
________________________
  
2. Erweiterung:
  -eine Email mit dem Bild als anhang verschicken
  
  --> dieser Schritt forderte ein Bisschen mehr Vorbereitung: 
        
   - eine Email verschicken: dafür musste ein Gmail-Konto vorbereitet werden, das Passwort als Token von Gmail erhalten, sich im Code bei dem besagten Gmail-Konto anmelden und ein Email verschicken. Als Grundgerüst galt eine Anleitung aus dem Internet: 
      (https://bc-robotics.com/tutorials/sending-email-using-python-raspberry-pi/)
      

   - die Email musste nun mit einem Anhang versehen weden, welcher aus dem vorher programmierten Bild besteht. Als Vorlage wurde wieder eine Anleitung aus dem Internet verwendet, welche aber mit anderen Funktionen versehen werden musste, da andere Buttons verwendet wurden. 
      (https://bc-robotics.com/tutorials/sending-email-attached-photo-using-python-raspberry-pi/)
      
________________________
________________________
*Version 2: "takepic.py", "emailkonto.py", "Comboablauf.py"*

Gleich wie die Version 1, hier wurde aber mit sich verändernden Bildnamen und Bilder speichern gearbeitet. Es wurde versucht "schön" zu programmieren, indem ein Dokument das Foto bei Knopfdruck aufnimmt, überprüft, ob es den Namen schon gibt, und dann abspeichert. Auch das Mailverschicken wurde als einzelnes Dokument ausgeführt, wobei sich jedoch das Prblem stellte, dass für den Anhang das schon geschossene Bild benötigt wird. Beide Funktionen wurden in einem 'Ablauf'- Dokument zusammengeführt. 

. .
. .
. .

Aufgrund von Unsicherheiten bezüglich der Sicherheit und öffentlichen Zugänglichkeit wurden die Mailadressen un Passwörter entfernt.
