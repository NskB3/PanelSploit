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


def cli():

    global args

    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--target', help="Target URL to Scan.")

    args = parser.parse_args()

    if args.target == None:

       print "No target specified."

       quit()

adminpages = ["/admin","/sysadmin","/adminpage","/adminlogin","/webadmin",

"/admin_login","/administrator","/admin_login","/admin_area", "/adminsonly", "/admin_only", "/admins_only", "/administrator_login", "/administrator_page", "/web_admin", "/administratorarea", "/cpanel", "/control_panel" ]
pages = [] 


def find():

    global args

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

           print fontstyles.messages.error + " " + adminpage +  " Is Not The Admin Page"




        if r.status_code == 200 or 202 and r.status_code != 404:

           print fontstyles.font.header

           print fontstyles.font.bold +  "Possible Admin page found:",adminpage

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

