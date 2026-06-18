#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  NumberConverter.py by ZenOokami
#
#  Copyright 2015 Essence Of Zen
#  www.EssenceOfZen.org
#  Updated to Python 3

version = "0.4.0"
dev_team = ["ZenOokami"]
last_updated = "2024"


def decimalBinaryMenu():
    switch = True
    while switch:
        try:
            number = int(input("Please input a decimal number to convert: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        decimalToBinaryConvert(number)
        print()
        while True:
            user_response = input("Convert again? (yes/no): ").strip().lower()
            if user_response in ("yes", "y"):
                break
            elif user_response in ("no", "n"):
                switch = False
                break
            else:
                print("Invalid response. Please enter yes or no.")


def decimalToBinaryConvert(number):
    binary_list = []
    original_number = number
    while number > 0:
        binary_list.append(number % 2)
        number //= 2
    print("The Binary form for " + str(original_number) + " is: ")
    final_binary = binary_list[::-1]
    print(final_binary)
    return final_binary


def binaryDecimalMenu():
    switch = True
    while switch:
        number = input("Please input a binary number to convert: ").strip()
        if not all(c in "01" for c in number):
            print("Invalid binary number. Use only 0 and 1.")
            continue
        binary = [int(c) for c in number]
        print("Binary number is: " + str(binary))
        print()
        decimal = binaryToDecimal(binary)
        print("Decimal number is: " + str(decimal))
        print()
        while True:
            user_response = input("Convert again? (yes/no): ").strip().lower()
            if user_response in ("yes", "y"):
                break
            elif user_response in ("no", "n"):
                switch = False
                break
            else:
                print("Invalid response, try again.")


def binaryToDecimal(array):
    decimal = 0
    power = len(array) - 1
    for item in array:
        decimal += (2 ** power) * item
        power -= 1
    return decimal


def main():
    print("Welcome to the Number Converter!")
    switch = True
    while switch:
        print("0.) Quit | 1.) Decimal to Binary | 2.) Binary to Decimal")
        print()
        try:
            user_choice = int(input("Please choose option: ").strip())
        except ValueError:
            print("Invalid input, try again.")
            continue

        if user_choice == 1:
            decimalBinaryMenu()
        elif user_choice == 2:
            binaryDecimalMenu()
        elif user_choice == 0:
            switch = False
        else:
            print("Invalid input, try again.")

    print("Thank you for using the Number Converter!")
    print("Version: " + str(version))
    print("Last Update: " + last_updated)


main()
