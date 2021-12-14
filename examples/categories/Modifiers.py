import bpy
from easybpy import *

#  Modifiers
# Adds a modifier of the given type to object.
add_modifier(object, "Name", 'SUBFURF')

# Gets a reference to modifier of given name.
mod = get_modifier(object, "Name")

# Removes a modifier of given name from object.
remove_modifier (object, "Name")

# Applies all modifiers on a given object.
apply_all_modifiers(object)
