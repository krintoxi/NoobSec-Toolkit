#!/usr/bin/env python3

print("This setup script will set up Twitter and Shodan API credentials.")

import os
from time import sleep
import sys

try:
    import twitter
    from twitter.oauth import write_token_file, read_token_file
    from twitter.oauth_dance import oauth_dance
except ImportError:
    print("[+] ERROR: Unable to import the twitter library!")
    print("Run: pip3 install twitter")
    sys.exit(1)


def setup():
    auth_dir = os.path.join(os.path.dirname(__file__), "..", "auth")
    auth_dir = os.path.normpath(auth_dir)
    if not os.path.exists(auth_dir):
        print("Adding the 'auth' directory.")
        try:
            os.makedirs(auth_dir, exist_ok=True)
            sleep(1)
        except Exception:
            sys.exit("Could not create auth directory. Try running as sudo!")
    twittersetup(auth_dir)
    shodansetup(auth_dir)


def twittersetup(auth_dir):
    app_dat = os.path.join(auth_dir, "twitter_app.dat")
    if not os.path.isfile(app_dat):
        try:
            with open(app_dat, "w") as appfile:
                appfile.write("#App name\n")
                appname = input("Enter twitter app name: ").strip()
                appfile.write(appname + "\n")
                appfile.write("#Consumer key\n")
                appconsumer = input("Enter twitter app consumer key: ").strip()
                appfile.write(appconsumer + "\n")
                appfile.write("#Consumer Secret\n")
                appsecret = input("Enter twitter app secret key: ").strip()
                appfile.write(appsecret + "\n")
        except Exception as e:
            print("There was an issue creating the twitter app auth data: " + str(e))
            sys.exit(1)

    try:
        with open(app_dat, "r") as tappfile:
            tappline = tappfile.readlines()
        APP_NAME = tappline[1].rstrip()
        CONSUMER_KEY = tappline[3].rstrip()
        CONSUMER_SECRET = tappline[5].rstrip()
    except Exception:
        sys.exit("Could not read app data file for twitter.")

    TOKEN_FILE = os.path.join(auth_dir, "token.txt")
    try:
        (oauth_token, oauth_token_secret) = read_token_file(TOKEN_FILE)
    except IOError as e:
        (oauth_token, oauth_token_secret) = oauth_dance(
            APP_NAME, CONSUMER_KEY, CONSUMER_SECRET
        )
        write_token_file(TOKEN_FILE, oauth_token, oauth_token_secret)


def shodansetup(auth_dir):
    shodan_key = os.path.join(auth_dir, "shodankey.txt")
    if os.path.isfile(shodan_key):
        print("Shodan auth is already present.")
        return
    key = input("Shodan API key: ").strip()
    with open(shodan_key, "w") as f:
        f.write("#Shodan API key\n")
        f.write(key + "\n")


setup()
