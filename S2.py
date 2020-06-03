import bpy

# Creating a panel
class MyPanel(bpy.types.Panel):
    bl_label = "My Panel"
    bl_idname = "PT_MyPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MyPanel"
# bl_options = {'DEFAULT_CLOSED'}
    
    # draw panel
    def draw(self, context):
        layout = self.layout
        
        # row1
        row = layout.row()
        row.label(text=None, icon='MATCUBE')
        row.operator("object.select_all", text="Toggle select all object").action = 'TOGGLE'
        
        # row2
        row = layout.row()
        row.operator('mesh.primitive_cube_add', icon='CUBE')
        row.operator('mesh.primitive_torus_add', icon='MESH_TORUS')
        
        # row3
        row = layout.row()
        row.operator('object.text_add', icon='FONT_DATA')
        
        
        
def register():
    bpy.utils.register_class(MyPanel)

def unregister():
    bpy.utils.unregister_class(MyPanel)



register()