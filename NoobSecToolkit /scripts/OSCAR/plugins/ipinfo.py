#!/usr/bin/python
# -*- coding: utf-8 -*-

#import urllib2
#import json
import time
import webbrowser
import requests


def lookup(ip):

    ipUrl = 'http://ip-api.com/json/'
    ip_query = ipUrl + ip
    try:
        #data = urllib2.urlopen(ip_query)
        #jsonResponse = json.load(data)
        data = requests.get(ip_query)
        jsonResponse = data.json()
        print
        print '-- IP Results --'
        print 'IP: ', jsonResponse['query']
        print 'ISP: ', jsonResponse['isp']
        print 'ASN: ', jsonResponse['as']
        print 'Country: ', jsonResponse['country']
        print 'City: ', jsonResponse['city']
        print 'Region: ', jsonResponse['regionName']
        print 'Longitude: ', jsonResponse['lon']
        print 'Latitude: ', jsonResponse['lat']
        print '-- END --'
        print
    except:
        print '[+]ERROR: Could not connect to IP lookup site. Trying another!'
        try:
            ipUrl = 'https://freegeoip.net/json/'
            ip_query = ipUrl + ip
            #data = urllib2.urlopen(ip_query)
            #jsonResponse = json.load(data)
            data = requests.get(ip_query)
            jsonResponse = data.json()
            print
            print '-- IP Results --'
            print 'IP: ', jsonResponse['ip']
            print 'Country: ', jsonResponse['country_name']
            print 'City: ', jsonResponse['city']
            print 'Region: ', jsonResponse['region_name']
            print 'Longitude: ', jsonResponse['longitude']
            print 'Latitude: ', jsonResponse['latitude']
            print '-- END --'
            print
        except:
            print 'Could not connect to second lookup site!'
            raise

  # wait 3 seconds until going back to the main menu

    time.sleep(3)
    avcheck = \
        raw_input('Check IP with AlienVault (opens in browser) [y/n]: ')
    if avcheck == 'y' or avcheck == 'Y':
        alienvault(ip)
    else:
        pass
    return


def alienvault(ip):
    n = 2
    url = 'http://www.alienvault.com/apps/rep_monitor/ip/' + ip
    webbrowser.open(url, new=n)
    return
