import requests
import re

username = "natas8"
password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

secretHex = re.findall(r"[a-z0-9]{32}",response.text)[0].decode("hex")
# reverse the hex
secret = secretHex[::-1].decode("base64")
response = session.post(url,auth=(username,password),data={"secret":secret,"submit":"submit"})
print(response.text)
print("="*50)

# Just Code Printing
code = re.findall("Access granted. The password for natas9 is (.*)", response.text)[0]
print("The code for the next level is: " + code)