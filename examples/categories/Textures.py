import bpy
from easybpy import *

#  Textures
# Creates a new texture of the type 'CLOUDS'.
tex = create_texture("Name", 'CLOUDS')

# Gets the texture of the given name.
tex = get_texture("Name")

# Gets a list of all texture in the file.
textures = get_all_textures()

# Renames the given texture with the new name.
rename_texture(texture, "Name")

# Deletes the given texture.
delete_texture(texture)
