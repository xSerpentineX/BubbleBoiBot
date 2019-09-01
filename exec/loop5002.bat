@echo off
title Bubbly Boi Bot - Port 5002
for %%I in (.) do set CurrDirName=%%~nxI
if "%CurrDirName%"=="exec" (
	cd..
)
:loop
BubblyBoiBot.py 5002
echo.
echo ----------------------------
echo.
goto loop
