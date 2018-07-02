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

def xtra():

    global found

    global args

    extras = ["/robots.txt", "/usernames.txt", "/profiles", "/accounts", "/index.php?id=1", "/main.php?id=1", "/view_items.php?id=", "/home.php?cat="]

    found = []

    if args.extra == "True":

       print "---------------------------"

       print "100% DONE!\n"

       time.sleep(1)

       print "[*] EXTRA SCAN STARTING\n"

       time.sleep(1.2)

       for x in extras:

           response = requests.get(args.target + x)

           if response.status_code == 404:

              print fontstyles.messages.error + " " + x +  " Was not found!\n"

           if response.status_code == 200 or 202 and response.status_code != 404:

              print fontstyles.messages.positive + x + " Is an existing page!\n"

              found.append(x)

    if args.extra != "True":

       quit()

def cli():

    global args

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--target', help="Target URL to Scan.")

    parser.add_argument('-x', '--extra', help="Extra Scan. Values: True/False")

    args = parser.parse_args()

    if args.target == None:

       print "No target specified."

       quit()

adminpages = ["/admin","/sysadmin","/adminpage","/adminlogin","/webadmin",
"/admin_login","/administrator","/admin_login","/admin_area", "/adminsonly", "/admin_only", "/admins_only", "/administrator_login", "/administrator_page", "/web_admin", "/administratorarea", "/cpanel", "/control_panel" ]

pages = [] 

def overall():

    global found

    print "_______________________"

    print "Scan Finished"

    print "Admin Pages Found:",len(pages)

    print "\n_______________________"

    if len(pages) == 0:

       print "No admin panels found."

       quit()

    if len(pages) > 0:

       print "Admin pages:",pages

    print "Extra Pages Found:",len(found)

    if len(found) == 0:

       print "No extra pages found!"

       quit()

    if len(found) > 0:

       print "Pages:",found

       quit()

def find():

    global args

    global adminpage

    print "Welcome to admin panel finder."

    print "Starting Scan on",args.target

    for adminpage in adminpages:

        try:

          r = requests.get(args.target + adminpage)
        except KeyboardInterrupt:
          print "Exiting program..." 
         
          quit()
        
        except:

          print "Target not found.",example

          quit()

        if r.status_code == 404:

           print fontstyles.messages.error + " " + adminpage +  " Is Not The Admin Page\n"

        if r.status_code == 200 or 202 and r.status_code != 404:

           print fontstyles.font.header

           print fontstyles.font.bold +  "Possible Admin page found:",adminpage

           print fontstyles.font.reset_all

           pages.append(adminpage)

           pass

def main():

    banner()

    cli()

    find()

    xtra()

    overall()

main()

