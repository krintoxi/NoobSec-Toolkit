#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bsoup
import urllib


def lookup():
    while True:
        try:
            url = 'https://isc.sans.edu/api/port/'
            port = raw_input('Enter port: ')
            fullUrl = url + port
            try:
                data = urllib.urlopen(fullUrl)
            except:
                print 'Could not connect to SANS website.'
                raise
            i = bsoup(data)

      # print i

            serviceUDP = i.html.body.services.udp.service
            serviceTCP = i.html.body.services.tcp.service
            udpName = i.html.body.services.udp.findAll('name')[0]
            tcpName = i.html.body.services.tcp.findAll('name')[0]
            try:
                print
                print '----------UDP-----------'
                print 'UDP Service Name: ' + serviceUDP.string
                print 'UDP Name: ' + udpName.string
                print
            except:
                pass
            try:
                print '----------TCP-----------'
                print 'TCP Service Name: ' + serviceTCP.string
                print 'TCP Name: ' + tcpName.string
                print
                print
            except:
                pass
            print '----------END-----------\n'
        except KeyboardInterrupt:
            raise


  # return
