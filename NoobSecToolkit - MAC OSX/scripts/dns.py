#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

print("-----------------------------------------------------------")
print("Author: @Zic")
print("Enter the domain below to gather basic DNS information.")
print("Example: website.com")
print("-----------------------------------------------------------")

target = input("Input Target: ").strip()

if not target:
    print("No target provided. Exiting.")
    sys.exit(1)

os.system("nslookup -type=any " + target)

print("-----------")
print("Finished!")
print("-----------")
