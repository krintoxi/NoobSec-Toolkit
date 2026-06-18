#!/usr/bin/env python3
import threading
import ssl
import os

try:
    from time import sleep
    from netaddr import IPNetwork
    import OpenSSL
except ImportError as e:
    print("Missing dependency: " + str(e))
    print("Install with: pip3 install netaddr pyopenssl")
    OpenSSL = None
    IPNetwork = None

ips = []
out = {}


def starter():
    init(ips)


def init(ips):
    multi = input("Are we looking up multiple IPs/Networks? [y/n]: ").strip().lower()
    if multi == "y":
        multiNetwork = True
    elif multi == "n":
        multiNetwork = False
    else:
        print("Invalid input!")
        starter()
        return

    if multiNetwork:
        try:
            while True:
                cpy = input("IP or IP/CIDR [enter 'done' when finished]: ").strip()
                if cpy == "done":
                    break
                if "/" in cpy and IPNetwork:
                    ip_list = list(IPNetwork(cpy))
                    for e in sorted(ip_list):
                        ips.append(str(e))
                else:
                    ips.append(cpy)
        except KeyboardInterrupt:
            return
    else:
        cpy = input("IP or IP/CIDR: ").strip()
        ips.append(cpy)

    trigger(ips, out)


def getcert(a):
    """Get SSL Cert CN"""
    if OpenSSL is None:
        return
    try:
        refPorts = open("config/ports.txt", "r").readlines()
    except FileNotFoundError:
        refPorts = ["443"]

    for port in refPorts:
        port = port.strip()
        try:
            cert = ssl.get_server_certificate((a, int(port)))
        except Exception:
            continue
        try:
            c = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
            subj = c.get_subject()
            comp = subj.get_components()
            for data in comp:
                if b"CN" in data:
                    out[a] = (a, data[1].decode("utf-8", errors="ignore"))
        except Exception:
            continue


def trigger(ips, out):
    """Start SSL search threads"""
    threads = []
    for ip in ips:
        t = threading.Thread(target=getcert, args=(ip,), daemon=True)
        t.start()
        threads.append(t)
        sleep(2)
    sleep(3)
    for val in out:
        print(out[val])
