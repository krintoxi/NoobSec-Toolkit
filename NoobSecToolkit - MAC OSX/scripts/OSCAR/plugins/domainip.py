#!/usr/bin/env python3
"""Module to get the IP address of a given domain."""
import socket


def c():
    """Get IP address of domain."""
    domain = input("Domain: ").strip()
    try:
        chk = socket.gethostbyname_ex(domain)
    except Exception:
        print("[+] ERROR: could not get hostname!")
        return
    print("\nIP Address of", domain, ":", chk[2], "\n")
