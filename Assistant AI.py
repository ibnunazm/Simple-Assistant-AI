import pyttsx3 as tts
import speech_recognition as sr
import datetime as dt
import wikipedia as wp
import webbrowser as wb
import os
import smtplib as smtp

AI = "Cxianz"
print("Initializing " + AI)
MASTER = "Ibnu Nazm"

engine = tts.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def Greating():
    hour = int(dt.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)

    elif hour >=12 and hour <18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-us")
        print(f"User said: {query}")
    
    except Exception as e:
        print("Say that again please")
        query = None
    
    return query


speak("Hello my name is " + AI)
Greating()
speak("I can help you!")
query = takeCommand()

if "wikipedia" in query.lower():
    speak("Searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wp.summary(query, sentences = 2)
    print(results)
    speak(results)

elif "youtube" in query.lower():
    wb.open_new_tab('https://www.youtube.com/')

elif "google" in query.lower():
    wb.open_new_tab('https://www.google.com/')
