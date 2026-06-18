#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from time import sleep

print("\nOSCAR-F requires various lib/modules to properly work.")
print('This script serves to check if you have those libs and will create the "auth" dir.\n')

sleep(1)

for lib, name in [
    ("readline", "readline"),
    ("tweepy", "tweepy"),
    ("twitter", "Twitter"),
    ("feedparser", "feedparser"),
    ("shodan", "shodan"),
    ("bs4", "bs4 (beautifulsoup 4)"),
    ("PIL", "PIL/Pillow"),
    ("mechanize", "mechanize"),
]:
    try:
        __import__(lib)
        print("[+] FOUND: " + name)
    except ImportError:
        print("[+] MISSING: " + name + "  -->  pip3 install " + lib)

auth_dir = os.path.join(os.path.dirname(__file__), "..", "auth")
auth_dir = os.path.normpath(auth_dir)
if not os.path.exists(auth_dir):
    print("Adding the 'auth' directory. Be sure to run the setup script after this one!")
    os.makedirs(auth_dir, exist_ok=True)

print("\nTo install all dependencies: pip3 install -r requirements.txt")
