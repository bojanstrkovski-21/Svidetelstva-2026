@echo off
cd /d "%~dp0"
start "" python app.py
timeout /t 7 /nobreak >nul
start "" "http://localhost:5000"
