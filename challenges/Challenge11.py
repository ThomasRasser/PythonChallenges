#region Challenge 11
import os
import urllib.request
from PIL import Image

print("Challenge 11: ")
print("-----------------------------------------------------")


# Username and password received from the challenge 8
username = "huge"
password = "file"

# Authenticate the user
# Stackoverflow: https://tinyurl.com/2xadpe65
url = "http://www.pythonchallenge.com/pc/return/cave.jpg"
passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, username, password)
authhandler = urllib.request.HTTPBasicAuthHandler(passman)
opener = urllib.request.build_opener(authhandler)
urllib.request.install_opener(opener)

# Load image
image = urllib.request.urlopen("http://www.pythonchallenge.com/pc/return/cave.jpg")
img = Image.open(image)

img_width = img.size[0]
img_height = img.size[1]

# Split the image into a list of even and odd pixels, in a checkerboard pattern
new_img_even = Image.new("RGB", (img_width, img_height))
new_img_odd = Image.new("RGB", (img_width, img_height))
for x in range(img_width):
    for y in range(img_height):
        pixel = img.getpixel((x, y))
        if((x+y) % 2 == 0):
            new_img_even.putpixel((x, y), pixel)
        else:
            new_img_odd.putpixel((x, y), pixel)

new_img_even.show()
# new_img_odd.show() # codeword is in the new_img_even

solution = "evil"
solution_url = "http://www.pythonchallenge.com/pc/return/" + solution + ".html"
print("\n" + solution_url)
os.system('echo ' + solution_url + ' | clip')

print("-----------------------------------------------------\n\n")
#endregion