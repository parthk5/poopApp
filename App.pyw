import tkinter as tk
from tkinter import messagebox
import pygame
import os
from time import sleep
from tkinter import Label
from ctypes import windll
import random
from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
from tkinter import ttk
from os import environ, getcwd
import keyboard
import psutil

ORIGIN_PATH = os.getcwd()

LISTENTOEXIT_PATH = str(ORIGIN_PATH) + '\\rsc\dist\win64\listenToExit.exe'

os.startfile(LISTENTOEXIT_PATH)


insults = ["fucknut", "asswipe", "asshole", "bitch", "stupid", "whore", "piece of shit", "shitter", "shitbag", "bitch", "son of a bitch", "fucker", "motherfucker", "dumbass", "retard", "disabled piece of shit", "ur mentally challenged", 'shitface']

#h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)
#windll.user32.ShowWindow(h, 0)

#show windll.user32.ShowWindow(h, 9)


root = tk.Tk()
root.title("L Bozo Ratio + Didn't Ask")
root.geometry("800x600")
if keyboard.is_pressed('control+shift+space'):
    os.system("TASKKILL /IM wscript.exe /F")
    os._exit(0)
    os.system("TASKKILL /IM python.exe /F")

def on_closing():
    if messagebox.askokcancel("Quit", "Can't do that shitter"):
        root.destroy()
        if "listenToExit.exe" not in (p.name() for p in psutil.process_iter()):
            os.startfile(LISTENTOEXIT_PATH)
        root.__init__()
        root.geometry("800x600")
        root.state("zoomed")
        root.title("L Bozo Ratio + Didn't Ask")
        root.attributes('-topmost',True)
        root.attributes('-fullscreen',True)
        
        insult = random.choice(insults)

        bg = str(ORIGIN_PATH) + "/rsc/dist/media/mem.png"
        img = ImageTk.PhotoImage(Image.open(bg))
        panel = Label(root, image=img)
        panel.photo = img
        panel.grid(column=2,row=2)

        l = Label(root, text = insult)
        l.config(font =("Arial", 40, BOLD))

        l.grid(column=2,row=3)

        root.protocol("WM_DELETE_WINDOW", on_closing)

ieoff = str(ORIGIN_PATH) + "/rsc/dist/win64/importEscapeOFF.bat"
os.startfile(ieoff)

root.lift()
root.attributes('-topmost',True)
root.attributes('-fullscreen',True)
insult = random.choice(insults)
bg = str(ORIGIN_PATH) + "/rsc/dist/media/mem.png"
img = ImageTk.PhotoImage(Image.open(bg))
panel = Label(root, image=img)
panel.photo = img
panel.grid(column=2,row=2)

l = Label(root, text = insult)
l.config(font =("Arial", 40, BOLD))

l.grid(column=2,row=3)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.state("zoomed")
root.mainloop()
