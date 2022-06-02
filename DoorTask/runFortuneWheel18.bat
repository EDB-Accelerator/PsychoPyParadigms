@echo off
set arg1=%1
echo Running the script...
taskkill /F /IM chrome.exe /T > nul
start /wait /min cmd /C "C:\Program Files\Google\Chrome\Application\chrome.exe" -kiosk -fullscreen --window-size=1024,768 --force-device-scale-factor=1 --app=%arg1%\FortuneWheel\index18.html