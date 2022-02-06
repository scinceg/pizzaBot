@echo off

call %~dp0TGB\venv\Scripts\activate

cd %~dp0TGB

set TOKEN=5085544544:AAGdJKnGrYGAmEA95hEETeEKHJZ-zVC5-TI

python bot.py

pause 