import shutil
import os
import sys
from elevate import elevate

elevate()

os.chdir(sys.path[0])

def goUp():
    parent_dir = os.path.split(os.getcwd())[0]
    os.chdir(parent_dir)
goUp()

APP_HOME = os.getcwd()
goUp()

print("Current Path: " + str(os.getcwd()))

if os.path.exists("C:/Windows/System32/poopApp"):
    shutil.rmtree('C:/Windows/System32/poopApp')
    print("Existing poopApp Uninstalled")

shutil.copytree('poopApp', 'C:/Windows/System32/poopApp')
print("Installed poopApp")


'''
os.chdir("C:/Windows/System32/")
os.mkdir("poopApp")
os.chdir("poopApp")
os.mkdir("rsc")
os.mkdir("final")

os.chdir(sys.path[0])

def goUp():
    parent_dir = os.path.split(os.getcwd())[0]
    os.chdir(parent_dir)

goUp()

os.chdir("rsc/dist/win64/")

shutil.copy("importEscapeOFF.bat", "C:/Windows/System32/poopApp/rsc/importEscapeOFF.bat")
shutil.copy("importEscapeOFF.bat", "C:/Windows/System32/poopApp/rsc/importEscapeON.bat")
shutil.copy("disableEscape.reg", "C:/Windows/System32//poopApp/rsc/disableEscape.reg")
shutil.copy("disableEscape.reg", "C:/Windows/System32//poopApp/rsc/enableEscape.reg")
shutil.copy("setChanges.bat", "C:/Windows/System32/poopApp/rsc/setChanges.bat")
shutil.copy("keepInFocus.pyw", "C:/Windows/System32/poopApp/final/keepInFocus.pyw")
shutil.copy("disableAltF4.exe", "C:/Windows/System32/poopApp/rsc/disableAltF4.exe")
shutil.copy("RUN.bat", "C:/Windows/System32/poopApp/final/RUN.bat")
shutil.copy("listenToExit.exe", "C:/Windows/System32/poopApp/rsc/listenToExit.exe")

os.chdir(sys.path[0])
goUp()
shutil.copy("App.pyw", "C:/Windows/System32/poopApp/final/App.pyw")

os.chdir("install")
shutil.copy("setup.pyw", "C:/Windows/System32/poopApp/final/setup.pyw")
shutil.copy("tasks.bat", "C:/Windows/System32/poopApp/rsc/tasks.bat")

os.chdir(sys.path[0])
goUp()
os.chdir("rsc/dist/media/")
shutil.copy("bkg.bmp", "C:/Windows/System32/poopApp/rsc/bkg.bmp")
shutil.copy("mem.png", "C:/Windows/System32/poopApp/rsc/mem.png")
shutil.copy("SOUND.mp3", "C:/Windows/System32/poopApp/rsc/SOUND.mp3")
shutil.copy("SoundPlayer.bat", "C:/Windows/System32/poopApp/rsc/SoundPlayer.bat")

goUp()
os.chdir('win64')
os.startfile("importEscapeOFF.bat")

'''