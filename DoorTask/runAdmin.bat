@echo off

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

@setlocal enableextensions
@cd /d "%~dp0"
"C:\Program Files\PsychoPy3\python.exe" main.py