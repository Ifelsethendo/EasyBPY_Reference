import bpy
from easybpy import *

#  Translate Scale
# Scale an object 5 units along an axis.
scale_along_axis(5, axis, object)

# Scale an object 5 units along the global X axis
scale_along_x(5, object)

# Scale an object 5 units along the local X axis.
scale_along_local_x(5, object)

# Scale an object 5 units prependicular to the X axis.
scale_perpendicular_to_x(5, object)
