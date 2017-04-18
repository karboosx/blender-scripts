import bpy
print("Object, Verts, faces, edges")

objects_count = 0
poly_sum = 0
poly_max = 0
poly_min = 999999999

for element in bpy.context.scene.objects:
    if element.type != "MESH": continue
    
    #if ('.001' in element.name):
        #element.name = (element.name.replace('.001', '_mobile'))
        
    print("%s\t%i\t%i\t%i" % (element.name, len(element.data.vertices), len(element.data.polygons), len(element.data.edges)))
    
    poly = len(element.data.polygons)
    
    objects_count=objects_count+1
    poly_sum=poly_sum+poly
    
    if (poly_min>poly):
        poly_min=poly
        
    if (poly_max<poly):
        poly_max=poly
        
    
    
    
print("objects count = %i" % (objects_count))
print("avg poly = %i" % (poly_sum/objects_count))
print("min poly = %i max poly = %i" % (poly_min,poly_max))
