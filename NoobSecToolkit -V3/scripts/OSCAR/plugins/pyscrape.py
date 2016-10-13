#!/usr/bin/env python

import urllib
import time
import thread
import sys
import os
import re
import datetime


def downloader(url, filename):
    patternFile = open('config/pSearch.dat', 'r').read().splitlines()
    data = ""
    try:
        try:
            data = urllib.urlopen(url).read()
        except:
            print "Error connecting to pastebin!"
            raise
        for pattern in patternFile:
            m = re.findall("'"+pattern+"'", data)
            if m:
                print ""
                print "Found Match"
                print "Expr:"+pattern
                print ""
                now = datetime.datetime.now()
                stime = str(time.ctime())
                hardFile = "pasteebin/downloaded/{0}-{1}.txt".format(filename,stime)
                file = open(hardFile, 'w')
                file.write(data)
                file.close
            else:
                continue
    except:
        #print "There was a file IO error"
        pass


def starter():
    if not os.path.exists("pastebin"):
        os.mkdir("pastebin")
        os.mkdir("pastebin/downloaded")
    if not os.path.exists("pastebin/seen-pastes.txt"):
        chkf = open("pastebin/seen-pastes.txt", 'w')
        chkf.close()
    print "Scraping for pastes...\n"
    while True:
        try:
            time.sleep(1)
            #open the pastebin archive
            data = urllib.urlopen("http://pastebin.com/archive").read()
            data = data.split('<table class="maintable" cellspacing="0">')
            data = data[1]
            data = data.split('</table>')
            data = data[0]
            data = data.replace('<td><img src="/i/t.gif"  class="i_p0" alt="" border="0" /><a href="/', "!!HTML!!")
            data = data.replace('</a>', "!!HTML!!")
            data = data.split("!!HTML!!")
            for i in data:
                i = i.split("\">")
                i = i[0]
                if not (("</td>" in i) or ("<tr class=" in i)):
                    seenf = open("pastebin/seen-pastes.txt",'r').read().splitlines()
                    if i not in seenf:
                        sys.stdout.write("\rCurrently on paste: %s" % i)
                        sys.stdout.flush()
                        seenf2 = open("pastebin/seen-pastes.txt", 'a')
                        seenf2.write(i)
                        seenf2.write("\n")
                        seenf2.close()
                        i2 = i
                        i = ("http://pastebin.com/raw.php?i="+i)
                        thread.start_new_thread(downloader, (i, i2))
                        time.sleep(4)
        except:
            print "Exiting..."
            pass
            raise


def stopper():
    raise
