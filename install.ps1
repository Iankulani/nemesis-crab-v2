<#
.SYNOPSIS
    NEMESIS-CRAB-V2 - PowerShell Installer (Windows)
.DESCRIPTION
    Installs Python dependencies, sets up a venv, and creates a launcher.
.PARAMETER InstallDir
    Target installation directory (default: $HOME\.nemesis-crab-v2)
.PARAMETER NoVenv
    Skip virtual environment creation (installs into system Python)
.PARAMETER Systemd
    On Linux, create a systemd service (requires sudo)
#>
[CmdletBinding()]
param(
    [string]$InstallDir = "$HOME\.nemesis-crab-v2",
    [switch]$NoVenv,
    [switch]$Systemd
)

$ErrorActionPreference = "Stop"
$AppName     = "NEMESIS-CRAB-V2"
$VenvDir     = Join-Path $InstallDir "venv"
$SrcDir      = Split-Path -Parent $MyInvocation.MyCommand.Path

function Write-Log   { param($m) Write-Host "[+] $m" -ForegroundColor Green }
function Write-Warn  { param($m) Write-Host "[!] $m" -ForegroundColor Yellow }
function Write-Err   { param($m) Write-Host "[x] $m" -ForegroundColor Red }
function Write-Info  { param($m) Write-Host "[i] $m" -ForegroundColor Cyan }

function Show-Banner {
    Write-Host ""
    Write-Host "╔══════════════════════════════════════════════════════════╗" -ForegroundColor Magenta
    Write-Host "║   🦀 NEMESIS-CRAB-V2 - Installer (PowerShell)            ║" -ForegroundColor Magenta
    Write-Host "╚══════════════════════════════════════════════════════════╝" -ForegroundColor Magenta
    Write-Host ""
}

function Test-Python {
    try {
        $v = & python --version 2>&1
        if ($v -match "Python (\d+)\.(\d+)") {
            $major = [int]$Matches[1]; $minor = [int]$Matches[2]
            if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 7)) {
                throw "Python 3.7+ required (found $v)"
            }
            Write-Log "Python $($Matches[1]).$($Matches[2]) detected"
            return $true
        }
    } catch {
        Write-Err "Python not found or too old: $_"
        Write-Err "Download: https://www.python.org/downloads/"
        return $false
    }
    return $false
}

function New-InstallDir {
    if (-not (Test-Path $InstallDir)) {
        New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null
    }
    Write-Log "Install dir: $InstallDir"
}

function New-Venv {
    if ($NoVenv) { Write-Warn "Skipping venv (-NoVenv)"; return }
    if (-not (Test-Path $VenvDir)) {
        Write-Log "Creating virtual environment..."
        & python -m venv $VenvDir
    }
    $activate = Join-Path $VenvDir "Scripts\Activate.ps1"
    if (Test-Path $activate) { . $activate }
    Write-Log "Virtual environment activated"
}

