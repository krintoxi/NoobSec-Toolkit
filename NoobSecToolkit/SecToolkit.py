#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys, traceback
#Title AREA
print"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print"NOOB Security Toolkit 2.0 - BETA"
print"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print"Dev: The_Chosen_One, TheAndreiM "
print"https://github.com/krintoxi"
print"https://github.com/JuliarLang"
print"~~~~~~~~~~~~~~~~~~~"
#End Of Title Area
#Start Of Options 
def loopfunc():
	print "*****************"
	print "Toolkit Options:"
	print "*****************"
	print "----------------"
	print "(sqli)SQL Injector"
	print "(vulscan) Vulnerability Scanner"
	print "(dinfo) Gather Basic Domain Info"
	print "(discover) Information Harvester (Kali Linux Only!)"
	print "-----------------"
	#Extra Options 
	print "**************"
	print "Misc Options:"
	print "**************"
	print "(itor) install Tor"
	print "(stor) Start Tor"
	print "(dvpn) Download VPN"
	print "(lvpn) Launch VPN (debian)"
	print "(encdns) Encrypt DNS"
	print "(quit)(exit)(q) Quit"
	print "--------------------------"
	#Script Input
	choice = raw_input("What do you want to do?:")

	if choice == "sqli":
		print "Launching SQLI Injector....c"
		cmd1 = os.system ("sudo python scripts/sqli.py")
		
	if choice == "vulscan":
		print "Launching NiktoST.pl...."
		cmd1 = os.system ("sudo python scripts/vulscan.py")
		
	#if choice == "":

	#Start of Misc Options
	if choice == "itor":
		print"Installing Tor...."
		cmd1 = os.system ("sudo apt-get install tor")
		
	if choice == "stor":
		print "Starting Tor...."
		cmd1 = os.system ("sudo service tor start")
		
	if choice == "dvpn":
		print "Downloading VPN Client to /Bitmask-Linux64-latest....." 
		cmd1 = os.system ("wget 'https://dl.bitmask.net/client/linux/stable/Bitmask-linux64-latest.tar.bz2'")	
		cmd1 = os.system ("bzip2 -d Bitmask-linux64-latest.tar.bz2 ")
		cmd1 = os.system ("tar -xvf Bitmask-linux64-latest.tar")
		
		# Start VPN broken
	if choice == "lvpn":
		
		cmd1 = os.system ("sudo python Bitmask-linux64-0.8.1/apps/launcher.py")

	if choice == "discover":
		print "Launching Discover.... By: Lee Baird"
		cmd1 = os.system ("sudo git clone git://github.com/leebaird/discover.git /opt/discover/")
		cmd1 = os.system ("cd /opt/discover/")
		cmd1 = os.system ("/opt/discover/./discover.sh")	
			

	if choice == "dinfo":
		print "Launching Domain Script..."
		cmd1 = os.system ("python scripts/dns.py")
		
	if choice == "encdns":
		print "Launching DNS Encryption Install!....."	
		cmd1 = os.system ("sudo git clone git://github.com/simonclausen/dnscrypt-autoinstall.git dloads/")	
		cmd1 = os.system ("cd scripts/")	
		cmd1 = os.system ("./dloads/dnscrypt-autoinstall.sh")
	if choice == "exit" or choice == "quit" or choice == "q":
		sys.exit()
	else:
		print "Choice "+choice+" is not valid."
		loopfunc()
loopfunc()
