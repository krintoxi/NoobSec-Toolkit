#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.error

try:
    from bs4 import BeautifulSoup as bsoup
except ImportError:
    bsoup = None


def lookup():
    if bsoup is None:
        print("[+] ERROR: beautifulsoup4 not installed. Run: pip3 install beautifulsoup4")
        return

    while True:
        try:
            url = "https://isc.sans.edu/api/port/"
            port = input("Enter port: ").strip()
            fullUrl = url + port
            try:
                data = urllib.request.urlopen(fullUrl, timeout=10)
            except Exception:
                print("Could not connect to SANS website.")
                return

            i = bsoup(data, "xml")

            try:
                serviceUDP = i.html.body.services.udp.service
                udpName = i.html.body.services.udp.find_all("name")[0]
                print()
                print("----------UDP-----------")
                print("UDP Service Name: " + str(serviceUDP.string))
                print("UDP Name: " + str(udpName.string))
                print()
            except Exception:
                pass

            try:
                serviceTCP = i.html.body.services.tcp.service
                tcpName = i.html.body.services.tcp.find_all("name")[0]
                print("----------TCP-----------")
                print("TCP Service Name: " + str(serviceTCP.string))
                print("TCP Name: " + str(tcpName.string))
                print()
            except Exception:
                pass

            print("----------END-----------\n")

        except KeyboardInterrupt:
            return
