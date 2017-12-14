@echo off
if not defined FOO (
  set FOO=1
  start /min "" %~0
  exit /b
)
pythonw corrector.py
taskkill /F /IM cmd.exe
