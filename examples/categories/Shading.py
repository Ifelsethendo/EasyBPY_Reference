import bpy
from easybpy import *

#  Shading
# Sets an object's shade type to smooth:
shade_object_smooth(object)

# Sets an object's shade type to flat.
shade_object_flat(object)
shade_flat(object)

# Enabled auto smooth and sets the angle to '60' degrees.
set_smooth_angle(object, 60)
