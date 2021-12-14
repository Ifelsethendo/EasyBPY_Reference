import bpy
from easybpy import *

#  Collections
# Create a new collection with the given name.
create_collection("New Collection")

# Deletes the given collection. The second argument decides
# whether to delete objects contained within the collection.
delete_collection(collection, True)

# Deletes all objects within the given collection.
deletes_objects_in_collection(collection)

# Deletes the entire hierarchy of the given collection.
delete_hierarchy(collection)

# Duplicates the collection as well as its contents.
duplicate_collection(collection)

# Returns a reference to the collection found by name.
# If no argument is provided, returns the active collection.
get_collection("Collection")

# Returns a list of all collections.
collections = get_all_collections()

# Links an object to a given collection.
link_object_to_collection(object, collection)

# Links a list of object to a given collection.
link_objects_to_collection(objects, collection)

# Unlinks an object from a given collection.
unlink_object_from_collection(object, collection)

# Unlinks a list of objects from a given collection.
unlink_objects_from_collection(objects, collection)

# Moves an object to a given collection.
move_object_to_collection(object, collection)

# Moves a list of objects to a given collection.
move_objects_to_collection(objects, collection)

# Returns a reference to an object's first collection.
get_object_collection(object)

# Returns a list of references to an object's collections.
get_object_collections(object)

# Returns True or False for if the collection exists.
exists = collection_exists("Collection")
