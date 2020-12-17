import bpy
        
class YogasmaraFileManager(bpy.types.Panel):
    bl_idname = "PANEL_PT_yogasmara_file_manager" # Panel Type yogasmara file manager
    bl_category = "Yogasmara Addon" # Name of the addon
    bl_space_type = "VIEW_3D" # where the addon will be placed
    bl_region_type = "UI"
    bl_label = "File Manager"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("wm.open_mainfile", text="Open File")
        
        row = layout.row()
        row.operator("wm.save_mainfile", text="Save File")
        
class YogasmaraDeleteManager(bpy.types.Panel):
    bl_idname = "PANEL_PT_yogasmara_delete_manager"
    bl_category = "Yogasmara Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Delete Manager"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("object.delete", text="Smooth")
        
        
 
def register():
    bpy.utils.register_class(YogasmaraFileManager)
    bpy.utils.register_class(YogasmaraDeleteManager)

def unregister():
    bpy.utils.unregister_class(YogasmaraFileManager)
    bpy.utils.unregister_class(YogasmaraDeleteManager)
        
if __name__ == "__main__":
    register()
    
