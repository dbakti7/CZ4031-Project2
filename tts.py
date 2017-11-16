from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("audio/test.mp3")
    os.system("afplay audio/test.mp3")
