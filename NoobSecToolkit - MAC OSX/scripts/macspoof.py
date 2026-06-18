#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import re

def get_interfaces():
    """Return list of available network interfaces."""
    try:
        result = subprocess.check_output(["ip", "link", "show"], text=True)
        interfaces = re.findall(r'\d+: (\w+):', result)
        return [i for i in interfaces if i != "lo"]
    except Exception:
        return ["eth0", "wlan0"]

print("********************************")
print("  MAC Address Spoofing Script   ")
print("  Linux Only                    ")
print("********************************")
print()

interfaces = get_interfaces()
print("Available interfaces: " + ", ".join(interfaces))
iface = input("Enter interface to spoof (default: eth0): ").strip() or "eth0"

option = input("Continue with MAC Spoofing on %s? (y/n): " % iface).strip().lower()

if option in ("y", "yes"):
    new_mac = input("Enter new MAC address (leave blank for 00:00:00:00:00:02): ").strip()
    if not new_mac:
        new_mac = "00:00:00:00:00:02"

    # Validate MAC format
    if not re.match(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$', new_mac):
        print("Invalid MAC address format. Example: 00:11:22:33:44:55")
        sys.exit(1)

    print("Starting MAC Spoofer...")
    os.system("sudo ip link set %s down" % iface)
    os.system("sudo ip link set %s address %s" % (iface, new_mac))
    os.system("sudo ip link set %s up" % iface)
    print("Finished spoofing MAC address on %s!" % iface)
    os.system("ip link show %s" % iface)
else:
    print("Cancelled.")
