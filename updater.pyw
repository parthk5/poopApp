import requests
#from git import Repo
import os
import shutil
import sys
from elevate import elevate
import stat
import subprocess
from time import sleep

elevate()

os.system("taskkill /IM powershell.exe /F")

HOME_PATH = os.getcwd()

USER_TEMP = os.environ['USERPROFILE'] + "/AppData/Local/"
os.chdir(USER_TEMP)

if os.path.exists("poopAppUpdate") == False:
    os.mkdir("poopAppUpdate")
else:
    shutil.rmtree('poopAppUpdate')
    os.mkdir('poopAppUpdate')

TEMP_UPDATE = os.environ['USERPROFILE'] + "/AppData/Local/poopAppUpdate/"

os.chdir(TEMP_UPDATE)

BASE = "https://github.com/parthk5/insultApp"

LATEST_RELEASE = "https://github.com/parthk5/poopApp/releases/latest"
EX_DOWNLOAD = "https://github.com/parthk5/poopApp/archive/refs/tags/v1.0.1.zip"


sleep(10)
r = requests.get(LATEST_RELEASE)
if r.status_code != 200:
    sys.exit(0) 
resp = r.url

latestReleaseV = resp[-6:]
latestReleaseNumber = resp[-5:].replace(".", "")

os.chdir(HOME_PATH)
openVersionFile = open("version.txt", 'r')

currentReleaseV = openVersionFile.readlines()[0]
currentReleaseNumber = currentReleaseV.replace('v', '').replace('.', '')
print(f"Current Release Number: {currentReleaseNumber}")
print(f"Latest Release Number Found: {latestReleaseNumber}")

openVersionFile.close()

if latestReleaseNumber > currentReleaseNumber:
    os.chdir(TEMP_UPDATE)
    
    GET_RELEASE_URL = f"https://github.com/parthk5/poopApp/archive/refs/tags/{latestReleaseV}.zip"
    GET_RELEASE_CMD = f"C:/Windows/System32/powershell.exe $ProgressPreference = 'SilentlyContinue' ; curl {GET_RELEASE_URL} -O latestrelease.zip"
    GET_RELEASE_ALT_CMD = f"C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe $ProgressPreference = 'SilentlyContinue' ; curl {GET_RELEASE_URL} -O latestrelease.zip"

    #NEW_RELEASE_CMD = f"certutil.exe -urlcache -split -f {GET_RELEASE_URL} latestrelease.zip"
    
    #print(f"POWERSHELL COMMAND: {GET_RELEASE_CMD}")
    #print(f"POWERSHELL ALT COMMAND: {GET_RELEASE_ALT_CMD}\n")

    subprocess.call(GET_RELEASE_CMD, shell=True)
    subprocess.call(GET_RELEASE_ALT_CMD, shell=True)
    #subprocess.call(NEW_RELEASE_CMD, shell=True)

    INSTALL_LOCATION = os.getcwd()

    print(f"UPDATE INSTALLED AT {INSTALL_LOCATION}")
    
    shutil.unpack_archive('latestrelease.zip', 'latestrelease')

    UNZIPPED_LOCATION = os.getcwd()
    print(f"UNZIPPED AT {UNZIPPED_LOCATION}")
    
    os.remove('latestrelease.zip')
    os.chdir('latestrelease')
    os.chdir(os.listdir()[0])
    loc = os.getcwd()

    CURRENT_PACKAGE_LOCATION = os.getcwd()
    BUILD_LOCATION = CURRENT_PACKAGE_LOCATION + "/poopApp"
    
    shutil.copytree(CURRENT_PACKAGE_LOCATION, BUILD_LOCATION)

    

    print(f'COPIED UPDATE FROM {CURRENT_PACKAGE_LOCATION} TO {BUILD_LOCATION}')
    
    os.chdir('poopApp')

    BUILT_LOCATION = os.getcwd()
    
    print(f"LAUNCHING update.pyw from {CURRENT_PACKAGE_LOCATION}")
    if os.path.exists('update.pyw'):
        os.chdir(CURRENT_PACKAGE_LOCATION)
        os.system('start FinishUpdate.bat')
        print("UPDATE COMPLETE")
        os.system("taskkill /IM python.exe /F")
        os.system("taskkill /IM pythonw.exe /F")
        sys.exit(0)
    else:
        print("update.pyw FILE NOT FOUND")
        print("QUITTING!")
        sys.exit(0)
else:
    print("YOU HAVE THE LATEST VERSION ")
    os.chdir(HOME_PATH)
    os.system("start run.bat")
sys.exit(0)
    




























'''
temp = os.environ['USERPROFILE'] + "/AppData/Local/Temp" + "/AppData/Local/Temp"
os.chdir(temp)

tempUpdate = os.environ['USERPROFILE'] + "/AppData/Local/Temp/insultAppUpdate/"

source_dir = os.getcwd()
target_dir = "C:/Windows/System32/poopApp"
target_dir2 = "C:/Users/Administrator/Desktop/"


base = "https://github.com/parthk5/insultApp"
test = "https://github.com/scotch-io/scotch-box"

latest = requests.get("https://github.com/parthk5/insultApp/releases/latest")

os.chdir(sys.path[0])
versionFile = open("version.txt", 'r')

currentVersion = (versionFile.readline()[-5:].replace(".",""))

print(f"Current Version Detected: {currentVersion}")

latestNumber = (latest.url[-5:].replace(".",""))

print(f"Latest Version Found: {latestNumber}")

toBeUpdatedVersionTag = ['v']
for i in str(latestNumber):
    toBeUpdatedVersionTag.append(i)
    toBeUpdatedVersionTag.append(".")
toBeUpdatedVersionTag.pop(-1)
print("To Be Updated Version Tag: " + str(toBeUpdatedVersionTag))


strLatest = str(latest.url)

print(strLatest)

nextRelease = str(latest.url).replace(strLatest[-3], str(int(strLatest[-3])+1))

print(nextRelease)


nextRelease = latest.url

print(nextRelease)

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

#if 1==1:
if currentVersion  != latestNumber:
    if requests.get(nextRelease).status_code == 200:
        validNextRelease = True
        print("Updating...")
        os.chdir(temp)
        if os.path.exists("insultAppUpdate") == True:
            shutil.rmtree("insultAppUpdate", onerror=remove_readonly)
        os.mkdir("insultAppUpdate")
        Repo.clone_from(base, "insultAppUpdate")
        os.chdir("C:/Windows/System32/")
        if os.path.exists("poopApp") == True:
                shutil.rmtree("poopApp", onerror=remove_readonly)
        os.mkdir("poopApp")
        contents = os.listdir(tempUpdate)
        for content in contents:
            shutil.move(os.path.join(tempUpdate, content), "poopApp")
        os.chdir(temp)
        shutil.rmtree("insultAppUpdate", onerror=remove_readonly)
        os.chdir(sys.path[0])
        versionFile = open("version.txt", 'w')
        for i in toBeUpdatedVersionTag:
            versionFile.write(i)
        print("Update Complete")
    else:
        print("No update found")

'''
