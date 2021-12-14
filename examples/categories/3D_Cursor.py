import bpy
from easybpy import *

#  3D Cursor
selection_to_cursor_without_offset()
selection_to_cursor_with_offset()
cursor_to_world_origin()
cursor_to_selection()
cursor_to_active()
selection_to_grid()
cursor_to_grid()

location = get_cursor_location()
set_cursor_location(new_location)
rotation = get_cursor_rotation()
mode = get_cursor_rotation_mode()
