import os
def banner():
    print ("""
______________________
SETUP SCRIPT FOR LINUX
______________________
""") 
banner() 
def setup():
    platform = os.uname()
    if 'linux' or 'Linux' in platform:
        os.system('pip2 install requests -y') 
    else:
        print("This is for LINUX only!!!") 
        quit() 
