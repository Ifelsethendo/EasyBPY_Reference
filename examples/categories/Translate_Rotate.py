import bpy
from easybpy import *

#  Translate Rotate
# Rotate an object 45 degrees around an axis.
rotate_around_axis(45, axis, object)
# Just like the translation functions, 'object' can.
# accept either a single object or list of objects.

# Rotate object 45 degrees around the global X axis.
rotate_around_x(45, object)

# Rotate object 45 degrees around the local X axis.
rotate_around_local_x(45, object)
