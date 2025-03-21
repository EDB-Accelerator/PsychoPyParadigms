@echo off
setlocal

set "arg1=%~1"
echo Running the script...

:: Kill Edge if it's already running
taskkill /F /IM msedge.exe /T > nul 2>&1

:: Check if Edge is installed (usually at this path)
set "EDGE_PATH=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
if not exist "%EDGE_PATH%" (
    set "EDGE_PATH=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
)

:: If Edge found, run in kiosk mode
if exist "%EDGE_PATH%" (
    echo Launching Microsoft Edge...
    start "" /wait /min "%EDGE_PATH%" --kiosk "%arg1%\FortuneWheel\index16.html" --edge-kiosk-type=fullscreen --no-first-run
    goto :eof
)

:: If Edge not found, fallback to Internet Explorer (only if exists)
set "IE_PATH=%ProgramFiles%\Internet Explorer\iexplore.exe"
if exist "%IE_PATH%" (
    echo Launching Internet Explorer (fallback)...
    start "" /wait /min "%IE_PATH%" "%arg1%\FortuneWheel\index16.html"
    goto :eof
)

:: Nothing found
echo No supported browser found (Edge or Internet Explorer).
exit /b 1

endlocal
