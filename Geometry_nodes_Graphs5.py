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
import csv

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

    my_enum23C : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OP23C7', "24 FPS (and reset)", "24 Frames per second"),
                ('OP23C8', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operator23c()
    )
    
    my_enum23P : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OP23P7', "24 FPS (and reset)", "24 Frames per second"),
                ('OP23P8', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operator23p()
    )
    
    my_enumLGC : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPLGC7', "24 FPS (and reset)", "24 Frames per second"),
                ('OPLGC8', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgc()
    )
    
    my_enumHBC : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPHBC7', "24 FPS (and reset)", "24 Frames per second"),
                ('OPHBC8', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbc()
    )
    
    my_enumMG : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPMG7', "24 FPS (and reset)", "24 Frames per second"),
                ('OPMG8', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatormg()
    )
    
    my_enumMGC : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPMGC7', "24 FPS (and reset)", "24 Frames per second"),
                ('OPMGC8', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatormgc()
    )
    
    my_enumVB : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPVB7', "24 FPS (and reset)", "24 Frames per second"),
                ('OPVB8', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatorvb()
    )
    
    my_enumVBC : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPVBC7', "24 FPS (and reset)", "24 Frames per second"),
                ('OPVBC8', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbc()
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
        description="link to csv file:",
        default="//csv/circle_graph.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathpie: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/pie_graph.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathline: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/line_graph.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathlinec: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/line_graph_comparison.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathhbar: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/horizontal_bar_graph.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathhbarc: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/horizontal_bar_graph_comparison.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathmcircle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/multiple_circle_graph.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathmpie: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/multiple_pie_graph.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_path23c: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/2_3_circle_graph.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_path23p: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/2_3_pie_graph.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathmg: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/mountain_graph.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathmgc: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/mountain_graph_comparison.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathvb: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/vertical_bar_graph.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathvbc: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/vertical_bar_graph_comparison.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_path2: bpy.props.StringProperty(
        name = "",
        description="location to save",
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
        
        rowCGcsv = layout.row()
        rowCGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_path")
        layout.operator("mesh.mycubeoperatorcgcsv")
        
        rowB = layout.row()
        rowB.label(text= "Frames per second:")
        
        layout.prop(mytool, "my_enum2")
       
        rowE = layout.row()
        rowE.label(text= "Length of Animation:")
        layout.prop(mytool, "my_float")
        
        rowG = layout.row()
        rowG.label(text= "Excess seconds:")
        layout.prop(mytool, "my_float2")
        
class TestPanel2C(bpy.types.Panel):
    bl_label = "2-3 Circle Graph"
    bl_idname = "PT_TestPanel2c"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        row23CGcsv = layout.row()
        row23CGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_path23c")
        layout.operator("mesh.mycubeoperatorcgccsv")

        row23FPS = layout.row()
        row23FPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enum23C")

        
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
        
        rowPGcsv = layout.row()
        rowPGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathpie")
        layout.operator("mesh.mycubeoperatorpgcsv")
        
        rowB = layout.row()
        rowB.label(text= "Frames per second:")
        
        layout.prop(mytool, "my_enum2pie")
       
        rowE = layout.row()
        rowE.label(text= "Length of Animation:")
        layout.prop(mytool, "my_floatpie")
        
        rowG = layout.row()
        rowG.label(text= "Excess seconds:")
        layout.prop(mytool, "my_float2pie")
        
class TestPanel3P(bpy.types.Panel):
    bl_label = "2-3 Pie Graph"
    bl_idname = "PT_TestPanel3p"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        row23PGcsv = layout.row()
        row23PGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_path23p")
        layout.operator("mesh.mycubeoperatorpgccsv")

        row23PFPS = layout.row()
        row23PFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enum23P")
        
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
        
        rowLGcsv = layout.row()
        rowLGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathline")
        layout.operator("mesh.mycubeoperatorlgcsv")
        
        rowLG = layout.row()
        rowLG.label(text= "Frames per second:")
        
        layout.prop(mytool, "my_enumLGpie")
        
class TestPanel4LGC(bpy.types.Panel):
    bl_label = "Line Graph Comparison"
    bl_idname = "PT_TestPanel4lgc"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowLGCcsv = layout.row()
        rowLGCcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathlinec")
        layout.operator("mesh.mycubeoperatorlgccsv")

        rowLGCFPS = layout.row()
        rowLGCFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumLGC")

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
        
        rowHBcsv = layout.row()
        rowHBcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathhbar")
        layout.operator("mesh.mycubeoperatorhbcsv")
        
        rowHB = layout.row()
        rowHB.label(text= "Frames per second:")
        
        layout.prop(mytool, "my_enumHBpie")
        
class TestPanel5C(bpy.types.Panel):
    bl_label = "Horizontal Bar Graph Comparison"
    bl_idname = "PT_TestPanel5c"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowHBCcsv = layout.row()
        rowHBCcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathhbarc")
        layout.operator("mesh.mycubeoperatorhbccsv")

        rowHBCFPS = layout.row()
        rowHBCFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumHBC")

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
        
        rowMCcsv = layout.row()
        rowMCcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathmcircle")
        layout.operator("mesh.mycubeoperatormccsv")
        
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
        
        rowMPcsv = layout.row()
        rowMPcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathmpie")
        layout.operator("mesh.mycubeoperatormpcsv")
        
        rowMP = layout.row()
        rowMP.label(text= "Frames per second:")
        
        layout.prop(mytool, "my_enumMPpie")
        
class TestPanel8(bpy.types.Panel):
    bl_label = "Mountain Graph"
    bl_idname = "PT_TestPanel8"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowMGcsv = layout.row()
        rowMGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathmg")
        layout.operator("mesh.mycubeoperatormgcsv")

        rowMGFPS = layout.row()
        rowMGFPS.label(text= "Frames per second:")  
        layout.prop(mytool, "my_enumMG")  
        
class TestPanel8C(bpy.types.Panel):
    bl_label = "Mountain Graph Comparison"
    bl_idname = "PT_TestPanel8c"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowMGCcsv = layout.row()
        rowMGCcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathmgc")
        layout.operator("mesh.mycubeoperatormgccsv")

        rowMGCFPS = layout.row()
        rowMGCFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumMGC")  
        
class TestPanel9(bpy.types.Panel):
    bl_label = "Vertical Bar Graph"
    bl_idname = "PT_TestPanel9"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowVBcsv = layout.row()
        rowVBcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathvb")
        layout.operator("mesh.mycubeoperatorvbcsv")

        rowVBFPS = layout.row()
        rowVBFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumVB")  
        
class TestPanel9VB(bpy.types.Panel):
    bl_label = "Vertical Bar Graph Comparison"
    bl_idname = "PT_TestPanel9vb"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowVBCcsv = layout.row()
        rowVBCcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathvbc")
        layout.operator("mesh.mycubeoperatorvbccsv")

        rowVBCFPS = layout.row()
        rowVBCFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumVBC") 
        
class MyoperatorCGcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorcgcsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full = bpy.path.abspath(mytool.my_path)
        with open(filepath_full) as f:
            readout = list(csv.reader(f))
            gregory = float(readout[1][0])
            mallory = float(readout[1][1])
            olatunji = float(readout[1][2])
            titlecirclegraph = str(readout[1][3])
            subtitlecirclegraph = str(readout[1][4])
            descriptioncirclegraph = str(readout[1][5])
            gregorypercentage = float(gregory/olatunji)
            
        bpy.data.objects["Circle_Graph"].modifiers["GeometryNodes"]["Input_2"] = gregorypercentage
        bpy.data.objects["Circle_Graph"].modifiers["GeometryNodes"]["Input_10"] = mallory
        bpy.data.objects["Circle_Graph"].modifiers["GeometryNodes"]["Input_11"] = olatunji
        bpy.data.objects["Circle_Graph"].modifiers["GeometryNodes"]["Input_22"] = titlecirclegraph
        bpy.data.objects["Circle_Graph"].modifiers["GeometryNodes"]["Input_23"] = subtitlecirclegraph
        bpy.data.objects["Circle_Graph"].modifiers["GeometryNodes"]["Input_16"] = descriptioncirclegraph
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class MyoperatorCGCcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorcgccsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full23c = bpy.path.abspath(mytool.my_path23c)
        with open(filepath_full23c) as f:
            readout = list(csv.reader(f))
            ncg23c = int(readout[1][0])
            wta23c = str(readout[1][1])
            wtb23c = str(readout[2][1])
            wtc23c = str(readout[3][1])
            psa23c = float(readout[1][2])
            psb23c = float(readout[2][2])
            psc23c = float(readout[3][2])
            minv23c = float(readout[1][3])
            maxv23c = float(readout[1][4])
            title23c = str(readout[1][5])
            subtitle23c = str(readout[1][6])
            desc23c = str(readout[1][7])
            wtpa23c = float(psa23c/maxv23c)
            wtpb23c = float(psb23c/maxv23c)
            wtpc23c = float(psc23c/maxv23c)
            
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_31"] = ncg23c
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_39"] = wta23c
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_40"] = wtb23c
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_38"] = wtc23c
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_2"] = wtpa23c
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_41"] = wtpb23c
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_42"] = wtpc23c
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_10"] = minv23c
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_11"] = maxv23c
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_22"] = title23c
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_23"] = subtitle23c
        bpy.data.objects["Circle_Graph.001"].modifiers["GeometryNodes"]["Input_16"] = desc23c
        bpy.context.object.data.update()
        return {'FINISHED'}  
    
class MyoperatorPGCcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorpgccsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full23p = bpy.path.abspath(mytool.my_path23p)
        with open(filepath_full23p) as f:
            readout = list(csv.reader(f))
            ncg23p = int(readout[1][0])
            wta23p = str(readout[1][1])
            wtb23p = str(readout[2][1])
            wtc23p = str(readout[3][1])
            psa23p = float(readout[1][2])
            psb23p = float(readout[2][2])
            psc23p = float(readout[3][2])
            minv23p = float(readout[1][3])
            maxv23p = float(readout[1][4])
            title23p = str(readout[1][5])
            subtitle23p = str(readout[1][6])
            desc23p = str(readout[1][7])
            wtpa23p = float(psa23p/maxv23p)
            wtpb23p = float(psb23p/maxv23p)
            wtpc23p = float(psc23p/maxv23p)
            
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_26"] = ncg23p
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_31"] = wta23p
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_32"] = wtb23p
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_33"] = wtc23p
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_2"] = wtpa23p
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_27"] = wtpb23p
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_28"] = wtpc23p
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_10"] = minv23p
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_11"] = maxv23p
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_15"] = title23p
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_17"] = subtitle23p
        bpy.data.objects["Circle Graph.002"].modifiers["GeometryNodes"]["Input_19"] = desc23p
        bpy.context.object.data.update()
        return {'FINISHED'} 
    
class MyoperatorPGcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorpgcsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full2 = bpy.path.abspath(mytool.my_pathpie)
        with open(filepath_full2) as f:
            readout = list(csv.reader(f))
            gregorypg = float(readout[1][0])
            mallorypg = float(readout[1][1])
            olatunjipg = float(readout[1][2])
            titlepg = str(readout[1][3])
            subtitlepg = str(readout[1][4])
            percentpg = str(readout[1][5])
            gregorypercentagepg = float(gregorypg/olatunjipg)
            
        bpy.data.objects["Circle Graphp.001"].modifiers["GeometryNodes"]["Input_2"] = gregorypercentagepg
        bpy.data.objects["Circle Graphp.001"].modifiers["GeometryNodes"]["Input_10"] = mallorypg
        bpy.data.objects["Circle Graphp.001"].modifiers["GeometryNodes"]["Input_11"] = olatunjipg
        bpy.data.objects["Circle Graphp.001"].modifiers["GeometryNodes"]["Input_15"] = titlepg
        bpy.data.objects["Circle Graphp.001"].modifiers["GeometryNodes"]["Input_17"] = subtitlepg
        bpy.data.objects["Circle Graphp.001"].modifiers["GeometryNodes"]["Input_19"] = percentpg

        bpy.context.object.data.update()
        return {'FINISHED'} 
    
class MyoperatorLGcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorlgcsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full3 = bpy.path.abspath(mytool.my_pathline)
        with open(filepath_full3) as f:
            readout = list(csv.reader(f))
            nplg = int(readout[1][0])
            minvlg = float(readout[1][3])
            maxvlg = float(readout[1][4])
            decimallg = int(readout[1][5])
            rnlg = int(readout[1][6])
            value1lg = float(readout[1][1])
            value2lg = float(readout[2][1])
            value3lg = float(readout[3][1])
            value4lg = float(readout[4][1])
            value5lg = float(readout[5][1])
            value6lg = float(readout[6][1])
            value7lg = float(readout[7][1])
            value8lg = float(readout[8][1])
            text1lg = str(readout[1][2])
            text2lg = str(readout[2][2])
            text3lg = str(readout[3][2])
            text4lg = str(readout[4][2])
            text5lg = str(readout[5][2])
            text6lg = str(readout[6][2])
            text7lg = str(readout[7][2])
            text8lg = str(readout[8][2])
            titlelg = str(readout[1][7])
            subtitlelg = str(readout[1][8])
            
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_2"] = nplg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_13"] = minvlg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_14"] = maxvlg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_15"] = decimallg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_18"] = rnlg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_4"] = value1lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_5"] = value2lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_6"] = value3lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_7"] = value4lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_8"] = value5lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_9"] = value6lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_10"] = value7lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes"]["Input_11"] = value8lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes.001"]["Input_4"] = text1lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes.001"]["Input_5"] = text2lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes.001"]["Input_6"] = text3lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes.001"]["Input_7"] = text4lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes.001"]["Input_8"] = text5lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes.001"]["Input_9"] = text6lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes.001"]["Input_10"] = text7lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes.001"]["Input_11"] = text8lg
        bpy.data.objects["Cube"].modifiers["GeometryNodes.001"]["Input_23"] = titlelg
        bpy.data.objects["Cube"].modifiers["GeometryNodes.001"]["Input_22"] = subtitlelg
        
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class MyoperatorLGCcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorlgccsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full3c = bpy.path.abspath(mytool.my_pathlinec)
        with open(filepath_full3c) as f:
            readout = list(csv.reader(f))
            nplgc = int(readout[1][0])
            minvlgc = float(readout[1][4])
            maxvlgc = float(readout[1][5])
            decimallgc = int(readout[1][6])
            rnlgc = int(readout[1][7])
            valuea1lgc = float(readout[1][2])
            valuea2lgc = float(readout[2][2])
            valuea3lgc = float(readout[3][2])
            valuea4lgc = float(readout[4][2])
            valuea5lgc = float(readout[5][2])
            valuea6lgc = float(readout[6][2])
            valuea7lgc = float(readout[7][2])
            valuea8lgc = float(readout[8][2])
            valueb1lgc = float(readout[1][3])
            valueb2lgc = float(readout[2][3])
            valueb3lgc = float(readout[3][3])
            valueb4lgc = float(readout[4][3])
            valueb5lgc = float(readout[5][3])
            valueb6lgc = float(readout[6][3])
            valueb7lgc = float(readout[7][3])
            valueb8lgc = float(readout[8][3])
            text1lgc = str(readout[1][1])
            text2lgc = str(readout[2][1])
            text3lgc = str(readout[3][1])
            text4lgc = str(readout[4][1])
            text5lgc = str(readout[5][1])
            text6lgc = str(readout[6][1])
            text7lgc = str(readout[7][1])
            text8lgc = str(readout[8][1])
            titlelgc = str(readout[1][8])
            subtitlelgc = str(readout[1][9])
            legendalgc = str(readout[1][10])
            legendblgc = str(readout[2][10])
            
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_2"] = nplgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_13"] = minvlgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_14"] = maxvlgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_15"] = decimallgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_18"] = rnlgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_4"] = valuea1lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_5"] = valuea2lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_6"] = valuea3lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_7"] = valuea4lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_8"] = valuea5lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_9"] = valuea6lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_10"] = valuea7lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_11"] = valuea8lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_34"] = valueb1lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_35"] = valueb2lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_36"] = valueb3lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_37"] = valueb4lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_38"] = valueb5lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_39"] = valueb6lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_40"] = valueb7lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes"]["Input_41"] = valueb8lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_4"] = text1lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_5"] = text2lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_6"] = text3lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_7"] = text4lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_8"] = text5lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_9"] = text6lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_10"] = text7lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_11"] = text8lgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_23"] = titlelgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_22"] = subtitlelgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_29"] = legendalgc
        bpy.data.objects["Cube.002"].modifiers["GeometryNodes.001"]["Input_30"] = legendblgc
        
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class MyoperatorHBcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorhbcsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full4 = bpy.path.abspath(mytool.my_pathhbar)
        with open(filepath_full4) as f:
            readout = list(csv.reader(f))
            gregoryhbar = int(readout[1][0])
            malloryhbar1 = float(readout[1][2])
            malloryhbar2 = float(readout[2][2])
            malloryhbar3 = float(readout[3][2])
            malloryhbar4 = float(readout[4][2])
            olatunjihbar1 = float(readout[1][3])
            olatunjihbar2 = float(readout[1][4])
            jeopardyhbar1 = int(readout[1][5])
            hogwashhbar1 = str(readout[1][1])
            hogwashhbar2 = str(readout[2][1])
            hogwashhbar3 = str(readout[3][1])
            hogwashhbar4 = str(readout[4][1])
            titlehbar1 = str(readout[1][6])
            subtitlehbar1 = str(readout[1][7])
            totalhbar1 = str(readout[1][8])
            
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_36"] = gregoryhbar
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_14"] = malloryhbar1
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_15"] = malloryhbar2
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_16"] = malloryhbar3
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_17"] = malloryhbar4
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_10"] = olatunjihbar1
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_11"] = olatunjihbar2
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_12"] = jeopardyhbar1
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_2"] = hogwashhbar1
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_3"] = hogwashhbar2
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_4"] = hogwashhbar3
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_5"] = hogwashhbar4
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_7"] = titlehbar1
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_8"] = subtitlehbar1
        bpy.data.objects["Plane.002"].modifiers["GeometryNodes"]["Input_6"] = totalhbar1
        

        
        bpy.context.object.data.update()
        return {'FINISHED'}  
    
class MyoperatorHBCcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorhbccsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full4c = bpy.path.abspath(mytool.my_pathhbarc)
        with open(filepath_full4c) as f:
            readout = list(csv.reader(f))
            nbhbarc = int(readout[1][0])
            bthbarc1 = str(readout[1][1])
            bthbarc2 = str(readout[2][1])
            bthbarc3 = str(readout[3][1])
            bthbarc4 = str(readout[4][1])
            minvhbarc1 = float(readout[1][4])
            maxvhbarc2 = float(readout[1][5])
            decimalhbarc1 = int(readout[1][6])
            bvahbarc1 = float(readout[1][2])
            bvahbarc2 = float(readout[2][2])
            bvahbarc3 = float(readout[3][2])
            bvahbarc4 = float(readout[4][2])
            bvbhbarc1 = float(readout[1][3])
            bvbhbarc2 = float(readout[2][3])
            bvbhbarc3 = float(readout[3][3])
            bvbhbarc4 = float(readout[4][3])
            titlehbarc1 = str(readout[1][7])
            subtitlehbarc1 = str(readout[1][8])
            legendhbarc1 = str(readout[1][9])
            legendhbarc2 = str(readout[2][9])
            
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_45"] = nbhbarc
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_2"] = bthbarc1
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_3"] = bthbarc2
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_4"] = bthbarc3
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_5"] = bthbarc4
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_10"] = minvhbarc1
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_11"] = maxvhbarc2
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_12"] = decimalhbarc1
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_14"] = bvahbarc1
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_15"] = bvahbarc2
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_16"] = bvahbarc3
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_17"] = bvahbarc4
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_36"] = bvbhbarc1
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_37"] = bvbhbarc2
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_38"] = bvbhbarc3
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_39"] = bvbhbarc4
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_7"] = titlehbarc1
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_8"] = subtitlehbarc1
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_6"] = legendhbarc1
        bpy.data.objects["Plane.001"].modifiers["GeometryNodes"]["Input_40"] = legendhbarc2
        

        
        bpy.context.object.data.update()
        return {'FINISHED'}  
    
class MyoperatorMCcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatormccsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full5 = bpy.path.abspath(mytool.my_pathmcircle)
        with open(filepath_full5) as f:
            readout = list(csv.reader(f))
            gregorymcircle = int(readout[1][0])
            mallorymcircle1 = float(readout[1][2])
            mallorymcircle2 = float(readout[2][2])
            mallorymcircle3 = float(readout[3][2])
            mallorymcircle4 = float(readout[4][2])
            mallorymcircle5 = float(readout[5][2])
            hogwashmcircle1 = str(readout[1][1])
            hogwashmcircle2 = str(readout[2][1])
            hogwashmcircle3 = str(readout[3][1])
            hogwashmcircle4 = str(readout[4][1])
            hogwashmcircle5 = str(readout[5][1])
            minvaluemcircle = float(readout[1][3])
            maxvaluemcircle = float(readout[1][4])
            decimalmcircle = int(readout[1][5])
            titlemcircle = str(readout[1][6])
            subtitlemcircle = str(readout[1][7])
            mallorympercentage1 = float(mallorymcircle1/maxvaluemcircle)
            mallorympercentage2 = float(mallorymcircle2/maxvaluemcircle)
            mallorympercentage3 = float(mallorymcircle3/maxvaluemcircle)
            mallorympercentage4 = float(mallorymcircle4/maxvaluemcircle)
            mallorympercentage5 = float(mallorymcircle5/maxvaluemcircle)
             

            
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_55"] = gregorymcircle
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_2"] = mallorympercentage1
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_12"] = mallorympercentage2
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_14"] = mallorympercentage3
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_15"] = mallorympercentage4
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_16"] = mallorympercentage5
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_10"] = minvaluemcircle
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_11"] = maxvaluemcircle
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_18"] = decimalmcircle
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_40"] = titlemcircle
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_41"] = subtitlemcircle
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_42"] = hogwashmcircle1
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_43"] = hogwashmcircle2
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_44"] = hogwashmcircle3
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_46"] = hogwashmcircle4
        bpy.data.objects["Circle Graph.004"].modifiers["GeometryNodes"]["Input_45"] = hogwashmcircle5
        

        
        
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class MyoperatorMPcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatormpcsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full6 = bpy.path.abspath(mytool.my_pathmpie)
        with open(filepath_full6) as f:
            readout = list(csv.reader(f))
            gregorympie = int(readout[1][0])
            mallorympie1 = float(readout[1][2])
            mallorympie2 = float(readout[2][2])
            mallorympie3 = float(readout[3][2])
            mallorympie4 = float(readout[4][2])
            mallorympie5 = float(readout[5][2])
            hogwashmpie1 = str(readout[1][1])
            hogwashmpie2 = str(readout[2][1])
            hogwashmpie3 = str(readout[3][1])
            hogwashmpie4 = str(readout[4][1])
            hogwashmpie5 = str(readout[5][1])
            minvaluempie = float(readout[1][3])
            maxvaluempie = float(readout[1][4])
            decimalmpie = int(readout[1][5])
            titlempie = str(readout[1][6])
            subtitlempie = str(readout[1][7])
            mallorympiepercentage1 = float(mallorympie1/maxvaluempie)
            mallorympiepercentage2 = float(mallorympie2/maxvaluempie)
            mallorympiepercentage3 = float(mallorympie3/maxvaluempie)
            mallorympiepercentage4 = float(mallorympie4/maxvaluempie)
            mallorympiepercentage5 = float(mallorympie5/maxvaluempie)           
            
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_54"] = gregorympie
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_2"] = mallorympiepercentage1
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_12"] = mallorympiepercentage2
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_14"] = mallorympiepercentage3
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_15"] = mallorympiepercentage4
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_16"] = mallorympiepercentage5
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_10"] = minvaluempie
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_11"] = maxvaluempie
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_18"] = decimalmpie
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_40"] = titlempie
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_41"] = subtitlempie
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_42"] = hogwashmpie1
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_43"] = hogwashmpie2
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_44"] = hogwashmpie3
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_46"] = hogwashmpie4
        bpy.data.objects["Circle Graph.005"].modifiers["GeometryNodes"]["Input_45"] = hogwashmpie5
            
        
        bpy.context.object.data.update()
        return {'FINISHED'} 
    
class MyoperatorMGcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatormgcsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full3mg = bpy.path.abspath(mytool.my_pathmg)
        with open(filepath_full3mg) as f:
            readout = list(csv.reader(f))
            npmg = int(readout[1][0])
            minvmg = float(readout[1][3])
            maxvmg = float(readout[1][4])
            decimalmg = int(readout[1][5])
            rnmg = int(readout[1][6])
            value1mg = float(readout[1][1])
            value2mg = float(readout[2][1])
            value3mg = float(readout[3][1])
            value4mg = float(readout[4][1])
            value5mg = float(readout[5][1])
            value6mg = float(readout[6][1])
            value7mg = float(readout[7][1])
            value8mg = float(readout[8][1])
            text1mg = str(readout[1][2])
            text2mg = str(readout[2][2])
            text3mg = str(readout[3][2])
            text4mg = str(readout[4][2])
            text5mg = str(readout[5][2])
            text6mg = str(readout[6][2])
            text7mg = str(readout[7][2])
            text8mg = str(readout[8][2])
            titlemg = str(readout[1][7])
            subtitlemg = str(readout[1][8])
            
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_2"] = npmg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_22"] = minvmg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_24"] = maxvmg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_23"] = decimalmg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_21"] = rnmg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_3"] = value1mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_4"] = value2mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_5"] = value3mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_6"] = value4mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_7"] = value5mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_8"] = value6mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_9"] = value7mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_10"] = value8mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_13"] = text1mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_14"] = text2mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_15"] = text3mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_16"] = text4mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_17"] = text5mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_18"] = text6mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_19"] = text7mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_20"] = text8mg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_38"] = titlemg
        bpy.data.objects["Cube.003"].modifiers["GeometryNodes"]["Input_39"] = subtitlemg
        
        bpy.context.object.data.update()
        return {'FINISHED'} 
    
class MyoperatorMGCcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatormgccsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full3mgc = bpy.path.abspath(mytool.my_pathmgc)
        with open(filepath_full3mgc) as f:
            readout = list(csv.reader(f))
            npmgc = int(readout[1][0])
            minvmgc = float(readout[1][4])
            maxvmgc = float(readout[1][5])
            decimalmgc = int(readout[1][6])
            rnmgc = int(readout[1][7])
            valuea1mgc = float(readout[1][2])
            valuea2mgc = float(readout[2][2])
            valuea3mgc = float(readout[3][2])
            valuea4mgc = float(readout[4][2])
            valuea5mgc = float(readout[5][2])
            valuea6mgc = float(readout[6][2])
            valuea7mgc = float(readout[7][2])
            valuea8mgc = float(readout[8][2])
            valueb1mgc = float(readout[1][3])
            valueb2mgc = float(readout[2][3])
            valueb3mgc = float(readout[3][3])
            valueb4mgc = float(readout[4][3])
            valueb5mgc = float(readout[5][3])
            valueb6mgc = float(readout[6][3])
            valueb7mgc = float(readout[7][3])
            valueb8mgc = float(readout[8][3])
            text1mgc = str(readout[1][1])
            text2mgc = str(readout[2][1])
            text3mgc = str(readout[3][1])
            text4mgc = str(readout[4][1])
            text5mgc = str(readout[5][1])
            text6mgc = str(readout[6][1])
            text7mgc = str(readout[7][1])
            text8mgc = str(readout[8][1])
            titlemgc = str(readout[1][8])
            subtitlemgc = str(readout[1][9])
            legendamgc = str(readout[1][10])
            legendbmgc = str(readout[2][10])
            
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_2"] = npmgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_22"] = minvmgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_24"] = maxvmgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_23"] = decimalmgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_21"] = rnmgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_3"] = valuea1mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_4"] = valuea2mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_5"] = valuea3mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_6"] = valuea4mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_7"] = valuea5mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_8"] = valuea6mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_9"] = valuea7mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_10"] = valuea8mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_30"] = valueb1mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_39"] = valueb2mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_40"] = valueb3mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_41"] = valueb4mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_42"] = valueb5mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_43"] = valueb6mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_44"] = valueb7mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_45"] = valueb8mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_13"] = text1mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_14"] = text2mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_15"] = text3mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_16"] = text4mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_17"] = text5mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_18"] = text6mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_19"] = text7mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_20"] = text8mgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_54"] = titlemgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_55"] = subtitlemgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_57"] = legendamgc
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_5"] = legendbmgc
        
        bpy.context.object.data.update()
        return {'FINISHED'} 
    
class MyoperatorVBcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorvbcsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full4vb = bpy.path.abspath(mytool.my_pathvb)
        with open(filepath_full4vb) as f:
            readout = list(csv.reader(f))
            gregoryvb = int(readout[1][0])
            malloryvb1 = float(readout[1][2])
            malloryvb2 = float(readout[2][2])
            malloryvb3 = float(readout[3][2])
            malloryvb4 = float(readout[4][2])
            malloryvb5 = float(readout[5][2])
            malloryvb6 = float(readout[6][2])
            malloryvb7 = float(readout[7][2])
            malloryvb8 = float(readout[8][2])
            olatunjivb1 = float(readout[1][3])
            olatunjivb2 = float(readout[1][4])
            jeopardyvb1 = int(readout[1][5])
            hogwashvb1 = str(readout[1][1])
            hogwashvb2 = str(readout[2][1])
            hogwashvb3 = str(readout[3][1])
            hogwashvb4 = str(readout[4][1])
            hogwashvb5 = str(readout[5][1])
            hogwashvb6 = str(readout[6][1])
            hogwashvb7 = str(readout[7][1])
            hogwashvb8 = str(readout[8][1])
            titlevb1 = str(readout[1][6])
            subtitlevb1 = str(readout[1][7])
            totalvb1 = str(readout[1][8])
            
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_57"] = gregoryvb
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_14"] = malloryvb1
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_41"] = malloryvb2
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_15"] = malloryvb3
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_44"] = malloryvb4
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_16"] = malloryvb5
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_48"] = malloryvb6
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_17"] = malloryvb7
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_50"] = malloryvb8
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_10"] = olatunjivb1
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_11"] = olatunjivb2
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_12"] = jeopardyvb1
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_2"] = hogwashvb1
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_42"] = hogwashvb2
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_3"] = hogwashvb3
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_45"] = hogwashvb4
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_4"] = hogwashvb5
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_47"] = hogwashvb6
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_5"] = hogwashvb7
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_49"] = hogwashvb8
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_7"] = titlevb1
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_8"] = subtitlevb1
        bpy.data.objects["Plane.003"].modifiers["GeometryNodes"]["Input_6"] = totalvb1
        

        
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class MyoperatorVBCcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorvbccsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        filepath_full4vbc = bpy.path.abspath(mytool.my_pathvbc)
        with open(filepath_full4vbc) as f:
            readout = list(csv.reader(f))
            nbvbc = int(readout[1][0])
            btvbc1 = str(readout[1][1])
            btvbc2 = str(readout[2][1])
            btvbc3 = str(readout[3][1])
            btvbc4 = str(readout[4][1])
            btvbc5 = str(readout[5][1])
            btvbc6 = str(readout[6][1])
            btvbc7 = str(readout[7][1])
            btvbc8 = str(readout[8][1])
            minvvbc1 = float(readout[1][4])
            maxvvbc2 = float(readout[1][5])
            decimalvbc1 = int(readout[1][6])
            bvavbc1 = float(readout[1][2])
            bvavbc2 = float(readout[2][2])
            bvavbc3 = float(readout[3][2])
            bvavbc4 = float(readout[4][2])
            bvavbc5 = float(readout[5][2])
            bvavbc6 = float(readout[6][2])
            bvavbc7 = float(readout[7][2])
            bvavbc8 = float(readout[8][2])
            bvbvbc1 = float(readout[1][3])
            bvbvbc2 = float(readout[2][3])
            bvbvbc3 = float(readout[3][3])
            bvbvbc4 = float(readout[4][3])
            bvbvbc5 = float(readout[5][3])
            bvbvbc6 = float(readout[6][3])
            bvbvbc7 = float(readout[7][3])
            bvbvbc8 = float(readout[8][3])
            titlevbc1 = str(readout[1][7])
            subtitlevbc1 = str(readout[1][8])
            legendvbc1 = str(readout[1][9])
            legendvbc2 = str(readout[2][9])
            
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_71"] = nbvbc
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_2"] = btvbc1
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_42"] = btvbc2
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_3"] = btvbc3
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_45"] = btvbc4
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_4"] = btvbc5
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_47"] = btvbc6
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_5"] = btvbc7
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_49"] = btvbc8
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_10"] = minvvbc1
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_11"] = maxvvbc2
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_12"] = decimalvbc1
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_14"] = bvavbc1
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_41"] = bvavbc2
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_15"] = bvavbc3
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_44"] = bvavbc4
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_16"] = bvavbc5
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_48"] = bvavbc6
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_17"] = bvavbc7
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_50"] = bvavbc8
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_57"] = bvbvbc1
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_58"] = bvbvbc2
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_59"] = bvbvbc3
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_64"] = bvbvbc4
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_60"] = bvbvbc5
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_61"] = bvbvbc6
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_62"] = bvbvbc7
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_63"] = bvbvbc8
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_7"] = titlevbc1
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_8"] = subtitlevbc1
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_70"] = legendvbc1
        bpy.data.objects["Plane.004"].modifiers["GeometryNodes"]["Input_69"] = legendvbc2
        

        
        bpy.context.object.data.update()
        return {'FINISHED'}     
        
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
            bpy.context.object.data.update()
            
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
            bpy.context.object.data.update()
            
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
    
