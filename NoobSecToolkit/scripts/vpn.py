#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys, traceback
print"-------------------------------------------------------------------"
print "Please Choose what version of the VPN you want to Download"
print "Example:(32bit)For the 32bit Version(64bit)for the 64bit version "
print"-------------------------------------------------------------------"
print "Once the Version you selected is done downloading,\
A Directory will be created named vpn, you must manually open the 'Bitmask' VPN applicaton. "
print"---------------------------------------------------------------------------------------"
print"To find out what Kernel you use, type: kernel"
VPNversion = raw_input("VPN Version?(32bit)or(64bit) :")

if VPNversion == "64bit":
    print"**************"
    print"You have chosen the VPN version "+VPNversion
    print"**************"
    Continue = raw_input("Continue? (yes) (no) :")
    if Continue == "no":
        sys.exit()
    cmd1 = os.system ("wget 'https://dl.bitmask.net/client/linux/stable/Bitmask-linux64-latest.tar.bz2 /vpn/'")	
    cmd1 = os.system ("bzip2 -d Bitmask-linux64-latest.tar.bz2 ")
    cmd1 = os.system ("tar -xvf Bitmask-linux64-latest.tar")

if VPNversion == "32bit":
    print"**************"
    print"You have chosen the VPN version "+VPNversion
    print"**************"
    Continue = raw_input("Continue? (yes) (no) :")
    if Continue == "no":
        sys.exit()
    cmd1 = os.system ("wget --output-document=/vpn 'https://dl.bitmask.net/client/linux/stable/Bitmask-linux32-latest.tar.bz2'")	
    cmd1 = os.system ("bzip2 -d Bitmask-linux32-latest.tar.bz2 ")
    cmd1 = os.system ("tar -xvf Bitmask-linux32-latest.tar vpn/")

if VPNversion == "kernel":
    print "--------------------"
    print "Kernel Information:"
    print "--------------------"
    cmd1 = os.system ("uname -m")
    
print"-----------"
print "Finished!"
print "----------"

