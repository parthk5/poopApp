import keyboard
import os
import time

while True:
    os.chdir("C:/Windows/System32/poopApp/rsc/dist/win64")
    if os.system("SetVol.exe report") != 100:
        os.system("SetVol.exe 100")
    time.sleep(1)
    if keyboard.is_pressed('control+shift+space'):
        os.startfile('importEscapeON.bat')
        os.system("TASKKILL /IM wscript.exe /F")
        os.system("TASKKILL /IM pythonw.exe /F")
        os.system("TASKKILL /IM disableAltF4.exe /F")
        os.system("TASKKILL /IM python.exe /F")
        os._exit(0)
