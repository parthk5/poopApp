import win32gui
import pygetwindow as gw
import os

while True:
    os.system("taskkill /f /im Taskmgr.exe")
    window = win32gui.GetWindowText (win32gui.GetForegroundWindow())
    if window != "L Bozo Ratio + Didn't Ask":
        win = gw.getWindowsWithTitle("L Bozo Ratio + Didn't Ask")[0] 
        win.activate()
