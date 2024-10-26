from PIL import Image

# Load the image
image = Image.open('/home/tumbu/Téléchargements/logo-nfa-transparent.png')

# Convert the image to RGBA if it's not already in that mode
image = image.convert("RGBA")

# Get the data of the image
data = image.getdata()

# Create a new data list
new_data = []

# Loop through the data
for item in data:
    # Change all black (or near-black shades) to white
    if item[0] in range(0, 35) and item[1] in range(0, 35) and item[2] in range(0, 35):
        # Change it to white with the same alpha value
        new_data.append((255, 255, 255, item[3]))
    else:
        # Keep the pixel the same
        new_data.append(item)

# Update image data
image.putdata(new_data)

# Save the new image
image.save('/home/tumbu/Téléchargements/logo-nfa-transparent-black-to-white.png')
