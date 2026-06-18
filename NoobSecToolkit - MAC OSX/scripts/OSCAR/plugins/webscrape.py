#!/usr/bin/env python3
import urllib.request
import urllib.error
import re

try:
    import readline
except ImportError:
    pass

import sys


def scrape():
    site = input("Enter page URL: ").strip()
    try:
        data = urllib.request.urlopen(site, timeout=10).read().decode("utf-8", errors="ignore")
    except ValueError:
        print("INVALID URL: Be sure to include protocol (e.g. http://)")
        return
    except urllib.error.URLError as e:
        print("Could not connect: " + str(e))
        return

    try:
        patternFile = open("config/webscrape.dat", "r").read().splitlines()
    except FileNotFoundError:
        print("Error opening config/webscrape.dat")
        return

    counter = 0
    for pattern in patternFile:
        m = re.findall(pattern, data)
        if m:
            with open("scrape-RESULTS.txt", "a", encoding="utf-8") as outfile:
                for i in m:
                    outfile.write(str(i) + "\n")
                    counter += 1
                    print("Scrape item %d successful. Data output to scrape-RESULTS.txt." % counter)
        else:
            counter += 1
            print("No match for item %d. Continuing." % counter)
            continue
