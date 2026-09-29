@echo off
REM ============================================================
REM NEMESIS-CRAB-V2 - Windows Batch Installer
REM ============================================================
setlocal EnableDelayedExpansion

set APP_NAME=NEMESIS-CRAB-V2
set INSTALL_DIR=%USERPROFILE%\.nemesis-crab-v2
set VENV_DIR=%INSTALL_DIR%\venv
set SRC_DIR=%~dp0

echo.
echo ============================================================
echo    NEMESIS-CRAB-V2 - Windows Installer
echo ============================================================
echo.

REM --- Check Python ---
python --version >nul 2>&1
if errorlevel 1 (
    echo [x] Python is not installed or not on PATH.
    echo     Download from https://www.python.org/downloads/
    echo     Make sure to check "Add Python to PATH".
    pause
    exit /b 1
)
for /f "tokens=2" %%v in ('python --version 2^>^&1') do set PYVER=%%v
echo [+] Python %PYVER% detected

REM --- Create install dir ---
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
echo [+] Install dir: %INSTALL_DIR%

REM --- Create venv ---
if not exist "%VENV_DIR%" (
    echo [+] Creating virtual environment...
    python -m venv "%VENV_DIR%"
)
call "%VENV_DIR%\Scripts\activate.bat"

REM --- Upgrade pip ---
echo [+] Upgrading pip...
python -m pip install --upgrade pip setuptools wheel

REM --- Install deps ---
if exist "%SRC_DIR%requirements.txt" (
    echo [+] Installing requirements.txt...
    pip install -r "%SRC_DIR%requirements.txt"
) else (
    echo [!] requirements.txt not found - installing default set
    pip install requests psutil colorama cryptography paramiko ^
                scapy python-whois dnspython PyYAML pyperclip ^
                reportlab matplotlib seaborn numpy pandas ^
                pyinstaller tqdm tabulate
)

REM --- Copy sources ---
echo [+] Copying sources...
copy /Y "%SRC_DIR%nemesis_crab_v2.py" "%INSTALL_DIR%\" >nul 2>&1
if exist "%SRC_DIR%requirements.txt"      copy /Y "%SRC_DIR%requirements.txt"      "%INSTALL_DIR%\" >nul
if exist "%SRC_DIR%requirements-check.py" copy /Y "%SRC_DIR%requirements-check.py" "%INSTALL_DIR%\" >nul
if exist "%SRC_DIR%test-command.py"       copy /Y "%SRC_DIR%test-command.py"       "%INSTALL_DIR%\" >nul
if exist "%SRC_DIR%health.py"             copy /Y "%SRC_DIR%health.py"             "%INSTALL_DIR%\" >nul
if not exist "%INSTALL_DIR%\.nemesis_crab_v2" mkdir "%INSTALL_DIR%\.nemesis_crab_v2"

REM --- Launcher .bat ---
echo [+] Creating launcher...
(
    echo @echo off
    echo call "%VENV_DIR%\Scripts\activate.bat"
    echo cd /d "%INSTALL_DIR%"
    echo python "%INSTALL_DIR%\nemesis_crab_v2.py" %%*
) > "%INSTALL_DIR%\nemesis-crab.bat"

REM Add install dir to user PATH if not already present
echo %PATH% | find /I "%INSTALL_DIR%" >nul
if errorlevel 1 (
    setx PATH "%PATH%;%INSTALL_DIR%" >nul
    echo [+] Added %INSTALL_DIR% to user PATH
)

REM --- Verify ---
echo.
echo [+] Verifying installation...
python "%INSTALL_DIR%\requirements-check.py"

echo.
echo ============================================================
echo    Installation Complete!
echo ============================================================
echo    Install dir : %INSTALL_DIR%
echo    Launcher    : %INSTALL_DIR%\nemesis-crab.bat
echo    Run         : nemesis-crab.bat
echo    Web         : http://localhost:5000
echo.
echo    NOTE: Restart your terminal for PATH changes.
echo.
pause
endlocal
