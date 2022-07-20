#region Challenge 5
import os
import pickle
import urllib.request

print("Challenge 5: ")
print("-----------------------------------------------------")

# Load the image from the website and serialize it
url_request = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(url_request)

# Decode the list of lists of tuples into a string
for line in data:
    # Tuples are (string, int)
    for tuple in line:
        print(tuple[0] * tuple[1], end="")
    print("")

solution_url = "http://www.pythonchallenge.com/pc/def/channel.html"
print("\n" + solution_url)
os.system('echo ' + solution_url + ' | clip')

print("-----------------------------------------------------\n\n")
#endregion
