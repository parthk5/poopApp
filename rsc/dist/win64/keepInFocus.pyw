import win32gui
import pygetwindow as gw
import os
from time import sleep
import psutil


def main():

    if "listenToExit.exe" not in (p.name() for p in psutil.process_iter()):
        os.startfile("listenToExit.exe")
    
    os.system("taskkill /f /im Taskmgr.exe")
    window = win32gui.GetWindowText (win32gui.GetForegroundWindow())
    print("Window: " + window)
    if window != "L Bozo Ratio + Didn't Ask":
        win = gw.getWindowsWithTitle("L Bozo Ratio + Didn't Ask")
        if len(win) == 0:
            sleep(3)
            main()
        win[0].activate()
        sleep(3)
        main()
    else:
        sleep(3)
        main()
main()
