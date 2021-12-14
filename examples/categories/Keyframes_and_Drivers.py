import bpy
from easybpy import *

#  Keyframes and Drivers
# Adds a keyframe of the location property at frame 0.
obj = active_object()
key_loc = add_keyframe(obj, "location", 0)

# Removes the location location keyframes.
remove_keyframe(key_loc)

# Adds drivers for each of the X,Y,Z location values.
driver = add_driver(obj, "location")

# Sets the X value to follow, the frame number.
driver[0].expression = 'frame'

# Removes the driver from the  X value.
remove_driver(driver[0])
