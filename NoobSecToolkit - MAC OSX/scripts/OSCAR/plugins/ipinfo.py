#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import webbrowser

try:
    import requests
except ImportError:
    requests = None


def lookup(ip):
    if requests is None:
        print("[+] ERROR: requests library not installed. Run: pip3 install requests")
        return

    ipUrl = "http://ip-api.com/json/"
    ip_query = ipUrl + ip
    try:
        data = requests.get(ip_query, timeout=10)
        jsonResponse = data.json()
        print()
        print("-- IP Results --")
        print("IP: ", jsonResponse.get("query", "N/A"))
        print("ISP: ", jsonResponse.get("isp", "N/A"))
        print("ASN: ", jsonResponse.get("as", "N/A"))
        print("Country: ", jsonResponse.get("country", "N/A"))
        print("City: ", jsonResponse.get("city", "N/A"))
        print("Region: ", jsonResponse.get("regionName", "N/A"))
        print("Longitude: ", jsonResponse.get("lon", "N/A"))
        print("Latitude: ", jsonResponse.get("lat", "N/A"))
        print("-- END --")
        print()
    except Exception:
        print("[+] ERROR: Could not connect to IP lookup site.")

    time.sleep(2)
    avcheck = input("Check IP with AlienVault (opens in browser) [y/n]: ").strip()
    if avcheck.lower() == "y":
        alienvault(ip)


def alienvault(ip):
    url = "https://otx.alienvault.com/indicator/ip/" + ip
    webbrowser.open(url, new=2)
