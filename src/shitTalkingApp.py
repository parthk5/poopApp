import tkinter as tk
from tkinter import messagebox
import pygame
import os
from time import sleep
#from ctypes import windll


#h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)
#windll.user32.ShowWindow(h, 0)

#show windll.user32.ShowWindow(h, 9)
'''
root = tk.Tk()
def on_closing():
    if messagebox.askokcancel("Quit", "Can't do that buddy"):
        root = tk.Tk()

root.lift()
root.attributes('-topmost',True)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

'''
os.chdir("C:/Users/Administrator/Desktop/shitTalkingApp/Resources/dist/win64")
os.startfile("importEscapeOFF.bat")

os.chdir("C:/Users/Administrator/Desktop/shitTalkingApp/Resources/dist/media/")
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("C:/Users/Administrator/Desktop/shitTalkingApp/Resources/dist/media/SOUND.mp3")
pygame.mixer.music.play(loops=0)
while pygame.mixer.music.get_busy():
    sleep(1)
print("done")