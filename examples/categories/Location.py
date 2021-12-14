import bpy
from easybpy import *

#  Location
# Getting the location of an object by reference.
position = location(object)

# Getting the location of the active object.
position = location()

# Setting the location of an object.
location(object, [3.0, 0.0, 4.0])

# Setting the location of an object by name.
location("Cube", [3.0, 0.0, 4.0])
