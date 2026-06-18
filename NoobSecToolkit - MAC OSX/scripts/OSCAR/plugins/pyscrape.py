#!/usr/bin/env python3
import urllib.request
import urllib.error
import re
import threading
import time
import sys
import os
import datetime

try:
    import readline
except ImportError:
    pass


def downloader(url, filename):
    try:
        patternFile = open("config/pSearch.dat", "r").read().splitlines()
    except FileNotFoundError:
        return

    data = ""
    try:
        data = urllib.request.urlopen(url, timeout=10).read().decode("utf-8", errors="ignore")
    except Exception:
        return

    for pattern in patternFile:
        m = re.findall("'" + pattern + "'", data)
        if m:
            print()
            print("Found Match")
            print("Expr: " + pattern)
            print()
            stime = str(time.ctime()).replace(":", "-").replace(" ", "_")
            os.makedirs("pastebin/downloaded", exist_ok=True)
            hardFile = "pastebin/downloaded/{0}-{1}.txt".format(filename, stime)
            with open(hardFile, "w", encoding="utf-8") as f:
                f.write(data)


def starter():
    os.makedirs("pastebin/downloaded", exist_ok=True)
    if not os.path.exists("pastebin/seen-pastes.txt"):
        open("pastebin/seen-pastes.txt", "w").close()

    print("Scraping for pastes...\n")
    while True:
        try:
            time.sleep(1)
            data = urllib.request.urlopen(
                "https://pastebin.com/archive", timeout=10
            ).read().decode("utf-8", errors="ignore")

            data = data.split('<table class="maintable" cellspacing="0">')
            if len(data) < 2:
                continue
            data = data[1].split("</table>")[0]
            data = data.replace(
                '<td><img src="/i/t.gif"  class="i_p0" alt="" border="0" /><a href="/',
                "!!HTML!!"
            )
            data = data.replace("</a>", "!!HTML!!")
            data = data.split("!!HTML!!")

            for i in data:
                i = i.split('">')[0]
                if not (("</td>" in i) or ("<tr class=" in i)):
                    with open("pastebin/seen-pastes.txt", "r") as seenf:
                        seen_list = seenf.read().splitlines()
                    if i not in seen_list:
                        sys.stdout.write("\rCurrently on paste: %s" % i)
                        sys.stdout.flush()
                        with open("pastebin/seen-pastes.txt", "a") as seenf2:
                            seenf2.write(i + "\n")
                        i2 = i
                        paste_url = "https://pastebin.com/raw/" + i
                        t = threading.Thread(target=downloader, args=(paste_url, i2), daemon=True)
                        t.start()
                        time.sleep(4)
        except KeyboardInterrupt:
            print("\nStopping scraper...")
            return
        except Exception:
            pass


def stopper():
    pass
