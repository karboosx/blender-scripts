import bpy
print("Object, Verts, faces, edges")
for element in bpy.context.scene.objects:
    if element.type != "MESH": continue
    
    element.data.name = element.name
    
