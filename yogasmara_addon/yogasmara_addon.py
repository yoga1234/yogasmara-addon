import bpy

class YogasmaraAddon(bpy.types.Panel):
  bl_idname= = "PT_yogasmara_addon" # Panel Type Yogasmara Addon
  bl_category = "Yogasmara Addon"
  bl_space_type = "VIEW_3D" # Where the panel will placed
  bl_region_type = "UI"


def register():
  bpy.utils.register_class(YogasmaraAddon)

def unregister():
  bpy.utils.unregister_class(YogasmaraAddon)

if __name__ == "__main__":
  register()