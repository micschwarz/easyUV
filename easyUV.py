#-------------------------------------------------------------------------------------------
#Plugin Infos
bl_info={
    "name" : "easyUV",
    "author" : "Michael S.",
    "version" : (0,1),
    "blender" : (2, 77, 0),
    "location" : "Properties > Material",
    "description" : "easy UV making",
    "category" : "Material"
}
#-------------------------------------------------------------------------------------------
import bpy
from bpy.props import *

#Attribute
atr = bpy.types.Scene

#atr.name = StringProperty(name = "name", default = "lol", description = "text")

#shared functions
class sf(bpy.types.Operator):
    #edit mode: m == True -> select all verts
    def edit(m):
        sop = bpy.ops
        sop.object.editmode_toggle()
        if m == True:
            sop.mesh.select_all(action='TOGGLE')
            sop.mesh.select_all(action='TOGGLE')
        return {'FINISHED'}

#Create UI: Tools Tab
class window (bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"
    bl_label = "easy UV"
    bl_category = "easyUV"
    
    
    def draw(self, context):
        layout = self.layout
        row = layout.row(align = True)
        row.operator("uv.cube",text = "Cube", icon="MESH_CUBE")
        row.operator("uv.sphere",text = "Sphere", icon="MATSPHERE")
        row.operator("uv.plane",text = "Plane", icon="MESH_PLANE")
   
        
#Create UI: Buttons

#UV Cube
class OBJECT_OT_buttonCube(bpy.types.Operator):
    bl_label = "Cube"
    bl_idname = "uv.cube"
    bl_description = "Create Cube UV"
    
    def execute(self, context):       
        #Shorts
        p = print
        scene = bpy.context.scene
        sop = bpy.ops        
    
        #Uv Map
        sf.edit(True)
        sop.uv.cube_project()
        sf.edit(False)
        return{'FINISHED'}
    
#UV Sphere
class OBJECT_OT_buttonSphere(bpy.types.Operator):
    bl_label = "Cube"
    bl_idname = "uv.sphere"
    bl_description = "Create Sphere UV"
    
    def execute(self, context):       
        #Shorts
        p = print
        scene = bpy.context.scene
        sop = bpy.ops        
    
        #Uv Map
        sf.edit(True)
        sop.uv.sphere_project()
        sf.edit(False)
        return{'FINISHED'}
    
#UV Plane
class OBJECT_OT_buttonPlane(bpy.types.Operator):
    bl_label = "Cube"
    bl_idname = "uv.plane"
    bl_description = "Create Plane UV"
    
    def execute(self, context):       
        #Shorts
        p = print
        scene = bpy.context.scene
        sop = bpy.ops        
    
        #Uv Map
        sf.edit(True)
        sop.uv.unwrap(method='ANGLE_BASED', margin=0.001)
        sf.edit(False)
        return{'FINISHED'}
    
        
def register(): bpy.utils.register_module(__name__)
    
def unregister(): bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__": register()