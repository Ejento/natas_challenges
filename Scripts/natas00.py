import requests
import re

username = "natas0"
password = "natas0"
url = "http://natas0.natas.labs.overthewire.org" 

response = requests.get(url, auth=((username,password)))
pageContent = response.text
print(pageContent)
print("="*50)

code = re.findall("The password for natas\d is (.*) -->", pageContent)[0]
print("\nThe password for the next level is: " + code)