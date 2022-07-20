#region Challenge 2
import os

print("Challenge 2: ")
print("-----------------------------------------------------")

# Load the text file, which was copied from the source code of the website
with open("additional_files\\challenge2.txt", "r") as f:
    code = f.read().replace('\n', '')

# Claculate character frequency
char_freq = {}
for letter in code:
    if letter in char_freq:
        char_freq[letter] += 1
    else:
        char_freq[letter] = 1

# Print char_freq sorted by value, starting by the biggest
solution = ""
for key, value in sorted(char_freq.items(), key=lambda item: item[1], reverse=True):
    print(key, value)
    if(value == 1):
        solution += key

solution_url = "http://www.pythonchallenge.com/pc/def/" + solution + ".html"
print("\n" + solution_url)
os.system('echo ' + solution_url + ' | clip')

print("-----------------------------------------------------\n\n")
#endregion