function Install-PythonDeps {
    Write-Log "Upgrading pip / setuptools / wheel..."
    & python -m pip install --upgrade pip setuptools wheel

    $req = Join-Path $SrcDir "requirements.txt"
    if (Test-Path $req) {
        Write-Log "Installing requirements.txt..."
        & pip install -r $req
    } else {
        Write-Warn "requirements.txt not found - installing default set"
        & pip install requests psutil colorama cryptography paramiko `
                     scapy python-whois dnspython PyYAML pyperclip `
                     reportlab matplotlib seaborn numpy pandas `
                     pyinstaller tqdm tabulate
    }
}

function Copy-Sources {
    Write-Log "Copying sources to $InstallDir"
    $files = @("nemesis_crab_v2.py", "requirements.txt",
               "requirements-check.py", "test-command.py", "health.py")
    foreach ($f in $files) {
        $src = Join-Path $SrcDir $f
        if (Test-Path $src) {
            Copy-Item $src -Destination $InstallDir -Force
        }
    }
    $cfg = Join-Path $InstallDir ".nemesis_crab_v2"
    if (-not (Test-Path $cfg)) { New-Item -ItemType Directory -Path $cfg -Force | Out-Null }
}

function New-Launcher {
    Write-Log "Creating launcher script"
    $launcher = Join-Path $InstallDir "nemesis-crab.ps1"
    $pythonExe = if ($NoVenv) { "python" } else { Join-Path $VenvDir "Scripts\python.exe" }
    @"
# NEMESIS-CRAB-V2 launcher
& "$pythonExe" "$InstallDir\nemesis_crab_v2.py" @args
"@ | Set-Content -Path $launcher -Encoding UTF8

    # .bat wrapper for cmd.exe users
    $bat = Join-Path $InstallDir "nemesis-crab.bat"
    @"
@echo off
powershell -ExecutionPolicy Bypass -File "$launcher" %*
"@ | Set-Content -Path $bat -Encoding ASCII

    # Add to user PATH
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($userPath -notlike "*$InstallDir*") {
        [Environment]::SetEnvironmentVariable("Path", "$userPath;$InstallDir", "User")
        Write-Log "Added $InstallDir to user PATH (restart terminal)"
    }
}

function New-DesktopShortcut {
    try {
        $ws  = New-Object -ComObject WScript.Shell
        $lnk = $ws.CreateShortcut("$([Environment]::GetFolderPath('Desktop'))\NEMESIS-CRAB-V2.lnk")
        $lnk.TargetPath       = "powershell.exe"
        $lnk.Arguments        = "-ExecutionPolicy Bypass -File `"$InstallDir\nemesis-crab.ps1`""
        $lnk.WorkingDirectory = $InstallDir
        $lnk.Description      = "NEMESIS-CRAB-V2 Cybersecurity Platform"
        $lnk.Save()
        Write-Log "Desktop shortcut created"
    } catch {
        Write-Warn "Could not create desktop shortcut: $_"
    }
}

function New-SystemdUnit {
    if (-not $Systemd) { return }
    if ($IsWindows) { Write-Warn "-Systemd only applies to Linux"; return }
    $unit = @"
[Unit]
Description=NEMESIS-CRAB-V2 Cybersecurity Platform
After=network.target

[Service]
Type=simple
User=$env:USER
WorkingDirectory=$InstallDir
ExecStart=$VenvDir/bin/python $InstallDir/nemesis_crab_v2.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
"@
    $tmp = "/tmp/nemesis-crab.service"
    $unit | Set-Content -Path $tmp -Encoding UTF8
    sudo mv $tmp /etc/systemd/system/nemesis-crab.service
    sudo systemctl daemon-reload
    Write-Log "systemd unit installed (enable: sudo systemctl enable --now nemesis-crab)"
}

function Invoke-Verify {
    Write-Log "Running dependency check..."
    try {
        & python (Join-Path $InstallDir "requirements-check.py")
    } catch { Write-Warn "Dependency check failed: $_" }

    Write-Log "Running health check..."
    try {
        & python (Join-Path $InstallDir "health.py")
    } catch { Write-Warn "Health check failed: $_" }
}

function Show-Summary {
    Write-Host ""
    Write-Host "══════════════════════════════════════════════════════════" -ForegroundColor Green
    Write-Host "  🎉 Installation Complete!" -ForegroundColor Green
    Write-Host "══════════════════════════════════════════════════════════" -ForegroundColor Green
    Write-Host "  Install dir : $InstallDir" -ForegroundColor Cyan
    Write-Host "  Venv        : $VenvDir" -ForegroundColor Cyan
    Write-Host "  Launcher    : $InstallDir\nemesis-crab.ps1" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  Run:  nemesis-crab" -ForegroundColor White
    Write-Host "  Web:  http://localhost:5000" -ForegroundColor White
    Write-Host "  Help: type 'help' inside the app" -ForegroundColor White
    Write-Host ""
}

# ---------------- Main ----------------
Show-Banner
if (-not (Test-Python)) { exit 1 }
New-InstallDir
New-Venv
Install-PythonDeps
Copy-Sources
New-Launcher
if ($IsWindows -or $PSVersionTable.Platform -eq "Win32NT") {
    New-DesktopShortcut
}
New-SystemdUnit
Invoke-Verify
Show-Summary
