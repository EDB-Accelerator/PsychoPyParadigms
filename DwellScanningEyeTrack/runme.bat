@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:-------------------------------------- 


if exist "%ProgramFiles%/PsychoPy3/python.exe" (
  echo Psychopy: Admin location installed
  "%ProgramFiles%/PsychoPy3/python.exe" main.py
  echo %ProgramFiles%/PsychoPy3/python.exe>.tmp/pythonpath
) else (
      if exist "%UserProfile%/AppData/Local/PsychoPy3/python.exe" (
      echo Psychopy: User location installed
      "%UserProfile%/AppData/Local/PsychoPy3/python.exe" main.py
      echo %UserProfile%/AppData/Local/PsychoPy3/python.exe>.tmp\pythonpath
    ) else (
      echo There is no installed Psychopy3. Please revise runUser.bat if you installed Psychopy3 in user-specific folder.
    )
)