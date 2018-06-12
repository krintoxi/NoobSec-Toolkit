#!/usr/bin/env python
"""Module to get the ip address of a given domain."""
#import socket :P -- Now that is how you comment in code.
import socket

def c():
    """Get ipaddress of domain..GO DNS!"""
    domain = raw_input("Domain: ")
    #try to resolve.
    try:
        chk = socket.gethostbyname_ex(domain)
    except Exception:
        print "[+]ERROR: could not get hostname!"
        raise
    print "\nIP Address of", domain, ":", chk[2], "\n"
    return
