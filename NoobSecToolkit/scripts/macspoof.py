import os
import sys

option = raw_input("Continue with Mac Spoofing? y/n: ")

if option == "y" or "yes":
    print "Starting MAC Spoofer..."
    cmd1 = os.system ("sudo ifconfig eth0 down")
    cmd1 = os.system ("sudo ifconfig eth0 hw ether 00:00:00:00:00:02")
    cmd1 = os.system ("sudo ifconfig eth0 up")
    print "Finished Spoofing Mac!..."
    cmd1 = os.system ("ifconfig eth0")


option2 = raw_input ("When you wish to go back to the Toolkit type home :")
if option2 == "home":
 cmd1 = os.system ("NSToolkit.py")
