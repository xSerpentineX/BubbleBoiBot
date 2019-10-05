@echo off
title BubbleBoiBot - Port 5002
for %%I in (.) do set CurrDirName=%%~nxI
if "%CurrDirName%"=="exec" (
	cd..
)
:loop
BubbleBoiBot.py 5002
echo.
echo ----------------------------
echo.
goto loop
