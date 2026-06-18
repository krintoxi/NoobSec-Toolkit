#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess


def main():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        wordlistname = sys.argv[2]
    else:
        print("Usage: steghidecracker.py [stegfile] [wordlist]")
        sys.exit(1)

    if not os.path.exists(filename):
        print("Error: Steg file not found: " + filename)
        sys.exit(1)

    if not os.path.exists(wordlistname):
        print("Error: Wordlist file not found: " + wordlistname)
        sys.exit(1)

    with open(wordlistname, "r", errors="ignore") as f:
        wordlist = f.readlines()

    length = len(wordlist)
    print("Loaded %d passwords from wordlist." % length)
    print("Starting steghide crack on: " + filename)
    print()

    for i, line in enumerate(wordlist):
        password = line.strip()
        remaining = length - (i + 1)
        try:
            result = subprocess.run(
                ["steghide", "extract", "-sf", filename, "-p", password, "-f"],
                capture_output=True,
                text=True
            )
            output = result.stdout + result.stderr
            if "could not extract" not in output.lower() and result.returncode == 0:
                print("PASSWORD FOUND! => " + password)
                print(output)
                return
            else:
                print("[%d remaining] Tried: %s" % (remaining, password))
        except FileNotFoundError:
            print("Error: steghide is not installed. Install it with: sudo apt-get install steghide")
            sys.exit(1)
        except Exception as e:
            print("Error: " + str(e))

    print("Password not found in wordlist.")


if __name__ == "__main__":
    main()
