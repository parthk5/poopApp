import requests
from git import Repo
import os
import shutil
import sys
from elevate import elevate
import stat

elevate()


os.chdir(os.environ['USERPROFILE'] + "/AppData/Local/Temp")
temp = os.environ['USERPROFILE'] + "/AppData/Local/Temp"
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

print(currentVersion)

latestNumber = (latest.url[-5:].replace(".",""))

print(latestNumber)

toBeUpdatedVersionTag = ['v']
for i in str(latestNumber):
    toBeUpdatedVersionTag.append(i)
    toBeUpdatedVersionTag.append(".")
toBeUpdatedVersionTag.pop(-1)
print("To Be Updated Version Tag: " + str(toBeUpdatedVersionTag))

'''
strLatest = str(latest.url)

print(strLatest)

nextRelease = str(latest.url).replace(strLatest[-3], str(int(strLatest[-3])+1))

print(nextRelease)
'''

nextRelease = latest.url

print(nextRelease)

CONFIRM = input("Proceed(y/n): ")

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

