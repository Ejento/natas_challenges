'''
At first we can see that this just a page with a button that sets the color of the background to whatever we want.
Looking through the source-index.html we can find some neat stuff though.
'''
import requests
import re

username = "natas11"
password = "<censored>"
url = "http://%s.natas.labs.overthewire.org/"  % username

session = requests.Session()

response = session.get(url,auth=(username,password))
print(response.text)
print(response.cookies["data"])
print("="*50)

source = "index-source.html"
response = session.get(url+source,auth=(username,password))
print(response.text)
print("="*50)

'''
As always reading throught the index-source.html we can understand how the page works:

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
	.....
	.....
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}
.....
.....

saveData($data);
?>

As we can see they are using a XOR encryption algorithm that saves the encrypted text to our cookie, as the variable "data".
If we find the key that is <censored> in the code above, we can encrypt the message that we want locally and sent it to the server.
I did that in the php file called "natas11_code.php" that you can find in this folder, next to this script.
'''

# I have to run natas11_code.php file to the get value and set it on the "data" variable that I will send to the server.
cookies = {"data":"ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

response = session.get(url,auth=(username,password),cookies=cookies) # The malicious cookie does all the work.
print(response.text)
print("="*50)

# Just Code Printing
code = re.findall(r"[A-Za-z0-9]{32}", response.text)[1]
print("\nThe password for the next level is: " + code)
