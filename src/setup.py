import subprocess
import os


def install(name):
	subprocess.call(['pip3', 'install', name])

modules = ['tkinter', 'pygame', 'ctypes', 'shutil', 'Pillow', 'pywin32', 'pygetwindow']

for module in modules:
    install(module)


os.chdir("%USERPROFILE%/AppData/Local/Programs/Python/Python37/Scripts/")
os.system("python pywin32_postinstall.py")