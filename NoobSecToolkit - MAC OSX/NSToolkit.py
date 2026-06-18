#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import traceback

print("""
      __   __   __       __   ___  __      ___  __   __              ___
|\ | /  \ /  \ |__)     /__` |__  /  `      |  /  \ /  \ |    |__/ |  |
| \| \__/ \__/ |__) ___ .__/ |___ \__, ___  |  \__/ \__/ |___ |  \ |  | v3  "- All day, every day."

     78 111 111 98 95 83 101 99 95 84 111 111 108 75 105 116

     A Penetration Testing Framework For The Inexperienced
     ------------------------------------------------------
     BY: Krintoxi https://github.com/krintoxi
     ------------------------------------------------------
     Url: https://github.com/krintoxi/NoobSec-Toolkit
     ------------------------------------------------------
""")

print("""
*****************
Toolkit Options:
*****************
(toxicdork) SQLI Scanner via Dorks
(sqli)      SQL Injector
(vulscan)   Vulnerability Scanner
(dinfo)     Gather Basic Domain Info
(apf)       Admin Page Finder
(hashtype)  Identify Hash Type
(hexconv)   Hex Encoder and Decoder
(numconv)   Number Base Converter
(dping)     DOS/Ping Target For 1,000 Seconds
(uihanalysis) Intrusion Analysis (URL, IP, HASH)
(osint)     OSINT Information Gathering
(steghide)  Steghide GUI Launcher
(stegattack) Steghide Dictionary Attacker
(toolbox)   Extra Set of Tools
(backdoorssh) SSH Backdoor Deployment Framework

*****************************
Security Options: (Linux Only for some)
*****************************
(macspoof)  Spoof MAC Address (Linux)
(itor)      Install Tor (Linux)
(stor)      Start Tor (Linux)
(tors)      Check Tor Status (Linux)
(vpn)       VPN Launcher (Linux)
(encdns)    Encrypt DNS (Linux)
(quit) | (home) | (clear) | (update)
""")


def loopfunc():
    choice = input("NoobSec_Toolkit Command: ").strip()

    if choice == "apf":
        print("-------------------")
        print("Launching Finder.PL")
        print("-------------------")
        os.system("perl scripts/finder.pl")

    elif choice == "sqli":
        print("****************************")
        print("Launching SQLI Injector....")
        print("****************************")
        os.system("python3 scripts/sqli.py")

    elif choice == "vulscan":
        print("-------------------------")
        print("Launching Vulnerability Scanner....")
        print("-------------------------")
        os.system("python3 scripts/vulscan.py")

    elif choice == "itor":
        print("------------------")
        print("Installing Tor....")
        print("------------------")
        os.system("sudo apt-get install tor")

    elif choice == "stor":
        print("-----------------")
        print("Starting Tor....")
        print("-----------------")
        os.system("sudo service tor start")

    elif choice == "tors":
        print("----------------")
        print("Tor Status Check")
        print("----------------")
        os.system("sudo service tor status")

    elif choice == "vpn":
        print("Starting VPN Launcher for Bitmask....")
        os.system("python3 scripts/vpn.py")

    elif choice == "backdoorssh":
        print("-------------------------------------")
        print("Launching SSH Backdoor Deploy Script")
        print("-------------------------------------")
        print("Deploy a specific backdoor, such as a netcat backdoor or msfvenom backdoor")
        os.system("python3 scripts/sshbackdoors/dependencies.py")
        os.system("python3 scripts/sshbackdoors/master.py")

    elif choice == "discover":
        print("*************************************")
        print("Launching Discover.... By: Lee Baird")
        print("*************************************")
        os.system("sudo git clone git://github.com/leebaird/discover.git /opt/discover/")
        os.system("/opt/discover/./discover.sh")

    elif choice == "dinfo":
        print("********************************")
        print("Launching DNS Info Script...")
        print("********************************")
        os.system("python3 scripts/dns.py")

    elif choice == "hashtype":
        print("----------------------------------")
        print("Launching Hash Identify Script...")
        print("----------------------------------")
        os.system("python3 scripts/Hash_ID.py")

    elif choice == "numconv":
        print("----------------------------------")
        print("Launching Number Converter Script...")
        print("----------------------------------")
        os.system("python3 scripts/NumberConverter.py")

    elif choice == "hexconv":
        print("----------------------------------")
        print("Launching Hex Converter Script...")
        print("----------------------------------")
        os.system("python3 scripts/hex_converter.py")

    elif choice == "update":
        print("----------------------------------")
        print("      UPDATING THE SYSTEM")
        print("----------------------------------")
        os.system("sudo apt-get update")
        os.system("sudo apt-get upgrade")
        os.system("sudo apt-get dist-upgrade")

    elif choice == "osint":
        print("----------------------------------")
        print("Launching OSCARF OSINT Script.....")
        print("----------------------------------")
        os.system("pip3 install -r scripts/OSCAR/requirements.txt")
        print("Done checking for dependencies!")
        os.system("python3 scripts/OSCAR/OSCARf.py")

    elif choice == "steghide":
        print("----------------------------------")
        print("       Launching Steghide GUI")
        print("----------------------------------")
        os.system("python3 scripts/pySteg/pysteg.py")

    elif choice == "dping":
        print("----------------------------------")
        print("     Launching DOS/PING Script    ")
        print("----------------------------------")
        tar = input("Target URL (include http://): ").strip()
        os.system("python3 scripts/dping.py -c 10 -t 1000 " + tar)

    elif choice == "encdns":
        print("***************************************")
        print("Launching DNS Encryption Install!.....")
        print("***************************************")
        os.system("sudo git clone git://github.com/simonclausen/dnscrypt-autoinstall.git dloads/")
        os.system("bash dloads/dnscrypt-autoinstall.sh")

    elif choice == "stegattack":
        print("***********************************")
        print("        Steghide Attacker")
        print("***********************************")
        stegfile = input("Steg file path: ").strip()
        wordlist = input("Wordlist path: ").strip()
        os.system("python3 scripts/steghidecracker.py %s %s" % (stegfile, wordlist))

    elif choice == "clear":
        os.system("clear")
        print("--------------")
        print("Fresh Terminal")
        print("--------------")

    elif choice == "home":
        os.system("python3 NSToolkit.py")

    elif choice == "uihanalysis":
        print("---------------------------")
        print("Launching Analysis Script...")
        print("---------------------------")
        uihtarget = input("URL, Hash, or IP for Analysis: ").strip()
        os.system("automater -b " + uihtarget + " -w uihresult.html")

    elif choice in ("exit", "quit", "q"):
        print("Goodbye!")
        sys.exit()

    elif choice == "toolbox":
        print("####################")
        print("Launching ToolBox...")
        print("####################")
        os.system("python3 scripts/toolbox.py")

    elif choice == "macspoof":
        print("********************************")
        print("Launching MAC Spoofing Script...")
        print("********************************")
        os.system("python3 scripts/macspoof.py")

    elif choice == "toxicdork":
        print("*********************************")
        print("Launching SQLI Dork Scanner...  ")
        print("*********************************")
        os.system("python3 scripts/sqli.py --dork")

    elif choice == "":
        pass

    else:
        print("Unknown command: '%s'. Type 'quit' to exit." % choice)

    loopfunc()


loopfunc()
