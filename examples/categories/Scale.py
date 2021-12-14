import bpy
from easybpy import *

#  Scale
# Getting the scale of an object by reference.
obj_scale = scale(object)

# Getting the scale of the active object.
obj_scale = scale()

# Setting the scale of an object.
scale(object, [5.0, 4.5, 2.0])

# Setting the scale of an object by name.
scale("Cube", [5.0, 4.5, 2.0])
