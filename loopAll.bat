@mode 70,40
@echo off
title Bubbly Boi Bot v1.62 - Starter

echo.

echo				 BubblyBoiBot v1.62
echo                 Original bot programmed by alekxeyuk
echo     Spam Integrated Bot programmed by TheLoveableBubblyNoodle#6853
echo         Batch support programmed by ! [( TheGamerX )]#7912

echo.
echo.
echo  [*] Loading Config File
for /F "usebackq tokens=*" %%a in ("exec\loopAll.config") do (
	set %%a
)

echo.
if "%hidden%"=="true" (
	echo  [*] Running in hidden mode
) else (
	echo  [*] Running in minimized mode
)

TIMEOUT /T 2 /NOBREAK >nul

echo.
echo  [/] Starting port 5001
for /l %%x in (1, 1, %startTimes%) do (
	echo     [*] Running port 5001 time %%x
	if "%devSkip%"=="false" (
		if "%hidden%"=="true" (
			exec\Quiet loop5001 >nul 2>&1
		) else (
			start "Port 5001" /MIN exec\loop5001
		)
	)
	TIMEOUT /T %delay% /NOBREAK >nul
)

echo.
echo  [/] Starting port 5002
for /l %%x in (1, 1, %startTimes%) do (
	echo     [*] Running port 5002 time %%x
	if "%devSkip%"=="false" (
		if "%hidden%"=="true" (
			exec\Quiet loop5001 >nul 2>&1
		) else (
			start "Port 5002" /MIN exec\loop5002
		)
	)
	TIMEOUT /T %delay% /NOBREAK >nul
)

echo.
echo  [/] Starting port 5003
for /l %%x in (1, 1, %startTimes%) do (
	echo     [*] Running port 5003 time %%x
	if "%devSkip%"=="false" (
		if "%hidden%"=="true" (
			exec\Quiet loop5001 >nul 2>&1
		) else (
			start "Port 5003" /MIN exec\loop5003
		)
	)
	TIMEOUT /T %delay% /NOBREAK >nul
)

echo.
echo.
echo                   Press [1] to close this window
echo                Press [9] to exit the other instances
echo.
exec\choice /C:19 /N

if %errorlevel%==1 (
	echo     [*] Closing this window
)

if %errorlevel%==2 (
	echo  [*] Killing Nodes
	TASKKILL /F /FI "WINDOWTITLE eq Bubbly Boi Bot - Port*" /IM "cmd.exe"
	TASKKILL /F /FI "WINDOWTITLE eq Bubbly Boi Bot - Port*" /IM "python.exe"
)

TIMEOUT /T 3 /NOBREAK >nul
