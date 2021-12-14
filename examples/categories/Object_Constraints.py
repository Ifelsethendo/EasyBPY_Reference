import bpy
from easybpy import *

#  Object Constraints
# Get the active object.
obj = active_object()

# Add the copy location constraint.
con = add_constraint('COPY_LOCTION', obj, "Name")

# Remove the constraint.