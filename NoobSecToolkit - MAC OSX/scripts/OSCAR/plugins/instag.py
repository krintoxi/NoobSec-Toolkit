#!/usr/bin/env python
"""Module to check if a username returns to a valid instagram user"""
import urllib2


def checker(usernom):
    """Check username. Send data to instagram and check status code."""
    #use username from FB profile and try it against instagram
    inst = "http://instagram.com/"+usernom
    try:
        data = urllib2.urlopen(inst)
        valid = True
        #If we get a 404/not found, then set valid to 0
    except urllib2.HTTPError:
        valid = False
    if valid:
        print
        print "---------"
        print "Found "+usernom+" on instagram!"
        print "Profile link: http://instagram.com/"+usernom
        print "---------\n"
    elif not valid:
        return
