Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> msg = "Hello Ram"
>>> "Ram" in msg
True
>>> intent = ["hello", "hi", "hey"]
>>> "hello" in intent
True
>>> x = 12
y = x
z = 12
x == y
True
x is y
True
id(12)
140717024994440
id(x)
140717024994440
id(y)
140717024994440
id(z)
140717024994440
x = "Ram Sharma"
y = x
x == y
True
x is y
True
y = "Ram Sharma"
x
'Ram Sharma'
y
'Ram Sharma'
x == y
True
x is y
False
x = 5
x & 1
1
x = 6
x & 1
0
import datetime
datetime.datetime.now()
datetime.datetime(2023, 2, 21, 10, 18, 31, 163268)
datetime.datetime.now().date()
datetime.date(2023, 2, 21)
datetime.datetime.now().time()
datetime.time(10, 18, 44, 288430)
from datetime import datetime as dt
date = dt.now().date()
time = dt.now().time()
print(date)
2023-02-21
print(time)
10:20:21.895609
date.strftime("%d/%m/%y")
'21/02/23'
date.strftime("%d %b, %y")
'21 Feb, 23'
date.strftime("%d %B, %y")
'21 February, 23'
date.strftime("%d %B, %Y")
'21 February, 2023'
date.strftime("%d %B, %Y, %a")
'21 February, 2023, Tue'
date.strftime("%d %B, %Y, %A")
'21 February, 2023, Tuesday'
time.strftime("%H:%M:%S")
'10:20:21'
time.strftime("%H:%M:%S, %p")
'10:20:21, AM'
import os
os.getcwd()
'C:\\Python311'
os.listdir()
['code_test.py', 'DLLs', 'Doc', 'etc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python311.dll', 'pythonw.exe', 'Scripts', 'share', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']
import glob
glob.glob("*.mp3")
[]
path = "C:\Users\asus\Music\new_songs"
SyntaxError: incomplete input
path = "C:\Users\asus\Music\new_songs\"
SyntaxError: incomplete input
path = "C:\Music\Songs"
path = "C:\Music\Songs\new_songs"
path = "C:\Users\Music\Songs\new_songs"
SyntaxError: incomplete input
path = "C:\Music\Songs\new_songs"
print(path)
C:\Music\Songs
ew_songs
path = "C:/Users/asus/Music/new_songs"
path = "C:\\Users\\asus\\Music\\new_songs"
path = r"C:\Users\asus\Music\new_songs"
#raw string
path
'C:\\Users\\asus\\Music\\new_songs'
os.chdir(path)
os.getcwd()
'C:\\Users\\asus\\Music\\new_songs'
os.listdir()
['bang-bang.mp3', 'Faded.mp3', 'FadedCopy.mp3', 'fifa world cup.mp3', 'song.mp3', 'songCopy.mp3']
glob.glob("*.mp3")
['bang-bang.mp3', 'Faded.mp3', 'FadedCopy.mp3', 'fifa world cup.mp3', 'song.mp3', 'songCopy.mp3']
import random
songs = glob.glob("*.mp3")
random_song = random.choice(songs)
os.startfile(random_song)
random_song = random.choice(songs)
os.startfile(random_song)
random_song = random.choice(songs)
os.startfile(random_song)
random_song = random.choice(songs)
os.startfile(random_song)
random.choice(songs)
'Faded.mp3'
random.choice(songs)
'FadedCopy.mp3'
random.choice(songs)
'FadedCopy.mp3'
random.choice(songs)
'Faded.mp3'
random.choice(songs)
'songCopy.mp3'
random.choice(songs)
'bang-bang.mp3'
random.choice(songs)
'bang-bang.mp3'
random.choice(songs)
'bang-bang.mp3'
random_song = random.choice(songs)
os.startfile(random_song)
