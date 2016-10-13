#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os 
import traceback
print "---------------------"
print "Vulnerability Scanner"
print "---------------------"
target = raw_input('Scan Target: ')

cmd1 = os.system ('perl '+'tools/vscan/nikto.pl -h ' +target+' -o target_output.html')
