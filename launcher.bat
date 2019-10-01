mode 50,16
@echo off
set vn=1.72
title Bubbly Boi Bot v%vn% - Loading
color 0C
SetLocal EnableDelayedExpansion
SetLocal enableextensions
chcp 437>nul

title Bubbly Boi Bot v%vn% - Loading powershell
for /f "tokens=3,4 delims=, " %%A in (
  'powershell -command "&{$H=get-host;$H.ui.rawui;}"^|findstr /b WindowSize'
) do (
    set /a windowWidth=%%A, windowHeight=%%B
)

title Bubbly Boi Bot v%vn% - Loading Config

<nul set /p "=[#] Loading Config "
if not exist "exec\config.ini" (
    echo ^(ERROR^)
    echo    [#] Config file is missing creating it.
    exec\nircmdc wait 1000
    call:configdefault
    call:configsave
    call:configrestart
) else (echo ^(OK^))
for /f "tokens=* eol=[" %%a in (exec\config.ini) do (set %%a)
if not %cver%==%vn% (
    echo    [#] Config file version is outdated, updating it.
    exec\nircmdc wait 1000
    call:configrestart
)
<nul set /p "=[#] Checking Config Variables "
set configcheck=cver hidden delay times
set "a="
for %%a in (%configcheck%) do (
    if not defined %%a (
        if not defined a (echo ^(ERROR^))
        echo    [-] Variable "%%a" is missing.
        set a=1
        set error=1
    )
)
if defined error (
    exec\nircmdc wait 1000
    call:configdefault
    call:configsave
    call:configrestart
)
call:configcheck

title Bubbly Boi Bot v%vn% - Loading Keys
for /f "tokens=* eol=[" %%a in (exec\keys.ini) do (set %%a)

title Bubbly Boi Bot v%vn% - Loading Menu
if "%1"=="auto" (
    call:start
)
set cursor=1
set items=7
call:cursorchange
goto:INI

:keyexit
    echo.
    echo  [-] Press any key to exit.
    pause>nul
exit 0

:cursorchange
    if /I "%1"=="enter" (
        if "%cursor%"=="1" (if /I %hidden%==true (set hidden=false) else (set hidden=true))
        if "%cursor%"=="2" (set /p delay=¯ Delay in miliseconds: )
        if "%cursor%"=="3" (set /p times=¯ Start times: )
        if "%cursor%"=="4" (call:configsave & call:start)
        if "%cursor%"=="5" (call:about)
        if "%cursor%"=="6" (call:configdefault)
        if "%cursor%"=="7" (set exit=1)
    )

    if /I "%1"=="slide" (
        if "%cursor%"=="1" (if /I %hidden%==true (set hidden=false) else (set hidden=true))
        if "%cursor%"=="2" (
            if %delay% GTR 250 (
                if /I "%2"=="left" (set /a delay-=250)
            )
            if /I "%2"=="right" (set /a delay+=250)
        )
        if "%cursor%"=="3" (
            if %times% GTR 1 (
                if /I "%2"=="left" (set /a times-=1)
            )
            if /I "%2"=="right" (set /a times+=1)
        )
    )
    if /I "%1"=="down" (if %cursor% LSS %items% (set /a cursor+=1))
    if /I "%1"=="up" (if %cursor% GTR 1 (set /a cursor-=1))
    for /l %%a in (1,1,%items%) do (
        set cursor[%%a]=  
        set "cursor0[%%a]="
    )
    set cursor[%cursor%]=¯
    set cursor0[%cursor%]=®
exit /b 0

:INI
title Bubbly Boi Bot v%vn% - Menu
cls & echo.
echo  ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»
echo  º                               Bubbly Boi Bot º
echo  Ì OptionsÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹
echo  º
echo  º   %cursor[1]% Hidden: %hidden%
echo  º   %cursor[2]% Delay: %delay%
echo  º   %cursor[3]% Start times: %times%
echo  º
echo  º   %cursor[4]% Start
echo  º   %cursor[5]% About
echo  º   %cursor[6]% Defaults
echo  º   %cursor[7]% Exit
echo  º
echo  ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼
exec\getkey

if "%errorlevel%"=="%keyLeft%" (call:cursorchange slide left)
if "%errorlevel%"=="%keyDown%" (call:cursorchange down)
if "%errorlevel%"=="%keyRight%" (call:cursorchange slide right)
if "%errorlevel%"=="%keyUp%" (call:cursorchange up)

if "%errorlevel%"=="%keyA%" (call:cursorchange slide left)
if "%errorlevel%"=="%keyS%" (call:cursorchange down)
if "%errorlevel%"=="%keyD%" (call:cursorchange slide right)
if "%errorlevel%"=="%keyW%" (call:cursorchange up)

if "%errorlevel%"=="%keyEnter%" (call:cursorchange enter)
if defined exit (call:exit)
goto:INI

:about
    mode 50,14 & echo.
    call exec\centertext %windowWidth% BubblyBoiBot v%vn%
    call exec\centertext %windowWidth% Original bot programmed by alekxeyuk
    echo.
    call exec\centertext %windowWidth% Spam Integrated Bot programmed
    call exec\centertext %windowWidth% by Catterall#6723
    call exec\centertext %windowWidth% Batch support programmed
    call exec\centertext %windowWidth% by ^^! [( TheGamerX )]#7912
    echo.
    call exec\centertext %windowWidth% Press any [KEY] to continue
    pause>nul
    mode 50,16
exit /b 0

:exit
    call:configcheck
    call:configsave
exit 0

:configcheck
    if /I NOT "%hidden%"=="true" (
        if /I NOT "%hidden%"=="false" (
            set hidden=false
        )
    )
    if "%delay%"=="" (
        set delay=250
    )
    if "%times%"=="" (
        set times=3
    )
exit /b 0

:configsave
    call:configcheck
    echo cver=%vn% >"exec\config.ini"
    echo hidden=%hidden% >>"exec\config.ini"
    echo delay=%delay% >>"exec\config.ini"
    echo times=%times% >>"exec\config.ini"
exit /b 0

:configdefault
    set hidden=false
    set delay=250
    set times=3
exit /b 0

:configrestart
    call:configsave
    start launcher.bat
exit 0

:start
    mode 50,35 & echo.
    if %hidden%==true (
        echo  [#] Running in hidden mode
    ) else (
        echo  [#] Running in minimized mode
    )
    echo.
    echo     [#] Starting port 5001
    for /l %%x in (1,1,%times%) do (
        <nul set /p "=.       [#] Running port 5001 time %%x "
        if %hidden%==true (
            exec\Quiet loop5001 >nul 2>&1
        ) else (
            start "Port 5001" /MIN exec\loop5001
        )
        echo ^(OK^)
        exec\nircmdc wait %delay%
    )

    echo.
    echo     [#] Starting port 5002
    for /l %%x in (1,1,%times%) do (
        <nul set /p "=.       [#] Running port 5002 time %%x "
        if %hidden%==true (
            exec\Quiet loop5002 >nul 2>&1
        ) else (
            start "Port 5002" /MIN exec\loop5002
        )
        echo ^(OK^)
        exec\nircmdc wait %delay%
    )

    echo.
    echo     [#] Starting port 5003
    for /l %%x in (1,1,%times%) do (
        <nul set /p "=.       [#] Running port 5003 time %%x "
        if %hidden%==true (
            exec\Quiet loop5003 >nul 2>&1
        ) else (
            start "Port 5003" /MIN exec\loop5003
        )
        echo ^(OK^)
        exec\nircmdc wait %delay%
    )
    set "done="
    call:startend
    mode 50,16
exit /b 0


:startend
    echo.
    echo.
    call exec\centertext %windowWidth% Press [1] to close this window.
    call exec\centertext %windowWidth% Press [9] to close nodes.
    echo.
:startend0
    exec\getkey
    
    if "%errorlevel%"=="49" (exit 0)
    if "%errorlevel%"=="57" (
        echo     [*] Killing Nodes
        TASKKILL /F /FI "WINDOWTITLE eq Bubbly Boi Bot - Port*" /IM "cmd.exe"
        TASKKILL /F /FI "WINDOWTITLE eq Bubbly Boi Bot - Port*" /IM "python.exe"
        set done=1
    )

    if not defined done (call:startend0)
exit /b 0
