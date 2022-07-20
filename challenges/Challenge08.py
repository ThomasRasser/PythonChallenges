#region Challenge 8
import os
import bz2

print("Challenge 8: ")
print("-----------------------------------------------------")

# Set username and password, which were copied from the source code of the website
username = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
password = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# Decompress the username and password
decompressed_username = bz2.decompress(username)
decompressed_password = bz2.decompress(password)

print("Username: " + str(decompressed_username))
print("Password: " + str(decompressed_password))

solution_url = "http://www.pythonchallenge.com/pc/return/good.html"
print("\n" + solution_url)
os.system('echo ' + solution_url + ' | clip')

print("-----------------------------------------------------\n\n")
#endregion