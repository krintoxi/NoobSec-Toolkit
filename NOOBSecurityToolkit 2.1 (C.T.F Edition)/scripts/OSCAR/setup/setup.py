#!/usr/bin/env python

print "This setup script will have you setup twitter and shodan."

import os
from time import sleep
import sys

try:
    import twitter
    from twitter.oauth import write_token_file, read_token_file
    from twitter.oauth_dance import oauth_dance
except:
    print "[+]ERROR: Unable to import the twitter library!",
    print "Run Dependency Check!!"
    exit()

def setup():
    if not os.path.exists("../auth"):
        print "Adding the 'auth' directory."
        try:
            os.mkdir("../auth")
            sleep(2)
            twittersetup()
            shodansetup()
        except:
            exit("run as sudo!")
    elif os.path.exists("../auth"):
        twittersetup()
        shodansetup()
    else:
        exit("Could not proceed with setup! Try running as sudo!")
        

def twittersetup():
    if not os.path.isfile('../auth/twitter_app.dat'):
        try:
            appfile = open('../auth/twitter_app.dat', 'w')
            appfile.write("#App name\n")
            appname = raw_input("Enter twitter app name: ")
            appfile.write(appname+'\n')
            appfile.write("#Consumer key\n")
            appconsumer = raw_input("Enter twitter app consumer key: ")
            appfile.write(appconsumer+'\n')
            appfile.write("#Consumer Secret\n")
            appsecret = raw_input("Enter twitter app secret key: ")
            appfile.write(appsecret+'\n')
        except:
            appfile.close()
            print "There was an issue creating the twitter app auth data!!"
            exit()
        finally:
            appfile.flush()
            os.fsync(appfile)
            appfile.close()
    try:
        tappfile = open('../auth/'+'twitter_app.dat', 'r')
        tappline = tappfile.readlines()
        APP_NAME = tappline[1].rstrip()
        CONSUMER_KEY = tappline[3].rstrip()
        CONSUMER_SECRET = tappline[5].rstrip()
        tappfile.close()
    except:
        exit("Could not read app data file for twitter")

    #file that Oauth data is stored
    TOKEN_FILE = '../auth/'+'token.txt'
    try:
        (oauth_token, oauth_token_secret) = read_token_file(TOKEN_FILE)
    except IOError, e:
        (oauth_token, oauth_token_secret) = oauth_dance(
            APP_NAME, CONSUMER_KEY, CONSUMER_SECRET)
        print e.errno
        print e
        write_token_file(TOKEN_FILE, oauth_token, oauth_token_secret)
    return

def shodansetup():
    if os.path.isfile('../auth/shodankey.txt'):
        exit('Shodan auth is already present!')
    else:
        f = open('../auth/'+'shodankey.txt', 'w')
        key = raw_input('Shodan API key: ')
        f.write('#Shodan API key\n')
        f.write(key+'\n')
        f.close()
    return
        
setup()