#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

print("****************************")
print("      SQLI Injector")
print("****************************")
print("Powered by SQLMap | Use only on systems you have permission to test.")
print()

target = input("SQLI Vulnerable Target URL: ").strip()

if not target:
    print("No target provided. Exiting.")
    sys.exit(1)

sqlmap_path = os.path.join(os.path.dirname(__file__), "..", "tools", "inject", "sqlmap.py")
sqlmap_path = os.path.normpath(sqlmap_path)

if os.path.exists(sqlmap_path):
    cmd = (
        "python3 {path} -u \"{target}\""
        " --tor --tor-type=SOCKS5 --check-tor --tor-port=9050"
        " --random-agent --level=3 --risk=3 --threads=2"
    ).format(path=sqlmap_path, target=target)
else:
    # Fall back to system sqlmap if installed
    cmd = (
        "sqlmap -u \"{target}\""
        " --tor --tor-type=SOCKS5 --check-tor --tor-port=9050"
        " --random-agent --level=3 --risk=3 --threads=2"
    ).format(target=target)
    print("Note: Bundled sqlmap not found. Attempting system sqlmap.")

os.system(cmd)
