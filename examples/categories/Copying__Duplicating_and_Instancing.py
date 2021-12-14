import bpy
from easybpy import *

#  Copying / Duplicating and Instancing
# Makes a copy of 'object' and puts it in the collection named 'My Collection'
copy_object(object, 'My Collection')

# Makes a copy of 'object' and puts it in the active collection.
copy_object(object)

# Finds 'Cube' and puts it in the collection named 'My Collection'
copy_object("Cube", "My Collection")

# You can also store the reference to the new object like this:
new_obj = copy_object(object)

# Created instance of 'object' with a new name and moves it to 'My Collection'
instance_object(object, "New Name", "My Collection")

# Yes, you can also grab the returned reference like so:
new_obj = instance_object(object, "New Object", "My Collection")
