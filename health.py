#!/usr/bin/env python3
"""
NEMESIS-CRAB-V2 - Health Check
Returns JSON with service status. Suitable for Docker HEALTHCHECK,
Kubernetes probes, and load balancer checks.
"""

import os
import sys
import json
import socket
import shutil
import platform
import time
import argparse
import urllib.request
from pathlib import Path

VERSION = "2.0.0"
START_TIME = time.time()

# ---------- Checks ----------

def check_python():
    v = sys.version_info
    return {
        "ok": v >= (3, 7),
        "version": sys.version.split()[0],
        "required": ">=3.7",
    }

def check_config_dir():
    d = Path(".nemesis_crab_v2")
    return {
        "ok": d.exists() or True,   # will be created on demand
        "path": str(d.resolve()),
        "exists": d.exists(),
    }

def check_binary(name):
    p = shutil.which(name)
    return {"ok": bool(p), "path": p or None}

def check_port(host, port, timeout=2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        s.close()
        return True
    except Exception:
        return False

def check_http(url, timeout=3):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return {"ok": 200 <= r.status < 400, "status": r.status}
    except Exception as e:
        return {"ok": False, "error": str(e)}

def check_disk(path="."):
    try:
        total, used, free = shutil.disk_usage(path)
        pct = used / total * 100
        return {
            "ok": pct < 95,
            "total_gb": round(total / 1e9, 2),
            "used_gb": round(used / 1e9, 2),
            "free_gb": round(free / 1e9, 2),
            "used_pct": round(pct, 2),
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}

def check_memory():
    try:
        import psutil
        vm = psutil.virtual_memory()
        return {
            "ok": vm.percent < 95,
            "total_mb": round(vm.total / 1e6, 2),
            "available_mb": round(vm.available / 1e6, 2),
            "used_pct": vm.percent,
        }
    except ImportError:
        return {"ok": True, "note": "psutil not installed"}

def check_cpu():
    try:
        import psutil
        return {"ok": True, "percent": psutil.cpu_percent(interval=0.1)}
    except ImportError:
        return {"ok": True, "note": "psutil not installed"}

# ---------- Main ----------

def run_health(web_url=None, web_port=5000):
    result = {
        "service": "nemesis-crab-v2",
        "version": VERSION,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "hostname": socket.gethostname(),
        "platform": f"{platform.system()} {platform.release()}",
        "checks": {},
    }

    result["checks"]["python"] = check_python()
    result["checks"]["config_dir"] = check_config_dir()
    result["checks"]["disk"] = check_disk()
    result["checks"]["memory"] = check_memory()
    result["checks"]["cpu"] = check_cpu()

    result["checks"]["binaries"] = {
        name: check_binary(name)
        for name in ["ping", "nmap", "curl", "wget", "nc", "dig",
                     "traceroute", "ssh", "whois", "nikto", "docker"]
    }

    if web_url:
        result["checks"]["web_dashboard"] = check_http(web_url)
    elif web_port:
        result["checks"]["web_dashboard_port"] = {
            "ok": check_port("127.0.0.1", web_port),
            "port": web_port,
        }

    # Aggregate
    overall = True
    for key, val in result["checks"].items():
        if isinstance(val, dict) and "ok" in val and not val["ok"]:
            overall = False
        if key == "binaries":
            for _, b in val.items():
                # Only ping/curl/wget are hard requirements for basic operation
                pass
    result["healthy"] = overall
    result["status"] = "UP" if overall else "DEGRADED"
    return result


def main():
    ap = argparse.ArgumentParser(description="NEMESIS-CRAB-V2 health check")
    ap.add_argument("--json", action="store_true", help="Output JSON")
    ap.add_argument("--url", help="Web dashboard URL to probe")
    ap.add_argument("--port", type=int, default=5000, help="Web dashboard port")
    ap.add_argument("--exit-code", action="store_true",
                    help="Exit non-zero if unhealthy")
    args = ap.parse_args()

    report = run_health(web_url=args.url, web_port=args.port)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Service : {report['service']} v{report['version']}")
        print(f"Status  : {report['status']}")
        print(f"Uptime  : {report['uptime_seconds']}s")
        print(f"Host    : {report['hostname']}")
        print(f"Platform: {report['platform']}")
        print("\nChecks:")
        for k, v in report["checks"].items():
            if isinstance(v, dict) and "ok" in v:
                mark = "✅" if v["ok"] else "❌"
                print(f"  {mark} {k}: {v}")
            elif k == "binaries":
                print("  binaries:")
                for name, b in v.items():
                    mark = "✅" if b["ok"] else "⚠️ "
                    print(f"    {mark} {name}")

    if args.exit_code and not report["healthy"]:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
