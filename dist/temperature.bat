@echo off
Title Mostrando a temperatura da CPU
:start
for /f "skip=1 delims=" %%a in ('"wmic path Win32_PerfRawData_Counters_ThermalZoneInformation get temperature"') do set /a Temperatura_Kelvin=%%a& goto Calculos

:Calculos
set /a Temperatura_Celcius=(%Temperatura_Kelvin%*100)-27315
set /a inteiros=%Temperatura_Celcius:~0,-2%
set /a quebrados=%Temperatura_Celcius:~-2%
set Temperatura_Celcius=%inteiros%,%quebrados%
set /a Temperatura_Fahrenheit=(%Temperatura_Kelvin% * 100 - 27315) * 9 
set /a Sobra_Fahrenheit=%Temperatura_Fahrenheit% %% 5
set /a Temperatura_Fahrenheit=%Temperatura_Fahrenheit% / 5
set /a inteiros=%Temperatura_Fahrenheit:~0,-2% + 32
set /a quebrados=%Temperatura_Fahrenheit:~-2% + %Sobra_Fahrenheit%
set Temperatura_Fahrenheit=%inteiros%,%quebrados%
cls
echo.
echo.
echo   Temperatura da CPU: %Temperatura_Celcius%ø Celcius ^| %Temperatura_Kelvin% Kelvin ^| %Temperatura_Fahrenheit%ø Fahrenheit
echo.
timeout /t 1 > Nul
goto :start