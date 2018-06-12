#!/usr/bin/python
# -*- coding: utf-8 -*-

import thread
try:
    shodan_key_file = open('auth/shodankey.txt', 'r')
    shodan_key_line = shodan_key_file.readlines()
    SHODAN_API_KEY = shodan_key_line[1].rstrip()
    sho_api = shodan.Shodan(SHODAN_API_KEY)
    shodan_key_file.close()
except:
    sho_api = None


def menu():
    print '**************************************'
    print '*     Shodan Search -- NinjaSl0th    *'
    print '**************************************'
    print
    print '[1] Search by subnet (add cidr value) ex:/24'
    print '[2] Search by hostname (ex: computing.site.com)'
    print '[3] Search for printers by organization (ex: Microsoft)'
    print '[4] Search for ports by organization (supported ports: ',
    print 'http://www.shodanhq.com/help/filters#port)'
    print '[5] Stream for SSL certs *REQUIRES STREAMING API ACCESS*' 
    print '[0] Exit'
    print
    select_mod()


def downloader(res_out, search_query):

  # search_query = sho_api.search(data)

    outfile = open(res_out, 'a')
    for result in search_query['matches']:
        outfile.write('--START--\n')
        outfile.write('IP: %s \n' % result['ip_str'])
        encout = result['data'].encode('UTF-8')
        #outfile.write(result['data'])
        outfile.write(encout)

    # print result['hostnames'][0]

        try:
            outfile.write(result['hostnames'][0])
        except:
            pass
        outfile.write('''''')
        outfile.write('\n')
        a = result['port']
        b = result['os']
        outfile.write('Port:')
        outfile.write(str(a))
        outfile.write('\n')
        outfile.write('Detected OS:')
        outfile.write(str(b))
        outfile.write('\n')
        outfile.write('--END--\n\n')
        outfile.write('''''')
    outfile.close()


def select_mod():
    if sho_api is None:
        print "Missing key; Please install a Shodan API key in",
        print"./auth/shodankey"
        return
    menu_select = raw_input('Please enter an option: ')
    if menu_select == '1':
        sub_search(sho_api)
    elif menu_select == '2':
        host_search(sho_api)
    elif menu_select == '3':
        print_search(sho_api)
    elif menu_select == '4':
        port_search(sho_api)
    elif menu_select == '5':
        cert_search(sho_api)
    elif menu_select == '0':
        return
    else:
        print 'please enter a valid choice'
        menu()


def sub_search(sho_api):
    res_out = 'NET-RESULTS.txt'
    prefix = 'net:'
    query = raw_input('Enter Subnet (with cidr): ')
    data = prefix + query
    try:
        search_query = sho_api.search(data)
        print 'Results found: %s' % search_query['total']
        thread.start_new_thread(downloader, (res_out, search_query))

        print 'Results have been exported to: NET-RESULTS.txt'
        menu()
    except Exception, e:
        print 'Error: %s' % e
        menu()


def host_search(sho_api):
    res_out = 'HOST-RESULTS.txt'
    prefix = 'hostname:'
    query = raw_input('Please enter hostname: ')
    data = prefix + query
    try:
        search_query = sho_api.search(data)
        print 'Results found: %s' % search_query['total']
        thread.start_new_thread(downloader, (res_out, search_query))

        print 'Results have been exported to: HOST-RESULTS.txt'
        menu()
    except Exception, e:
        print 'Error: %s' % e
        menu()


def print_search(sho_api):
    res_out = 'PRINTER-RESULTS.txt'
    prefix = 'org:'
    query = raw_input('Please enter company/org: ')
    data = prefix + '"' + query + '"' + ' print'
    try:
        search_query = sho_api.search(data)
        print 'Results found: %s' % search_query['total']
        thread.start_new_thread(downloader, (res_out, search_query))

        print 'Results have been exported to: PRINTER-RESULTS.txt'
        menu()
    except Exception, e:
        print 'Error: %s' % e
        menu()


def port_search(sho_api):
    res_out = 'PORT-RESULTS.txt'
    prefix = 'org:'
    query = raw_input('Please enter company/org: ')
    port_prefix = 'port:'
    search_port = raw_input('Please enter the port: ')
    data = prefix + '"' + query + '"' + port_prefix + search_port
    try:
        search_query = sho_api.search(data)
        print 'Results found: %s' % search_query['total']
        thread.start_new_thread(downloader, (res_out, search_query))

        print 'Results have been exported to: PORT-RESULTS.txt'
        menu()
    except Exception, e:
        print 'Error: %s' % e
        menu()

def cert_search(sho_api):
    #res_out = 'CERTS.txt'
    try:
        for banner in sho_api.stream.ports(['443']):
            if 'opts' in banner and 'pem' in banner['opts']:
                print banner['opts']['pem']
    except Exception, e:
        print 'Error: %s' % e
        menu()
