# -------------------------------------------------------------------------------------------
# Plugin Infos
bl_info = {
    "name": "easyUV",
    "author": "Michael S.",
    "version": (0, 2, 1),
    "blender": (2, 80, 0),
    "location": "Properties > Material",
    "description": "easy UV mapping",
    "category": "Material"
}
# -------------------------------------------------------------------------------------------

import bpy

class SharedFunctions():
    @staticmethod
    def setEditMode(editMode):
        # Get which mode to set
        setMode = "OBJECT"
        if editMode:
            setMode = "EDIT"
        
        # Set proper Mode
        bpy.ops.object.mode_set(mode = setMode)
        
        if editMode:
            bpy.ops.mesh.select_all(action = "SELECT")
        

class LayoutEasyUvPanel(bpy.types.Panel):
    bl_label = "easyUV"
    bl_idname = "SCENE_EASY_UV_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        row = layout.row(align = True)
        
        row.operator("uv.cube", icon="MESH_CUBE")
        row.operator("uv.sphere", icon="MATSPHERE")
        row.operator("uv.plane", icon="MESH_PLANE")
        
# Operators
class UvCubeOperator(bpy.types.Operator):
    bl_idname = "uv.cube"
    bl_label = "Cube"
    
    returnToModeObject = True

    @classmethod
    def poll(self, context):
        self.returnToModeObject = context.mode == 'OBJECT'
        return (True)

    def execute(self, context):
        SharedFunctions.setEditMode(True)
        bpy.ops.uv.cube_project()
        
        if self.returnToModeObject:
            SharedFunctions.setEditMode(False)
            
        return {'FINISHED'}

class UvSphereOperator(bpy.types.Operator):
    bl_idname = "uv.sphere"
    bl_label = "Sphere"

    @classmethod
    def poll(self, context):
        self.returnToModeObject = context.mode == 'OBJECT'
        return (True)

    def execute(self, context):
        SharedFunctions.setEditMode(True)
        bpy.ops.uv.sphere_project()
        
        if self.returnToModeObject:
            SharedFunctions.setEditMode(False)
        
        return {'FINISHED'}
    
class UvPlaneOperator(bpy.types.Operator):
    bl_idname = "uv.plane"
    bl_label = "Plane"

    @classmethod
    def poll(self, context):
        self.returnToModeObject = context.mode == 'OBJECT'
        return (True)

    def execute(self, context):
        SharedFunctions.setEditMode(True)
        bpy.ops.uv.unwrap()
        
        if self.returnToModeObject:
            SharedFunctions.setEditMode(False)
        
        return {'FINISHED'}
    
# Addon Stuff
def register():
    # Register Operators
    bpy.utils.register_class(UvCubeOperator)
    bpy.utils.register_class(UvSphereOperator)
    bpy.utils.register_class(UvPlaneOperator)
    
    # Register Panel
    bpy.utils.register_class(LayoutEasyUvPanel)


def unregister():
    # Unregister Operators
    bpy.utils.unregister_class(UvCubeOperator)
    bpy.utils.unregister_class(UvSphereOperator)
    bpy.utils.unregister_class(UvPlaneOperator)
    
    # Unregister Panel
    bpy.utils.unregister_class(LayoutEasyUvPanel)


if __name__ == "__main__":
    register()
