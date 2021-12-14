import bpy
from easybpy import *

#  Materials
# Creates a new material with the given name.
create_material("Name")

# Returns True or False for if the material exists.
exists = material_exists(material)

# Deletes the given material.
delete_material(material)

# Adds the given material to the object.
add_material_to_object(object, material)

# Remove given material from the object.
remove_material_from_object(object, material)

# Returns a list of all material.
material = get_all_materials()

# Returns a list of materials assigned to a given object.
materials = get_materials_from_object(object)
