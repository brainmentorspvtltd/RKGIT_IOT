from datetime import datetime as dt
import os, glob, random

chat = True
greetIntent = ["hi","hello","hey","hello there","hi there"]
dateIntent = ["date","tell me date","please tell me date"]
timeIntent = ["time","tell me time","please tell me time"]
musicIntent = ["play song", "play music", "please play song"]

while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()

    if msg in greetIntent:
        print("Hello User")
    elif msg in dateIntent:
        date = dt.now().date()
        print("Date is :",date.strftime("%d %B, %Y, %a"))
    elif msg in timeIntent:
        time = dt.now().time()
        print("Time is :",time.strftime("%H:%M:%S, %p"))
    elif msg in musicIntent:
        path = r"C:\Users\asus\Music\new_songs"
        os.chdir(path)
        songs = glob.glob("*.mp3")
        randomSong = random.choice(songs)
        print("Playing : " + randomSong)
        os.startfile(randomSong)
    elif msg == "bye":
        print("Bye User...")
        chat = False
    else:
        print("I don't understand")
