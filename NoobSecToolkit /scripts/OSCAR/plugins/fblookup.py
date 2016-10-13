#!/usr/bin/python
# -*- coding: utf-8 -*-

#import json
import urllib2
import urllib
import os
import thread
from time import sleep
import requests

# PIL is used to open/process images with python

try:
    from PIL import Image
except:
    print 'PIL/Pillow module is not installed'
    print 'sudo pip install pillow'


# instagram lookup gunction. Very basic for now.

def instacheck(usernom):

  # use username from FB profile and try it against instagram

    inst = 'http://instagram.com/' + usernom
    try:
        data = urllib2.urlopen(inst)
        valid = 1
    except urllib2.HTTPError:

  # If we get a 404/not found, then set valid to 0

        valid = 0
    if valid:
        print
        print '---------'
        print 'Found ' + usernom + ' on instagram too!'
        print 'Profile link: http://instagram.com/' + usernom
        print '---------\n'
    elif not valid:
        pass


# download FB profile as a function being called via new thread.

def downloader(a):
    if not os.path.exists('FBpics'):
        os.mkdir('FBpics')

  # full url for FB image

    data = 'https://graph.facebook.com/' + a + '/picture?type=large'

  # open the image using urllib

    pic = urllib.urlopen(data)

  # open and write bytes as a jpg. Save image as the user id + .jpg

    f = open('FBpics/' + a + '.jpg', 'wb')
    f.write(pic.read())
    f.close()
    sleep(1)


def FBInfo():
    FBurl = 'https://graph.facebook.com/'
    print 'Please enter the username or ID of the target'
    print 'EX: bobsmith3'
    userName = raw_input(': ')

  # construct full url for graph lookup

    fullURL = FBurl + userName
    try:
        #data = urllib2.urlopen(fullURL)
        data = requests.get(fullURL)
        #jsonResponse = json.load(data)
        #print jsonResponse
        print data.json()
        print '\n'
    except:

        pass
    return


def FBUsr():
    FBurl = 'https://graph.facebook.com/'
    peopleInput = raw_input('How many people would you like to lookup?: ')
    people = 0 # set to 0 to skip if user input is invalid
    myCounter = 1

    # validate user input
    try:
        people = int(peopleInput)
    except ValueError:
        print "INVALID INPUT: Enter a number..."

    while myCounter <= people:
        print '\n'
        print 'Please enter the username of the person - type ''exit!'' to quit'
        print 'EX: bobsmith3'
        userName = raw_input(': ')
        fullURL = FBurl + userName

        # bail out early if the user chooses to exit
        if userName == "exit!":
            return

        try:
            try:
                #data = urllib2.urlopen(fullURL)
                data = requests.get(fullURL)
            #except urllib2.HTTPError:
            except:
                print 'There was an error connecting to Facebook!'
                return

      # load the JSON response from FB

            #jsonResponse = json.load(data)
            res = data.json()
            print '\n', '\n', '\n'

      # Try and set the f_link var to the link section of json data..
      # If not found, then the link will just be something null or
      # a message

            try:
                #f_link = jsonResponse['link']
                #fblink1 = 'https://facebook.com/' + jsonResponse['id']
                fblink1 = 'https://facebook.com/' + res['id']
                req = requests.get(fblink1)
                cookieref = req.cookies['reg_fb_ref']
                decoded = urllib.unquote(cookieref)
                f_link = decoded
            except:

        # can still generate link, just will not get username.

                #f_link = 'https://facebook.com/' + jsonResponse['id']
                f_link = 'https://facebook.com/' + res['id']

            try:
                #gender = jsonResponse['gender']
                #locale = jsonResponse['locale']
                gender = res['gender']
                locale = res['locale']
            except:
                gender = ""
                locale = ""
            print '---------------Results-------------------'
            #print jsonResponse['id'], '\n', jsonResponse['name'], '\n', \
                #gender, '\n', locale, \
                #'\n', f_link, '\n'
            print res['id'], '\n', res['name'], '\n', \
                gender, '\n', locale, \
                '\n', f_link, '\n'
            print '---------------Results-------------------\n'
            #a = jsonResponse['id']
            a = res['id']
            dlprof = raw_input('Download Profile Picture?[y/n]: ')
            if dlprof == 'y' or dlprof == 'Y':

        # start a thread to download the image

                thread.start_new_thread(downloader, (a, ))
                view = raw_input('View downloaded image?[y/n]: ')
                if view == 'y' or view == 'Y':
                    try:
                        img = Image.open('FBpics/' + a + '.jpg')
                        img.show()
                    except:
                        print 'There was an error opening the file'
                        pass
                else:
                    pass
            else:
                pass
            #if jsonResponse['username']:
            if res['username']:
                #usernom = jsonResponse['username']
                usernom = res['username']

        # thread.start_new_thread(instacheck,(usernom,))

        # Check for the username on instagram-check function

                instacheck(usernom)

      # sleep(5)

            myCounter += 1
            sleep(2)
        except:

            pass
    return
