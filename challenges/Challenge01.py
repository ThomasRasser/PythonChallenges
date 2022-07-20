#region Challenge 1
import os

print("Challenge 1: ")
print("-----------------------------------------------------")

code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
print(code)

# Ceaser cipher
def ceaser_cipher(code, key):
    cipher = ""
    for char in code:
        if(char in alphabet):
            cipher += alphabet[(alphabet.index(char) + key) % len(alphabet)]
        else:
            cipher += char
    return cipher

# Decode the cipher
print("\n" + ceaser_cipher(code, 2))

# Decode the url
solution = ceaser_cipher("map", 2)

solution_url = "http://www.pythonchallenge.com/pc/def/" + solution + ".html"
print("\n" + solution_url)
os.system('echo ' + solution_url + ' | clip')

print("-----------------------------------------------------\n\n")
#endregion
