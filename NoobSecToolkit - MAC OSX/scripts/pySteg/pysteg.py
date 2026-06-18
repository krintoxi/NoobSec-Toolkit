#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

print("-------------------------")
print("    StegHide Options     ")
print("-------------------------")
print("Usage Examples:")
print("")
print("  Embed emb.txt in cvr.jpg:")
print("    steghide embed -cf cvr.jpg -ef emb.txt")
print("")
print("  Extract embedded data from stg.jpg:")
print("    steghide extract -sf stg.jpg")
print("")
print("  Check if steghide is installed:")
print("    steghide --version")
print("")

choice = input("Open a terminal for steghide commands? (y/n): ").strip().lower()
if choice in ("y", "yes"):
    if sys.platform == "darwin":
        os.system("open -a Terminal .")
    else:
        os.system("xterm")
