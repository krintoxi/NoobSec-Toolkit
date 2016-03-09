#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os 
import traceback

print "SQLI Injector"

target = raw_input('SQLI Vulnerable Target: ')

cmd1 = os.system ('python '+'tools/inject/sqlmap.py -u'+target+'--tor-type=SOCKS5 --check-tor --tor-port=9050 --random-agent --level=3 --risk=3 --threads=2')
