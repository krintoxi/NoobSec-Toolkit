#!/usr/bin/env python
"""Python script to aid in the collection of OSINT data"""

"""
____   ________________   ________
\   \ /   /_   \_____  \  \_____  \ ______  ______
 \   Y   / |   |/  ____/   /   |   \\____ \/  ___/
  \     /  |   /       \  /    |    \  |_> >___ \
   \___/   |___\_______ \ \_______  /   __/____  >
                       \/         \/|__|       \/
v12 operations
NoobSecToolkit (C.T.F Edition)
"""

#External libraries needed to use oscar:
#twitter
#tweepy
#feedparser
#shodan
#readline
#beautifulsoup

#oscar will automatically try to import first.
#On exception it will alert the user
import urllib2

import sys
import os
import time


try:
    import readline
except:
    pass
try:
    import pyreadline
except:
    pass

if "nt" in os.name:
    print "Windows Support is in alpha! Proceed with caution!"
    time.sleep(3)
else:
    pass

#################
# LOCAL IMPORTS #
#################
from plugins import *

#----Why 2 twitter libs?----#
#The auth for the twitter lib is nicer as it can create an auth file
#to read from. the twitter auth will also open a browser window where
# you will accept the app to use your twitter account. Read and Write
#is what it requires. When accepted, you will get a pin to enter into
# the application. You will not be prompted for a pin after getting a
#token.
#----END----#
# imports for the streaming lib

try:
    import tweepy
    from tweepy.streaming import *
except:
    print "[+]ERROR: Unable to import the tweepy library installed!!"
    print "You will not be able to use the twitter collection side of oscar!"

#Twitter lib for AUTH
try:
    import twitter
    from twitter.oauth import write_token_file, read_token_file
    from twitter.oauth_dance import oauth_dance
except:
    print "[+]ERROR: Unable to import the twitter library installed!"
    print "You will not be able to use the twitter collection side of oscar!"


try:
    #Open file for twitter app auth
    tappfile = open('auth/'+'twitter_app.dat', 'r')
    tappline = tappfile.readlines()
    APP_NAME = tappline[1].rstrip()
    CONSUMER_KEY = tappline[3].rstrip()
    CONSUMER_SECRET = tappline[5].rstrip()
    tappfile.close()

    #file that Oauth data is stored
    TOKEN_FILE = 'auth/'+'token.txt'

    try:
        (oauth_token, oauth_token_secret) = read_token_file(TOKEN_FILE)
    except IOError, e:
        print "Please run the setup.py file to get your token file!"
        exit()

    t_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    t_auth.set_access_token(oauth_token, oauth_token_secret)
    t_api = tweepy.API(t_auth)
except:
    t_auth = None
    t_api = None

__author__ = "NinjaSl0th - @ninjasl0th"

def main():
    """Main Function"""
    time.sleep(3)
    try:
        os.system('clear')
    except Exception:
        os.system('cls')
    finally:
        asciis.asciiart()
    try:
        print """
        NoobSecToolkit(C.T.F Edition)(Open Source Collection And Recon) Framework
        (OSCARF by: NinjaSl0th )
        ----------------------------------
        (CTRL+C returns back to main menu)
        -------------
        1. Social Networking
        -------------
        2. Shodan (Not Working)
        -------------
        3. News
        -------------
        4. Network Info
        -------------
        5. Pastebin Scraper
        -------------
        6. Web Tools
        -------------

        0. Exit 
        """
        opt = raw_input("Enter an option: ")
        if opt == "1":
            socialMenu()
        elif opt == "2":
            oscrShodan()
            main()
        elif opt == "3":
            news()
        elif opt == "4":
            networkMod()
        elif opt == "5":
            pasteScrape()
        elif opt == "6":
            webtools()
            #wscrape()
        elif opt == "0":
            print "Thanks for using NoobSecToolkit (C.T.F Edition)!"
            sys.exit(0)
        else:
            print "Sorry you entered an invalid option!"
            main()
    except (KeyboardInterrupt):
        main()


###########################
#-- Social Media Menu   --#
###########################
def socialMenu():
    """Select Social Media Source"""

    print """
    1. Twitter (Not Working)
    2. FaceBook
    3. LinkedIn
    4. Check username on instagram
    0. Return
    """
    opt = raw_input("Enter an option: ")
    if opt == "1":
        twitMenu()
    elif opt == "2":
        fbMenu()
    elif opt == "3":
        linkedin()
    elif opt == "4":
        instachek()
    elif opt == "0":
        main()
    else:
        print "You entered an invalid choice!"
        socialMenu()


