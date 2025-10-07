
import pyttsx3
from gtts import gTTS
import os

def speak(words, rate):
    
    #Greet with pyttsx3
    engine = pyttsx3.init()
    #Sets speed and volume
    engine.setProperty('rate', rate)
    engine.setProperty('volume', 1)
    #Speak text
    engine.say(words)
    #Waits until speach is finished
    engine.runAndWait()

    #speak with gtts
    # tts = gTTS(text="Hey Kevin!", lang='en')
    # tts.save("speech.mp3")       
    # os.system("start speech.mp3")      
