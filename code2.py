import os
from gtts import gTTS

#Bootup
#tts = gTTS('Welcome to the program!')
#tts.save('audio.mp3')
#os.system('mpg123 audio.mp3')

def scanMode(scanned):    
    print(scanned)
    sData = gTTS(scanned)
    sData.save('scannedData.mp3')
    os.system('mpg123 scannedData.mp3')
    

while True:
    
    scanInput = input("Scan product: ")
    scanMode(scanInput)
    



