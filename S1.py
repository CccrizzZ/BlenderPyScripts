import bpy
from random import randint



# select all object in scene
for obj in bpy.context.scene.objects:
   if obj.type == 'MESH':
       obj.select_set(True)
   else:
       obj.select_set(False)



# delete selected object
bpy.ops.object.delete()




# for i in range(0,300):
#    x = randint(-30, 30)
#    y = randint(-30, 30)
#    z = randint(-30, 30)
#    bpy.ops.mesh.primitive_monkey_add(location=(x,y,z))