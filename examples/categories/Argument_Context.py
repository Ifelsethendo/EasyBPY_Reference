import bpy
from easybpy import *

#  Argument Context
# Returns a reference to the ative object.
obj = get_object()

# Finds the object named 'Cube' and returns a reference to it.
obj = get_object("Cube")

# Changes the name of the 'objct' to 'New Name'
rename_object(object, "New Name")

# Changes the name of the active object to 'New Name'
rename_object("New Name")

# Deletes the object named 'Cube'.
delete_object("Cube")

# Deletes the active object.
delete_object()

# Deletes the object from the reference provided.
delete_object(object)
