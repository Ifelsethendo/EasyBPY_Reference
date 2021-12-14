import bpy
from easybpy import *

#  Images
# Creates a new image.
img = create_image("Name", weight = 1024, height = 1024)

# Gets the image of the given name.
img = get_image("Name")

# Gets a list of all images in the file.
images = get_all_images()

# Renames the given image with the new name.
rename_image(image, "Name")

# Delted the given image.
delete_image(texture)