class ADDONNAME_23C(bpy.types.Operator):
    bl_label = "Add Ob33ject23c"
    bl_idname = "addonname.myop_operator23c"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enum23C == 'OP23C7':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 144
            bpy.context.object.data.update()
            
            action_name = 'Circle_GraphAction.001'
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

            
        if mytool.my_enum23C == 'OP23C8':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 180
            bpy.context.object.data.update()
            
            action_name = 'Circle_GraphAction.001'
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
    
class ADDONNAME_23P(bpy.types.Operator):
    bl_label = "Add Ob33ject23P"
    bl_idname = "addonname.myop_operator23p"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enum23P == 'OP23P7':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 144
            
            action_name = 'Circle Graph.001Action.001'
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

            
        if mytool.my_enum23P == 'OP23P8':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 180
            
            action_name = 'Circle Graph.001Action.001'
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
    
class ADDONNAME_LGC(bpy.types.Operator):
    bl_label = "Add Ob33jectlgc"
    bl_idname = "addonname.myop_operatorlgc"  
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enumLGC == 'OPLGC7':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 96
            
            action_name = 'CubeAction.003'
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
            
            action_name = 'CubeAction.003'
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

            action_name = 'CubeAction.003'
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
            
            action_name = 'CubeAction.003'
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

            action_name = 'CubeAction.003'
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
            
            action_name = 'CubeAction.003'
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

            action_name = 'CubeAction.003'
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
            
            action_name = 'CubeAction.003'
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


            
        if mytool.my_enumLGC == 'OPLGC8':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 120
            
            action_name = 'CubeAction.003'
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
            
            action_name = 'CubeAction.003'
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

            action_name = 'CubeAction.003'
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
            
            action_name = 'CubeAction.003'
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

            action_name = 'CubeAction.003'
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
            
            action_name = 'CubeAction.003'
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

            action_name = 'CubeAction.003'
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
            
            action_name = 'CubeAction.003'
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
    
class ADDONNAME_HBC(bpy.types.Operator):
    bl_label = "Add Ob33jectHBC"
    bl_idname = "addonname.myop_operatorhbc"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enumHBC == 'OPHBC7':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 168
            
            action_name = 'Plane.004Action.001'
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
                
            action_name = 'Plane.004Action.001'
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
                
            action_name = 'Plane.004Action.001'
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
                
            action_name = 'Plane.004Action.001'
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

            
        if mytool.my_enumHBC == 'OPHBC8':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 210
            
            action_name = 'Plane.004Action.001'
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
                
            action_name = 'Plane.004Action.001'
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
                
            action_name = 'Plane.004Action.001'
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
                
            action_name = 'Plane.004Action.001'
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
    
class ADDONNAME_MG(bpy.types.Operator):
    bl_label = "Add Ob33jectMG"
    bl_idname = "addonname.myop_operatormg"  
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enumMG == 'OPMG7':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 96
            
            action_name = 'Cube.003Action'
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
            
            action_name = 'Cube.003Action'
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

            action_name = 'Cube.003Action'
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
            
            action_name = 'Cube.003Action'
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

            action_name = 'Cube.003Action'
            data_path = 'modifiers["GeometryNodes"]["Input_34"]'
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
            
            action_name = 'Cube.003Action'
            data_path = 'modifiers["GeometryNodes"]["Input_35"]'
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

            action_name = 'Cube.003Action'
            data_path = 'modifiers["GeometryNodes"]["Input_36"]'
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
            
            action_name = 'Cube.003Action'
            data_path = 'modifiers["GeometryNodes"]["Input_37"]'
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


            
        if mytool.my_enumMG == 'OPMG8':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 120
            
            action_name = 'Cube.003Action'
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
            
            action_name = 'Cube.003Action'
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

            action_name = 'Cube.003Action'
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
            
            action_name = 'Cube.003Action'
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

            action_name = 'Cube.003Action'
            data_path = 'modifiers["GeometryNodes"]["Input_34"]'
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
            
            action_name = 'Cube.003Action'
            data_path = 'modifiers["GeometryNodes"]["Input_35"]'
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

            action_name = 'Cube.003Action'
            data_path = 'modifiers["GeometryNodes"]["Input_36"]'
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
            
            action_name = 'Cube.003Action'
            data_path = 'modifiers["GeometryNodes"]["Input_37"]'
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

