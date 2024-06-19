import os
import pyttsx3
import speech_recognition
import requests
import datetime 
import pyautogui
import time
import pygame



from bs4 import BeautifulSoup
from intro import play_gif
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("understanding..")
        query =  r.recognize_google(audio,language='en-in')
        print(f"you said: {query}\n")
    except Exception as e:
        print("say that agin")
        return "None"
    return query
    
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
def youtube_control(action):
    if action.lower() == "play":
        pyautogui.hotkey("space")
        speak("Playing the video")
    elif action.lower() == "pause":
        pyautogui.hotkey("space")
        speak("Pausing the video")
    elif action.lower() == "volume up":
        pyautogui.hotkey("volume up")
        speak("Turning volume up")
    elif action.lower() == "volume down":
        pyautogui.hotkey("volume down ")
        speak("Turning volume down")

    
    
    else:
        speak("Invalid action")
    
    
   



if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if "wake up"in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takecommand().lower()
                if "go to sleep" in query:
                    speak("ok sir , you can call anytime ")
                    break

                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("i am fine, because i am your lovable assistant" )
                elif "who is your owner" in query:
                    speak("its you, the master bhuvanesh")
                elif "thank you" in query:
                    speak("your welcome, sir")
            

                 
               
                elif "open" in query:
                    from dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from dictapp import closeappweb
                    closeappweb(query) 

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "play" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchwikipedia
                    searchwikipedia(query)
                
                
               

                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeaWE").text
                    speak(f"current{search} is {temp}")
                elif"set an alarm" in query:
                    print("input time example:-10 and 10 and 10 ")
                    a = input("please tell the time:-")
                    alarm(a)
                    speak("done,sir")
                    
                elif "start" in query:
                   youtube_control("play")
                elif "pause" in query:
                   youtube_control("pause")
                elif "volume up" in query:
                   youtube_control("volume up")
                elif "volume down" in query:
                    youtube_control("volume down")
                elif "send message" in query or "phone call" in query or "video call" in query:
                  from feature import findContact, whatsApp
       

                
                elif " what is the time" in query:
                    strtime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir, the time is {strtime}")
                elif "finally sleep" in query:
                    speak("Going to sleep , bhuvanesh")
                    exit()






                




        



