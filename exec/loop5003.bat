@echo off
title Bubbly Boi Bot - Port 5003
for %%I in (.) do set CurrDirName=%%~nxI
if "%CurrDirName%"=="exec" (
	cd..
)
:loop
BubblyBoiBot.py 5003
echo.
echo ----------------------------
echo.
goto loop
