#!/usr/bin/env python3
"""Setup script for NEMESIS-CRAB-V2."""

from setuptools import setup, find_packages
from pathlib import Path

HERE = Path(__file__).parent
long_desc = (HERE / "README.md").read_text(encoding="utf-8") if (HERE / "README.md").exists() else ""

setup(
    name="nemesis-crab-v2",
    version="2.0.0",
    author="Ian Carter Kulani",
    description="Ultimate Cybersecurity Command & Control Platform",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/nemesis-crab-v2",
    license="MIT",
    py_modules=["nemesis_crab_v2"],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.31.0",
        "psutil>=5.9.0",
        "colorama>=0.4.6",
        "cryptography>=41.0.0",
        "paramiko>=3.3.0",
        "scapy>=2.5.0",
        "python-whois>=0.9.4",
        "dnspython>=2.4.0",
        "PyYAML>=6.0",
        "pyperclip>=1.8.2",
        "reportlab>=4.0.0",
        "tqdm>=4.66.0",
        "tabulate>=0.9.0",
    ],
    extras_require={
        "bots":    ["discord.py>=2.3.0", "telethon>=1.31.0", "slack-sdk>=3.23.0"],
        "web":     ["flask>=3.0.0", "flask-socketio>=5.3.0", "flask-cors>=4.0.0"],
        "gfx":     ["matplotlib>=3.7.0", "seaborn>=0.13.0", "numpy>=1.24.0", "pandas>=2.0.0"],
        "keylogger": ["pynput>=1.7.6", "pyautogui>=0.9.54"],
        "selenium": ["selenium>=4.15.0", "webdriver-manager>=4.0.1"],
        "full":    [
            "discord.py>=2.3.0", "telethon>=1.31.0", "slack-sdk>=3.23.0",
            "flask>=3.0.0", "flask-socketio>=5.3.0", "flask-cors>=4.0.0",
            "matplotlib>=3.7.0", "seaborn>=0.13.0", "numpy>=1.24.0", "pandas>=2.0.0",
            "pynput>=1.7.6", "pyautogui>=0.9.54",
            "selenium>=4.15.0", "webdriver-manager>=4.0.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "nemesis-crab=nemesis_crab_v2:main",
            "nemesis-health=health:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
    ],
    keywords="cybersecurity pentesting redteam c2 nmap scapy keylogger",
)
