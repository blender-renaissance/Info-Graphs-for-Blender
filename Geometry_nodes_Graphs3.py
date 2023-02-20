bl_info = {
    "name": "Info_graphs_for_blender",
    "author": "Vikrant Jadhav, Blender Renaissance",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "View3D > Sidebar > Renaissance tab",
    "description": "Quick Render Presets for Blender Renaissance Graphs.",
    "warning": "",
    "doc_url": "https://twitter.com/b3d_Renaissance",
    "category": "3D View",
}


import bpy
import os

from bpy.types import (Panel,
                       Menu,
                       PropertyGroup,
                       )
                       
class MyProperties(bpy.types.PropertyGroup):
    
    my_enum : bpy.props.EnumProperty(
        name= "",
        description= "Change Resolution / Aspect Ratio of the scene",
        items= [('OP1', "Rectangle [1920x1080]", "1080p"),
                ('OP2', "Rectangle [3840x2160]", "4K"),
                ('OP3', "Square [1080x1080]", "Instagram Ratio"),
                ('OP4', "Square [720x720]", "Instagram mini Ratio"),
                ('OP5', "Vertical [1080x1920]", "Youtube Vertical"),
                ('OP6', "Vertical [720x1280]", "Tiktok Vertical"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operator()
    )
    
    my_enum0 : bpy.props.EnumProperty(
        name= "",
        description= "Change the render engine of the scene",
        items= [('OP1', "Cycles (for CPU rendering)", "f"),
                ('OP2', "Eevee (Nvidia GPU rendering)", "fg"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operator00()
    )
    
    my_enum2 : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OP7', "24 FPS (and reset to 4 seconds)", "24 Frames per second"),
                ('OP8', "30 FPS (and reset to 4 seconds)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operator2()
    )

    my_enum2pie : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OP7pie', "24 FPS (and reset to 4 seconds)", "24 Frames per second"),
                ('OP8pie', "30 FPS (and reset to 4 seconds)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operator2pie()
    )
    
    my_enumLGpie : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPLG7pie', "24 FPS (and reset)", "24 Frames per second"),
                ('OPLG8pie', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgpie()
    )
    
    my_enumHBpie : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPHB7pie', "24 FPS (and reset)", "24 Frames per second"),
                ('OPHB8pie', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbpie()
    )
    
    my_enumMCpie : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPMC7pie', "24 FPS (and reset)", "24 Frames per second"),
                ('OPMC8pie', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatormcpie()
    )

    my_enumMPpie : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPMP7pie', "24 FPS (and reset)", "24 Frames per second"),
                ('OPMP8pie', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatormppie()
    )

    
    my_enum3 : bpy.props.EnumProperty(
        name= "",
        description= "Change Output Format of the Final Render",
        items= [('OP9', "PNG Image Sequence", "(with transparency)"),
                ('OP10', "OpenEXR Image Sequence", "(with transparency)"),
                ('OP11', "MP4 Video", "(No transparency)"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operator3()
    )
    
    my_float: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 3,
        min = 0.1,
        max = 30.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorgg()
        )
        
    my_floatpie: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 30.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorggpie()
        )
        
    my_float2: bpy.props.FloatProperty(
        name = "Excess seconds",
        description = "A float2 property",
        default =0,
        min = 0,
        max = 100000,
        update=lambda self, context: bpy.ops.addonname.myop_operatori()
        )
        
    my_float2pie: bpy.props.FloatProperty(
        name = "Excess seconds",
        description = "A float2 property",
        default =0,
        min = 0,
        max = 100000,
        update=lambda self, context: bpy.ops.addonname.myop_operatoripie()
        )
        
    my_path: bpy.props.StringProperty(
        name = "",
        description="Choose a Font:",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        update=lambda self, context: bpy.ops.addonname.myop_operatorf()
        )
        
    my_pathpie: bpy.props.StringProperty(
        name = "",
        description="Choose a Font:",
        default="",
        maxlen=1024,
        subtype='FILE_PATH',
        update=lambda self, context: bpy.ops.addonname.myop_operatorfpie()
        )
        
    my_path2: bpy.props.StringProperty(
        name = "",
        description="Choose a Font:",
        default="//Rendered/rendered####",
        maxlen=1024,
        subtype='FILE_PATH',
        update=lambda self, context: bpy.ops.addonname.myop_operatorffg()
        )


class TestPanel(bpy.types.Panel):
    bl_label = "Quick Render Presets"
    bl_idname = "PT_TestPanel"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"} 
   
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool        
        
        rowD = layout.row()
        rowD.label(text= "Render buttons:")
        
        row0 = layout.row()
        row0.operator("render.render", text="Render Image (and save in path)", icon='RENDER_STILL').write_still = True
        
        row00 = layout.row()
        row00.operator("render.render", text="Render Animation", icon='RENDER_ANIMATION').animation = True
        
        rowAA = layout.row()
        rowAA.label(text= "Render Engine:")
        
        layout.prop(mytool, "my_enum0")
        
        row = layout.row()
        row.label(text= "Aspect Ratio and Resolution:")
        
        layout.prop(mytool, "my_enum")
        
        rowC = layout.row()
        rowC.label(text= "Output Format:")
        
        layout.prop(mytool, "my_enum3")
        
        rowFFG = layout.row()
        rowFFG.label(text= "Path:")
        layout.prop(mytool, "my_path2")
        

class TestPanel2(bpy.types.Panel):
    bl_label = "Circle Graph"
    bl_idname = "PT_TestPanel2"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowB = layout.row()
        rowB.label(text= "Frames per second:")
        
        layout.prop(mytool, "my_enum2")
       
        rowE = layout.row()
        rowE.label(text= "Length of Animation:")
        layout.prop(mytool, "my_float")
        
        rowG = layout.row()
        rowG.label(text= "Excess seconds:")
        layout.prop(mytool, "my_float2")

        
class TestPanel3(bpy.types.Panel):
    bl_label = "Pie Graph"
    bl_idname = "PT_TestPanel3"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowB = layout.row()
        rowB.label(text= "Frames per second:")
        
        layout.prop(mytool, "my_enum2pie")
       
        rowE = layout.row()
        rowE.label(text= "Length of Animation:")
        layout.prop(mytool, "my_floatpie")
        
        rowG = layout.row()
        rowG.label(text= "Excess seconds:")
        layout.prop(mytool, "my_float2pie")
        
class TestPanel4(bpy.types.Panel):
    bl_label = "Line Graph"
    bl_idname = "PT_TestPanel4"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowLG = layout.row()
        rowLG.label(text= "Frames per second:")
        
        layout.prop(mytool, "my_enumLGpie")

class TestPanel5(bpy.types.Panel):
    bl_label = "Horizontal Bar Graph"
    bl_idname = "PT_TestPanel5"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowHB = layout.row()
        rowHB.label(text= "Frames per second:")
        
        layout.prop(mytool, "my_enumHBpie")

class TestPanel6(bpy.types.Panel):
    bl_label = "Multiple Circle Graph"
    bl_idname = "PT_TestPanel6"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowMC = layout.row()
        rowMC.label(text= "Frames per second:")
        
        layout.prop(mytool, "my_enumMCpie")
        
class TestPanel7(bpy.types.Panel):
    bl_label = "Multiple Pie Graph"
    bl_idname = "PT_TestPanel7"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowMP = layout.row()
        rowMP.label(text= "Frames per second:")
        
        layout.prop(mytool, "my_enumMPpie")
        
class ADDONNAME_OT_my_opgg(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorgg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle_GraphAction'
        data_path = 'modifiers["GeometryNodes"]["Input_30"]'
        index = 0
        jeff = bpy.context.scene.render.fps    
        bob = jeff*(1+mytool.my_float)               # Z axis

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeff
                
                bob = int(bob)
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bob
                kpz.handle_left[0] = bob/2
                kpz.handle_right[0] = bob+1
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bob+jeff


             
        return {'FINISHED'}

class ADDONNAME_OT_my_opggpie(bpy.types.Operator):
    bl_label = "Add Objecggggggtpie"
    bl_idname = "addonname.myop_operatorggpie"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.001Action'
        data_path = 'modifiers["GeometryNodes"]["Input_25"]'
        index = 0
        jeffpie = bpy.context.scene.render.fps    
        bobpie = jeffpie*(1+mytool.my_floatpie)              # Z axis

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffpie
                
                bobpie = int(bobpie)
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobpie
                kpz.handle_left[0] = bobpie/2
                kpz.handle_right[0] = bobpie+1
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobpie+jeffpie


             
        return {'FINISHED'}    

class RenderRender2(bpy.types.Operator):
    bl_label = "Render Engine"
    bl_idname = "addonname.myop_operator00"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        if mytool.my_enum0 == 'OP1':
            bpy.context.scene.render.engine = 'CYCLES'
            bpy.context.scene.cycles.device = 'CPU'
            bpy.context.scene.cycles.preview_samples = 20
            bpy.context.scene.cycles.samples = 20
            bpy.context.scene.render.film_transparent = True

            print("tried cycles")
                      
        if mytool.my_enum0 == 'OP2':
            bpy.context.scene.render.engine = 'BLENDER_EEVEE'
            bpy.context.scene.eevee.taa_render_samples = 64

            print("tried eevee")
        print("in execute")

            
        return {'FINISHED'}

class ADDONNAME_OT_my_op(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operator"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        if mytool.my_enum == 'OP1':
            scene.render.resolution_x = 1920
            scene.render.resolution_y = 1080
            scene.objects["PlaneC"].scale.x = 2.568
            scene.objects["PlaneC"].scale.y = 1.445
            scene.objects["PlaneC"].location.y = -0.012
                       
        if mytool.my_enum == 'OP2':
            scene.render.resolution_x = 3840
            scene.render.resolution_y = 2160
            scene.objects["PlaneC"].scale.x = 2.568
            scene.objects["PlaneC"].scale.y = 1.445
            scene.objects["PlaneC"].location.y = -0.012
                                   
        if mytool.my_enum == 'OP3':
            scene.render.resolution_x = 1080
            scene.render.resolution_y = 1080
            scene.objects["PlaneC"].scale.x = 2.568
            scene.objects["PlaneC"].scale.y = 2.568
            scene.objects["PlaneC"].location.y = -0.012
            
        if mytool.my_enum == 'OP4':
            scene.render.resolution_x = 720
            scene.render.resolution_y = 720
            scene.objects["PlaneC"].scale.x = 2.568
            scene.objects["PlaneC"].scale.y = 2.568
            scene.objects["PlaneC"].location.y = -0.012
            
        if mytool.my_enum == 'OP5':
            scene.render.resolution_x = 1080
            scene.render.resolution_y = 1920
            scene.objects["PlaneC"].scale.x = 1.445
            scene.objects["PlaneC"].scale.y = 2.568
            scene.objects["PlaneC"].location.y = -0.012
            
        if mytool.my_enum == 'OP6':
            scene.render.resolution_x = 720
            scene.render.resolution_y = 1280
            scene.objects["PlaneC"].scale.x = 1.445
            scene.objects["PlaneC"].scale.y = 2.568
            scene.objects["PlaneC"].location.y = -0.012
        
        return {'FINISHED'}
    
class ADDONNAME_OT_my_op2(bpy.types.Operator):
    bl_label = "Add Ob33ject"
    bl_idname = "addonname.myop_operator2"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enum2 == 'OP7':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 144
            
            action_name = 'Circle_GraphAction'
            data_path = 'modifiers["GeometryNodes"]["Input_30"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[1].co.x = 120
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            
        if mytool.my_enum2 == 'OP8':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 180
            
            action_name = 'Circle_GraphAction'
            data_path = 'modifiers["GeometryNodes"]["Input_30"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[1].co.x = 150
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

        return {'FINISHED'}

class ADDONNAME_OT_my_op2pie(bpy.types.Operator):
    bl_label = "Add Ob33ject2"
    bl_idname = "addonname.myop_operator2pie"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enum2pie == 'OP7pie':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 144
            
            action_name = 'Circle Graph.001Action'
            data_path = 'modifiers["GeometryNodes"]["Input_25"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[1].co.x = 120
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            
        if mytool.my_enum2pie == 'OP8pie':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 180
            
            action_name = 'Circle Graph.001Action'
            data_path = 'modifiers["GeometryNodes"]["Input_25"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[1].co.x = 150
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

        return {'FINISHED'}

class ADDONNAME_OT_my_oplgpie(bpy.types.Operator):
    bl_label = "Add Ob33jectlg"
    bl_idname = "addonname.myop_operatorlgpie"  
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enumLGpie == 'OPLG7pie':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 96
            
            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_26"]'
            index = 0              # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 32
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 48
                    fcurve.keyframe_points[1].handle_left[0] = 40
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 56
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_27"]'
            index = 0              # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 32
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 48
                    fcurve.keyframe_points[1].handle_left[0] = 40
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 56
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_28"]'
            index = 0              # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 32
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 48
                    fcurve.keyframe_points[1].handle_left[0] = 40
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 56
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_29"]'
            index = 0              # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 32
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 48
                    fcurve.keyframe_points[1].handle_left[0] = 40
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 56
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_30"]'
            index = 0              # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 32
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 48
                    fcurve.keyframe_points[1].handle_left[0] = 40
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 56
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_31"]'
            index = 0              # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 32
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 48
                    fcurve.keyframe_points[1].handle_left[0] = 40
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 56
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_32"]'
            index = 0              # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 32
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 48
                    fcurve.keyframe_points[1].handle_left[0] = 40
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 56
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_33"]'
            index = 0              # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 32
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 48
                    fcurve.keyframe_points[1].handle_left[0] = 40
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 56
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")


            
        if mytool.my_enumLGpie == 'OPLG8pie':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 120
            
            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_26"]'
            index = 0               # Z axis
            

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 40
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 60
                    fcurve.keyframe_points[1].handle_left[0] = 50
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 70
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_27"]'
            index = 0               # Z axis
            

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 40
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 60
                    fcurve.keyframe_points[1].handle_left[0] = 50
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 70
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_28"]'
            index = 0               # Z axis
            

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 40
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 60
                    fcurve.keyframe_points[1].handle_left[0] = 50
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 70
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_29"]'
            index = 0               # Z axis
            

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 40
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 60
                    fcurve.keyframe_points[1].handle_left[0] = 50
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 70
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_30"]'
            index = 0               # Z axis
            

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 40
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 60
                    fcurve.keyframe_points[1].handle_left[0] = 50
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 70
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_31"]'
            index = 0               # Z axis
            

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 40
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 60
                    fcurve.keyframe_points[1].handle_left[0] = 50
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 70
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_32"]'
            index = 0               # Z axis
            

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 40
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 60
                    fcurve.keyframe_points[1].handle_left[0] = 50
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 70
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'CubeAction.001'
            data_path = 'modifiers["GeometryNodes"]["Input_33"]'
            index = 0               # Z axis
            

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_left[0] = 16
                    fcurve.keyframe_points[0].handle_left[1] = 0
                    fcurve.keyframe_points[0].handle_right[0] = 40
                    fcurve.keyframe_points[0].handle_right[1] = 0
                    fcurve.keyframe_points[1].co.x = 60
                    fcurve.keyframe_points[1].handle_left[0] = 50
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 70
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")



        return {'FINISHED'}

class ADDONNAME_OT_my_ophbpie(bpy.types.Operator):
    bl_label = "Add Ob33ject2"
    bl_idname = "addonname.myop_operatorhbpie"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enumHBpie == 'OPHB7pie':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 168
            
            action_name = 'Plane.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_28"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_right[1] = 0.573
                    fcurve.keyframe_points[1].co.x = 120
                    fcurve.keyframe_points[1].handle_left[0] = 66.708
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
                
            action_name = 'Plane.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_29"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_right[1] = 0.573
                    fcurve.keyframe_points[1].co.x = 120
                    fcurve.keyframe_points[1].handle_left[0] = 66.708
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
                
            action_name = 'Plane.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_30"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_right[1] = 0.573
                    fcurve.keyframe_points[1].co.x = 120
                    fcurve.keyframe_points[1].handle_left[0] = 66.708
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
                
            action_name = 'Plane.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_31"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_right[1] = 0.573
                    fcurve.keyframe_points[1].co.x = 120
                    fcurve.keyframe_points[1].handle_left[0] = 66.708
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            
        if mytool.my_enumHBpie == 'OPHB8pie':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 210
            
            action_name = 'Plane.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_28"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_right[1] = 0.757
                    fcurve.keyframe_points[1].co.x = 150
                    fcurve.keyframe_points[1].handle_left[0] = 90
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
                
            action_name = 'Plane.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_29"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_right[1] = 0.757
                    fcurve.keyframe_points[1].co.x = 150
                    fcurve.keyframe_points[1].handle_left[0] = 90
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
                
            action_name = 'Plane.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_30"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_right[1] = 0.757
                    fcurve.keyframe_points[1].co.x = 150
                    fcurve.keyframe_points[1].handle_left[0] = 90
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
                
            action_name = 'Plane.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_31"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_right[1] = 0.757
                    fcurve.keyframe_points[1].co.x = 150
                    fcurve.keyframe_points[1].handle_left[0] = 90
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

        return {'FINISHED'}

class ADDONNAME_OT_my_opmcpie(bpy.types.Operator):
    bl_label = "Add Ob33ject2"
    bl_idname = "addonname.myop_operatormcpie"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enumMCpie == 'OPMC7pie':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 192
            
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Input_50"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_left[0] = 24
                    fcurve.keyframe_points[0].handle_left[1] = -7.667
                    fcurve.keyframe_points[0].handle_right[0] = 24
                    fcurve.keyframe_points[0].handle_right[1] = 0.623
                    fcurve.keyframe_points[1].co.x = 48
                    fcurve.keyframe_points[1].handle_left[0] = 37.893
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 55.667
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Input_51"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 48
                    fcurve.keyframe_points[0].handle_left[0] = 48
                    fcurve.keyframe_points[0].handle_left[1] = -0.675
                    fcurve.keyframe_points[0].handle_right[0] = 48
                    fcurve.keyframe_points[0].handle_right[1] = 0.675
                    fcurve.keyframe_points[1].co.x = 72
                    fcurve.keyframe_points[1].handle_left[0] = 60.567
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 90
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Input_52"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 72
                    fcurve.keyframe_points[0].handle_left[0] = 72
                    fcurve.keyframe_points[0].handle_left[1] = -0.576
                    fcurve.keyframe_points[0].handle_right[0] = 72
                    fcurve.keyframe_points[0].handle_right[1] = 0.576
                    fcurve.keyframe_points[1].co.x = 96
                    fcurve.keyframe_points[1].handle_left[0] = 80.1
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 121
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Input_53"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 96
                    fcurve.keyframe_points[0].handle_left[0] = 96
                    fcurve.keyframe_points[0].handle_left[1] = -0.704
                    fcurve.keyframe_points[0].handle_right[0] = 96
                    fcurve.keyframe_points[0].handle_right[1] = 0.699
                    fcurve.keyframe_points[1].co.x = 120
                    fcurve.keyframe_points[1].handle_left[0] = 109.4
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 151
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Input_54"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 120
                    fcurve.keyframe_points[0].handle_left[0] = 120
                    fcurve.keyframe_points[0].handle_left[1] = -0.896
                    fcurve.keyframe_points[0].handle_right[0] = 120
                    fcurve.keyframe_points[0].handle_right[1] = 0.762
                    fcurve.keyframe_points[1].co.x = 144
                    fcurve.keyframe_points[1].handle_left[0] = 132.836
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 145
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

        if mytool.my_enumMCpie == 'OPMC8pie':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 240
            
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Input_50"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_left[0] = 30
                    fcurve.keyframe_points[0].handle_left[1] = -0.623
                    fcurve.keyframe_points[0].handle_right[0] = 30
                    fcurve.keyframe_points[0].handle_right[1] = 0.623
                    fcurve.keyframe_points[1].co.x = 60
                    fcurve.keyframe_points[1].handle_left[0] = 47.614
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 72.398
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Input_51"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 60
                    fcurve.keyframe_points[0].handle_left[0] = 48
                    fcurve.keyframe_points[0].handle_left[1] = -0.623
                    fcurve.keyframe_points[0].handle_right[0] = 60.432
                    fcurve.keyframe_points[0].handle_right[1] = 0.519
                    fcurve.keyframe_points[1].co.x = 90
                    fcurve.keyframe_points[1].handle_left[0] = 72.7
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 91
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Input_52"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 90
                    fcurve.keyframe_points[0].handle_left[0] = 90
                    fcurve.keyframe_points[0].handle_left[1] = -0.841
                    fcurve.keyframe_points[0].handle_right[0] = 90
                    fcurve.keyframe_points[0].handle_right[1] = 0.576
                    fcurve.keyframe_points[1].co.x = 120
                    fcurve.keyframe_points[1].handle_left[0] = 102.946
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 121
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Input_53"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 120
                    fcurve.keyframe_points[0].handle_left[0] = 120
                    fcurve.keyframe_points[0].handle_left[1] = -0.462
                    fcurve.keyframe_points[0].handle_right[0] = 120
                    fcurve.keyframe_points[0].handle_right[1] = 0.274
                    fcurve.keyframe_points[1].co.x = 150
                    fcurve.keyframe_points[1].handle_left[0] = 121.518
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 151
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Input_54"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 150
                    fcurve.keyframe_points[0].handle_left[0] = 150
                    fcurve.keyframe_points[0].handle_left[1] = -0.722
                    fcurve.keyframe_points[0].handle_right[0] = 150
                    fcurve.keyframe_points[0].handle_right[1] = 0.762
                    fcurve.keyframe_points[1].co.x = 180
                    fcurve.keyframe_points[1].handle_left[0] = 164.3
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 181
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

        return {'FINISHED'}

class ADDONNAME_OT_my_opmppie(bpy.types.Operator):
    bl_label = "Add Ob33ject2"
    bl_idname = "addonname.myop_operatormppie"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enumMPpie == 'OPMP7pie':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 192
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_49"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 24
                    fcurve.keyframe_points[0].handle_left[0] = 24
                    fcurve.keyframe_points[0].handle_left[1] = -7.667
                    fcurve.keyframe_points[0].handle_right[0] = 24
                    fcurve.keyframe_points[0].handle_right[1] = 0.623
                    fcurve.keyframe_points[1].co.x = 48
                    fcurve.keyframe_points[1].handle_left[0] = 37.893
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 55.667
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_50"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 48
                    fcurve.keyframe_points[0].handle_left[0] = 48
                    fcurve.keyframe_points[0].handle_left[1] = -0.675
                    fcurve.keyframe_points[0].handle_right[0] = 48
                    fcurve.keyframe_points[0].handle_right[1] = 0.675
                    fcurve.keyframe_points[1].co.x = 72
                    fcurve.keyframe_points[1].handle_left[0] = 60.567
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 90
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_51"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 72
                    fcurve.keyframe_points[0].handle_left[0] = 72
                    fcurve.keyframe_points[0].handle_left[1] = -0.576
                    fcurve.keyframe_points[0].handle_right[0] = 72
                    fcurve.keyframe_points[0].handle_right[1] = 0.576
                    fcurve.keyframe_points[1].co.x = 96
                    fcurve.keyframe_points[1].handle_left[0] = 80.1
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 121
                    fcurve.keyframe_points[1].handle_right[1] = 1

            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_52"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 96
                    fcurve.keyframe_points[0].handle_left[0] = 96
                    fcurve.keyframe_points[0].handle_left[1] = -0.704
                    fcurve.keyframe_points[0].handle_right[0] = 96
                    fcurve.keyframe_points[0].handle_right[1] = 0.699
                    fcurve.keyframe_points[1].co.x = 120
                    fcurve.keyframe_points[1].handle_left[0] = 109.4
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 151
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_53"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 120
                    fcurve.keyframe_points[0].handle_left[0] = 120
                    fcurve.keyframe_points[0].handle_left[1] = -0.896
                    fcurve.keyframe_points[0].handle_right[0] = 120
                    fcurve.keyframe_points[0].handle_right[1] = 0.762
                    fcurve.keyframe_points[1].co.x = 144
                    fcurve.keyframe_points[1].handle_left[0] = 132.836
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 145
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

        if mytool.my_enumMPpie == 'OPMP8pie':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 240
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_49"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 30
                    fcurve.keyframe_points[0].handle_left[0] = 30
                    fcurve.keyframe_points[0].handle_left[1] = -0.623
                    fcurve.keyframe_points[0].handle_right[0] = 30
                    fcurve.keyframe_points[0].handle_right[1] = 0.623
                    fcurve.keyframe_points[1].co.x = 60
                    fcurve.keyframe_points[1].handle_left[0] = 47.614
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 72.398
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_50"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 60
                    fcurve.keyframe_points[0].handle_left[0] = 48
                    fcurve.keyframe_points[0].handle_left[1] = -0.623
                    fcurve.keyframe_points[0].handle_right[0] = 60.432
                    fcurve.keyframe_points[0].handle_right[1] = 0.519
                    fcurve.keyframe_points[1].co.x = 90
                    fcurve.keyframe_points[1].handle_left[0] = 72.7
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 91
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_51"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 90
                    fcurve.keyframe_points[0].handle_left[0] = 90
                    fcurve.keyframe_points[0].handle_left[1] = -0.841
                    fcurve.keyframe_points[0].handle_right[0] = 90
                    fcurve.keyframe_points[0].handle_right[1] = 0.576
                    fcurve.keyframe_points[1].co.x = 120
                    fcurve.keyframe_points[1].handle_left[0] = 102.946
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 121
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_52"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 120
                    fcurve.keyframe_points[0].handle_left[0] = 120
                    fcurve.keyframe_points[0].handle_left[1] = -0.462
                    fcurve.keyframe_points[0].handle_right[0] = 120
                    fcurve.keyframe_points[0].handle_right[1] = 0.274
                    fcurve.keyframe_points[1].co.x = 150
                    fcurve.keyframe_points[1].handle_left[0] = 121.518
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 151
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_53"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 150
                    fcurve.keyframe_points[0].handle_left[0] = 150
                    fcurve.keyframe_points[0].handle_left[1] = -0.722
                    fcurve.keyframe_points[0].handle_right[0] = 150
                    fcurve.keyframe_points[0].handle_right[1] = 0.762
                    fcurve.keyframe_points[1].co.x = 180
                    fcurve.keyframe_points[1].handle_left[0] = 164.3
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 181
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

        return {'FINISHED'}
    
class Fontchange(bpy.types.Operator):
    bl_label = "font Object"
    bl_idname = "addonname.myop_operatorf"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.active_object
        modifier = obj.modifiers["GeometryNodes"]
        node_group = modifier.node_group
        node = node_group.nodes['String to Curves']
        data_font = bpy.data.fonts.load(mytool.my_path)
        node.font = data_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class Fontchangepie(bpy.types.Operator):
    bl_label = "font Objectpie"
    bl_idname = "addonname.myop_operatorfpie"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.active_object
        modifier = obj.modifiers["GeometryNodes"]
        node_group = modifier.node_group
        node = node_group.nodes['String to Curves']
        data_font = bpy.data.fonts.load(mytool.my_pathpie)
        node.font = data_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class Fontrestore(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorres"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.active_object
        modifier = obj.modifiers["GeometryNodes"]
        node_group = modifier.node_group
        node = node_group.nodes['String to Curves']
        data_font = bpy.data.fonts["Open Sans Regular"]
        node.font = data_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class Fontrestorepie(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorrespie"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.active_object
        modifier = obj.modifiers["GeometryNodes"]
        node_group = modifier.node_group
        node = node_group.nodes['String to Curves']
        data_font = bpy.data.fonts["Open Sans Regular"]
        node.font = data_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class Endchange(bpy.types.Operator):
    bl_label = "End frame"
    bl_idname = "addonname.myop_operatori"
               
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle_GraphAction'
        data_path = 'modifiers["GeometryNodes"]["Input_30"]'
        index = 0
        jeff = bpy.context.scene.render.fps    
        bob = jeff*mytool.my_float          # Z axis
        mike = (bob*(1+mytool.my_float2))
        
        mike = int(mike)
    
        bpy.context.scene.frame_end = mike+jeff
        
        
        
        return {'FINISHED'}
    
class Endchangepie(bpy.types.Operator):
    bl_label = "End framepie"
    bl_idname = "addonname.myop_operatoripie"
               
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.001Action'
        data_path = 'modifiers["GeometryNodes"]["Input_25"]'
        index = 0
        jeffpie = bpy.context.scene.render.fps    
        bobpie = jeffpie*mytool.my_floatpie              # Z axis
        mikepie = (bobpie*(1+mytool.my_float2pie))
        
        mikepie = int(mikepie)
    
        bpy.context.scene.frame_end = mikepie+jeffpie
        
        
        
        return {'FINISHED'}
    
class ADDONNAME_OT_my_op3(bpy.types.Operator):
    bl_label = "Add Object3"
    bl_idname = "addonname.myop_operator3"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enum3 == 'OP9':

            bpy.context.scene.render.use_file_extension = True
            bpy.context.scene.render.use_render_cache = False
            bpy.context.scene.render.image_settings.file_format = 'PNG'
            bpy.context.scene.render.image_settings.color_mode = 'RGBA'
            bpy.context.scene.render.image_settings.color_depth = '8'
            bpy.context.scene.render.image_settings.compression = 50
            bpy.context.scene.render.use_overwrite = True
            bpy.context.scene.render.use_placeholder = False
            
        if mytool.my_enum3 == 'OP10':

            bpy.context.scene.render.use_file_extension = True
            bpy.context.scene.render.use_render_cache = False
            bpy.context.scene.render.image_settings.file_format = 'OPEN_EXR'
            bpy.context.scene.render.image_settings.color_mode = 'RGBA'
            bpy.context.scene.render.image_settings.color_depth = '32'
            bpy.context.scene.render.image_settings.exr_codec = 'ZIP'
            bpy.context.scene.render.image_settings.use_zbuffer = False
            bpy.context.scene.render.image_settings.use_preview = False
            bpy.context.scene.render.use_overwrite = True
            bpy.context.scene.render.use_placeholder = False
            
        if mytool.my_enum3 == 'OP11':

            bpy.context.scene.render.use_file_extension = True
            bpy.context.scene.render.use_render_cache = False
            bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
            bpy.context.scene.render.image_settings.color_mode = 'RGB'
            bpy.context.scene.render.image_settings.color_management = 'FOLLOW_SCENE'
            bpy.context.scene.render.ffmpeg.format = 'MPEG4'
            bpy.context.scene.render.ffmpeg.use_autosplit = False
            bpy.context.scene.render.ffmpeg.audio_codec = 'NONE'
            bpy.context.scene.render.ffmpeg.codec = 'H264'
            bpy.context.scene.render.ffmpeg.constant_rate_factor = 'MEDIUM'
            bpy.context.scene.render.ffmpeg.ffmpeg_preset = 'GOOD'
            bpy.context.scene.render.ffmpeg.gopsize = 18
            bpy.context.scene.render.ffmpeg.use_max_b_frames = False
        
        return {'FINISHED'}

class Locationchange(bpy.types.Operator):
    bl_label = "font Object"
    bl_idname = "addonname.myop_operatorffg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        bpy.context.scene.render.filepath = mytool.my_path2  
        
        return {'FINISHED'}    

classes = [MyProperties, RenderRender2, ADDONNAME_OT_my_opgg, ADDONNAME_OT_my_opggpie, ADDONNAME_OT_my_op, ADDONNAME_OT_my_op2, ADDONNAME_OT_my_op2pie, ADDONNAME_OT_my_oplgpie, ADDONNAME_OT_my_ophbpie, ADDONNAME_OT_my_opmcpie, ADDONNAME_OT_my_opmppie, ADDONNAME_OT_my_op3, Fontchange, Fontchangepie, Fontrestore, Fontrestorepie, Endchange, Endchangepie, Locationchange,  TestPanel, TestPanel2, TestPanel3, TestPanel4, TestPanel5, TestPanel6, TestPanel7]
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type= MyProperties)
        
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        del bpy.types.Scene.my_tool
 
    
if __name__ == "__main__":
    register()


