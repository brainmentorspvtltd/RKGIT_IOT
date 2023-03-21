import streamlit as st
from datetime import datetime as dt
import os, glob, random
import json
import urllib.request as url

chat = True
greetIntent = ["hi","hello","hey","hello there","hi there"]
dateIntent = ["date","tell me date","please tell me date"]
timeIntent = ["time","tell me time","please tell me time"]
musicIntent = ["play song", "play music", "please play song"]
newsIntent = ["news","tell me news"]
news_category_intent = ["sports","politics","entertainment","science"]

st.set_page_config(
    page_title='Chat app',
    layout='wide')

st.title("Streamlit Chat Application...")
st.write("Try saying hi, play music, tell me date...")

form = st.form("chat_form")
msg = form.text_input("Enter your message...")
btn = form.form_submit_button("Send message")

if btn:
    msg = msg.lower()

    if msg in greetIntent:
        st.write("Hello User")
    elif msg in dateIntent:
        date = dt.now().date()
        st.write("Date is :",date.strftime("%d %B, %Y, %a"))
    elif msg in timeIntent:
        time = dt.now().time()
        st.write("Time is :",time.strftime("%H:%M:%S, %p"))
    elif msg in musicIntent:
        path = r"C:\Users\asus\Music\new_songs"
        os.chdir(path)
        songs = glob.glob("*.mp3")
        randomSong = random.choice(songs)
        st.write("Playing : " + randomSong)
        os.startfile(randomSong)
    elif msg in newsIntent:
        st.write("1. Politics")
        st.write("2. Entertainment")
        st.write("3. Sports")
        # form_2 = st.form("news_form")
        # msg_2 = form_2.text_input("Enter news category...")
        # btn_2 = form_2.form_submit_button("Send message")
    elif msg in news_category_intent:
        # news api
        path = f"https://newsapi.org/v2/top-headlines?country=in&category={msg}&apiKey=695e07af402f4b119f0703e9b19f4683"
        response = url.urlopen(path)
        data = json.load(response)
        articles = data['articles']

        for i in range(len(articles)):
            st.write(articles[i]['title'])
            st.write("*" * 40)
    elif msg == "bye":
        st.write("Bye User...")
        chat = False
    else:
        st.write("I don't understand")