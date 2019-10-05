@echo off
title BubbleBoiBot - Port 5003
for %%I in (.) do set CurrDirName=%%~nxI
if "%CurrDirName%"=="exec" (
	cd..
)
:loop
BubbleBoiBot.py 5003
echo.
echo ----------------------------
echo.
goto loop
