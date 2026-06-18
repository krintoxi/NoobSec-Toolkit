#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import urllib.parse
import os
import threading
from time import sleep

try:
    import requests
except ImportError:
    requests = None

try:
    from PIL import Image
    PIL_available = True
except ImportError:
    PIL_available = False
    print("PIL/Pillow module is not installed. Run: pip3 install pillow")


def instacheck(usernom):
    inst = "https://www.instagram.com/" + usernom + "/"
    try:
        urllib.request.urlopen(inst, timeout=10)
        valid = True
    except urllib.error.HTTPError:
        valid = False
    except Exception:
        valid = False

    if valid:
        print()
        print("---------")
        print("Found " + usernom + " on Instagram too!")
        print("Profile link: https://www.instagram.com/" + usernom + "/")
        print("---------\n")


def downloader(a):
    os.makedirs("FBpics", exist_ok=True)
    data = "https://graph.facebook.com/" + a + "/picture?type=large"
    try:
        pic = urllib.request.urlopen(data, timeout=10)
        with open("FBpics/" + a + ".jpg", "wb") as f:
            f.write(pic.read())
        sleep(1)
    except Exception as e:
        print("Error downloading profile picture: " + str(e))


def FBInfo():
    if requests is None:
        print("requests library not installed. Run: pip3 install requests")
        return
    FBurl = "https://graph.facebook.com/"
    print("Please enter the username or ID of the target")
    print("EX: bobsmith3")
    userName = input(": ").strip()
    fullURL = FBurl + userName
    try:
        data = requests.get(fullURL, timeout=10)
        print(data.json())
        print()
    except Exception:
        pass


def FBUsr():
    if requests is None:
        print("requests library not installed. Run: pip3 install requests")
        return
    FBurl = "https://graph.facebook.com/"
    peopleInput = input("How many people would you like to lookup?: ").strip()
    people = 0
    myCounter = 1

    try:
        people = int(peopleInput)
    except ValueError:
        print("INVALID INPUT: Enter a number...")
        return

    while myCounter <= people:
        print()
        print("Please enter the username of the person - type 'exit!' to quit")
        print("EX: bobsmith3")
        userName = input(": ").strip()
        fullURL = FBurl + userName

        if userName == "exit!":
            return

        try:
            data = requests.get(fullURL, timeout=10)
            res = data.json()
            print("\n\n")

            try:
                fblink1 = "https://facebook.com/" + res.get("id", "")
                req = requests.get(fblink1, timeout=10)
                cookieref = req.cookies.get("reg_fb_ref", "")
                f_link = urllib.parse.unquote(cookieref) if cookieref else fblink1
            except Exception:
                f_link = "https://facebook.com/" + res.get("id", "")

            gender = res.get("gender", "")
            locale = res.get("locale", "")

            print("---------------Results-------------------")
            print(res.get("id", ""), "\n", res.get("name", ""), "\n",
                  gender, "\n", locale, "\n", f_link, "\n")
            print("---------------Results-------------------\n")

            a = res.get("id", "")
            if a:
                dlprof = input("Download Profile Picture? [y/n]: ").strip().lower()
                if dlprof == "y":
                    t = threading.Thread(target=downloader, args=(a,), daemon=True)
                    t.start()
                    t.join()
                    view = input("View downloaded image? [y/n]: ").strip().lower()
                    if view == "y" and PIL_available:
                        try:
                            img = Image.open("FBpics/" + a + ".jpg")
                            img.show()
                        except Exception:
                            print("There was an error opening the file.")

            usernom = res.get("username", "")
            if usernom:
                instacheck(usernom)

            myCounter += 1
            sleep(2)
        except Exception:
            pass
