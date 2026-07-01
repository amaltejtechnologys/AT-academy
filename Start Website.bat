@echo off
title AT Academy Website
echo Starting AT Academy Website...
echo.

cd /d "%~dp0atacademy"

echo Starting Django server on http://localhost:8000
echo Website: http://localhost:8000
echo Admin Panel: http://localhost:8000/admin/
echo.

start "" "http://localhost:8000"
start "" "http://localhost:8000/admin/"

"C:\Users\User.DESKTOP-53UC8KT\AppData\Local\Python\pythoncore-3.14-64\python.exe" manage.py runserver 0.0.0.0:8000

pause
