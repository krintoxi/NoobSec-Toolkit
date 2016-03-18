#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys, traceback
#Title AREA
print"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print"NOOB Security Toolkit 2.1  (C.T.F Edition)"
print"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print"By: The_Chosen_One (Krintoxi)"
print "Url: https://krintoxi.github.io/NoobSecToolkit/"
print"~~~~~~~~~~~~~~~~~~~"
#End Of Title Area
#Start Of Options 
print "*****************"
print "Toolkit Options:"
print "*****************"
print "----------------"
print "(sqli)SQL Injector"
print "(vulscan) Vulnerability Scanner"
print "(dinfo) Gather Basic Domain Info"
print "(apf) Admin Page Finder"
print "(discover) Information Harvester"
print "(hashtype) Identify Hash Type"
print "(aconv) ASCII Converter"
print "(hexconv) Hex encoder and decoder!"
print "(converters) Web Converters"
print "(dping) DOS/Ping Target For 1,000 Seconds"
print "(stegattack) Steghide Dictionary Attacker"
print "(steghide) Install, Learn and Use Steghide"
print "(uihanalysis) Intrusion Analysis (URL,IP,HASH)"
print "(backdoorssh) Options For Deploying an SSH Backdoor"
print "-----------------"
#Extra Options 
print "******************"
print "Security Options:"
print "******************"
print "(macspoof) Spoof Mac Address"
print "(itor) install Tor"
print "(stor) Start Tor"
print "(tors) Check Tor Status"
print "(vpn)  VPN Launcher"
print "(encdns) Encrypt DNS"
print "(quit) - (home) - (clear)-(update)"
print "-----------------------------------"
def loopfunc():
	#Script Input
	print ""
	choice = raw_input("What do you want to do?:")

	if choice == "apf":
                cmd1 = os.system ("perl scripts/finder.pl")

	if choice == "macspoof":
                print "Loading Mac Spoof...."
                cmd1 = os.system ("python scripts/macspoof.py")
                
	if choice == "sqli":
		print "Launching SQLI Injector...."
		cmd1 = os.system ("sudo python scripts/sqli.py")
		
	if choice == "vulscan":
		print "Launching NiktoST.pl...."
		cmd1 = os.system ("sudo python scripts/vulscan.py")

	#Start of Misc Options
	if choice == "itor":
		print"Installing Tor...."
		cmd1 = os.system ("sudo apt-get install tor")
		
	if choice == "stor":
		print "Starting Tor...."
		cmd1 = os.system ("sudo service tor start")
		
	if choice == "tors":
                print "----------------"
                print "Tor Status Check"
                print "----------------"
                cmd1 = os.system ("sudo service tor status")
                
	#if choice == "dvpn":
		#print "Downloading VPN Client to /Bitmask-Linux64-latest....." 
		#cmd1 = os.system ("wget 'https://dl.bitmask.net/client/linux/stable/Bitmask-linux64-latest.tar.bz2'")	
		#cmd1 = os.system ("bzip2 -d Bitmask-linux64-latest.tar.bz2 ")
		#cmd1 = os.system ("tar -xvf Bitmask-linux64-latest.tar")
		
		# Start VPN broken
		
	if choice == "vpn":
		print "Starting VPN Launcher for Bitmask...."
		cmd1 = os.system ("sudo python scripts/vpn.py")

	if choice == "backdoorssh":
                print "-------------------------------------"
		print "Launching Deploy Script.. "
		print "-------------------------------------"
		print "deploy a specific backdoor, such as a netcat backdoor or msfvenom backdoor"
		cmd1 = os.system ("sudo python scripts/sshbackdoors/dependencies.py")
		cmd1 = os.system ("sudo python scripts/sshbackdoors/main.py")


	if choice == "discover":
		print "Launching Discover.... By: Lee Baird"
		cmd1 = os.system ("sudo git clone git://github.com/leebaird/discover.git /opt/discover/")
		cmd1 = os.system ("cd /opt/discover/")
		cmd1 = os.system ("/opt/discover/./discover.sh")	
			

	if choice == "dinfo":
		print "Launching NSlookup Script..."
		cmd1 = os.system ("python scripts/dns.py")

	if choice == "hashtype":
		print "----------------------------------"
		print "Launching Hash Identify Script..."
		print "----------------------------------"
		cmd1 = os.system ("python scripts/Hash_ID.py")

	if choice == "numconverter":
		print "----------------------------------"
		print "Launching Converter Script..."
		print "----------------------------------"
		cmd1 = os.system ("python scripts/NumberConverter.py")

	if choice == "hexconv":
		print "----------------------------------"
		print "Launching Converter Script..."
		print "----------------------------------"
		cmd1 = os.system ("python scripts/hex_converter.py")
	
	if choice == "update":
		print "----------------------------------"
		print "      UPDATING THE SYSTEM"
		print "----------------------------------"
		cmd1 = os.system ("sudo apt-get update")
		cmd1 = os.system ("sudo apt-get upgrade")
		cmd1 = os.system ("sudo apt-get dist-upgrade")
	
	if choice == "converters":
		print "----------------------------------"
		print "Launching Binary Converter Website"
		print "----------------------------------"
		cmd1 = os.system ("iceweasel http://www.exploringbinary.com/converters-and-calculators/")

	if choice == "aconv":
		print "----------------------------------"
		print "Launching ASCII Converter Website"
		print "----------------------------------"
		cmd1 = os.system ("iceweasel https://www.branah.com/ascii-converter")
	
	if choice == "steghide":
		print "----------------------------------"
		print "       Launching Steghide GUI"
		print "----------------------------------"
		cmd1 = os.system ("sudo apt-get install steghide")
		cmd1 = os.system ("python scripts/pySteg/pysteg.py")

	if choice == "dping":
		print "----------------------------------"
		print "     Launching DOS/PING Script 	"
		print "----------------------------------"
		tar = raw_input('Target link #Include http://# : ')
		cmd1 = os.system ("python scripts/dping.py -c 10 -t 1000 "+tar )

		
	if choice == "encdns":
		print "Launching DNS Encryption Install!....."	
		cmd1 = os.system ("sudo git clone git://github.com/simonclausen/dnscrypt-autoinstall.git dloads/")
		cmd1 = os.system ("cd scripts/")	
		cmd1 = os.system ("./dloads/dnscrypt-autoinstall.sh")

	if choice == "stegattack":
		print "----------------------------------"
		print "        Steghide Attacker"
		print "----------------------------------"
		print "In order to use this script , you must call: "
		print "# pyhon scripts/steghidecracker.py [stegfile] [wordlist]"
		print "Launching Fresh Terminal"
		cmd1 = os.system ("xterm")
		

        if choice == "clear":
                cmd1 = os.system ("clear")
                print "--------------"
                print "Fresh Terminal"
                print "--------------"

        if choice == "home":
                cmd1 = os.system ("python NSToolkit.py")

        if choice == "uihanalysis":
		print"---------------------------"
		print"Launching Analysis Script..."
		print"---------------------------"
		uihtarget = raw_input ("Url , Hash Or IP for Analysis: ")
                cmd1 = os.system ("automater -b "+uihtarget +" -w uihresult.html")
                

	if choice == "exit" or choice == "quit" or choice == "q":
		sys.exit()
	else:
		print "We are done here!" 
		
		loopfunc()
loopfunc()


