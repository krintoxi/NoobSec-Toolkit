#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys, traceback

print """
      __   __   __       __   ___  __      ___  __   __              ___ 
|\ | /  \ /  \ |__)     /__` |__  /  `      |  /  \ /  \ |    |__/ |  |  
| \| \__/ \__/ |__) ___ .__/ |___ \__, ___  |  \__/ \__/ |___ |  \ |  | v3  "- All day, every day."
                                                                                     
     78 111 111 98 95 83 101 99 95 84 111 111 108 75 105 116                   
     
     A Penetration Testing Framework For The inexperienced
     ------------------------------------------------------
     BY: Krintoxi https://www.cybrary.it/members/leoedge
     ------------------------------------------------------
     Url: https://github.com/krintoxi/NoobSec-Toolkit                   
     ------------------------------------------------------
"""
#End Of Title Area
#Start Of Options 
print """
*****************
Toolkit Options:
*****************
(toxicdork) SQLI Scanner via Dorks
(sqli) SQL Injector
(vulscan) Vulnerability Scanner
(dinfo) Gather Basic Domain Info
(apf) Admin Page Finder
(hashtype) Identify Hash Type
(hexconv) Hex encoder and decoder!
(dping) DOS/Ping Target For 1,000 Seconds
(uihanalysis) Intrusion Analysis (URL,IP,HASH)
(osint) aids in the process of information gathering (Needs Tweaking)
(toolbox) Extra Set of Tools (Requires PIP)


*****************************
LINUX ONLY Security Options: (NO OSX SUPPORT)
*****************************
(macspoof) Spoof Mac Address
(itor) install Tor
(stor) Start Tor
(tors) Check Tor Status
(vpn)  VPN Launcher (COMING SOON)
(encdns) Encrypt DNS
(quit) - (home) - (clear)-(update)

"""
def loopfunc():

	#Script Input
	choice = raw_input("NoobSec_Toolkit Command :")
	
	if choice == "apf":
		print """
		-------------------
		Launching Finder.PL
		-------------------
		"""
		cmd1 = os.system ("perl scripts/finder.pl")
                

	if choice == "sqli":
		print "****************************"
		print "Launching SQLI Injector...."
		print "****************************"
		cmd1 = os.system ("sudo python scripts/sqli.py")
		
	if choice == "vulscan":
		print "-------------------------"
		print "Launching NiktoST.pl...."
		print "-------------------------"
		cmd1 = os.system ("sudo python scripts/vulscan.py")

	#Start of Misc Options
	if choice == "itor":
		print "------------------"
		print "Installing Tor...."
		print "------------------"
		cmd1 = os.system ("sudo apt-get install tor")
		
	if choice == "stor":
		print "-----------------"
		print "Starting Tor...."
		print "-----------------"
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
		cmd1 = os.system ("sudo python scripts/sshbackdoors/master.py")


	if choice == "discover":
		print "*************************************"
		print "Launching Discover.... By: Lee Baird"
		print "*************************************"
		cmd1 = os.system ("sudo git clone git://github.com/leebaird/discover.git /opt/discover/")
		cmd1 = os.system ("cd /opt/discover/")
		cmd1 = os.system ("/opt/discover/./discover.sh")	
			

	if choice == "dinfo":
		print "********************************"
		print "Launching NSlookup Script..."
		print "********************************"
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
		cmd1 = os.system ("sudo apt-get install iceweasel")
		cmd1 = os.system ("iceweasel http://www.exploringbinary.com/converters-and-calculators/")
		cmd1 = os.system ("firefox http://www.exploringbinary.com/converters-and-calculators/")

	if choice == "aconv":
		print "----------------------------------"
		print "Launching ASCII Converter Website"
		print "----------------------------------"
		cmd1 = os.system ("iceweasel https://www.branah.com/ascii-converter")

	if choice == "osint":
		print "----------------------------------"
		print "Launching OSCARF OSINT Script....."
		print "----------------------------------"
		cmd1 = os.system("sudo python scripts/OSCAR/DEPENDENCY_CHECK.py")
		cmd1 = os.system("sudo pip install -r scripts/OSCAR/requirements.txt")
		cmd1 = os.system ("sudo apt-get install python-dev")
                print "Done Checking For Updates!"
                cmd1 = os.system ("sudo python scripts/OSCAR/OSCARf.py")

	
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
		print "***************************************"
		print "Launching DNS Encryption Install!....."
		print "***************************************"	
		cmd1 = os.system ("sudo git clone git://github.com/simonclausen/dnscrypt-autoinstall.git dloadss/")
		cmd1 = os.system ("cd scripts/")	
		cmd1 = os.system ("./dloads/dnscrypt-autoinstall.sh")

	if choice == "stegattack":
		print "***********************************"
		print "        Steghide Attacker"
		print "***********************************"
		print "@In order to use this script , you must call: "
		print "# pyhon scripts/steghidecracker.py [stegfile] [wordlist]"
		cmd1 = os.system ("sudo apt-get install xterm")
		cmd1 = os.system ("xterm echo ")
		

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
		print "Finished!" 
	
	if choice == "toolbox":
		print """
		####################
		Launching ToolBox...
		####################
		"""
		print "This Toolbox has some requirements , if you think you have them, continue."
		cmd1 = os.system ("python scripts/toolbox.py")
	
	if choice == "macspoof":
		print """ 
		********************************
		Launching Mac Spoofing Script...
		*********************************
		"""
		cmd1 = os.system ("python scripts/macspoof.py")
		
		loopfunc()
loopfunc()


