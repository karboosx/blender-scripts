import bpy
import os

# get the current path and make a new folder for the exported meshes
path = bpy.path.abspath('//Env//')

if not os.path.exists(path):
    os.makedirs(path)

for object in bpy.context.selected_objects:

    # deselect all meshes
    bpy.ops.object.select_all(action='DESELECT')

    # select the object
    object.select = True

    # export object with its name as file name
    fPath = str((path + object.name + '.fbx'))

    #bpy.context.active_object = object
    bpy.ops.export_scene.fbx(filepath=fPath,use_selection=True, bake_space_transform=True)
