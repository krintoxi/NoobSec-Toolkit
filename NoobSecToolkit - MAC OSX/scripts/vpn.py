#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

print("-------------------------------------------------------------------")
print("VPN Launcher - Downloads Bitmask VPN Client (Linux Only)")
print("-------------------------------------------------------------------")
print("To find out your kernel architecture, enter: kernel")
print("-------------------------------------------------------------------")

VPNversion = input("VPN Version? (32bit) or (64bit): ").strip()

if VPNversion == "64bit":
    print("**************")
    print("You have chosen the VPN version " + VPNversion)
    print("**************")
    cont = input("Continue? (yes) (no): ").strip()
    if cont.lower() in ("no", "n"):
        sys.exit()
    os.system("wget 'https://dl.bitmask.net/client/linux/stable/Bitmask-linux64-latest.tar.bz2'")
    os.system("bzip2 -d Bitmask-linux64-latest.tar.bz2")
    os.system("tar -xvf Bitmask-linux64-latest.tar")

elif VPNversion == "32bit":
    print("**************")
    print("You have chosen the VPN version " + VPNversion)
    print("**************")
    cont = input("Continue? (yes) (no): ").strip()
    if cont.lower() in ("no", "n"):
        sys.exit()
    os.system("wget 'https://dl.bitmask.net/client/linux/stable/Bitmask-linux32-latest.tar.bz2'")
    os.system("bzip2 -d Bitmask-linux32-latest.tar.bz2")
    os.system("tar -xvf Bitmask-linux32-latest.tar")

elif VPNversion == "kernel":
    print("--------------------")
    print("Kernel Information:")
    print("--------------------")
    os.system("uname -m")

else:
    print("Invalid option. Please choose 32bit, 64bit, or kernel.")

print("-----------")
print("Finished!")
print("-----------")
