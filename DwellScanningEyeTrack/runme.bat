@setlocal enableextensions
@cd /d "%~dp0"

if exist "C:\Program Files\PsychoPy3/python.exe" (
  echo Psychopy: Admin location installed
  C:\Program Files\PsychoPy3/python.exe main.py
  echo C:\Program Files\PsychoPy3/python.exe>.tmp\pythonpath
) else (
      if exist "%UserProfile%/AppData/Local/PsychoPy3/python.exe" (
      echo Psychopy: User location installed
      %UserProfile%/AppData/Local/PsychoPy3/python.exe main.py
      echo %UserProfile%/AppData/Local/PsychoPy3/python.exe>.tmp\pythonpath
    ) else (
      echo There is no installed Psychopy3. Please revise runUser.bat if you installed Psychopy3 in user-specific folder.
    )
)