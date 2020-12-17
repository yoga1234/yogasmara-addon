import bpy

class YogasmaraDeleteAll(bpy.types.Operator):
    """Delete all available object on the scene"""
    bl_idname = "object.delete_all"
    bl_label = "Delete All Object"
    
    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=True)
        
        return {'FINISHED'}
        
        
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
        
class YogasmaraObjectManager(bpy.types.Panel):
    bl_idname = "PANEL_PT_yogasmara_object_manager"
    bl_category = "Yogasmara Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Object Manager"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("object.delete", text="Delete Selected Object")
        
        row = layout.row()
        row.operator("outliner.delete", text="Delete All Object").hierarchy = True
        
        row = layout.row()
        row.operator("object.select_all", text="Select All Object")
        
class YogasmaraMeshManager(bpy.types.Panel):
    bl_idname = "PANEL_PT_yogasmara_mesh_manager"
    bl_category = "Yogasmara Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Mesh Manager"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator("mesh.primitive_plane_add", text="Add New Plane")
        
        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Add New Cube")
        
        row = layout.row()
        row.operator("mesh.primitive_circle_add", text="Add New Circle")
        
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", text="Add New UV Sphere")
        
        row = layout.row()
        row.operator("mesh.primitive_ico_sphere_add", text="Add New ICO Sphere")
        
        row = layout.row()
        row.operator("mesh.primitive_cylinder_add", text="Add New Cylinder")
        
        row = layout.row()
        row.operator("mesh.primitive_cone_add", text="Add New Cone")
        
        row = layout.row()
        row.operator("mesh.primitive_torus_add", text="Add New Torus")
        
        
 
def register():
    bpy.utils.register_class(YogasmaraFileManager)
    bpy.utils.register_class(YogasmaraObjectManager)
    bpy.utils.register_class(YogasmaraMeshManager)
    bpy.utils.register_class(YogasmaraDeleteAll)

def unregister():
    bpy.utils.unregister_class(YogasmaraFileManager)
    bpy.utils.unregister_class(YogasmaraObjectManager)
    bpy.utils.unregister_class(YogasmaraMeshManager)
    bpy.utils.unregister_class(YogasmaraDeleteAll)
        
if __name__ == "__main__":
    register()
    
