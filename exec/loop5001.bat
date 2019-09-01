@echo off
title Bubbly Boi Bot - Port 5001
for %%I in (.) do set CurrDirName=%%~nxI
if "%CurrDirName%"=="exec" (
	cd..
)
:loop
BubblyBoiBot.py 5001
echo.
echo ----------------------------
echo.
goto loop
