# URL: http://www.pythonchallenge.com/pc/def/linkedlist.html -> php
# URL: http://www.pythonchallenge.com/pc/def/linkedlist.php
#region Challenge 4
import os
import urllib.request

print("Challenge 4: ")
print("-----------------------------------------------------")

url_base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
# cur_number = "12345"  # first index
# cur_number = "8022"   # second index
# cur_number = "63579"  # third index
cur_number = "75635"    # fourth index

for i in range(0, 400):
    # Request url and decode to utf-8
    url_request = urllib.request.urlopen(url_base + cur_number)
    data = url_request.read()
    data = data.decode("utf-8")
    print(data)
    
    # Find number in data and update cur_number
    cur_number = data.split(" ")[-1]
    if(not cur_number.isdigit()):
        solution = cur_number
        break

solution_url = "http://www.pythonchallenge.com/pc/def/" + solution
print("\n" + solution_url)
os.system('echo ' + solution_url + ' | clip')

print("-----------------------------------------------------\n\n")
#endregion
