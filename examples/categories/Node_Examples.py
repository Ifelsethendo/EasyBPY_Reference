import bpy
from easybpy import *

#  Node Examples
a = active_object()

# Get material and nodes:
m = get_material(a)
nodes = get_nodes(m)

# Create texture node:
texnode = create_node(nodes, "ShaderNodeTexImage")

# Get the Principled BSDF node:
bsdf = get_node(nodes, "Principled BSDF")

# Create a link between the two nodes:
create_node_link(texnode.outputs[0], bsdf.inputs[0])

# Create image:
img = create_image("Text", 256, 256)

# Connect the image to the texture node:
texnode.image = img
