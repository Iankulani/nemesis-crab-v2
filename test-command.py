#!/usr/bin/env python3
"""
NEMESIS-CRAB-V2 - Command Test Harness
Runs safe, non-destructive commands against the handler to verify install.
"""

import sys
import time
import json
import traceback

# Import the main app (must be named nemesis_crab_v2.py)
try:
    import nemesis_crab_v2 as ncv2
except ImportError as e:
    print(f"❌ Could not import nemesis_crab_v2: {e}")
    print("   Make sure the main file is named 'nemesis_crab_v2.py' in the same dir.")
    sys.exit(1)

# ANSI
G = "\033[92m"; R = "\033[91m"; Y = "\033[93m"; B = "\033[94m"; RESET = "\033[0m"

# Safe commands to test (read-only / non-invasive)
SAFE_COMMANDS = [
    ("help",                       "Show help"),
    ("status",                     "System status"),
    ("system",                     "System info"),
    ("history 5",                  "Recent history"),
    ("threats 5",                  "Recent threats"),
    ("list_ips",                   "List managed IPs"),
    ("list_domains",               "List hosted domains"),
    ("phish_list",                 "List phishing links"),
    ("traffic_types",              "List traffic types"),
    ("crack_list",                 "List cracking jobs"),
    ("re_list",                    "List reverse-engineering jobs"),
    ("report_list",                "List reports"),
    ("keylogger_status",           "Keylogger status"),
    ("docker_info",                "Docker info (may fail if no docker)"),
    ("location 8.8.8.8",           "Geolocate public IP"),
    ("whois example.com",          "WHOIS lookup"),
    ("dns example.com",            "DNS lookup"),
    ("ping 127.0.0.1 1",           "Local ping (loopback)"),
    ("ip_info 127.0.0.1",          "Local IP info"),
]

def run_test(app, cmd, description):
    print(f"\n{B}▶ Test:{RESET} {cmd}  ({description})")
    try:
        t0 = time.time()
        result = app.handler.execute(cmd, source="test")
        dt = time.time() - t0
        success = result.get("success", False)
        out = result.get("output", "")
        marker = f"{G}✅ PASS{RESET}" if success else f"{Y}⚠️  SOFT-FAIL{RESET}"
        print(f"  {marker}  ({dt:.2f}s)")
        preview = out.replace("\n", " ")[:160]
        print(f"  output: {preview}{'...' if len(out) > 160 else ''}")
        return success
    except Exception as e:
        print(f"  {R}❌ FAIL{RESET} -> {e}")
        traceback.print_exc()
        return False

def main():
    print(f"{B}{'='*60}{RESET}")
    print(f"{B}  🦀 NEMESIS-CRAB-V2 - Command Test Suite{RESET}")
    print(f"{B}{'='*60}{RESET}")

    print("\nInitializing application...")
    try:
        app = ncv2.NemesisCrabV2()
    except Exception as e:
        print(f"{R}❌ Failed to initialize app: {e}{RESET}")
        traceback.print_exc()
        sys.exit(1)
    print(f"{G}✅ App initialized{RESET}")

    passed = 0
    failed = 0
    for cmd, desc in SAFE_COMMANDS:
        if run_test(app, cmd, desc):
            passed += 1
        else:
            failed += 1

    print(f"\n{B}{'='*60}{RESET}")
    print(f"{B}  Results: {G}{passed} passed{RESET}, {R}{failed} failed{RESET}, total {passed+failed}")
    print(f"{B}{'='*60}{RESET}")

    summary = {
        "passed": passed,
        "failed": failed,
        "total": passed + failed,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    with open("test_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    try:
        app.db.close()
    except Exception:
        pass

    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()
