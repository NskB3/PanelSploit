import os, socket, fontstyles
import argparse
import time
import sys
try:
  import requests
except ImportError:
  print "Please install the requests library. "
  quit()
example = "\nExample: python2 panelsploit.py -t https://www.google.com"
def banner():
    print("""
                                         
___________________
|___PanelSploit___ |
|------------------|
|Admin Panel Finder|
|    By NSK B3     |
|__________________|
""")

def tcp():
    print "Starting TCP Connect Scan."
    args.target = raw_input("Enter target again: ")
    adminpages = ["/admin","/sysadmin" ,"/adminpage","/adminlogin","/webadmin", "/admin_login","/administrator","/admin_login","/admin_area"]
    for adm in adminpages:
        try:

          sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          r = sock.connect((args.target + adm, 80))

          sock.close()
        except socket.gaierror:
               print "This type of scan isn't supported yet!"
               quit()
        if r == 0:
           print "Admin Page Found:",adm
        else:
           print fontstyles.messages.error + adm + " Not found"

def cli():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', help="Target URL to Scan.")   
    parser.add_argument('-Tc','--tcpscan', help="Scan Using TCP Packets", default=False)
    args = parser.parse_args()
    if args.target == None:
       print "No target specified."
       quit()
adminpages = ["/admin","/sysadmin","/adminpage","/adminlogin","/webadmin", "/admin_login","/administrator","/admin_login","/admin_area"]

pages = []
def find():
    global args
    print "Welcome to admin panel finder."
    print "Starting Scan on",args.target
    if args.tcpscan == "true":
       tcp()
    if args.tcpscan != "true":
       args.tcpscan = False
       pass
    for adminpage in adminpages:
        try:

          r = requests.get(args.target + adminpage)
        except:
          print "Target not found.",example
          quit()
        if r.status_code == 404:
           print fontstyles.messages.error + adminpage +  " Is Not valid. Checking next page."
        if r.status_code == 200 or 202 and r.status_code != 404:
           print fontstyles.font.header
           print fontstyles.font.bold +  "Admin page found:",adminpage
           print fontstyles.font.reset_all
           pages.append(adminpage)
           quit()
def overall():
    print "Scan ended."
    print "Admin panels found:",len(pages)
    print pages
def main():
    banner()
    cli()
    find()
main()
