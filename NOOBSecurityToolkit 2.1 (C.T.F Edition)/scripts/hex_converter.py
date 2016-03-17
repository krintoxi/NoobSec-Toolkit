#-------------------------------------------------------------------------------
# Name:        hex encoder, and decoder
# Purpose:     A small tool created to assisit in <<SQL INJECTION>>
#              And of course, for us to learn together.
# Notice:      Coded in python 2.7
# Author:      <4sec>, <PTT>
# Created:     23/05/2013
# Copyright:   (c) <4sec> <PTT> 2013
# Licence:     <Opensource GNU>
# Version:     v1.21
# What's new:  Removed function to find your ip address
# Love To:     MHU NullByte,Xero MHU,Master Leet,Little MHU,Tayalma MHU,
#              3zero MHU,Dongoth, and all Python Think Tank members
#-------------------------------------------------------------------------------

import os
import sys
from time import sleep

def clear_screen():
    if sys.platform == 'win32' or sys.platform == 'win':
        os.system('cls')
    elif sys.platform == 'linux' or sys.platform == 'linux2':
        os.system('clear')

def banner():
    print('\n\n\n\n\n\n')
    print'''
    +=======================================================================+
   			 	Hex encoder and decoder!

    '''


def bye():
    clear_screen()
    print'''
    

    
    +=================================================+
      	   Noob Security Toolkit C.T.F Edition
    +=================================================+
    
    '''
    sleep(2)
    sys.exit()

def hex_convert(x,y):
    if y == 'e':
        enc_hex = '0x' + x.encode('hex')
        print''
        print'+' + '='*78 + '+'
        print'Plaintext : ',x
        print'+' + '='*78 + '+'
        print'Hex Value : ', enc_hex
        print'+' + '='*78 + '+'
        sleep(3)
        print'\n\n\n'
        choice()
    elif y == 'd':
        if x[0] == '0' and x[1] == 'x':
            plain_hex = x.replace('0x','') # This is the part making error in version 1.
            # With a small trick.. No error anymore.!!
            dec_hex = plain_hex.decode('hex')
        else:
            dec_hex = x.decode('hex')
        print''
        print'+' + '='*78 + '+'
        print'Hex Value : ',x
        print'+' + '='*78 + '+'
        print'Plaintext : ', dec_hex
        print'+' + '='*78 + '+'
        sleep(3)
        print'\n\n\n'
        choice()


def choice():
    print"\t  1. String to Hex"
    print"\t  2. Hex to string"
    print"\n\n\n\t  0. exit"

    usr_input = input('\n # : ')
    if usr_input == 1:
       clear_screen()
       print'\n\nEnter string '
       string = raw_input(" : ")
       hex_convert(string,'e')
    elif usr_input == 2:
         clear_screen()
         print'\nEnter hex '
         hex = raw_input(" : ")
         hex_convert(hex,'d')
    elif usr_input == 0:
         bye()
    else:
        print'Invalid choice!'
        main()

def main():
    banner()
    choice()

main()



