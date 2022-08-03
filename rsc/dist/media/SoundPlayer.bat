@echo off
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "SOUND.mp3"
  echo Sound.settings.volume = 100
  echo Sound.settings.setMode "loop", True
  echo Sound.Controls.play
  echo While Sound.playState ^<^> 1
  echo      WScript.Sleep 100
  echo Wend
)>sound.vbs
start /min sound.vbs
exit /b