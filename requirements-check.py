#!/usr/bin/env python3
"""
NEMESIS-CRAB-V2 - Dependency Checker
Verifies all required and optional dependencies are installed.
"""

import sys
import importlib
import subprocess
import shutil
import json
from pathlib import Path

# ANSI colors
class C:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# ---------- Python modules (import name -> pip name) ----------
PYTHON_MODULES = {
    # Core
    "requests":        "requests",
    "urllib3":         "urllib3",
    "psutil":          "psutil",
    "colorama":        "colorama",
    # Crypto
    "cryptography":    "cryptography",
    # SSH
    "paramiko":        "paramiko",
    # Bots
    "discord":         "discord.py",
    "telethon":        "telethon",
    "slack_sdk":       "slack-sdk",
    # Selenium
    "selenium":        "selenium",
    "webdriver_manager":"webdriver-manager",
    # Google
    "httplib2":        "httplib2",
    "google.oauth2":   "google-auth",
    "googleapiclient": "google-api-python-client",
    # Web
    "flask":           "flask",
    "flask_socketio":  "flask-socketio",
    "flask_cors":      "flask-cors",
    # Network
    "scapy":           "scapy",
    "whois":           "python-whois",
    "dns":             "dnspython",
    # Utilities
    "qrcode":          "qrcode[pil]",
    "pyshorteners":    "pyshorteners",
    # Graphics
    "matplotlib":      "matplotlib",
    "seaborn":         "seaborn",
    "numpy":           "numpy",
    "pandas":          "pandas",
    # PDF
    "reportlab":       "reportlab",
    # Keylogger
    "pynput":          "pynput",
    # DOCX
    "docx":            "python-docx",
    # Misc
    "yaml":            "PyYAML",
    "PIL":             "Pillow",
    "pyperclip":       "pyperclip",
    "pyautogui":       "pyautogui",
    "tqdm":            "tqdm",
    "tabulate":        "tabulate",
}

# ---------- System binaries ----------
SYSTEM_TOOLS = {
    "ping":         "iputils-ping",
    "nmap":         "nmap",
    "curl":         "curl",
    "wget":         "wget",
    "nc":           "netcat",
    "dig":          "dnsutils",
    "traceroute":   "traceroute",
    "ssh":          "openssh-client",
    "whois":        "whois",
    "nikto":        "nikto",
    "docker":       "docker.io",
    "pyinstaller":  "pyinstaller",
}

def check_python_modules():
    print(f"\n{C.BOLD}{C.CYAN}═══ Python Modules ═══{C.RESET}\n")
    missing = []
    for module, pip_name in PYTHON_MODULES.items():
        try:
            importlib.import_module(module)
            print(f"  {C.GREEN}✅{C.RESET} {module:<22} ({pip_name})")
        except ImportError:
            print(f"  {C.RED}❌{C.RESET} {module:<22} ({pip_name}) {C.YELLOW}[MISSING]{C.RESET}")
            missing.append(pip_name)
    return missing

def check_system_tools():
    print(f"\n{C.BOLD}{C.CYAN}═══ System Tools ═══{C.RESET}\n")
    missing = []
    for tool, pkg in SYSTEM_TOOLS.items():
        path = shutil.which(tool)
        if path:
            print(f"  {C.GREEN}✅{C.RESET} {tool:<14} -> {path}")
        else:
            print(f"  {C.RED}❌{C.RESET} {tool:<14} {C.YELLOW}[MISSING - install: {pkg}]{C.RESET}")
            missing.append((tool, pkg))
    return missing

def check_python_version():
    print(f"\n{C.BOLD}{C.CYAN}═══ Python Version ═══{C.RESET}\n")
    v = sys.version_info
    print(f"  Python: {C.GREEN}{sys.version.split()[0]}{C.RESET}")
    if v < (3, 7):
        print(f"  {C.RED}❌ Python 3.7+ required{C.RESET}")
        return False
    print(f"  {C.GREEN}✅ Version OK{C.RESET}")
    return True

def check_platform():
    import platform
    print(f"\n{C.BOLD}{C.CYAN}═══ Platform ═══{C.RESET}\n")
    print(f"  OS:      {platform.system()} {platform.release()}")
    print(f"  Machine: {platform.machine()}")
    print(f"  Node:    {platform.node()}")
    return True

def generate_report(py_missing, sys_missing):
    report = {
        "python_version": sys.version,
        "platform": __import__("platform").system(),
        "missing_python_modules": py_missing,
        "missing_system_tools": [t[0] for t in sys_missing],
    }
    out = Path("dependency_report.json")
    out.write_text(json.dumps(report, indent=2))
    print(f"\n{C.CYAN}📄 Report saved: {out.resolve()}{C.RESET}")

def main():
    print(f"{C.MAGENTA}{C.BOLD}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   🦀 NEMESIS-CRAB-V2 - Dependency Checker                ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(C.RESET)

    ok = check_python_version()
    check_platform()
    py_missing = check_python_modules()
    sys_missing = check_system_tools()
    generate_report(py_missing, sys_missing)

    print(f"\n{C.BOLD}{C.CYAN}═══ Summary ═══{C.RESET}\n")
    if py_missing:
        print(f"{C.YELLOW}Install missing Python packages:{C.RESET}")
        print(f"  pip install {' '.join(py_missing)}")
    else:
        print(f"{C.GREEN}✅ All Python modules present.{C.RESET}")

    if sys_missing:
        print(f"\n{C.YELLOW}Missing system tools:{C.RESET}")
        for tool, pkg in sys_missing:
            print(f"  • {tool} (apt install {pkg})")

    if not py_missing and not sys_missing and ok:
        print(f"\n{C.GREEN}{C.BOLD}🎉 All dependencies satisfied!{C.RESET}")
        return 0
    print(f"\n{C.YELLOW}⚠️  Some dependencies are missing.{C.RESET}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
