@echo off & setlocal enableDelayedExpansion

set /a windowWidth=%1-1
for /f "tokens=1,* delims= " %%a in ("%*") do set text=%%b
if "%text%"=="" (
    exit /b 0
)
for /L %%# in (1,2,!windowWidth!) do (
    if "!text:~%windowWidth%,1!"=="" (
        set "text= !text! "
    )
)
echo !text!