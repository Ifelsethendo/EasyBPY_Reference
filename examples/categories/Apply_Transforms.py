import bpy
from easybpy import *

#  Apply Transforms
# Applies the location (Ctrl+A -> Location)
apply_location(object)

# Applies the rotation (Ctrl+A -> Rotation)
apply_rotation(object)

# Applies the scale (Ctrl+A -> Scale)
apply_scale(object)

# Applies rotation and scale (Ctrl+A -> Rotation & Scale)
apply_rotation_and_scale(object)

# Applies all transofmrs (Ctrl+A -> All Transforms)
apply_all_transforms(object)
