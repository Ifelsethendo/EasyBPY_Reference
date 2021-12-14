import bpy
from easybpy import *

#  Advanced Selection
# Returns a list of object containing "Cube" in their name.
cubes = get_objects_including("Cube")

# Selects all objects containing "Cube" in their name.
select_objects_including("Cube")

# Gets all objects with more than 3000 vertices.
objs = get_objects_by_vertex(3000, "GREATER")

# Selects all objects with less than 3000 vertices.
select_objects_by_vertex(3000, "LESS")
