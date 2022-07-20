# URL: http://www.pythonchallenge.com/pc/def/oxygen.html
#region Challenge 7
import os
import urllib.request
from PIL import Image
import re

print("Challenge 7: ")
print("-----------------------------------------------------")

# Load image
image = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
img = Image.open(image)
img_width = img.size[0]
img_height = img.size[1]

# Get the values of each grey rectangel in the middle of the pixel
# rectangel_width = 7
pixel_values = []
for pixel in range(0, img_width, 7):
    pixel_value = img.getpixel((pixel, img_height/2))
    pixel_values.append(pixel_value[0])

# Remove last 3 values in list, since they are not part of the message
pixel_values = pixel_values[:-3]

# Decode the message
message = ""
for pixel in pixel_values:
    message += chr(pixel)
print(message + "\n")

# Decode the message in the message
solution = ""
regex = re.compile(r'\d{1,3}')
for number in regex.findall(message):
    solution += chr(int(number))

solution_url = "http://www.pythonchallenge.com/pc/def/" + solution + ".html"
print("\n" + solution_url)
os.system('echo ' + solution_url + ' | clip')

print("-----------------------------------------------------\n\n")
#endregion