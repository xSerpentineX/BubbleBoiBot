@echo off
title BubbleBoiBot - Port 5001
for %%I in (.) do set CurrDirName=%%~nxI
if "%CurrDirName%"=="exec" (
	cd..
)
:loop
BubbleBoiBot.py 5001
echo.
echo ----------------------------
echo.
goto loop
