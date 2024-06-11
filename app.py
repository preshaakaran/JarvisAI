import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import datetime
import subprocess
import sys

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold=1
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
    
        except Exception as e:
            print("Some Error Ocurred.Sorry",str(e))
            sys.exit()

if __name__=='__main__':
    print("Hello")
    say("Hello I am Jarvis AI")
    say(" Hi,Presha How may I help you?")
    while True:
        query=takeCommand()
        sites=[["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query.lower():
            say("Opening music sir...")
            musicPath = "C:\\Users\\karan\\OneDrive\\Desktop\\Web Development\\Jarvis\\This_year.m4a"
            webbrowser.open(musicPath)

        if "the time" in query.lower():
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strfTime}")

        if "open blender" in query.lower():
            subprocess.Popen(r'"C:\Program Files\Blender Foundation\Blender 4.0\blender-launcher.exe"')
