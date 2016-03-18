#!/usr/bin/env python

try:
    from time import sleep
    import os
    import sys
    from netaddr import *
    from socket import socket
    import OpenSSL
    import ssl
    from timeout import timeout
    import thread
except Exception, e:
    print e
    raise

ips = []
out = {}

def starter():
    init(ips)
def init(ips):
    multi = raw_input("Are we looking up multiple IP's/Networks? [y/n]: ")
    if multi == "Y" or multi == "y":
        multiNetwork = True
    elif multi == "n" or multi == "N":
        multiNetwork = False
    else:
        print "Invalid input!"
        starter()
    if multiNetwork:
        try:
            while True:
                cpy = raw_input("IP or IP/CIDR [enter 'done' when finished]: ")
                if "/" in cpy:
                    i = cpy.rstrip()
                    ip_list = list(IPNetwork(i))
                    for e in sorted(ip_list):
                        st = str(e)
                        ips.append(st)
                else:
                    cpy = cpy.rstrip()
                    ips.append(cpy)
                if cpy == "done":
                    trigger(ips,out)
                    break
                else:
                    pass
        except KeyboardInterrupt:
            raise
    else:
        cpy = raw_input("IP or IP/CIDR: ")
        cpy = cpy.rstrip()
        ips.append(cpy)
    trigger(ips,out)

def getcert(a):
    """Get SSL Cert CN"""
    refPorts = open('config/ports.txt', 'r').readlines()
    for port in refPorts:
        # Make sure we don't have any extra characters like \n or \r
        port = port.rstrip()
        try:
            # time to connect!
            cert = ssl.get_server_certificate((a, port))
        except Exception, e:
            # If it can't connect go to the next iteration so we don't waste time
            continue
        try:
            # use openssl to pull cert information
            c = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
            subj = c.get_subject()
            comp = subj.get_components()
            for data in comp:
                if 'CN' in data:
                    out[a] = a,data[1]
                elif 'CN' not in data:
                    continue
                else:
                    continue
        except Exception,e:
            # if openssl fails to get information, return nothing
            continue


def trigger(ips,out):
    """Start our SSL search/thread"""
    for ip in ips:
        thread.start_new_thread(getcert, (ip,))
        # Sleep so our threads don't get out of control
        sleep(2)
    sleep(3)
    for val in out:
        print out[val]
