import requests
import re

username = "natas11"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print(response.cookies["data"])
print("="*50)


source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

#cookie = requests.utils.unquote(response.cookies["data"]).decode("base64").encode("hex") # ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=
# I have to run natas11_code.php file to the get value
cookies = {"data":"ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

response = session.get(url,auth=(username,password),cookies=cookies)

# Just Code Printing
code = re.findall(r"[A-Za-z0-9]{32}", response.text)[1]
print("\nThe password for the next level is: " + code)