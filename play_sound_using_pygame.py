import pygame
from gtts import gTTS

pygame.init()
pygame.mixer.init()

# text to speech function
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

msg = "hello how are you.."
speak(msg)
