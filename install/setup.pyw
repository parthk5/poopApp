import subprocess
import os
import sys
from os import environ,getcwd

START_PATH = getcwd()

installed_ver = sys.version[:4].replace('.', '')

getUser = lambda: environ["USERNAME"] if "C:" in getcwd() else environ["USER"]
user = getUser()

scripts_path = "C:/Users/" + str(user) + "/AppData/Local/Programs/Python/Python" + str(installed_ver) + "/Scripts/"
alt_scripts_path = "C:\Program Files\Python" + str(installed_ver) + "\Scripts"

python_loc = scripts_path = "C:/Users/" + str(user) + "/AppData/Local/Programs/Python/"


try:
        os.chmod(python_loc,0o777)
except:
        os.chmod('C:\Program Files\Python37',0o777)



def old_install(name):
	subprocess.call(['pip3', 'install', name])

# modules = ['tkinter', 'pygame', 'ctypes', 'shutil', 'Pillow', 'pywin32', 'pygetwindow', 'elevate', 'GitPython', 'requests', 'keyboard', 'psutil', '']


def install():
        os.chdir(START_PATH)
        os.system("pip3 install -r requirements.txt")
install()

'''
for module in modules:
    install(module)

'''  

try:
        os.chdir(scripts_path)
        os.system("python pywin32_postinstall.py -install")
except:
        os.chdir(alt_scripts_path)
        os.system("python pywin32_postinstall.py -install")
