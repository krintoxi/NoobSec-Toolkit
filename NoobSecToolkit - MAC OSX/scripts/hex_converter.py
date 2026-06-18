#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        hex encoder and decoder
# Purpose:     A small tool created to assist in SQL Injection testing
#              and to learn hex encoding/decoding.
# Notice:      Updated to Python 3
# Original:    Coded in Python 2.7 by <4sec>, <PTT> 2013
# Version:     v2.0
#-------------------------------------------------------------------------------

import os
import sys
import binascii
from time import sleep


def clear_screen():
    if sys.platform in ("win32", "win"):
        os.system("cls")
    else:
        os.system("clear")


def banner():
    print("\n\n")
    print("+=======================================================================+")
    print("                    Hex Encoder and Decoder")
    print("+=======================================================================+")
    print()


def bye():
    clear_screen()
    print()
    print("+=================================================+")
    print("       NoobSec Toolkit - Hex Converter")
    print("+=================================================+")
    sleep(1)
    sys.exit()


def hex_convert(x, y):
    if y == "e":
        encoded = binascii.hexlify(x.encode("utf-8")).decode("utf-8")
        enc_hex = "0x" + encoded
        print()
        print("+" + "=" * 78 + "+")
        print("Plaintext : " + x)
        print("+" + "=" * 78 + "+")
        print("Hex Value : " + enc_hex)
        print("+" + "=" * 78 + "+")
        sleep(2)
        print("\n")
        choice()
    elif y == "d":
        try:
            hex_str = x
            if hex_str.startswith("0x") or hex_str.startswith("0X"):
                hex_str = hex_str[2:]
            dec_hex = binascii.unhexlify(hex_str).decode("utf-8", errors="replace")
            print()
            print("+" + "=" * 78 + "+")
            print("Hex Value : " + x)
            print("+" + "=" * 78 + "+")
            print("Plaintext : " + dec_hex)
            print("+" + "=" * 78 + "+")
            sleep(2)
            print("\n")
            choice()
        except (binascii.Error, ValueError) as e:
            print("Error decoding hex: " + str(e))
            choice()


def choice():
    print("\t  1. String to Hex")
    print("\t  2. Hex to String")
    print("\n\t  0. Exit")

    try:
        usr_input = int(input("\n # : ").strip())
    except ValueError:
        print("Invalid choice!")
        choice()
        return

    if usr_input == 1:
        clear_screen()
        print("\nEnter string: ")
        string = input(" : ").strip()
        hex_convert(string, "e")
    elif usr_input == 2:
        clear_screen()
        print("\nEnter hex value: ")
        hex_val = input(" : ").strip()
        hex_convert(hex_val, "d")
    elif usr_input == 0:
        bye()
    else:
        print("Invalid choice!")
        choice()


def main():
    banner()
    choice()


main()
