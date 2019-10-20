@echo off
title BubbleBoiBot - Port 5003
for %%I in (.) do set CurrDirName=%%~nxI
if "%CurrDirName%"=="exec" (
	cd..
	Call bubble_venv\Scripts\activate.bat
)
:loop
BubbleBoiBot.py 5003
echo.
echo ----------------------------
echo.
goto loop
