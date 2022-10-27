@echo off
cd %~dp0
set PYTHONDONTWRITEBYTECODE=1
@echo on

python main.py -f %~dp0master\Masters.xlsx -o %~dp0generate\\gen.py