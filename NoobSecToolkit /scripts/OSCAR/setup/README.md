OSCAR-F
=======

Python OSINT Platform

**OSCARf was coded/designed in Linux and Mac. Don't complain if you are running Windows and you cannot get it working**
Windows support is something that I am going to address at a later date.

OSCAR-F is designed to aid in the process of information gathering. It was formed with the idea of not having to open
so many tabs in a browser.

There are a few bugs in OSCAR-F, however, we are slowly working on crushing them and working on features.

## Installing

**All setup files are located within the setup directory!**

OSCAR uses a few libraries. These include:

- Twitter
- tweepy
- feedparser
- shodan
- readline
- pillow

These can be installed via pip: `pip install -r requirements.txt`

**Please note that you will need to setup ONE twitter app for you/your business.**

~**You will probably need to use sudo to run the setup script. This is becasue it creates files and directories.**~

The the readline feature is completely optional.

Please be sure to run the `DEPENDENCY_CHECK` script first! Additionally, as noted above,  dependencies can be installed via `pip install -r requirements.txt`

After running the dependency check, run the setup.py script. This will allow you to setup all necessary auth files/data.
**PLEASE NOTE THAT THE SETUP SCRIPT WILL NOT INSTALL MISSING LIBRARIES! Please use pip.**

## To setup Twitter Application

Navigate to: https://apps.twitter.com/ and setup a new application. Please note the name and keys associated with it. 
You sould only need to have a read only application!

## Shodan API KEY

Once you have a ShodanHQ account or login, go to: http://www.shodanhq.com/api_doc and copy the API key. Please note that if you want to use ALL of the shodan functionality of OSCAR, you will need to purchase an "Unlocked API" 

View API KEY: http://www.shodanhq.com/api_doc

You can purchase the "Unlocked API" addon here: http://www.shodanhq.com/data/addons

## To scrape pastebin

To scrape pastebin, add regex strings to /config/pSearch.dat located in the root directory. After this, proceed to use oscar.

## To edit rss filter options

Edit the keywords in /config/rssfilter.dat

## To add/remove rss feeds

Edit rss links in /config/rssfeeds.dat

## To scrape web source code

Edit regex info in /config/webscrape.dat in the root. The path will change soon. 
