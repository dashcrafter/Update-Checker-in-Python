@echo off
set "pscmd=cd C:\Users\$env:USERNAME\Downloads; python Update_Checker.py; pause"

:: Start PowerShell as administrator and execute the command
powershell -Command "Start-Process powershell -Verb runAs -ArgumentList '-NoProfile -Command %pscmd%'"
exit
