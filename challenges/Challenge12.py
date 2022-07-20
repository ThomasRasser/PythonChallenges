#region Challenge 12
import os
import PIL.Image, PIL.ImageFile
import codecs
import io

# To allow PIL to be tolerant of files that are truncated
# Stackoverflow: https://tinyurl.com/bdd6659z
PIL.ImageFile.LOAD_TRUNCATED_IMAGES = True

print("Challenge 12: ")
print("-----------------------------------------------------")

# Read the .gfx file as bytes
with codecs.open("additional_files\\challenge12.gfx", "rb") as file:
    data = file.read()

# Turn the bytes into a list of images
images = [None]*5
for i in range(5):
    images[i] = PIL.Image.open(io.BytesIO(data[i::5]))


# Combine images into a single image

    # Get new dimensions
widths, heights = zip(*(i.size for i in images))
total_width = sum(widths)
max_height = max(heights)

    # Create new image
combined_image = PIL.Image.new('RGB', (total_width, max_height))

x_offset = 0
for img in images:
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixel = img.getpixel((x, y))
            combined_image.putpixel((x_offset + x, y), pixel)
    x_offset += img.size[0]

    # Show image
combined_image.show()
 
solution = "disproportional"
solution_url = "http://www.pythonchallenge.com/pc/def/" + solution + ".html"
print("\n" + solution_url)
os.system('echo ' + solution_url + ' | clip')

print("-----------------------------------------------------\n\n")
#endregion