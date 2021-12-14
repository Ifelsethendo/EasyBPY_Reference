import bpy
from easybpy import *

#  Rotation
# Getting the rotation of an object by reference.
rotation_euler = rotation(object)

# Getting the rotation of the active object.
rotation_euler = rotation()

# Setting the rotation of an object.
rotation(object, [45.0,0.0,40.0])

# Setting the rotation of an object by name.
rotation("Cube", [45.0, 0.0, 40.0])
