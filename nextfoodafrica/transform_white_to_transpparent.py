from PIL import Image

# Load the image
image = Image.open(r'/home/tumbu/Téléchargements/logo-nfa.png')

# Convert the image to RGBA if it's not already in that mode
image = image.convert("RGBA")

# Get the data of the image
data = image.getdata()

# Create a new data list
new_data = []

# Define the color you want to replace (white in this example)
replace_color = (255, 255, 255, 255)

# Define the color you want to replace with (transparent in this example)
new_color = (0, 0, 0, 0)  # Fully transparent for the RGBA mode

# Loop through the data
for item in data:
    # Change all white (also shades of whites)
    # to the new color (in this case, transparent)
    if item[0] in range(200, 256) and item[1] in range(200, 256) and item[2] in range(200, 256):
        new_data.append(new_color)
    else:
        new_data.append(item)

# Update image data
image.putdata(new_data)

# Save the new image
image.save(r'/home/tumbu/Téléchargements/logo-nfa-transparent.png')
print('edit terminated.')
