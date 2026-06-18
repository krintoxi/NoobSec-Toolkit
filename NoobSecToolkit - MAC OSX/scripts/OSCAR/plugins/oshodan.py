#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading

try:
    import shodan
except ImportError:
    shodan = None

sho_api = None

try:
    shodan_key_file = open("auth/shodankey.txt", "r")
    shodan_key_line = shodan_key_file.readlines()
    SHODAN_API_KEY = shodan_key_line[1].rstrip()
    shodan_key_file.close()
    if shodan:
        sho_api = shodan.Shodan(SHODAN_API_KEY)
except Exception:
    sho_api = None


def menu():
    print("**************************************")
    print("*     Shodan Search -- NinjaSl0th    *")
    print("**************************************")
    print()
    print("[1] Search by subnet (add cidr value) ex:/24")
    print("[2] Search by hostname (ex: computing.site.com)")
    print("[3] Search for printers by organization (ex: Microsoft)")
    print("[4] Search for ports by organization")
    print("[5] Stream for SSL certs *REQUIRES STREAMING API ACCESS*")
    print("[0] Exit")
    print()
    select_mod()


def downloader(res_out, search_query):
    with open(res_out, "a", encoding="utf-8") as outfile:
        for result in search_query["matches"]:
            outfile.write("--START--\n")
            outfile.write("IP: %s\n" % result["ip_str"])
            outfile.write(result.get("data", "") + "\n")
            try:
                outfile.write(result["hostnames"][0] + "\n")
            except (KeyError, IndexError):
                pass
            outfile.write("Port: %s\n" % str(result.get("port", "")))
            outfile.write("Detected OS: %s\n" % str(result.get("os", "")))
            outfile.write("--END--\n\n")


def select_mod():
    if sho_api is None:
        print("Missing key; please install a Shodan API key in ./auth/shodankey.txt")
        return
    menu_select = input("Please enter an option: ").strip()
    if menu_select == "1":
        sub_search(sho_api)
    elif menu_select == "2":
        host_search(sho_api)
    elif menu_select == "3":
        print_search(sho_api)
    elif menu_select == "4":
        port_search(sho_api)
    elif menu_select == "5":
        cert_search(sho_api)
    elif menu_select == "0":
        return
    else:
        print("Please enter a valid choice.")
        menu()


def sub_search(sho_api):
    res_out = "NET-RESULTS.txt"
    query = input("Enter Subnet (with cidr): ").strip()
    data = "net:" + query
    try:
        search_query = sho_api.search(data)
        print("Results found: %s" % search_query["total"])
        t = threading.Thread(target=downloader, args=(res_out, search_query), daemon=True)
        t.start()
        t.join()
        print("Results exported to: NET-RESULTS.txt")
        menu()
    except Exception as e:
        print("Error: %s" % e)
        menu()


def host_search(sho_api):
    res_out = "HOST-RESULTS.txt"
    query = input("Please enter hostname: ").strip()
    data = "hostname:" + query
    try:
        search_query = sho_api.search(data)
        print("Results found: %s" % search_query["total"])
        t = threading.Thread(target=downloader, args=(res_out, search_query), daemon=True)
        t.start()
        t.join()
        print("Results exported to: HOST-RESULTS.txt")
        menu()
    except Exception as e:
        print("Error: %s" % e)
        menu()


def print_search(sho_api):
    res_out = "PRINTER-RESULTS.txt"
    query = input("Please enter company/org: ").strip()
    data = 'org:"' + query + '" print'
    try:
        search_query = sho_api.search(data)
        print("Results found: %s" % search_query["total"])
        t = threading.Thread(target=downloader, args=(res_out, search_query), daemon=True)
        t.start()
        t.join()
        print("Results exported to: PRINTER-RESULTS.txt")
        menu()
    except Exception as e:
        print("Error: %s" % e)
        menu()


def port_search(sho_api):
    res_out = "PORT-RESULTS.txt"
    query = input("Please enter company/org: ").strip()
    search_port = input("Please enter the port: ").strip()
    data = 'org:"' + query + '" port:' + search_port
    try:
        search_query = sho_api.search(data)
        print("Results found: %s" % search_query["total"])
        t = threading.Thread(target=downloader, args=(res_out, search_query), daemon=True)
        t.start()
        t.join()
        print("Results exported to: PORT-RESULTS.txt")
        menu()
    except Exception as e:
        print("Error: %s" % e)
        menu()


def cert_search(sho_api):
    try:
        for banner in sho_api.stream.ports(["443"]):
            if "opts" in banner and "pem" in banner["opts"]:
                print(banner["opts"]["pem"])
    except Exception as e:
        print("Error: %s" % e)
        menu()
