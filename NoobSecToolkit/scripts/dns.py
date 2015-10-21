#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys, traceback
print "-----------------------------------------------------------"
print "Author: @Zic"
print "Enter the domain below to gather basic DNS information."
print "Example: website.com"
print"------------------------------------------------------------"
target = raw_input("Input Target: ")  
cmd1 = os.system ("nslookup -type=any " +target)

print"-----------"
print "Finished!"
print "----------"

