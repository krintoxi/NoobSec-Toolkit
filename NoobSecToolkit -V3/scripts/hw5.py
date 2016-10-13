# File:        hw5.py
# Written by:  Kyle Fritz
# Date:        10/10/2013
# Lab Section: 10
# UMBC email:  fritzk1@umbc.edu
# Description: This program will convert Decimal notation to either Binary
#  or Hexadecimal notation as well as Binary to Decimal.
############### USE WITH PYTHON 3 ###########
# scl enable python33 bash


def printgreeting():
    # input: No input
    # output: No output
    print("This program will convert values.")
    print("[A] - Convert from Decimal to Binary")
    print("[B] - Convert from Decimal to Hexadecimal")
    print("[C] - Convert from Binary to Decimal")
    print("[D] - Quit")


printgreeting()

def decToBin(numDB):
    # input: decimal number as a string
    # output: binary number as a string
    numDB = "a"
    numDB = str(input("What is your value: "))
    # This makes sure that the value is a number
    while numDB.isdigit() == False:
        numDB = str(input("Please type in a valid value: "))
    a = int(numDB)
    # This determines the correct binary form of the decimal
    if a/128 < 1:
        print("0", end = " ")
    else:
        print("1", end = " ")
    if a%128/64 < 1:
        print("0", end = " ")
    else:
        print("1", end = " ")
    if a%64/32 < 1:
        print("0", end = " ")
    else:
        print("1", end = " ")    
    if a%32/16 < 1:
        print("0", end = " ")
    else:
        print("1", end = " ")
    if a%16/8 < 1:
        print("0", end = " ")
    else:
        print("1", end = " ")
    if a%8/4 < 1:
        print("0", end = " ")
    else:
        print("1", end = " ")
    if a%4/2 < 1:
        print("0", end = " ")
    else:
        print("1", end = " ")
    if a%2/1 < 1:
        print("0", end = " ")
    else:
        print("1", end = " ")
    print("\n")
    
def decToHex(numDH):
    # input: decimal number as a string
    # output: hexadecimal number as a string
    numDH = "b"
    numDH = str(input("Type in your value: "))
    while numDH.isdigit() == False:
        numDH = str(input("Please type in a valid value: "))
    b = int(numDH)
    # This calculates the first number/letter of hexadecimal
    if b > 240:
        print("F", end = " ")
    elif b >= 224 and b < 240:
        print("E", end = " ")
    elif b >= 208 and b < 224:
        print("D", end = " ")    
    elif b >= 192 and b < 208:
        print("C", end = " ")
    elif b >= 176 and b < 192:
        print("B", end = " ")
    elif b >= 160 and b < 176:
        print("A", end = " ")
    elif b >= 144 and b < 160:
        print("9", end = " ")
    elif b >= 128 and b < 144:
        print("8", end = " ")
    elif b >= 112 and b < 128:
        print("7", end = " ")
    elif b >= 96 and b < 112:
        print("6", end = " ")    
    elif b >= 80 and b < 96:
        print("5", end = " ")
    elif b >= 64 and b < 80:
        print("4", end = " ")
    elif b >= 48 and b < 64:
        print("3", end = " ")
    elif b >= 32 and b < 48:
        print("2", end = " ")
    elif b >= 16 and b < 32:
        print("1", end = " ")
    else:
        print("0", end = " ")
    # This calculates the second number/letter of hexadecimal
    if b%16 != 0:
        if b%16 == 1:
            print("1")
        elif b%16 == 2:
            print("2")
        elif b%16 == 3:
            print("3")
        elif b%16 == 4:
            print("4")
        elif b%16 == 5:
            print("5")
        elif b%16 == 6:
            print("6")
        elif b%16 == 7:
            print("7")
        elif b%16 == 8:
            print("8")
        elif b%16 == 9:
            print("9")
        elif b%16 == 10:
            print("A")
        elif b%16 == 11:
            print("B")    
        elif b%16 == 12:
            print("C")
        elif b%16 == 13:
            print("D")
        elif b%16 == 14:
            print("E")
        elif b%16 == 15:
            print("F")
    else:
        print("0")

def binToDec(numBD):
    # input: binary number as a string
    # output: decimal number as a string
    numBD = -1
    ans = 0
    nums = 0
    numBD = str(input("What is your 8 digit value: "))
    nums = list(numBD)
    while "0" not in nums and "1" not in nums or len(numBD) != len("aaaaaaaa"):
         numBD = str(input("Must be a valid 8 digit value in binary form: "))
    if numBD[0] == "1":
        ans = 128
    if numBD[1] == "1":
        ans = ans + 64
    if numBD[2] == "1":
        ans = ans + 32
    if numBD[3] == "1":
            ans = ans + 16
    if numBD[4] == "1":
        ans = ans + 8
    if numBD[5] == "1":
        ans = ans + 4
    if numBD[6] == "1":
        ans = ans + 2
    if numBD[7] == "1":
        ans = ans + 1
    print("Your number in decimal form is", ans)

def main():
    # input: Choice of what function to perform
    # output: Take user to that function
    Choice = str(input("What is your choice?  "))
    A = 0
    B = 0
    C = 0
    D = 0
    l1 = "ABCD"
    # This makes sure that the user types in "A", "B", "C", or "D"
    while Choice.upper() not in l1 or len(Choice.upper()) > len("h"):
        Choice = str(input("Invalid option, try again: "))
    if Choice.upper() == "A":
        A = decToBin(A)
    elif Choice.upper() == "B":
        B = decToHex(B)
    elif Choice.upper() == "C":
        C = binToDec(C)
    elif Choice.upper() == "D":
        print()

main()
