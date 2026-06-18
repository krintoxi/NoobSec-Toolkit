#!/usr/bin/env python3
"""Module to check if a username returns a valid instagram user."""
import urllib.request
import urllib.error


def checker(usernom):
    """Check username against Instagram."""
    inst = "https://www.instagram.com/" + usernom + "/"
    try:
        urllib.request.urlopen(inst, timeout=10)
        valid = True
    except urllib.error.HTTPError as e:
        valid = e.code != 404
    except Exception:
        valid = False

    if valid:
        print()
        print("---------")
        print("Found " + usernom + " on Instagram!")
        print("Profile link: https://www.instagram.com/" + usernom + "/")
        print("---------\n")
    else:
        print("Username '" + usernom + "' not found on Instagram.")
