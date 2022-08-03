@echo off

reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d C:/Windows/System32/poopApp/rsc/bkg.bmp /f 
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v WallPaper /t REG_SZ /d C:/Windows/System32/poopApp/rsc/bkg.bmp /f 

reg add "HKCU\Control Panel\Desktop" /v Wallpaper /f /t REG_SZ /d C:/Windows/System32/poopApp/rsc/bkg.bmp
reg add "HKCU\Control Panel\Desktop" /v WallPaper /f /t REG_SZ /d C:/Windows/System32/poopApp/rsc/bkg.bmp

RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters

reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v WallpaperStyle /t REG_SZ /d 2 /f

RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters