#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import time
import threading

try:
    from bs4 import BeautifulSoup as bsoup
except ImportError:
    bsoup = None
    print("[+] ERROR: beautifulsoup4 not installed. Run: pip3 install beautifulsoup4")

try:
    import mechanize
except ImportError:
    mechanize = None
    print("[+] ERROR: mechanize not installed. Run: pip3 install mechanize")

try:
    from http import cookiejar as cookielib
except ImportError:
    cookielib = None

saveout = False


def start():
    pos = input("Enter position: ").strip().lower()
    com = input("Enter company: ").strip().lower()
    useout = input("Save output? [y/n]: ").strip().lower()
    global saveout
    saveout = useout == "y"
    bing(pos, com, saveout)


def csvwrite(p1, c1, plink):
    with open("OUTPUT.csv", "a", encoding="utf-8", newline="") as saveFile:
        saveFile.write(p1 + "+" + c1 + "+" + plink + "\n")


def bing(pos, com, saveout):
    if mechanize is None or bsoup is None or cookielib is None:
        print("[+] ERROR: Missing dependencies (mechanize, beautifulsoup4).")
        return

    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [("User-agent",
                      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) "
                      "AppleWebKit/537.17 (KHTML, like Gecko) "
                      "Chrome/24.0.1309.1 Safari/537.17")]

    burl = "http://www.bing.com/search?q=site:linkedin.com " + '"' + pos + '" "' + com + '"'
    r = br.open(burl.replace(" ", "%20"))
    html = r.read()
    soup = bsoup(html, "html.parser")

    result = (soup.find_all("li", {"class": "b_algo"})
              or soup.find_all("div", {"class": "sb_tlst"}))

    refs = []
    for i in result:
        try:
            link = i.a["href"]
            if "/dir/" in link or "groupItem" in link or "linkedin.com" not in link:
                continue
            refs.append(link)
        except Exception:
            pass

    nodupLinks = set(refs)
    comp = [com]

    for links in nodupLinks:
        try:
            r = br.open(links)
            html = r.read()
            soup = bsoup(html, "html.parser")

            result_name = soup.find("title")
            result_name = result_name.string.strip().split(" | ")

            result_title = (
                soup.find("p", {"class": "headline-title title"})
                or soup.find("ul", {"class": "current"})
                or soup.find("p", {"class": "title"})
            )

            try:
                if comp[0] not in result_title.string.lower():
                    continue

                print()
                print("-----------START--------------")
                print(result_name[0], result_title.string)
                print(links)
                print("------------END---------------")
                print()

                if saveout:
                    restitle = result_title.string.strip("\n")
                    resnom = result_name[0]
                    t = threading.Thread(target=csvwrite, args=(resnom, restitle, links), daemon=True)
                    t.start()
            except Exception:
                pass
        except Exception:
            pass
        time.sleep(2)

    refs = []
    comp = []

    print("""
    End of results...
    1. Search again
    0. Return
    """)
    retCheck = input("Choose an option: ").strip()
    if retCheck == "1":
        start()


def dupr(saveout):
    try:
        with open("OUTPUT.csv", "r", encoding="utf-8", newline="") as f_in, \
             open("LINKEDIN_OUT.csv", "w", encoding="utf-8", newline="") as f_out:
            f1 = csv.reader(f_in, delimiter="+")
            f2 = csv.writer(f_out, delimiter="+")
            links = set()
            for row in f1:
                if len(row) > 2 and row[2] not in links:
                    f2.writerow(row)
                    links.add(row[2])
    except FileNotFoundError:
        pass
