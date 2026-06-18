#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

print("---------------------")
print(" Vulnerability Scanner")
print("   Powered by Nikto  ")
print("---------------------")
print("Use only on systems you have permission to test.")
print()

target = input("Scan Target (hostname or IP): ").strip()

if not target:
    print("No target provided. Exiting.")
    sys.exit(1)

nikto_path = os.path.join(os.path.dirname(__file__), "..", "tools", "vscan", "nikto.pl")
nikto_path = os.path.normpath(nikto_path)

if os.path.exists(nikto_path):
    cmd = "perl {path} -h {target} -o target_output.html".format(
        path=nikto_path, target=target
    )
else:
    cmd = "nikto -h {target} -o target_output.html".format(target=target)
    print("Note: Bundled Nikto not found. Attempting system nikto.")

os.system(cmd)
print()
print("Scan complete. Results saved to target_output.html")
