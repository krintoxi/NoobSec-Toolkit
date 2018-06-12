#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from time import sleep

print "\nOSCAR-F requires various lib/modules to properly work."
print "This script serves to check if you have those libs and",
print 'will create the "auth" dir.\n'

sleep(2)

try:
    import readline
    print '[+]FOUND: readline'
except:
    print '[+]MISSING: readline'

try:
    import tweepy
    print '[+]FOUND: tweepy'
except:
    print '[+]MISSING: tweepy'

try:
    import twitter
    print '[+]FOUND: Twitter'
except:
    print '[+]MISSING: Twitter'

try:
    import feedparser
    print '[+]FOUND: feedparser'
except:
    print '[+]MISSING: feedparser'

try:
    import shodan
    print '[+]FOUND: shodan'
except:
    print '[+]MISSING: shodan'

try:
    import bs4
    print '[+]FOUND: bs4 (beautifulsoup 4)'
except:
    print '[+]MISSING: bs4 (beautifulsoup 4)'

try:
    from PIL import Image
    print '[+]FOUND: PIL/Pillow'
except:
    print '[+]MISSING: PIL/Pillow module'

try:
    import mechanize
    print "[+]FOUND: mechanize"
except:
    print "[+]MISSING: mechanize"

if not os.path.exists('../auth'):
    print "Adding the 'auth' directory. Be sure to run the setup",
    print "script after this one!!!"
    os.mkdir('../auth')
print "To install dependencies: pip install -r requirements.txt"
