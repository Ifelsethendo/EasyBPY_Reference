import bpy
from easybpy import *

#  Translate Move
# Moved the object 5 units along the X axis.
move_along_axis(5.0, Vector((1,0,0)), object)
# 'object' can accept either a single object.
# or a list of objects.

# You can also use make_vector to build a Vector type.
axis = make_vector([1,0,0])
move_along_axis(5.0, axis, object)

# Moves 'object' 5 units along the global X axis.
translate_along_x(5, object)
move_along_x(5, object)

# Moves 'object' 5 units along the local X axis.
translate_along_local_x(5, object)
move_along_local_x(5, object)
