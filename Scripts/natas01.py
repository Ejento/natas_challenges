'''
Same as before. Easy challenge.
You have to read the source code of the page.
'''
import requests
import re

username = "natas1"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org" % username

response = requests.get(url, auth=(username,password))
pageContent = response.text
print(pageContent)
print("="*50)

code = re.findall("The password for natas\d is (.*) -->", pageContent)[0]
print("\nThe password for the next level is: " + code)