class ADDONNAME_MGC(bpy.types.Operator):
    bl_label = "Add Ob33jectmgc"
    bl_idname = "addonname.myop_operatormgc"  
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enumMGC == 'OPMGC7':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 96
            
            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_46"]'
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
            
            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_47"]'
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

            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_48"]'
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
            
            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_49"]'
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

            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_50"]'
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
            
            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_51"]'
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

            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_52"]'
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
            
            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_53"]'
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


            
        if mytool.my_enumMGC == 'OPMGC8':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 120
            
            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_46"]'
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
            
            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_47"]'
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

            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_48"]'
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
            
            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_49"]'
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

            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_50"]'
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
            
            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_51"]'
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

            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_52"]'
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
            
            action_name = 'Cube.004Action'
            data_path = 'modifiers["GeometryNodes"]["Input_53"]'
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

    
class ADDONNAME_VB(bpy.types.Operator):
    bl_label = "Add Ob33jectVB"
    bl_idname = "addonname.myop_operatorvb"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enumVB == 'OPVB7':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 168
            
            action_name = 'Plane.004Action.003'
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
                
            action_name = 'Plane.004Action.003'
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
                
            action_name = 'Plane.004Action.003'
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
                
            action_name = 'Plane.004Action.003'
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

            action_name = 'Plane.004Action.003'
            data_path = 'modifiers["GeometryNodes"]["Input_53"]'
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
 
            action_name = 'Plane.004Action.003'
            data_path = 'modifiers["GeometryNodes"]["Input_54"]'
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
 
            action_name = 'Plane.004Action.003'
            data_path = 'modifiers["GeometryNodes"]["Input_55"]'
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
 
            action_name = 'Plane.004Action.003'
            data_path = 'modifiers["GeometryNodes"]["Input_56"]'
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

            
        if mytool.my_enumVB == 'OPVB8':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 210
            
            action_name = 'Plane.004Action.003'
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
                
            action_name = 'Plane.004Action.003'
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
                
            action_name = 'Plane.004Action.003'
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
                
            action_name = 'Plane.004Action.003'
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
    
            action_name = 'Plane.004Action.003'
            data_path = 'modifiers["GeometryNodes"]["Input_53"]'
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
  
            action_name = 'Plane.004Action.003'
            data_path = 'modifiers["GeometryNodes"]["Input_54"]'
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

            action_name = 'Plane.004Action.003'
            data_path = 'modifiers["GeometryNodes"]["Input_55"]'
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

            action_name = 'Plane.004Action.003'
            data_path = 'modifiers["GeometryNodes"]["Input_56"]'
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

class ADDONNAME_VBC(bpy.types.Operator):
    bl_label = "Add Ob33jectVBC"
    bl_idname = "addonname.myop_operatorvbc"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enumVBC == 'OPVBC7':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 168
            
            action_name = 'Plane.004Action.004'
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
                
            action_name = 'Plane.004Action.004'
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
                
            action_name = 'Plane.004Action.004'
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
                
            action_name = 'Plane.004Action.004'
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

            action_name = 'Plane.004Action.004'
            data_path = 'modifiers["GeometryNodes"]["Input_53"]'
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
 
            action_name = 'Plane.004Action.004'
            data_path = 'modifiers["GeometryNodes"]["Input_54"]'
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
 
            action_name = 'Plane.004Action.004'
            data_path = 'modifiers["GeometryNodes"]["Input_55"]'
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
 
            action_name = 'Plane.004Action.004'
            data_path = 'modifiers["GeometryNodes"]["Input_56"]'
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

            
        if mytool.my_enumVBC == 'OPVBC8':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 210
            
            action_name = 'Plane.004Action.004'
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
                
            action_name = 'Plane.004Action.004'
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
                
            action_name = 'Plane.004Action.004'
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
                
            action_name = 'Plane.004Action.004'
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
    
            action_name = 'Plane.004Action.004'
            data_path = 'modifiers["GeometryNodes"]["Input_53"]'
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
  
            action_name = 'Plane.004Action.004'
            data_path = 'modifiers["GeometryNodes"]["Input_54"]'
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

            action_name = 'Plane.004Action.004'
            data_path = 'modifiers["GeometryNodes"]["Input_55"]'
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

            action_name = 'Plane.004Action.004'
            data_path = 'modifiers["GeometryNodes"]["Input_56"]'
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

classes = [MyProperties, MyoperatorCGcsv, MyoperatorCGCcsv, MyoperatorPGCcsv, MyoperatorPGcsv, MyoperatorLGcsv, MyoperatorLGCcsv, MyoperatorHBcsv, MyoperatorHBCcsv, MyoperatorMCcsv, MyoperatorMPcsv, MyoperatorMGcsv, MyoperatorMGCcsv, MyoperatorVBcsv, MyoperatorVBCcsv, RenderRender2, ADDONNAME_OT_my_opgg, ADDONNAME_23C, ADDONNAME_23P, ADDONNAME_LGC, ADDONNAME_HBC, ADDONNAME_MG, ADDONNAME_MGC, ADDONNAME_VB, ADDONNAME_VBC, ADDONNAME_OT_my_opggpie, ADDONNAME_OT_my_op, ADDONNAME_OT_my_op2, ADDONNAME_OT_my_op2pie, ADDONNAME_OT_my_oplgpie, ADDONNAME_OT_my_ophbpie, ADDONNAME_OT_my_opmcpie, ADDONNAME_OT_my_opmppie, ADDONNAME_OT_my_op3, Fontchange, Fontchangepie, Fontrestore, Fontrestorepie, Endchange, Endchangepie, Locationchange,  TestPanel, TestPanel2, TestPanel2C, TestPanel3, TestPanel3P, TestPanel4, TestPanel4LGC, TestPanel5, TestPanel5C, TestPanel6, TestPanel7, TestPanel8, TestPanel8C, TestPanel9, TestPanel9VB]
 
 
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


