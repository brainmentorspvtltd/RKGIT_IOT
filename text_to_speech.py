# first we need to import these packages
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


# text to speech function
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

#speak("Hello How are you...")

# speech recognition function
def get_audio():
    # initialize microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
	# waiting to recognize audio from user
        try:
            msg = r.recognize_google(audio)
            print("You said :",msg)
        except Exception as e:
            print("Exception: " + str(e))

    return msg

text = get_audio()
speak(text)
