import bpy

def rename_selected(context, x):
    """rename selected object to string x"""
    for ob in context.selected_objects:
        ob.name = x # change the object name

class RenameSelected(bpy.types.Operator):
    """Rename selected objects"""
    bl_idname= "object.rename_selected"
    bl_label = "Rename Selected"
    bl_options = {'UNDO','REGISTER'}
    new_name = bpy.props.StringProperty(default = 'steer')
    def execute(self,context):
        rename_selected(context, self.new_name)
        return {'FINISHED'}

bpy.utils.register_class(RenameSelected)
