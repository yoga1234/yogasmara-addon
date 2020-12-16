import bpy
        
class YogasmaraFileManager(bpy.types.Panel):
    bl_idname = "PT_yogasmara_file_manager" # Panel Type yogasmara file manager
    bl_category = "Yogasmara Addon" # Name of the addon
    bl_space_type = "VIEW_3D" # where the addon will be placed
    bl_region_type = "UI"
    bl_label = "File Manager"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("wm.open_mainfile")
        
        row = layout.row()
        row.operator("wm.save_mainfile")
 
def register():
    bpy.utils.register_class(YogasmaraFileManager)

def unregister():
    bpy.utils.unregister_class(YogasmaraFileManager)
    
if __name__ == "__main__":
    register()
    
