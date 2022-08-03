import subprocess


def uninstall(name):
	subprocess.call(['pip3', 'uninstall', "-y", name])

modules = ['tkinter', 'pygame', 'ctypes', 'shutil', 'Pillow', 'pywin32', 'pygetwindow', 'elevate', 'GitPython', 'requests', 'keyboard', '']

for module in modules:
    uninstall(module)
