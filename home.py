import time
from pyfirmata import Arduino, SERVO, util
import pyttsx3
import speech_recognition as sr

# Initialize the servo motor control function
def control_servo(command):
    pin = 10
    board = Arduino('COM9')
    board.digital[pin].mode = SERVO

    def rotate(pin, angle):
        board.digital[pin].write(angle)
        time.sleep(0.05)

    if command == 'switch on':
        print("switch is on")
        for i in range(0, 45):
            rotate(pin, i)

    elif command == 'switch off':
        print("switch is off")
        for i in range(45, -1, -1):
            rotate(pin, i)

    board.exit()

# Initialize the voice assistance
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello! I'm your voice assistant. How can I help you today?")

with sr.Microphone() as source:
    r.energy_threshold = 500
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

    if "switch on" in text:
        control_servo('switch on')
        speak("Sure, I have switched on the device for you.")

    elif "switch off" in text:
        control_servo('switch off')
        speak("Sure, I have switched off the device for you.")

    else:
        speak("I'm sorry, I didn't understand your request. Could you please repeat it?")