###########################
#-- Twitter Collection -- #
###########################


def twitMenu():
    """Menu for twitter"""
    if t_auth is None or t_api is None:
        print "Twitter is disabled; please install an API key for twitter"
        return
    oscrtwitter.mmenu()
    opt = raw_input("Enter an option: ")
    if opt == "1":
        oscrtwitter.lv_stream(t_auth)
    elif opt == "2":
        oscrtwitter.lv_streamno(t_auth)
    elif opt == "3":
        oscrtwitter.hist_tweet(t_api)
        twitMenu()
    elif opt == "4":
        oscrtwitter.rcntFllw(t_api)
        twitMenu()
    elif opt == "5":
        oscrtwitter.rcntFllwrs(t_api)
        twitMenu()
    elif opt == "6":
        oscrtwitter.mentionCount(t_api)
        twitMenu()
    elif opt == "7":
        oscrtwitter.twitSearch(t_api)
        twitMenu()
    elif opt == "8":
        oscrtwitter.twitlookup(t_api)
        twitMenu()
    elif opt == "9":
        oscrtwitter.batch_delete(t_api)
        twitMenu()
    elif opt == "10":
        oscrtwitter.favdelete(t_api)
        twitMenu()
    elif opt == "11":
        oscrtwitter.dm_batch(t_api)
        twitMenu()
    elif opt == "12":
        oscrtwitter.dm_sent(t_api)
        twitMenu()
    elif opt == "0":
        main()
    else:
        print "[+]ERROR: You entered an invalid option!"
        twitMenu()


########################
## --- FB Analysis -- ##
########################

def fbMenu():
    """Facebook Menu"""
    print """
    1. Get user info - Raw JSON Dump/Not Formatted
    2. Get user info - Formatted, Lookup multiple users
    0. Return
    """
    opt = raw_input("Enter an input: ")
    if opt == "1":
        fblookup.FBInfo()
        fbMenu()
    elif opt == "2":
        fblookup.FBUsr()
        fbMenu()
    elif opt == "0":
        main()
    else:
        print "You entered an invalid option"
        fbMenu()


def instachek():
    """Initiate Instagram username checker"""
    usernom = raw_input("Enter username: ")
    instag.checker(usernom)
    socialMenu()

#############################
#-- News Feed Integration --#
#############################


def news():
    """Launch the newsfeed reader"""
    newsfeed.newsStart()
    main()


###############
#-- IP Info --#
###############
def ipInfo():
    """IP Address lookup function"""
    ip = raw_input("Enter IP: ")
    ip = ip.rstrip()
    ipinfo.lookup(ip)
    networkMod()


def prtLook():
    """Function to call the portlookup lib"""
    portlook.lookup()
    networkMod()


def networkMod():
    """Function to choose what network lookup tool to use"""
    print """
    1. Lookup IP Address
    2. Port Lookup (SANS website)
    3. Domain to IP
    0. Return
    """
    opt = raw_input('Enter an option: ')
    if opt == "1":
        ipInfo()
    elif opt == "2":
        prtLook()
    elif opt == "3":
        domainip.c()
    elif opt == "0":
        main()
    else:
        print "Invalid option!"
        networkMod()
    networkMod()


######################
#- Pastebin Scraper -#
######################
def pasteScrape():
    """Initiate pastebin scraper"""
    try:
        pyscrape.starter()
    except KeyboardInterrupt:
        pyscrape.stopper()
        main()


def linkedin():
    """Start linkedin search tool"""
    linked.start()
    time.sleep(5)
    if linked.saveout:
        linked.dupr(linked.saveout)
    main()


def oscrShodan():
    """Call/launch the Shodan module"""
    oshodan.menu()
    main()


def wscrape():
    """Call/launch the web scraper module"""
    webscrape.scrape()
    main()

def getcn():
    sslscan.starter()

def webtools():
    """Menu for web tools"""
    print """
    1. Web Source Scraper
    2. SSL CN grabber

    0. Back
    """
    opt = raw_input("Enter an option: ")
    if opt == "1":
        wscrape()
    elif opt == "2":
        getcn()
    elif opt == "0":
        main()
    else:
        print "Invalid Option!"
        webtools()
    webtools()


if __name__ == "__main__":
    # users may wish to import part of this...
    main()
