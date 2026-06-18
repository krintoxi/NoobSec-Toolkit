#!/usr/bin/env python3
"""Python script to aid in the collection of OSINT data"""

"""
____   ________________   ________
\   \ /   /_   \_____  \  \_____  \ ______  ______
 \   Y   / |   |/  ____/   /   |   \\____ \/  ___/
  \     /  |   /       \  /    |    \  |_> >___ \\
   \___/   |___\_______ \ \_______  /   __/____  >
                       \/         \/|__|       \/
v12 operations
NoobSecToolkit (C.T.F Edition)
"""

# External libraries needed:
# tweepy, twitter, feedparser, shodan, readline, beautifulsoup4

import urllib.request
import sys
import os
import time

try:
    import readline
except ImportError:
    pass
try:
    import pyreadline
except ImportError:
    pass

if "nt" in os.name:
    print("Windows Support is in alpha! Proceed with caution!")
    time.sleep(3)

#################
# LOCAL IMPORTS #
#################
from plugins import *

try:
    import tweepy
    from tweepy.streaming import *
except ImportError:
    print("[+] WARNING: tweepy not installed. Twitter features disabled.")
    print("    Install with: pip3 install tweepy")

try:
    import twitter
    from twitter.oauth import write_token_file, read_token_file
    from twitter.oauth_dance import oauth_dance
except ImportError:
    print("[+] WARNING: twitter library not installed. Twitter auth features disabled.")
    print("    Install with: pip3 install twitter")

t_auth = None
t_api = None

try:
    tappfile = open("auth/twitter_app.dat", "r")
    tappline = tappfile.readlines()
    APP_NAME = tappline[1].rstrip()
    CONSUMER_KEY = tappline[3].rstrip()
    CONSUMER_SECRET = tappline[5].rstrip()
    tappfile.close()

    TOKEN_FILE = "auth/token.txt"

    try:
        (oauth_token, oauth_token_secret) = read_token_file(TOKEN_FILE)
    except IOError as e:
        print("Please run the setup.py file to get your token file!")
        oauth_token = None
        oauth_token_secret = None

    if oauth_token:
        t_auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        t_auth.set_access_token(oauth_token, oauth_token_secret)
        t_api = tweepy.API(t_auth)
except Exception:
    t_auth = None
    t_api = None

__author__ = "NinjaSl0th - @ninjasl0th"


def main():
    """Main Function"""
    time.sleep(1)
    try:
        os.system("clear")
    except Exception:
        os.system("cls")
    finally:
        asciis.asciiart()

    try:
        print("""
        NoobSecToolkit (Open Source Collection And Recon) Framework
        (OSCARF by: NinjaSl0th)
        ----------------------------------
        (CTRL+C returns back to main menu)
        -------------
        1. Social Networking
        -------------
        2. Shodan (Needs API Key)
        -------------
        3. Network Info
        -------------
        4. Pastebin Scraper
        -------------
        0. Exit
        """)
        opt = input("Enter an option: ").strip()
        if opt == "1":
            socialMenu()
        elif opt == "2":
            oscrShodan()
            main()
        elif opt == "3":
            networkMod()
        elif opt == "4":
            pasteScrape()
        elif opt == "0":
            print("Thanks for using NoobSecToolkit!")
            sys.exit(0)
        else:
            print("Invalid option!")
            main()
    except KeyboardInterrupt:
        main()


def socialMenu():
    """Select Social Media Source"""
    print("""
    1. Check username on Instagram
    0. Return
    """)
    opt = input("Enter an option: ").strip()
    if opt == "1":
        instachek()
    elif opt == "0":
        main()
    else:
        print("Invalid choice!")
        socialMenu()


def twitMenu():
    """Menu for twitter"""
    if t_auth is None or t_api is None:
        print("Twitter is disabled; please install an API key for twitter.")
        return
    oscrtwitter.mmenu()
    opt = input("Enter an option: ").strip()
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
        print("[+] ERROR: Invalid option!")
        twitMenu()


def fbMenu():
    """Facebook Menu"""
    print("""
    1. Get user info - Raw JSON Dump
    2. Get user info - Formatted, Lookup multiple users
    0. Return
    """)
    opt = input("Enter an option: ").strip()
    if opt == "1":
        fblookup.FBInfo()
        fbMenu()
    elif opt == "2":
        fblookup.FBUsr()
        fbMenu()
    elif opt == "0":
        main()
    else:
        print("Invalid option.")
        fbMenu()


def instachek():
    """Initiate Instagram username checker"""
    usernom = input("Enter username: ").strip()
    instag.checker(usernom)
    socialMenu()


def news():
    """Launch the newsfeed reader"""
    newsfeed.newsStart()
    main()


def ipInfo():
    """IP Address lookup function"""
    ip = input("Enter IP: ").strip()
    ipinfo.lookup(ip)
    networkMod()


def prtLook():
    """Function to call the portlookup lib"""
    portlook.lookup()
    networkMod()


def networkMod():
    """Function to choose what network lookup tool to use"""
    print("""
    1. Lookup IP Address
    2. Port Lookup
    3. Domain to IP
    0. Return
    """)
    opt = input("Enter an option: ").strip()
    if opt == "1":
        ipInfo()
    elif opt == "2":
        prtLook()
    elif opt == "3":
        domainip.c()
        networkMod()
    elif opt == "0":
        main()
    else:
        print("Invalid option!")
        networkMod()


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
    print("""
    1. Web Source Scraper
    2. SSL CN Grabber
    0. Back
    """)
    opt = input("Enter an option: ").strip()
    if opt == "1":
        wscrape()
    elif opt == "2":
        getcn()
        webtools()
    elif opt == "0":
        main()
    else:
        print("Invalid Option!")
        webtools()


if __name__ == "__main__":
    main()
