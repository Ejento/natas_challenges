'''
This is a more complex challenge.
You can find some intresting things in the "index-source.html" file.
'''
import requests
import re

username = "natas8"
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
The code that we are instrested is:

<?
$encodedSecret = "3d3d516343746d4d6d6c315669563362";
function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}
if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
		print "Access granted. The password for natas9 is <censored>";
	} else {
		print "Wrong secret";
    }
}
?>

So here we have the encodedSecret variable, which is an encoded string of something that we don't know, but we can reverse the progress and found out.
First we are getting the "encodeSecret" that's a hex and we decode that to find something in a base64 format.
The base64 string is reversed, so we have to reverse that before decode it.
'''

secretHex = re.findall(r"[a-z0-9]{32}",response.text)[0]
secretHex = secretHex.decode("hex") # decode hex.
secret = secretHex[::-1].decode("base64") # reverse the string and decode base64.
# After we are doing a POST request with the secret that we find.
response = session.post(url,auth=(username,password),data={"secret":secret,"submit":"submit"})
print(response.text)
print("="*50)

# Just Code Printing
code = re.findall("Access granted. The password for natas9 is (.*)", response.text)[0]
print("The password for the next level is: " + code)
