@echo off
REM Verificar si se proporcionó un argumento (ruta de la carpeta)
if "%~1"=="" (
    echo Por favor, arrastra y suelta una carpeta sobre este archivo .bat.
    pause
    exit /b
)

REM Ejecutar el script Python pasando la ruta de la carpeta
python "%~dp0+LGA_UTF-pyCleaner.py" "%~1"

pause
