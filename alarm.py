import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()


deletetime = open("Alarmtext.txt","r+")
deletetime.truncate()
deletetime.close()
def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvios","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ","")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%H:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing , sir")
            os.startfile("music.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)            
           