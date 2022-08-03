import os
import shutil
import stat

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

CURRENT_PACKAGED_DIR = os.getcwd() + "//poopApp"
SYSTEM32_LOCATION = "C:/Windows/System32/poopApp"

if os.path.exists(SYSTEM32_LOCATION):
    shutil.rmtree(SYSTEM32_LOCATION, onerror=remove_readonly)

shutil.copytree(CURRENT_PACKAGED_DIR, SYSTEM32_LOCATION)
print("UPDATE COMPLETE")
