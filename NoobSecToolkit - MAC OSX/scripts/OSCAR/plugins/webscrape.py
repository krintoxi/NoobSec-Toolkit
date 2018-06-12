#!/usr/bin/env python

import urllib2
import re
# not all systems have readline...if not, just pass and continue.
try:
    import readline  # nice when you need to use arrow keys and backspace
except:
    pass
import sys


def scrape():
    site = raw_input("Enter page: ")

    #open site. read so we can read in a string context
    #test for valid and complete URL
    try:
        data = urllib2.urlopen(site).read()
    except ValueError:
        print "INVALID URL: Be sure to include protocol (e.g. HTTP)"
        return
    
    #print data

    #try an open the pattern file.
    try:
        patternFile = open('config/webscrape.dat', 'r').read().splitlines()
    except:
        print "There was an error opening the webscrape.dat file"
        raise
    #create counter for counting regex expressions from webscrape.dat
    counter = 0
    #for each loop so we can process each specified regex
    for pattern in patternFile:
        m = re.findall(pattern, data)
        #m will return as true/false. Just need an if m:
        if m:
            for i in m:
                #open output/results file...append because we are cool
                outfile = open('scrape-RESULTS.txt', 'a')
            #print m
                outfile.write(str(i))
                outfile.write("\n")  # may be needed. can always be removed.

            #close the file..or else
                outfile.close()
                counter+=1
                print "Scrape item " + str(counter) + " successsful. Data output to scrape-RESULTS.txt."
        else:  # only need an else because m is boolean
            counter+=1
            print "No match for item " + str(counter) + ". Continuing."
            # Continue the loop if not a match so it can go on to the next
            # sequence
            # NOTE: you don't *really* need an else here...
            continue
