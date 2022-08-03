@echo off

:: C:\Windows\System32\cmd.exe /k %windir%\System32\reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f

regedit.exe /S rsc/dist/win64/runasadmincmd.REG

taskkill /IM explorer.exe /F & start explorer.exe

CALL rsc/dist/python/py-install.bat

TIMEOUT 1 > NUL

setx /M PATH "%PATH%;C:\Program Files\Python37"
setx /M PATH "%PATH%;C:\Program Files\Python37\Scripts"
setx /M PATH "%PATH%;C:\Program Files\Python37"

setx PATH "%PATH%;C:\Program Files\Python37\Scripts"
setx PATH "%PATH%;C:\Program Files\Python37"

setx path "%PATH%;C:\Program Files\Python37"
set "path=%PATH%;C:\Program Files\Python37"

setx path "%PATH%;C:\Program Files\Python37\Scripts"
set "path=%PATH%;C:\Program Files\Python37\Scripts"


cd ../../../

cd install
pythonw setup.pyw

TIMEOUT 1 > NUL

pythonw setupFiles.pyw


CALL tasks.bat

cd ..

:: CALL run.bat

cmd /k