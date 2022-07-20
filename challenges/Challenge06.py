#region Challenge 6
import os
import zipfile

print("Challenge 6: ")
print("-----------------------------------------------------")

zip_folder = zipfile.ZipFile("additional_files\\challenge6.zip")
comments = []

cur_number = "90052" # first index

for i in range(0, 1000):
    # Extract number of the next file and zipfile-comment
    data = zip_folder.read(cur_number + ".txt").decode("utf-8")
    comments += zip_folder.getinfo(cur_number + ".txt").comment.decode("utf-8")

    # Find number in data and update cur_number
    cur_number = data.split(" ")[-1]
    if(not cur_number.isdigit()):
        solution = cur_number
        break

print("".join(comments))

solution_url = "http://www.pythonchallenge.com/pc/def/oxygen.html"
print("\n" + solution_url)
os.system('echo ' + solution_url + ' | clip')

print("-----------------------------------------------------\n\n")
#endregion