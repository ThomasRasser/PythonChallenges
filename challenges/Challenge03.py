# URL: http://www.pythonchallenge.com/pc/def/equality.html
#region Challenge 3
import os
import re

print("Challenge 3: ")
print("-----------------------------------------------------")

# Load the text file, which was copied from the source code of the website
with open("additional_files\\challenge3.txt", "r") as f:
    code = f.read().replace('\n', '')

# Find every word in the file, that matches the regex
solution = ""
regex = re.compile(r'[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}')
for word in regex.findall(code):
    solution += word[4]
    print(word[0] + " " + word[1:4] + " " + word[4] + " " + word[5:8] + " " + word[8])

solution_url = "http://www.pythonchallenge.com/pc/def/" + solution + ".html"
print("\n" + solution_url)
os.system('echo ' + solution_url + ' | clip')

print("-----------------------------------------------------\n\n")
#endregion
