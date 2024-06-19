from tkinter import *
from PIL import Image , ImageTk, ImageSequence
import time 
import pygame
from pygame import mixer
mixer. init()

root = Tk()
root.geometry("1000x500")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("voice.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()
play_gif()
root.mainloop



