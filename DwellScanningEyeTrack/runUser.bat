@setlocal enableextensions
@cd /d "%~dp0"
"python-dwellscansub/python.exe" src/MusicSelectionGUI.py
"%UserProfile%/AppData/Local/PsychoPy3/python.exe" main.py