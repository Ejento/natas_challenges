import requests
import re

username = "natas1"
password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"
url = "http://%s.natas.labs.overthewire.org" % username

response = requests.get(url, auth=((username,password)))
pageContent = response.text
code = re.findall("The password for natas\d is (.*) -->", pageContent)[0]
print("\nThe code for the next level is: " + code)