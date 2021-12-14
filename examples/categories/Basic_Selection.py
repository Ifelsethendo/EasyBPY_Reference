import bpy
from easybpy import *

#  Basic Selection
# Returns the active object.
my_object = active_object()

# Returns all selected objects.
my_objects = selected_objects()

# Selects all objects in the scene.
select_all_objects()

# Selects all light objects in the scene.
lights = select_all_lights()

# Inverts the current selection.
invert_selection()

# Returns a list of objects that have at least one modifier.
mod_objects = get_objects_with_modifiers()

# Selects all objects that have at least one modifier.
select_objects_with_modifiers()
