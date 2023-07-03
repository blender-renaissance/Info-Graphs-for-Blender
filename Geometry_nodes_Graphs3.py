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
        
    my_float23CA: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23cal()
        )
        
    my_float23CLA: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23cal()
        )
        
    my_float23CB: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23cbl()
        )
        
    my_float23CLB: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23cbl()
        )
        
    my_float23CC: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23ccl()
        )
        
    my_float23CLC: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23ccl()
        )
        
    my_float23PA: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23pal()
        )
        
    my_float23PLA: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23pal()
        )
        
    my_float23PB: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23pbl()
        )
        
    my_float23PLB: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23pbl()
        )
        
    my_float23PC: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23pcl()
        )
        
    my_float23PLC: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operator23pcl()
        )
        
    my_floatHBGA: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgal()
        )
        
    my_floatHBGLA: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgal()
        )
        
    my_floatHBGB: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgbl()
        )
        
    my_floatHBGLB: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgbl()
        )
        
    my_floatHBGC: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgcl()
        )
        
    my_floatHBGLC: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgcl()
        )
        
    my_floatHBGD: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgdl()
        )
        
    my_floatHBGLD: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgdl()
        )
        
        
    my_floatCOMPARISONAHBARA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbara()
    )
    
    my_floatCOMPARISONAHBARLA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbara()
    )
    
    my_floatCOMPARISONAHBARB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbarb()
    )
    
    my_floatCOMPARISONAHBARLB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbarb()
    )
    
    my_floatCOMPARISONAHBARC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbarc()
    )
    
    my_floatCOMPARISONAHBARLC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbarc()
    )
    
    my_floatCOMPARISONAHBARD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbard()
    )
    
    my_floatCOMPARISONAHBARLD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbard()
    )

    my_floatCOMPARISONBHBARA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbara()
    )

    my_floatCOMPARISONBHBARLA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbara()
    )

    my_floatCOMPARISONBHBARB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbarb()
    )

    my_floatCOMPARISONBHBARLB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbarb()
    )

    my_floatCOMPARISONBHBARC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbarc()
    )

    my_floatCOMPARISONBHBARLC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbarc()
    )

    my_floatCOMPARISONBHBARD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbard()
    )

    my_floatCOMPARISONBHBARDL: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbard()
    )


    my_floatCOMPARISONALINEA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalinea()
    )

    my_floatCOMPARISONALINELA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalinea()
    )

    my_floatCOMPARISONALINEB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalineb()
    )

    my_floatCOMPARISONALINELB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalineb()
    )

    my_floatCOMPARISONALINEC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalinec()
    )

    my_floatCOMPARISONALINELC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalinec()
    )

    my_floatCOMPARISONALINED: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalined()
    )

    my_floatCOMPARISONALINELD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalined()
    )

    my_floatCOMPARISONBLINEA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblinea()
    )

    my_floatCOMPARISONBLINELA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblinea()
    )

    my_floatCOMPARISONBLINEB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblineb()
    )

    my_floatCOMPARISONBLINELB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblineb()
    )

    my_floatCOMPARISONBLINEC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblinec()
    )

    my_floatCOMPARISONBLINELC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblinec()
    )

    my_floatCOMPARISONBLINED: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblined()
    )

    my_floatCOMPARISONBLINELD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblined()
    )

    my_floatCOMPARISONALINEE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonealinee()
    )

    my_floatCOMPARISONALINELE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonealinee()
    )

    my_floatCOMPARISONALINEF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalinef()
    )

    my_floatCOMPARISONALINELF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalinef()
    )

    my_floatCOMPARISONALINEG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalineg()
    )

    my_floatCOMPARISONALINELG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalineg()
    )

    my_floatCOMPARISONALINEH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalineh()
    )

    my_floatCOMPARISONALINELH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonalineh()
    )

    my_floatCOMPARISONBLINEE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisoneblinee()
    )

    my_floatCOMPARISONBLINELE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisoneblinee()
    )

    my_floatCOMPARISONBLINEF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblinef()
    )

    my_floatCOMPARISONBLINELF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblinef()
    )

    my_floatCOMPARISONBLINEG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblineg()
    )

    my_floatCOMPARISONBLINELG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblineg()
    )

    my_floatCOMPARISONBLINEH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblineh()
    )

    my_floatCOMPARISONBLINELH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonblineh()
    )


        
    my_floatLGA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgal()
    )
        
    my_floatLGLA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgal()
    )
        
    my_floatLGB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgbl()
    )
        
    my_floatLGLB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgbl()
    )
        
    my_floatLGC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgcl()
    )
        
    my_floatLGLC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgcl()
    )
        
    my_floatLGD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgdl()
    )
        
    my_floatLGLD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgdl()
    )
        
    my_floatLGE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgel()
    )
        
    my_floatLGLE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgel()
    )
        
    my_floatLGF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgfl()
    )
        
    my_floatLGLF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgfl()
    )
        
    my_floatLGG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlggl()
    )
        
    my_floatLGLG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlggl()
    )
        
    my_floatLGH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlghl()
    )
        
    my_floatLGLH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlghl()
    )

    my_floatMCGA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgal()
    )

    my_floatMCGLA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgal()
    )

    my_floatMCGB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=2,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgbl()
    )

    my_floatMCGLB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgbl()
    )

    my_floatMCGC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=3,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgcl()
    )

    my_floatMCGLC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgcl()
    )

    my_floatMCGD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgdl()
    )

    my_floatMCGLD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgdl()
    )

    my_floatMCGE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=5,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgel()
    )

    my_floatMCGLE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgel()
    )

    my_floatMPGA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgal()
    )

    my_floatMPGLA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgal()
    )

    my_floatMPGB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=2,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgbl()
    )

    my_floatMPGLB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgbl()
    )

    my_floatMPGC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=3,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgcl()
    )

    my_floatMPGLC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgcl()
    )

    my_floatMPGD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgdl()
    )

    my_floatMPGLD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgdl()
    )

    my_floatMPGE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=5,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgel()
    )

    my_floatMPGLE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgel()
    )



    my_floatMGA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgal()
    )
        
    my_floatMGLA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgal()
    )
        
    my_floatMGB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgbl()
    )
        
    my_floatMGLB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgbl()
    )
        
    my_floatMGC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgcl()
    )
        
    my_floatMGLC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgcl()
    )
        
    my_floatMGD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgdl()
    )
        
    my_floatMGLD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgdl()
    )
        
    my_floatMGE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgel()
    )
        
    my_floatMGLE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgel()
    )
        
    my_floatMGF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgfl()
    )
        
    my_floatMGLF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormgfl()
    )
        
    my_floatMGG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormggl()
    )
        
    my_floatMGLG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormggl()
    )
        
    my_floatMGH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormghl()
    )
        
    my_floatMGLH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormghl()
    )
    
    

    my_floatCOMPARISONAMOUNTA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamounta()
    )

    my_floatCOMPARISONAMOUNTLA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamounta()
    )

    my_floatCOMPARISONAMOUNTB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamountb()
    )

    my_floatCOMPARISONAMOUNTLB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamountb()
    )

    my_floatCOMPARISONAMOUNTC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamountc()
    )

    my_floatCOMPARISONAMOUNTLC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamountc()
    )

    my_floatCOMPARISONAMOUNTD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamountd()
    )

    my_floatCOMPARISONAMOUNTLD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamountd()
    )

    my_floatCOMPARISONBMOUNTA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmounta()
    )

    my_floatCOMPARISONBMOUNTLA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmounta()
    )

    my_floatCOMPARISONBMOUNTB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmountb()
    )

    my_floatCOMPARISONBMOUNTLB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmountb()
    )

    my_floatCOMPARISONBMOUNTC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmountc()
    )

    my_floatCOMPARISONBMOUNTLC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmountc()
    )

    my_floatCOMPARISONBMOUNTD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmountd()
    )

    my_floatCOMPARISONBMOUNTLD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmountd()
    )

    my_floatCOMPARISONAMOUNTE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamounte()
    )

    my_floatCOMPARISONAMOUNTLE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamounte()
    )

    my_floatCOMPARISONAMOUNTF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamountf()
    )

    my_floatCOMPARISONAMOUNTLF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamountf()
    )

    my_floatCOMPARISONAMOUNTG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamountg()
    )

    my_floatCOMPARISONAMOUNTLG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamountg()
    )

    my_floatCOMPARISONAMOUNTH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamounth()
    )

    my_floatCOMPARISONAMOUNTLH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonamounth()
    )

    my_floatCOMPARISONBMOUNTE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmounte()
    )

    my_floatCOMPARISONBMOUNTLE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmounte()
    )

    my_floatCOMPARISONBMOUNTF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmountf()
    )

    my_floatCOMPARISONBMOUNTLF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmountf()
    )

    my_floatCOMPARISONBMOUNTG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmountg()
    )

    my_floatCOMPARISONBMOUNTLG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmountg()
    )

    my_floatCOMPARISONBMOUNTH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmounth()
    )

    my_floatCOMPARISONBMOUNTLH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbmounth()
    )

    my_floatCOMPARISONABARVA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarva()
    )

    my_floatCOMPARISONABARVLA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarva()
    )

    my_floatCOMPARISONABARVB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvb()
    )

    my_floatCOMPARISONABARVLB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvb()
    )

    my_floatCOMPARISONABARVC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvc()
    )

    my_floatCOMPARISONABARVLC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvc()
    )

    my_floatCOMPARISONABARVD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvd()
    )

    my_floatCOMPARISONABARVLD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvd()
    )

    my_floatCOMPARISONBBARVA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarva()
    )

    my_floatCOMPARISONBBARVLA: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarva()
    )

    my_floatCOMPARISONBBARVB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvb()
    )

    my_floatCOMPARISONBBARVLB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvb()
    )

    my_floatCOMPARISONBBARVC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvc()
    )

    my_floatCOMPARISONBBARVLC: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvc()
    )

    my_floatCOMPARISONBBARVD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvd()
    )

    my_floatCOMPARISONBBARVLD: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvd()
    )

    my_floatCOMPARISONABARVE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarve()
    )

    my_floatCOMPARISONABARVLE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarve()
    )

    my_floatCOMPARISONABARVF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvf()
    )

    my_floatCOMPARISONABARVLF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvf()
    )

    my_floatCOMPARISONABARVG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvg()
    )

    my_floatCOMPARISONABARVLG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvg()
    )

    my_floatCOMPARISONABARVH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvh()
    )

    my_floatCOMPARISONABARVLH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonabarvh()
    )

    my_floatCOMPARISONBBARVE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarve()
    )

    my_floatCOMPARISONBBARVLE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarve()
    )

    my_floatCOMPARISONBBARVF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvf()
    )

    my_floatCOMPARISONBBARVLF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvf()
    )

    my_floatCOMPARISONBBARVG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvg()
    )

    my_floatCOMPARISONBBARVLG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvg()
    )

    my_floatCOMPARISONBBARVH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvh()
    )

    my_floatCOMPARISONBBARVLH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbbarvh()
    )


    
        
    my_floatVBGA: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgal()
        )
        
    my_floatVBGLA: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgal()
        )
        
    my_floatVBGB: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgbl()
        )
        
    my_floatVBGLB: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgbl()
        )
        
    my_floatVBGC: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgcl()
        )
        
    my_floatVBGLC: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgcl()
        )
        
    my_floatVBGD: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgdl()
        )
        
    my_floatVBGLD: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgdl()
        )
        
    my_floatVBGE: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgel()
        )
        
    my_floatVBGLE: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgel()
        )
        
    my_floatVBGF: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgfl()
        )
        
    my_floatVBGLF: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbgfl()
        )
        
    my_floatVBGG: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbggl()
        )
        
    my_floatVBGLG: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbggl()
        )
        
    my_floatVBGH: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbghl()
        )
        
    my_floatVBGLH: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorvbghl()
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
        name = "In seconds",
        description = "A float2 property",
        default =0,
        min = 0,
        max = 100000,
        update=lambda self, context: bpy.ops.addonname.myop_operatorgg()
        )
        
    my_float2pie: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float2 property",
        default =0,
        min = 0,
        max = 100000,
        update=lambda self, context: bpy.ops.addonname.myop_operatorggpie()
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
        

class TestPanel2:
    bl_label = "CG"
    bl_idname = "PT_TestPanel2"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel2_panel_1(TestPanel2, bpy.types.Panel):
    bl_idname = "TestPanel2_panel_1"
    bl_label = "Circle Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        row23CGcsv = layout.row()
        row23CGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_path")
        layout.operator("mesh.mycubeoperatorcgcsv")

        row23FPS = layout.row()
        row23FPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enum2")
       

class TestPanel2_panel_2(TestPanel2, bpy.types.Panel):
    bl_parent_id = "TestPanel2_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowG = layout.row()
        rowG.label(text= "Start Animation:")
        layout.prop(mytool, "my_float2")

        rowE = layout.row()
        rowE.label(text= "Length of Animation:")
        layout.prop(mytool, "my_float")
        
        
class TestPanel2C:
    bl_label = "2-3CG"
    bl_idname = "PT_TestPanel2c"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel2C_panel_1(TestPanel2C, bpy.types.Panel):
    bl_idname = "TestPanel2C_panel_1"
    bl_label = "2-3 Circle Graph"

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
        

class TestPanel2C_panel_2(TestPanel2C, bpy.types.Panel):
    bl_parent_id = "TestPanel2C_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        row23CA = layout.row()
        row23CA.label(text= "Start A:")
        layout.prop(mytool, "my_float23CA")
        
        row23CLA = layout.row()
        row23CLA.label(text= "Length of Animation A:")
        layout.prop(mytool, "my_float23CLA")
        
        row23CB = layout.row()
        row23CB.label(text= "Start B:")
        layout.prop(mytool, "my_float23CB")
        
        row23CLB = layout.row()
        row23CLB.label(text= "Length of Animation B:")
        layout.prop(mytool, "my_float23CLB")
        
        row23CC = layout.row()
        row23CC.label(text= "Start C:")
        layout.prop(mytool, "my_float23CC")
        
        row23CLC = layout.row()
        row23CLC.label(text= "Length of Animation C:")
        layout.prop(mytool, "my_float23CLC")
        
        
class TestPanel3:
    bl_label = "PG"
    bl_idname = "PT_TestPanel3"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel3_panel_1(TestPanel3, bpy.types.Panel):
    bl_idname = "TestPanel3_panel_1"
    bl_label = "Pie Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        row23CGcsv = layout.row()
        row23CGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathpie")
        layout.operator("mesh.mycubeoperatorpgcsv")

        row23FPS = layout.row()
        row23FPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enum2pie")
       

class TestPanel3_panel_2(TestPanel3, bpy.types.Panel):
    bl_parent_id = "TestPanel3_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowG = layout.row()
        rowG.label(text= "Start Animation:")
        layout.prop(mytool, "my_float2pie")

        rowE = layout.row()
        rowE.label(text= "Length of Animation:")
        layout.prop(mytool, "my_floatpie")

        
class TestPanel3P:
    bl_label = "2-3PG"
    bl_idname = "PT_TestPanel3p"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel3P_panel_1(TestPanel3P, bpy.types.Panel):
    bl_idname = "TestPanel3P_panel_1"
    bl_label = "2-3 Pie Graph"

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
        

class TestPanel3P_panel_2(TestPanel3P, bpy.types.Panel):
    bl_parent_id = "TestPanel3P_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        row23PA = layout.row()
        row23PA.label(text= "Start A:")
        layout.prop(mytool, "my_float23PA")
        
        row23PLA = layout.row()
        row23PLA.label(text= "Length of Animation A:")
        layout.prop(mytool, "my_float23PLA")
        
        row23PB = layout.row()
        row23PB.label(text= "Start B:")
        layout.prop(mytool, "my_float23PB")
        
        row23PLB = layout.row()
        row23PLB.label(text= "Length of Animation B:")
        layout.prop(mytool, "my_float23PLB")
        
        row23PC = layout.row()
        row23PC.label(text= "Start C:")
        layout.prop(mytool, "my_float23PC")
        
        row23PLC = layout.row()
        row23PLC.label(text= "Length of Animation C:")
        layout.prop(mytool, "my_float23PLC")
        
class TestPanel4:
    bl_label = "LG"
    bl_idname = "PT_TestPanel4"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel4_panel_1(TestPanel4, bpy.types.Panel):
    bl_idname = "TestPanel4_panel_1"
    bl_label = "Line Graph"

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
       

class TestPanel4_panel_2(TestPanel4, bpy.types.Panel):
    bl_parent_id = "TestPanel4_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowLGA = layout.row()
        rowLGA.label(text= "Start A:")
        layout.prop(mytool, "my_floatLGA")

        rowLGLA = layout.row()
        rowLGLA.label(text= "Length of Animation A:")
        layout.prop(mytool, "my_floatLGLA")

        rowLGB = layout.row()
        rowLGB.label(text= "Start B:")
        layout.prop(mytool, "my_floatLGB")

        rowLGLB = layout.row()
        rowLGLB.label(text= "Length of Animation B:")
        layout.prop(mytool, "my_floatLGLB")

        rowLGC = layout.row()
        rowLGC.label(text= "Start C:")
        layout.prop(mytool, "my_floatLGC")

        rowLGLC = layout.row()
        rowLGLC.label(text= "Length of Animation C:")
        layout.prop(mytool, "my_floatLGLC")

        rowLGD = layout.row()
        rowLGD.label(text= "Start D:")
        layout.prop(mytool, "my_floatLGD")

        rowLGLD = layout.row()
        rowLGLD.label(text= "Length of Animation D:")
        layout.prop(mytool, "my_floatLGLD")

        rowLGE = layout.row()
        rowLGE.label(text= "Start E:")
        layout.prop(mytool, "my_floatLGE")

        rowLGLE = layout.row()
        rowLGLE.label(text= "Length of Animation E:")
        layout.prop(mytool, "my_floatLGLE")

        rowLGF = layout.row()
        rowLGF.label(text= "Start F:")
        layout.prop(mytool, "my_floatLGF")

        rowLGLF = layout.row()
        rowLGLF.label(text= "Length of Animation F:")
        layout.prop(mytool, "my_floatLGLF")

        rowLGG = layout.row()
        rowLGG.label(text= "Start G:")
        layout.prop(mytool, "my_floatLGG")

        rowLGLG = layout.row()
        rowLGLG.label(text= "Length of Animation G:")
        layout.prop(mytool, "my_floatLGLG")

        rowLGH = layout.row()
        rowLGH.label(text= "Start H:")
        layout.prop(mytool, "my_floatLGH")

        rowLGLH = layout.row()
        rowLGLH.label(text= "Length of Animation H:")
        layout.prop(mytool, "my_floatLGLH")

        
class TestPanel4LGC:
    bl_label = "LGC"
    bl_idname = "PT_TestPanel4lgc"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel4LGC_panel_1(TestPanel4LGC, bpy.types.Panel):
    bl_idname = "TestPanel4LGC_panel_1"
    bl_label = "Line Graph Comparison"

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
       

class TestPanel4LGC_panel_2(TestPanel4LGC, bpy.types.Panel):
    bl_parent_id = "TestPanel4LGC_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCOMPARISONALINEA = layout.row()
        rowCOMPARISONALINEA.label(text= "Start A1:")
        layout.prop(mytool, "my_floatCOMPARISONALINEA")

        rowCOMPARISONALINELA = layout.row()
        rowCOMPARISONALINELA.label(text= "Length of Animation A1:")
        layout.prop(mytool, "my_floatCOMPARISONALINELA")

        rowCOMPARISONALINEB = layout.row()
        rowCOMPARISONALINEB.label(text= "Start B1:")
        layout.prop(mytool, "my_floatCOMPARISONBLINEA")

        rowCOMPARISONALINELB = layout.row()
        rowCOMPARISONALINELB.label(text= "Length of Animation B1:")
        layout.prop(mytool, "my_floatCOMPARISONBLINELA")

        rowCOMPARISONBLINEA = layout.row()
        rowCOMPARISONBLINEA.label(text= "Start A2:")
        layout.prop(mytool, "my_floatCOMPARISONALINEB")

        rowCOMPARISONBLINELA = layout.row()
        rowCOMPARISONBLINELA.label(text= "Length of Animation A2:")
        layout.prop(mytool, "my_floatCOMPARISONALINELB")

        rowCOMPARISONBLINEB = layout.row()
        rowCOMPARISONBLINEB.label(text= "Start B2:")
        layout.prop(mytool, "my_floatCOMPARISONBLINEB")

        rowCOMPARISONBLINELB = layout.row()
        rowCOMPARISONBLINELB.label(text= "Length of Animation B2:")
        layout.prop(mytool, "my_floatCOMPARISONBLINELB")

        rowCOMPARISONALINEC = layout.row()
        rowCOMPARISONALINEC.label(text= "Start A3:")
        layout.prop(mytool, "my_floatCOMPARISONALINEC")

        rowCOMPARISONALINELC = layout.row()
        rowCOMPARISONALINELC.label(text= "Length of Animation A3:")
        layout.prop(mytool, "my_floatCOMPARISONALINELC")

        rowCOMPARISONBLINEC = layout.row()
        rowCOMPARISONBLINEC.label(text= "Start B3:")
        layout.prop(mytool, "my_floatCOMPARISONBLINEC")

        rowCOMPARISONBLINELC = layout.row()
        rowCOMPARISONBLINELC.label(text= "Length of Animation B3:")
        layout.prop(mytool, "my_floatCOMPARISONBLINELC")

        rowCOMPARISONALINED = layout.row()
        rowCOMPARISONALINED.label(text= "Start A4:")
        layout.prop(mytool, "my_floatCOMPARISONALINED")

        rowCOMPARISONALINELD = layout.row()
        rowCOMPARISONALINELD.label(text= "Length of Animation A4:")
        layout.prop(mytool, "my_floatCOMPARISONALINELD")

        rowCOMPARISONBLINED = layout.row()
        rowCOMPARISONBLINED.label(text= "Start B4:")
        layout.prop(mytool, "my_floatCOMPARISONBLINED")

        rowCOMPARISONBLINELD = layout.row()
        rowCOMPARISONBLINELD.label(text= "Length of Animation B4:")
        layout.prop(mytool, "my_floatCOMPARISONBLINELD")

        rowCOMPARISONALINEE = layout.row()
        rowCOMPARISONALINEE.label(text= "Start A5:")
        layout.prop(mytool, "my_floatCOMPARISONALINEE")

        rowCOMPARISONALINELE = layout.row()
        rowCOMPARISONALINELE.label(text= "Length of Animation A5:")
        layout.prop(mytool, "my_floatCOMPARISONALINELE")

        rowCOMPARISONBLINEE = layout.row()
        rowCOMPARISONBLINEE.label(text= "Start B5:")
        layout.prop(mytool, "my_floatCOMPARISONBLINEE")

        rowCOMPARISONBLINELE = layout.row()
        rowCOMPARISONBLINELE.label(text= "Length of Animation B5:")
        layout.prop(mytool, "my_floatCOMPARISONBLINELE")

        rowCOMPARISONALINEF = layout.row()
        rowCOMPARISONALINEF.label(text= "Start A6:")
        layout.prop(mytool, "my_floatCOMPARISONALINEF")

        rowCOMPARISONALINELF = layout.row()
        rowCOMPARISONALINELF.label(text= "Length of Animation A6:")
        layout.prop(mytool, "my_floatCOMPARISONALINELF")

        rowCOMPARISONBLINEF = layout.row()
        rowCOMPARISONBLINEF.label(text= "Start B6:")
        layout.prop(mytool, "my_floatCOMPARISONBLINEF")

        rowCOMPARISONBLINELF = layout.row()
        rowCOMPARISONBLINELF.label(text= "Length of Animation B6:")
        layout.prop(mytool, "my_floatCOMPARISONBLINELF")

        rowCOMPARISONALINEG = layout.row()
        rowCOMPARISONALINEG.label(text= "Start A7:")
        layout.prop(mytool, "my_floatCOMPARISONALINEG")

        rowCOMPARISONALINELG = layout.row()
        rowCOMPARISONALINELG.label(text= "Length of Animation A7:")
        layout.prop(mytool, "my_floatCOMPARISONALINELG")

        rowCOMPARISONBLINEG = layout.row()
        rowCOMPARISONBLINEG.label(text= "Start B7:")
        layout.prop(mytool, "my_floatCOMPARISONBLINEG")

        rowCOMPARISONBLINELG = layout.row()
        rowCOMPARISONBLINELG.label(text= "Length of Animation B7:")
        layout.prop(mytool, "my_floatCOMPARISONBLINELG")

        rowCOMPARISONALINEH = layout.row()
        rowCOMPARISONALINEH.label(text= "Start A8:")
        layout.prop(mytool, "my_floatCOMPARISONALINEH")

        rowCOMPARISONALINELH = layout.row()
        rowCOMPARISONALINELH.label(text= "Length of Animation A8:")
        layout.prop(mytool, "my_floatCOMPARISONALINELH")

        rowCOMPARISONBLINEH = layout.row()
        rowCOMPARISONBLINEH.label(text= "Start B8:")
        layout.prop(mytool, "my_floatCOMPARISONBLINEH")

        rowCOMPARISONBLINELH = layout.row()
        rowCOMPARISONBLINELH.label(text= "Length of Animation B8:")
        layout.prop(mytool, "my_floatCOMPARISONBLINELH")


class TestPanel5:
    bl_label = "HBG"
    bl_idname = "PT_TestPanel5"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel5_panel_1(TestPanel5, bpy.types.Panel):
    bl_idname = "TestPanel5_panel_1"
    bl_label = "Horizontal Bar Graph"

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
        

class TestPanel5_panel_2(TestPanel5, bpy.types.Panel):
    bl_parent_id = "TestPanel5_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowHBGA = layout.row()
        rowHBGA.label(text= "Start A:")
        layout.prop(mytool, "my_floatHBGA")
        
        rowHBGLA = layout.row()
        rowHBGLA.label(text= "Length of Animation A:")
        layout.prop(mytool, "my_floatHBGLA")
        
        rowHBGB = layout.row()
        rowHBGB.label(text= "Start B:")
        layout.prop(mytool, "my_floatHBGB")
        
        rowHBGLB = layout.row()
        rowHBGLB.label(text= "Length of Animation B:")
        layout.prop(mytool, "my_floatHBGLB")
        
        rowHBGC = layout.row()
        rowHBGC.label(text= "Start C:")
        layout.prop(mytool, "my_floatHBGC")
        
        rowHBGLC = layout.row()
        rowHBGLC.label(text= "Length of Animation C:")
        layout.prop(mytool, "my_floatHBGLC")
        
        rowHBGD = layout.row()
        rowHBGD.label(text= "Start D:")
        layout.prop(mytool, "my_floatHBGD")
        
        rowHBGLD = layout.row()
        rowHBGLD.label(text= "Length of Animation D:")
        layout.prop(mytool, "my_floatHBGLD")
        
class TestPanel5C:
    bl_label = "HBGC"
    bl_idname = "PT_TestPanel5c"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel5c_panel_1(TestPanel5C, bpy.types.Panel):
    bl_idname = "TestPanel5C_panel_1"
    bl_label = "Horizontal Bar Graph Comparison"

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
        
class TestPanel5c_panel_2(TestPanel5C, bpy.types.Panel):
    bl_parent_id = "TestPanel5C_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCOMPARISONAHBARA = layout.row()
        rowCOMPARISONAHBARA.label(text= "Start A1:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARA")

        rowCOMPARISONAHBARLA = layout.row()
        rowCOMPARISONAHBARLA.label(text= "Length of Animation A1:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARLA")
        
        rowCOMPARISONAHBARB = layout.row()
        rowCOMPARISONAHBARB.label(text= "Start B1:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARA")

        rowCOMPARISONAHBARLB = layout.row()
        rowCOMPARISONAHBARLB.label(text= "Length of Animation B1:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARLA")
        
        rowCOMPARISONBHBARA = layout.row()
        rowCOMPARISONBHBARA.label(text= "Start A2:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARB")

        rowCOMPARISONBHBARLA = layout.row()
        rowCOMPARISONBHBARLA.label(text= "Length of Animation A2:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARLB")
        
        rowCOMPARISONBHBARB = layout.row()
        rowCOMPARISONBHBARB.label(text= "Start B2:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARB")

        rowCOMPARISONBHBARLB = layout.row()
        rowCOMPARISONBHBARLB.label(text= "Length of Animation B2:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARLB")

        rowCOMPARISONAHBARC = layout.row()
        rowCOMPARISONAHBARC.label(text= "Start A3:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARC")

        rowCOMPARISONAHBARLC = layout.row()
        rowCOMPARISONAHBARLC.label(text= "Length of Animation A3:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARLC")
        
        rowCOMPARISONBHBARC = layout.row()
        rowCOMPARISONBHBARC.label(text= "Start B3:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARC")

        rowCOMPARISONBHBARLC = layout.row()
        rowCOMPARISONBHBARLC.label(text= "Length of Animation B3:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARLC")

        rowCOMPARISONAHBARD = layout.row()
        rowCOMPARISONAHBARD.label(text= "Start A4:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARD")

        rowCOMPARISONAHBARLD = layout.row()
        rowCOMPARISONAHBARLD.label(text= "Length of Animation A4:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARLD")
        
        rowCOMPARISONBHBARD = layout.row()
        rowCOMPARISONBHBARD.label(text= "Start B4:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARD")

        rowCOMPARISONBHBARLD = layout.row()
        rowCOMPARISONBHBARLD.label(text= "Length of Animation B4:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARDL")


class TestPanel6:
    bl_label = "MCG"
    bl_idname = "PT_TestPanel6"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel6_panel_1(TestPanel6, bpy.types.Panel):
    bl_idname = "TestPanel6_panel_1"
    bl_label = "Multiple Circle Graph"

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
        
class TestPanel6_panel_2(TestPanel6, bpy.types.Panel):
    bl_parent_id = "TestPanel6_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowMCGA = layout.row()
        rowMCGA.label(text= "Start A:")
        layout.prop(mytool, "my_floatMCGA")

        rowMCGLA = layout.row()
        rowMCGLA.label(text= "Length of Animation A:")
        layout.prop(mytool, "my_floatMCGLA")

        rowMCGB = layout.row()
        rowMCGB.label(text= "Start B:")
        layout.prop(mytool, "my_floatMCGB")

        rowMCGLB = layout.row()
        rowMCGLB.label(text= "Length of Animation B:")
        layout.prop(mytool, "my_floatMCGLB")

        rowMCGC = layout.row()
        rowMCGC.label(text= "Start C:")
        layout.prop(mytool, "my_floatMCGC")

        rowMCGLC = layout.row()
        rowMCGLC.label(text= "Length of Animation C:")
        layout.prop(mytool, "my_floatMCGLC")

        rowMCGD = layout.row()
        rowMCGD.label(text= "Start D:")
        layout.prop(mytool, "my_floatMCGD")

        rowMCGLD = layout.row()
        rowMCGLD.label(text= "Length of Animation D:")
        layout.prop(mytool, "my_floatMCGLD")

        rowMCGE = layout.row()
        rowMCGE.label(text= "Start E:")
        layout.prop(mytool, "my_floatMCGE")

        rowMCGLE = layout.row()
        rowMCGLE.label(text= "Length of Animation E:")
        layout.prop(mytool, "my_floatMCGLE")

        
class TestPanel7:
    bl_label = "MPG"
    bl_idname = "PT_TestPanel7"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel7_panel_1(TestPanel7, bpy.types.Panel):
    bl_idname = "TestPanel7_panel_1"
    bl_label = "Multiple Pie Graph"

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
        
class TestPanel7_panel_2(TestPanel7, bpy.types.Panel):
    bl_parent_id = "TestPanel7_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowMPGA = layout.row()
        rowMPGA.label(text="Start A:")
        layout.prop(mytool, "my_floatMPGA")

        rowMPLA = layout.row()
        rowMPLA.label(text="Length of Animation A:")
        layout.prop(mytool, "my_floatMPGLA")

        rowMPGB = layout.row()
        rowMPGB.label(text="Start B:")
        layout.prop(mytool, "my_floatMPGB")

        rowMPLB = layout.row()
        rowMPLB.label(text="Length of Animation B:")
        layout.prop(mytool, "my_floatMPGLB")

        rowMPC = layout.row()
        rowMPC.label(text="Start C:")
        layout.prop(mytool, "my_floatMPGC")

        rowMPLC = layout.row()
        rowMPLC.label(text="Length of Animation C:")
        layout.prop(mytool, "my_floatMPGLC")

        rowMPD = layout.row()
        rowMPD.label(text="Start D:")
        layout.prop(mytool, "my_floatMPGD")

        rowMPLD = layout.row()
        rowMPLD.label(text="Length of Animation D:")
        layout.prop(mytool, "my_floatMPGLD")

        rowMPE = layout.row()
        rowMPE.label(text="Start E:")
        layout.prop(mytool, "my_floatMPGE")

        rowMPLE = layout.row()
        rowMPLE.label(text="Length of Animation E:")
        layout.prop(mytool, "my_floatMPGLE")

        
class TestPanel8:
    bl_label = "MG"
    bl_idname = "PT_TestPanel8"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel8_panel_1(TestPanel8, bpy.types.Panel):
    bl_idname = "TestPanel8_panel_1"
    bl_label = "Mountain Graph"

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
        
class TestPanel8_panel_2(TestPanel8, bpy.types.Panel):
    bl_parent_id = "TestPanel8_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowMGA = layout.row()
        rowMGA.label(text= "Start A:")
        layout.prop(mytool, "my_floatMGA")

        rowMGLA = layout.row()
        rowMGLA.label(text= "Length of Animation A:")
        layout.prop(mytool, "my_floatMGLA")

        rowMGB = layout.row()
        rowMGB.label(text= "Start B:")
        layout.prop(mytool, "my_floatMGB")

        rowMGLB = layout.row()
        rowMGLB.label(text= "Length of Animation B:")
        layout.prop(mytool, "my_floatMGLB")

        rowMGC = layout.row()
        rowMGC.label(text= "Start C:")
        layout.prop(mytool, "my_floatMGC")

        rowMGLC = layout.row()
        rowMGLC.label(text= "Length of Animation C:")
        layout.prop(mytool, "my_floatMGLC")

        rowMGD = layout.row()
        rowMGD.label(text= "Start D:")
        layout.prop(mytool, "my_floatMGD")

        rowMGLD = layout.row()
        rowMGLD.label(text= "Length of Animation D:")
        layout.prop(mytool, "my_floatMGLD")

        rowMGE = layout.row()
        rowMGE.label(text= "Start E:")
        layout.prop(mytool, "my_floatMGE")

        rowMGLE = layout.row()
        rowMGLE.label(text= "Length of Animation E:")
        layout.prop(mytool, "my_floatMGLE")

        rowMGF = layout.row()
        rowMGF.label(text= "Start F:")
        layout.prop(mytool, "my_floatMGF")

        rowMGLF = layout.row()
        rowMGLF.label(text= "Length of Animation F:")
        layout.prop(mytool, "my_floatMGLF")

        rowMGG = layout.row()
        rowMGG.label(text= "Start G:")
        layout.prop(mytool, "my_floatMGG")

        rowMGLG = layout.row()
        rowMGLG.label(text= "Length of Animation G:")
        layout.prop(mytool, "my_floatMGLG")

        rowMGH = layout.row()
        rowMGH.label(text= "Start H:")
        layout.prop(mytool, "my_floatMGH")

        rowMGLH = layout.row()
        rowMGLH.label(text= "Length of Animation H:")
        layout.prop(mytool, "my_floatMGLH")
        
        
class TestPanel8C:
    bl_label = "MGC"
    bl_idname = "PT_TestPanel8c"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel8C_panel_1(TestPanel8C, bpy.types.Panel):
    bl_idname = "TestPanel8c_panel_1"
    bl_label = "Mountain Graph Comparison"

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
        
class TestPanel8C_panel_2(TestPanel8C, bpy.types.Panel):
    bl_parent_id = "TestPanel8c_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool 
        
        rowCOMPARISONAMOUNTA = layout.row()
        rowCOMPARISONAMOUNTA.label(text= "Start A1:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTA")

        rowCOMPARISONAMOUNTLA = layout.row()
        rowCOMPARISONAMOUNTLA.label(text= "Length of Animation A1:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTLA")

        rowCOMPARISONAMOUNTB = layout.row()
        rowCOMPARISONAMOUNTB.label(text= "Start B1:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTA")

        rowCOMPARISONAMOUNTLB = layout.row()
        rowCOMPARISONAMOUNTLB.label(text= "Length of Animation B1:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTLA")

        rowCOMPARISONBMOUNTA = layout.row()
        rowCOMPARISONBMOUNTA.label(text= "Start A2:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTB")

        rowCOMPARISONBMOUNTLA = layout.row()
        rowCOMPARISONBMOUNTLA.label(text= "Length of Animation A2:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTLB")

        rowCOMPARISONBMOUNTB = layout.row()
        rowCOMPARISONBMOUNTB.label(text= "Start B2:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTB")

        rowCOMPARISONBMOUNTLB = layout.row()
        rowCOMPARISONBMOUNTLB.label(text= "Length of Animation B2:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTLB")

        rowCOMPARISONAMOUNTC = layout.row()
        rowCOMPARISONAMOUNTC.label(text= "Start A3:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTC")

        rowCOMPARISONAMOUNTLC = layout.row()
        rowCOMPARISONAMOUNTLC.label(text= "Length of Animation A3:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTLC")

        rowCOMPARISONBMOUNTC = layout.row()
        rowCOMPARISONBMOUNTC.label(text= "Start B3:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTC")

        rowCOMPARISONBMOUNTLC = layout.row()
        rowCOMPARISONBMOUNTLC.label(text= "Length of Animation B3:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTLC")

        rowCOMPARISONAMOUNTD = layout.row()
        rowCOMPARISONAMOUNTD.label(text= "Start A4:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTD")

        rowCOMPARISONAMOUNTLD = layout.row()
        rowCOMPARISONAMOUNTLD.label(text= "Length of Animation A4:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTLD")

        rowCOMPARISONBMOUNTD = layout.row()
        rowCOMPARISONBMOUNTD.label(text= "Start B4:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTD")

        rowCOMPARISONBMOUNTLD = layout.row()
        rowCOMPARISONBMOUNTLD.label(text= "Length of Animation B4:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTLD")

        rowCOMPARISONAMOUNTE = layout.row()
        rowCOMPARISONAMOUNTE.label(text= "Start A5:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTE")

        rowCOMPARISONAMOUNTLE = layout.row()
        rowCOMPARISONAMOUNTLE.label(text= "Length of Animation A5:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTLE")

        rowCOMPARISONBMOUNTE = layout.row()
        rowCOMPARISONBMOUNTE.label(text= "Start B5:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTE")

        rowCOMPARISONBMOUNTLE = layout.row()
        rowCOMPARISONBMOUNTLE.label(text= "Length of Animation B5:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTLE")

        rowCOMPARISONAMOUNTF = layout.row()
        rowCOMPARISONAMOUNTF.label(text= "Start A6:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTF")

        rowCOMPARISONAMOUNTLF = layout.row()
        rowCOMPARISONAMOUNTLF.label(text= "Length of Animation A6:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTLF")

        rowCOMPARISONBMOUNTF = layout.row()
        rowCOMPARISONBMOUNTF.label(text= "Start B6:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTF")

        rowCOMPARISONBMOUNTLF = layout.row()
        rowCOMPARISONBMOUNTLF.label(text= "Length of Animation B6:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTLF")

        rowCOMPARISONAMOUNTG = layout.row()
        rowCOMPARISONAMOUNTG.label(text= "Start A7:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTG")

        rowCOMPARISONAMOUNTLG = layout.row()
        rowCOMPARISONAMOUNTLG.label(text= "Length of Animation A7:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTLG")

        rowCOMPARISONBMOUNTG = layout.row()
        rowCOMPARISONBMOUNTG.label(text= "Start B7:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTG")

        rowCOMPARISONBMOUNTLG = layout.row()
        rowCOMPARISONBMOUNTLG.label(text= "Length of Animation B7:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTLG")

        rowCOMPARISONAMOUNTH = layout.row()
        rowCOMPARISONAMOUNTH.label(text= "Start A8:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTH")

        rowCOMPARISONAMOUNTLH = layout.row()
        rowCOMPARISONAMOUNTLH.label(text= "Length of Animation A8:")
        layout.prop(mytool, "my_floatCOMPARISONAMOUNTLH")

        rowCOMPARISONBMOUNTH = layout.row()
        rowCOMPARISONBMOUNTH.label(text= "Start B8:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTH")

        rowCOMPARISONBMOUNTLH = layout.row()
        rowCOMPARISONBMOUNTLH.label(text= "Length of Animation B8:")
        layout.prop(mytool, "my_floatCOMPARISONBMOUNTLH")

        
class TestPanel9:
    bl_label = "VBG"
    bl_idname = "PT_TestPanel9"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel9_panel_1(TestPanel9, bpy.types.Panel):
    bl_idname = "TestPanel9_panel_1"
    bl_label = "Vertical Bar Graph"

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
        
class TestPanel9_panel_2(TestPanel9, bpy.types.Panel):
    bl_parent_id = "TestPanel9_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowVBGA = layout.row()
        rowVBGA.label(text= "Start A:")
        layout.prop(mytool, "my_floatVBGA")
        
        rowVBGLA = layout.row()
        rowVBGLA.label(text= "Length of Animation A:")
        layout.prop(mytool, "my_floatVBGLA")
        
        rowVBGB = layout.row()
        rowVBGB.label(text= "Start B:")
        layout.prop(mytool, "my_floatVBGB")
        
        rowVBGLB = layout.row()
        rowVBGLB.label(text= "Length of Animation B:")
        layout.prop(mytool, "my_floatVBGLB")
        
        rowVBGC = layout.row()
        rowVBGC.label(text= "Start C:")
        layout.prop(mytool, "my_floatVBGC")
        
        rowVBGLC = layout.row()
        rowVBGLC.label(text= "Length of Animation C:")
        layout.prop(mytool, "my_floatVBGLC")
        
        rowVBGD = layout.row()
        rowVBGD.label(text= "Start D:")
        layout.prop(mytool, "my_floatVBGD")
        
        rowVBGLD = layout.row()
        rowVBGLD.label(text= "Length of Animation D:")
        layout.prop(mytool, "my_floatVBGLD")
        
        rowVBGE = layout.row()
        rowVBGE.label(text= "Start E:")
        layout.prop(mytool, "my_floatVBGE")
        
        rowVBGLE = layout.row()
        rowVBGLE.label(text= "Length of Animation E:")
        layout.prop(mytool, "my_floatVBGLE")
        
        rowVBGF = layout.row()
        rowVBGF.label(text= "Start F:")
        layout.prop(mytool, "my_floatVBGF")
        
        rowVBGLF = layout.row()
        rowVBGLF.label(text= "Length of Animation F:")
        layout.prop(mytool, "my_floatVBGLF")
        
        rowVBGG = layout.row()
        rowVBGG.label(text= "Start G:")
        layout.prop(mytool, "my_floatVBGG")
        
        rowVBGLG = layout.row()
        rowVBGLG.label(text= "Length of Animation G:")
        layout.prop(mytool, "my_floatVBGLG")
        
        rowVBGH = layout.row()
        rowVBGH.label(text= "Start H:")
        layout.prop(mytool, "my_floatVBGH")
        
        rowVBGLH = layout.row()
        rowVBGLH.label(text= "Length of Animation H:")
        layout.prop(mytool, "my_floatVBGLH") 
 
        
class TestPanel9VB:
    bl_label = "VBGC"
    bl_idname = "PT_TestPanel9vb"  
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}
    
class TestPanel9vb_panel_1(TestPanel9VB, bpy.types.Panel):
    bl_idname = "TestPanel9vb_panel_1"
    bl_label = "Vertical Bar Graph Comparison"

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
        
class TestPanel9vb_panel_2(TestPanel9VB, bpy.types.Panel):
    bl_parent_id = "TestPanel9vb_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCOMPARISONABARVA = layout.row()
        rowCOMPARISONABARVA.label(text= "Start A1:")
        layout.prop(mytool, "my_floatCOMPARISONABARVA")

        rowCOMPARISONABARVLA = layout.row()
        rowCOMPARISONABARVLA.label(text= "Length of Animation A1:")
        layout.prop(mytool, "my_floatCOMPARISONABARVLA")

        rowCOMPARISONBBARVB = layout.row()
        rowCOMPARISONBBARVB.label(text= "Start B1:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVA")

        rowCOMPARISONBBARVLB = layout.row()
        rowCOMPARISONBBARVLB.label(text= "Length of Animation B1:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVLA")

        rowCOMPARISONABARVB = layout.row()
        rowCOMPARISONABARVB.label(text= "Start A2:")
        layout.prop(mytool, "my_floatCOMPARISONABARVB")

        rowCOMPARISONABARVLB = layout.row()
        rowCOMPARISONABARVLB.label(text= "Length of Animation A2:")
        layout.prop(mytool, "my_floatCOMPARISONABARVLB")

        rowCOMPARISONBBARVB = layout.row()
        rowCOMPARISONBBARVB.label(text= "Start B2:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVB")

        rowCOMPARISONBBARVLB = layout.row()
        rowCOMPARISONBBARVLB.label(text= "Length of Animation B2:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVLB")

        rowCOMPARISONABARVC = layout.row()
        rowCOMPARISONABARVC.label(text= "Start A3:")
        layout.prop(mytool, "my_floatCOMPARISONABARVC")

        rowCOMPARISONABARVLC = layout.row()
        rowCOMPARISONABARVLC.label(text= "Length of Animation A3:")
        layout.prop(mytool, "my_floatCOMPARISONABARVLC")

        rowCOMPARISONBBARVC = layout.row()
        rowCOMPARISONBBARVC.label(text= "Start B3:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVC")

        rowCOMPARISONBBARVLC = layout.row()
        rowCOMPARISONBBARVLC.label(text= "Length of Animation B3:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVLC")

        rowCOMPARISONABARVD = layout.row()
        rowCOMPARISONABARVD.label(text= "Start A4:")
        layout.prop(mytool, "my_floatCOMPARISONABARVD")

        rowCOMPARISONABARVLD = layout.row()
        rowCOMPARISONABARVLD.label(text= "Length of Animation A4:")
        layout.prop(mytool, "my_floatCOMPARISONABARVLD")

        rowCOMPARISONBBARVD = layout.row()
        rowCOMPARISONBBARVD.label(text= "Start B4:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVD")

        rowCOMPARISONBBARVLD = layout.row()
        rowCOMPARISONBBARVLD.label(text= "Length of Animation B4:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVLD")

        rowCOMPARISONABARVE = layout.row()
        rowCOMPARISONABARVE.label(text= "Start A5:")
        layout.prop(mytool, "my_floatCOMPARISONABARVE")

        rowCOMPARISONABARVLE = layout.row()
        rowCOMPARISONABARVLE.label(text= "Length of Animation A5:")
        layout.prop(mytool, "my_floatCOMPARISONABARVLE")

        rowCOMPARISONBBARVE = layout.row()
        rowCOMPARISONBBARVE.label(text= "Start B5:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVE")

        rowCOMPARISONBBARVLE = layout.row()
        rowCOMPARISONBBARVLE.label(text= "Length of Animation B5:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVLE")

        rowCOMPARISONABARVF = layout.row()
        rowCOMPARISONABARVF.label(text= "Start A6:")
        layout.prop(mytool, "my_floatCOMPARISONABARVF")

        rowCOMPARISONABARVLF = layout.row()
        rowCOMPARISONABARVLF.label(text= "Length of Animation A6:")
        layout.prop(mytool, "my_floatCOMPARISONABARVLF")

        rowCOMPARISONBBARVF = layout.row()
        rowCOMPARISONBBARVF.label(text= "Start B6:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVF")

        rowCOMPARISONBBARVLF = layout.row()
        rowCOMPARISONBBARVLF.label(text= "Length of Animation B6:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVLF")

        rowCOMPARISONABARVG = layout.row()
        rowCOMPARISONABARVG.label(text= "Start A7:")
        layout.prop(mytool, "my_floatCOMPARISONABARVG")

        rowCOMPARISONABARVLG = layout.row()
        rowCOMPARISONABARVLG.label(text= "Length of Animation A7:")
        layout.prop(mytool, "my_floatCOMPARISONABARVLG")

        rowCOMPARISONBBARVG = layout.row()
        rowCOMPARISONBBARVG.label(text= "Start B7:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVG")

        rowCOMPARISONBBARVLG = layout.row()
        rowCOMPARISONBBARVLG.label(text= "Length of Animation B7:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVLG")

        rowCOMPARISONABARVH = layout.row()
        rowCOMPARISONABARVH.label(text= "Start A8:")
        layout.prop(mytool, "my_floatCOMPARISONABARVH")

        rowCOMPARISONABARVLH = layout.row()
        rowCOMPARISONABARVLH.label(text= "Length of Animation A8:")
        layout.prop(mytool, "my_floatCOMPARISONABARVLH")

        rowCOMPARISONBBARVH = layout.row()
        rowCOMPARISONBBARVH.label(text= "Start B8:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVH")

        rowCOMPARISONBBARVLH = layout.row()
        rowCOMPARISONBBARVLH.label(text= "Length of Animation B8:")
        layout.prop(mytool, "my_floatCOMPARISONBBARVLH")

        
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
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_67"] = valuea3mgc
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
        bpy.data.objects["Cube.004"].modifiers["GeometryNodes"]["Input_56"] = legendbmgc
        
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
        
class ADDONNAME_OT_my_opc(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorgg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle_GraphAction'
        data_path = 'modifiers["GeometryNodes"]["Input_30"]'
        index = 0
        stringc = mytool.my_float2
        frc = bpy.context.scene.render.fps
        jeffc = stringc*frc
        onemorec =  (mytool.my_float*frc) + jeffc
        bobc = onemorec 

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobc = int(bobc)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffc
                kps.handle_left[0] = jeffc-30
                kps.handle_right[0] = jeffc
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobc
                kpz.handle_left[0] = bobc-60
                kpz.handle_right[0] = bobc+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobc+frc


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_op23cAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operator23cal"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle_GraphAction.001'
        data_path = 'modifiers["GeometryNodes"]["Input_30"]'
        index = 0
        string23CA = mytool.my_float23CA
        fr23CA = bpy.context.scene.render.fps
        jeff23cal = string23CA*fr23CA
        onemorecal =  (mytool.my_float23CLA*fr23CA) + jeff23cal
        bob23cal = onemorecal       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bob23cal = int(bob23cal)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeff23cal
                kps.handle_left[0] = jeff23cal-30
                kps.handle_right[0] = jeff23cal
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bob23cal
                kpz.handle_left[0] = bob23cal-30
                kpz.handle_right[0] = bob23cal+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bob23cal+fr23CA


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_op23cBL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operator23cbl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle_GraphAction.001'
        data_path = 'modifiers["GeometryNodes"]["Input_49"]'
        index = 0
        string23CB = mytool.my_float23CB
        fr23CB = bpy.context.scene.render.fps
        jeff23cbl = string23CB*fr23CB
        onemorecbl =  (mytool.my_float23CLB*fr23CB) + jeff23cbl
        bob23cbl = onemorecbl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bob23cbl = int(bob23cbl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeff23cbl
                kps.handle_left[0] = jeff23cbl-30
                kps.handle_right[0] = jeff23cbl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bob23cbl
                kpz.handle_left[0] = bob23cbl-30
                kpz.handle_right[0] = bob23cbl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bob23cbl+fr23CB


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_op23cCL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operator23ccl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle_GraphAction.001'
        data_path = 'modifiers["GeometryNodes"]["Input_50"]'
        index = 0
        string23CC = mytool.my_float23CC
        fr23CC = bpy.context.scene.render.fps
        jeff23ccl = string23CC*fr23CC
        onemoreccl =  (mytool.my_float23CLC*fr23CC) + jeff23ccl
        bob23ccl = onemoreccl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bob23ccl = int(bob23ccl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeff23ccl
                kps.handle_left[0] = jeff23ccl-30
                kps.handle_right[0] = jeff23ccl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bob23ccl
                kpz.handle_left[0] = bob23ccl-30
                kpz.handle_right[0] = bob23ccl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bob23ccl+fr23CC


             
        return {'FINISHED'}
    

class ADDONNAME_OT_my_op23pAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operator23pal"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.001Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_25"]'
        index = 0
        string23PA = mytool.my_float23PA
        fr23PA = bpy.context.scene.render.fps
        jeff23pal = string23PA*fr23PA
        onemorepal =  (mytool.my_float23PLA*fr23PA) + jeff23pal
        bob23pal = onemorepal       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bob23pal = int(bob23pal)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeff23pal
                kps.handle_left[0] = jeff23pal-30
                kps.handle_right[0] = jeff23pal
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bob23pal
                kpz.handle_left[0] = bob23pal-30
                kpz.handle_right[0] = bob23pal+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bob23pal+fr23PA


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_op23pBL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operator23pbl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.001Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_44"]'
        index = 0
        string23PB = mytool.my_float23PB
        fr23PB = bpy.context.scene.render.fps
        jeff23pbl = string23PB*fr23PB
        onemorepbl =  (mytool.my_float23PLB*fr23PB) + jeff23pbl
        bob23pbl = onemorepbl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bob23pbl = int(bob23pbl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeff23pbl
                kps.handle_left[0] = jeff23pbl-30
                kps.handle_right[0] = jeff23pbl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bob23pbl
                kpz.handle_left[0] = bob23pbl-30
                kpz.handle_right[0] = bob23pbl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bob23pbl+fr23PB


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_op23pCL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operator23pcl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.001Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_45"]'
        index = 0
        string23PC = mytool.my_float23PC
        fr23PC = bpy.context.scene.render.fps
        jeff23pcl = string23PC*fr23PC
        onemorepcl =  (mytool.my_float23PLC*fr23PC) + jeff23pcl
        bob23pcl = onemorepcl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bob23pcl = int(bob23pcl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeff23pcl
                kps.handle_left[0] = jeff23pcl-30
                kps.handle_right[0] = jeff23pcl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bob23pcl
                kpz.handle_left[0] = bob23pcl-30
                kpz.handle_right[0] = bob23pcl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bob23pcl+fr23PC


             
        return {'FINISHED'}

class ADDONNAME_OT_my_opLGAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorlgal"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.001'
        data_path = 'modifiers["GeometryNodes"]["Input_26"]'
        index = 0
        stringLGAC = mytool.my_floatLGA
        frLGAC = bpy.context.scene.render.fps
        jefflga = stringLGAC*frLGAC
        onemorelga =  (mytool.my_floatLGLA*frLGAC) + jefflga
        boblga = onemorelga     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                boblga = int(boblga)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jefflga
                kps.handle_left[0] = jefflga-6
                kps.handle_right[0] = jefflga
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = boblga
                kpz.handle_left[0] = boblga-6
                kpz.handle_right[0] = boblga+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = boblga+(frLGAC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opLGBL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorlgbl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.001'
        data_path = 'modifiers["GeometryNodes"]["Input_27"]'
        index = 0
        stringLGBC = mytool.my_floatLGB
        frLGBC = bpy.context.scene.render.fps
        jefflgb = stringLGBC*frLGBC
        onemorelgb =  (mytool.my_floatLGLB*frLGBC) + jefflgb
        boblgb = onemorelgb    

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                boblgb = int(boblgb)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jefflgb
                kps.handle_left[0] = jefflgb-6
                kps.handle_right[0] = jefflgb
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = boblgb
                kpz.handle_left[0] = boblgb-6
                kpz.handle_right[0] = boblgb+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = boblgb+(frLGBC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opLGCL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorlgcl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.001'
        data_path = 'modifiers["GeometryNodes"]["Input_28"]'
        index = 0
        stringLGCC = mytool.my_floatLGC
        frLGCC = bpy.context.scene.render.fps
        jefflgc = stringLGCC*frLGCC
        onemorelgc =  (mytool.my_floatLGLC*frLGCC) + jefflgc
        boblgc = onemorelgc   

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                boblgc = int(boblgc)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jefflgc
                kps.handle_left[0] = jefflgc-6
                kps.handle_right[0] = jefflgc
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = boblgc
                kpz.handle_left[0] = boblgc-6
                kpz.handle_right[0] = boblgc+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = boblgc+(frLGCC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opLGDL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorlgdl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.001'
        data_path = 'modifiers["GeometryNodes"]["Input_29"]'
        index = 0
        stringLGDC = mytool.my_floatLGD
        frLGDC = bpy.context.scene.render.fps
        jefflgd = stringLGDC*frLGDC
        onemorelgd =  (mytool.my_floatLGLD*frLGDC) + jefflgd
        boblgd = onemorelgd   

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                boblgd = int(boblgd)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jefflgd
                kps.handle_left[0] = jefflgd-6
                kps.handle_right[0] = jefflgd
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = boblgd
                kpz.handle_left[0] = boblgd-6
                kpz.handle_right[0] = boblgd+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = boblgd+(frLGDC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opLGEL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorlgel"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.001'
        data_path = 'modifiers["GeometryNodes"]["Input_30"]'
        index = 0
        stringLGEC = mytool.my_floatLGE
        frLGEC = bpy.context.scene.render.fps
        jefflge = stringLGEC*frLGEC
        onemorelge =  (mytool.my_floatLGLE*frLGEC) + jefflge
        boblge = onemorelge 

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                boblge = int(boblge)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jefflge
                kps.handle_left[0] = jefflge-6
                kps.handle_right[0] = jefflge
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = boblge
                kpz.handle_left[0] = boblge-6
                kpz.handle_right[0] = boblge+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = boblge+(frLGEC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opLGFL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorlgfl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.001'
        data_path = 'modifiers["GeometryNodes"]["Input_31"]'
        index = 0
        stringLGFC = mytool.my_floatLGF
        frLGFC = bpy.context.scene.render.fps
        jefflgf = stringLGFC*frLGFC
        onemorelgf =  (mytool.my_floatLGLF*frLGFC) + jefflgf
        boblgf = onemorelgf    

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                boblgf = int(boblgf)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jefflgf
                kps.handle_left[0] = jefflgf-6
                kps.handle_right[0] = jefflgf
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = boblgf
                kpz.handle_left[0] = boblgf-6
                kpz.handle_right[0] = boblgf+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = boblgf+(frLGFC*2)


             
        return {'FINISHED'}
    

class ADDONNAME_OT_my_opLGGL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorlggl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.001'
        data_path = 'modifiers["GeometryNodes"]["Input_32"]'
        index = 0
        stringLGGC = mytool.my_floatLGG
        frLGGC = bpy.context.scene.render.fps
        jefflgg = stringLGGC*frLGGC
        onemorelgg =  (mytool.my_floatLGLG*frLGGC) + jefflgg
        boblgg = onemorelgg 

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                boblgg = int(boblgg)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jefflgg
                kps.handle_left[0] = jefflgg-6
                kps.handle_right[0] = jefflgg
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = boblgg
                kpz.handle_left[0] = boblgg-6
                kpz.handle_right[0] = boblgg+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = boblgg+(frLGGC*2)


             
        return {'FINISHED'}

    
class ADDONNAME_OT_my_opLGHL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorlghl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.001'
        data_path = 'modifiers["GeometryNodes"]["Input_33"]'
        index = 0
        stringLGHC = mytool.my_floatLGH
        frLGHC = bpy.context.scene.render.fps
        jefflgh = stringLGHC*frLGHC
        onemorelgh =  (mytool.my_floatLGLH*frLGHC) + jefflgh
        boblgh = onemorelgh   

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                boblgh = int(boblgh)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jefflgh
                kps.handle_left[0] = jefflgh-6
                kps.handle_right[0] = jefflgh
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = boblgh
                kpz.handle_left[0] = boblgh-6
                kpz.handle_right[0] = boblgh+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = boblgh+(frLGHC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONALINEAL(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonalinea"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_26"]'
        index = 0
        stringCALINEA = mytool.my_floatCOMPARISONALINEA
        frCALINEA = bpy.context.scene.render.fps
        jeffCALINEal = stringCALINEA * frCALINEA
        onemorecalineal = (mytool.my_floatCOMPARISONALINELA * frCALINEA) + jeffCALINEal
        bobCALINEal = onemorecalineal       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCALINEal = int(bobCALINEal)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCALINEal
                kps.handle_left[0] = jeffCALINEal - 6
                kps.handle_right[0] = jeffCALINEal
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCALINEal
                kpz.handle_left[0] = bobCALINEal - 6
                kpz.handle_right[0] = bobCALINEal + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCALINEal + frCALINEA

        return {'FINISHED'}
    

class ADDONNAME_OT_my_opCOMPARISONALINEB(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonalineb"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_27"]'
        index = 0
        stringCALINEB = mytool.my_floatCOMPARISONALINEB
        frCALINEB = bpy.context.scene.render.fps
        jeffCALINEb = stringCALINEB * frCALINEB
        onemorecalineb = (mytool.my_floatCOMPARISONALINELB * frCALINEB) + jeffCALINEb
        bobCALINEb = onemorecalineb       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCALINEb = int(bobCALINEb)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCALINEb
                kps.handle_left[0] = jeffCALINEb - 6
                kps.handle_right[0] = jeffCALINEb
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCALINEb
                kpz.handle_left[0] = bobCALINEb - 6
                kpz.handle_right[0] = bobCALINEb + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCALINEb + frCALINEB

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONALINEC(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonalinec"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_28"]'
        index = 0
        stringCALINEC = mytool.my_floatCOMPARISONALINEC
        frCALINEC = bpy.context.scene.render.fps
        jeffCALINEc = stringCALINEC * frCALINEC
        onemorecalinec = (mytool.my_floatCOMPARISONALINELC * frCALINEC) + jeffCALINEc
        bobCALINEc = onemorecalinec       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCALINEc = int(bobCALINEc)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCALINEc
                kps.handle_left[0] = jeffCALINEc - 6
                kps.handle_right[0] = jeffCALINEc
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCALINEc
                kpz.handle_left[0] = bobCALINEc - 6
                kpz.handle_right[0] = bobCALINEc + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCALINEc + frCALINEC

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONALINED(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonalined"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_29"]'
        index = 0
        stringCALINED = mytool.my_floatCOMPARISONALINED
        frCALINED = bpy.context.scene.render.fps
        jeffCALINEd = stringCALINED * frCALINED
        onemorecalined = (mytool.my_floatCOMPARISONALINELD * frCALINED) + jeffCALINEd
        bobCALINEd = onemorecalined       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCALINEd = int(bobCALINEd)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCALINEd
                kps.handle_left[0] = jeffCALINEd - 6
                kps.handle_right[0] = jeffCALINEd
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCALINEd
                kpz.handle_left[0] = bobCALINEd - 6
                kpz.handle_right[0] = bobCALINEd + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCALINEd + frCALINED

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONALINEE(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonealinee"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_30"]'
        index = 0
        stringCALINEE = mytool.my_floatCOMPARISONALINEE
        frCALINEE = bpy.context.scene.render.fps
        jeffCALINEe = stringCALINEE * frCALINEE
        onemorecalinee = (mytool.my_floatCOMPARISONALINELE * frCALINEE) + jeffCALINEe
        bobCALINEe = onemorecalinee       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCALINEe = int(bobCALINEe)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCALINEe
                kps.handle_left[0] = jeffCALINEe - 6
                kps.handle_right[0] = jeffCALINEe
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCALINEe
                kpz.handle_left[0] = bobCALINEe - 6
                kpz.handle_right[0] = bobCALINEe + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCALINEe + frCALINEE

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONALINEF(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonalinef"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_31"]'
        index = 0
        stringCALINEF = mytool.my_floatCOMPARISONALINEF
        frCALINEF = bpy.context.scene.render.fps
        jeffCALINEF = stringCALINEF * frCALINEF
        onemorecalinef = (mytool.my_floatCOMPARISONALINELF * frCALINEF) + jeffCALINEF
        bobCALINEF = onemorecalinef       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCALINEF = int(bobCALINEF)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCALINEF
                kps.handle_left[0] = jeffCALINEF - 6
                kps.handle_right[0] = jeffCALINEF
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCALINEF
                kpz.handle_left[0] = bobCALINEF - 6
                kpz.handle_right[0] = bobCALINEF + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCALINEF + frCALINEF

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONALINEG(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonalineg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_32"]'
        index = 0
        stringCALINEG = mytool.my_floatCOMPARISONALINEG
        frCALINEG = bpy.context.scene.render.fps
        jeffCALINEg = stringCALINEG * frCALINEG
        onemorecalineg = (mytool.my_floatCOMPARISONALINELG * frCALINEG) + jeffCALINEg
        bobCALINEg = onemorecalineg       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCALINEg = int(bobCALINEg)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCALINEg
                kps.handle_left[0] = jeffCALINEg - 6
                kps.handle_right[0] = jeffCALINEg
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCALINEg
                kpz.handle_left[0] = bobCALINEg - 6
                kpz.handle_right[0] = bobCALINEg + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCALINEg + frCALINEG

        return {'FINISHED'}

    
class ADDONNAME_OT_my_opCOMPARISONALINEH(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonalineh"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_33"]'
        index = 0
        stringCALINEH = mytool.my_floatCOMPARISONALINEH
        frCALINEH = bpy.context.scene.render.fps
        jeffCALINEh = stringCALINEH * frCALINEH
        onemorecalineh = (mytool.my_floatCOMPARISONALINELH * frCALINEH) + jeffCALINEh
        bobCALINEh = onemorecalineh       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCALINEh = int(bobCALINEh)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCALINEh
                kps.handle_left[0] = jeffCALINEh - 6
                kps.handle_right[0] = jeffCALINEh
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCALINEh
                kpz.handle_left[0] = bobCALINEh - 6
                kpz.handle_right[0] = bobCALINEh + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCALINEh + frCALINEH

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBLINEA(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonblinea"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_46"]'
        index = 0
        stringCBLINEA = mytool.my_floatCOMPARISONBLINEA
        frCBLINEA = bpy.context.scene.render.fps
        jeffCBLINEa = stringCBLINEA * frCBLINEA
        onemoreblinea = (mytool.my_floatCOMPARISONBLINELA * frCBLINEA) + jeffCBLINEa
        bobCBLINEa = onemoreblinea       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBLINEa = int(bobCBLINEa)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBLINEa
                kps.handle_left[0] = jeffCBLINEa - 6
                kps.handle_right[0] = jeffCBLINEa
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBLINEa
                kpz.handle_left[0] = bobCBLINEa - 6
                kpz.handle_right[0] = bobCBLINEa + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBLINEa + frCBLINEA

        return {'FINISHED'}


class ADDONNAME_OT_my_opCOMPARISONBLINEB(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonblineb"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_47"]'
        index = 0
        stringCBLINEB = mytool.my_floatCOMPARISONBLINEB
        frCBLINEB = bpy.context.scene.render.fps
        jeffCBLINEb = stringCBLINEB * frCBLINEB
        onemoreblineb = (mytool.my_floatCOMPARISONBLINELB * frCBLINEB) + jeffCBLINEb
        bobCBLINEb = onemoreblineb       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBLINEb = int(bobCBLINEb)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBLINEb
                kps.handle_left[0] = jeffCBLINEb - 6
                kps.handle_right[0] = jeffCBLINEb
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBLINEb
                kpz.handle_left[0] = bobCBLINEb - 6
                kpz.handle_right[0] = bobCBLINEb + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBLINEb + frCBLINEB

        return {'FINISHED'}


class ADDONNAME_OT_my_opCOMPARISONBLINEC(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonblinec"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_48"]'
        index = 0
        stringCBLINEC = mytool.my_floatCOMPARISONBLINEC
        frCBLINEC = bpy.context.scene.render.fps
        jeffCBLINEc = stringCBLINEC * frCBLINEC
        onemoreblinec = (mytool.my_floatCOMPARISONBLINELC * frCBLINEC) + jeffCBLINEc
        bobCBLINEc = onemoreblinec       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBLINEc = int(bobCBLINEc)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBLINEc
                kps.handle_left[0] = jeffCBLINEc - 6
                kps.handle_right[0] = jeffCBLINEc
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBLINEc
                kpz.handle_left[0] = bobCBLINEc - 6
                kpz.handle_right[0] = bobCBLINEc + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBLINEc + frCBLINEC

        return {'FINISHED'}


class ADDONNAME_OT_my_opCOMPARISONBLINED(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonblined"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_49"]'
        index = 0
        stringCBLINED = mytool.my_floatCOMPARISONBLINED
        frCBLINED = bpy.context.scene.render.fps
        jeffCBINEd = stringCBLINED * frCBLINED
        onemoreblined = (mytool.my_floatCOMPARISONBLINELD * frCBLINED) + jeffCBINEd
        bobCBINEd = onemoreblined       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBINEd = int(bobCBINEd)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBINEd
                kps.handle_left[0] = jeffCBINEd - 6
                kps.handle_right[0] = jeffCBINEd
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBINEd
                kpz.handle_left[0] = bobCBINEd - 6
                kpz.handle_right[0] = bobCBINEd + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBINEd + frCBLINED

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONBLINEE(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisoneblinee"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_50"]'
        index = 0
        stringCBLINEE = mytool.my_floatCOMPARISONBLINEE
        frCBLINEE = bpy.context.scene.render.fps
        jeffCBLINEe = stringCBLINEE * frCBLINEE
        onemoreblinee = (mytool.my_floatCOMPARISONBLINELE * frCBLINEE) + jeffCBLINEe
        bobCBLINEe = onemoreblinee       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBLINEe = int(bobCBLINEe)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBLINEe
                kps.handle_left[0] = jeffCBLINEe - 6
                kps.handle_right[0] = jeffCBLINEe
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBLINEe
                kpz.handle_left[0] = bobCBLINEe - 6
                kpz.handle_right[0] = bobCBLINEe + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBLINEe + frCBLINEE

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBLINEF(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonblinef"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_51"]'
        index = 0
        stringCBLINEF = mytool.my_floatCOMPARISONBLINEF
        frCBLINEF = bpy.context.scene.render.fps
        jeffCBLINEF = stringCBLINEF * frCBLINEF
        onemoreblinef = (mytool.my_floatCOMPARISONBLINELF * frCBLINEF) + jeffCBLINEF
        bobCBLINEF = onemoreblinef       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBLINEF = int(bobCBLINEF)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBLINEF
                kps.handle_left[0] = jeffCBLINEF - 6
                kps.handle_right[0] = jeffCBLINEF
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBLINEF
                kpz.handle_left[0] = bobCBLINEF - 6
                kpz.handle_right[0] = bobCBLINEF + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBLINEF + frCBLINEF

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBLINEG(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonblineg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_52"]'
        index = 0
        stringCBLINEG = mytool.my_floatCOMPARISONBLINEG
        frCBLINEG = bpy.context.scene.render.fps
        jeffCBLINEg = stringCBLINEG * frCBLINEG
        onemoreblineg = (mytool.my_floatCOMPARISONBLINELG * frCBLINEG) + jeffCBLINEg
        bobCBLINEg = onemoreblineg       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBLINEg = int(bobCBLINEg)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBLINEg
                kps.handle_left[0] = jeffCBLINEg - 6
                kps.handle_right[0] = jeffCBLINEg
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBLINEg
                kpz.handle_left[0] = bobCBLINEg - 6
                kpz.handle_right[0] = bobCBLINEg + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBLINEg + frCBLINEG

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBLINEH(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonblineh"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'CubeAction.003'
        data_path = 'modifiers["GeometryNodes"]["Input_53"]'
        index = 0
        stringCBLINEH = mytool.my_floatCOMPARISONBLINEH
        frCBLINEH = bpy.context.scene.render.fps
        jeffCBLINEh = stringCBLINEH * frCBLINEH
        onemoreblineh = (mytool.my_floatCOMPARISONBLINELH * frCBLINEH) + jeffCBLINEh
        bobCBLINEh = onemoreblineh       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBLINEh = int(bobCBLINEh)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBLINEh
                kps.handle_left[0] = jeffCBLINEh - 6
                kps.handle_right[0] = jeffCBLINEh
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBLINEh
                kpz.handle_left[0] = bobCBLINEh - 6
                kpz.handle_right[0] = bobCBLINEh + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBLINEh + frCBLINEH

        return {'FINISHED'}



class ADDONNAME_OT_my_opMGAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormgal"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.003Action'
        data_path = 'modifiers["GeometryNodes"]["Input_30"]'
        index = 0
        stringMGAC = mytool.my_floatMGA
        frMGAC = bpy.context.scene.render.fps
        jeffmga = stringMGAC*frMGAC
        onemoremga =  (mytool.my_floatMGLA*frMGAC) + jeffmga
        bobmga = onemoremga     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmga = int(bobmga)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmga
                kps.handle_left[0] = jeffmga-6
                kps.handle_right[0] = jeffmga
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmga
                kpz.handle_left[0] = bobmga-6
                kpz.handle_right[0] = bobmga+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmga+(frMGAC*2)


             
        return {'FINISHED'}


class ADDONNAME_OT_my_opMGBL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormgbl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.003Action'
        data_path = 'modifiers["GeometryNodes"]["Input_31"]'
        index = 0
        stringMGBC = mytool.my_floatMGB
        frMGBC = bpy.context.scene.render.fps
        jeffmgb = stringMGBC*frMGBC
        onemoremgb =  (mytool.my_floatMGLB*frMGBC) + jeffmgb
        bobmgb = onemoremgb    

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmgb = int(bobmgb)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmgb
                kps.handle_left[0] = jeffmgb-6
                kps.handle_right[0] = jeffmgb
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmgb
                kpz.handle_left[0] = bobmgb-6
                kpz.handle_right[0] = bobmgb+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmgb+(frMGBC*2)


             
        return {'FINISHED'}

class ADDONNAME_OT_my_opMGCL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormgcl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.003Action'
        data_path = 'modifiers["GeometryNodes"]["Input_32"]'
        index = 0
        stringMGCC = mytool.my_floatMGC
        frMGCC = bpy.context.scene.render.fps
        jeffmgc = stringMGCC*frMGCC
        onemoremgc =  (mytool.my_floatMGLC*frMGCC) + jeffmgc
        bobmgc = onemoremgc   

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmgc = int(bobmgc)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmgc
                kps.handle_left[0] = jeffmgc-6
                kps.handle_right[0] = jeffmgc
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmgc
                kpz.handle_left[0] = bobmgc-6
                kpz.handle_right[0] = bobmgc+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmgc+(frMGCC*2)


             
        return {'FINISHED'}

class ADDONNAME_OT_my_opMGDL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormgdl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.003Action'
        data_path = 'modifiers["GeometryNodes"]["Input_33"]'
        index = 0
        stringMGDC = mytool.my_floatMGD
        frMGDC = bpy.context.scene.render.fps
        jeffmgd = stringMGDC*frMGDC
        onemoremgd =  (mytool.my_floatMGLD*frMGDC) + jeffmgd
        bobmgd = onemoremgd   

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmgd = int(bobmgd)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmgd
                kps.handle_left[0] = jeffmgd-6
                kps.handle_right[0] = jeffmgd
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmgd
                kpz.handle_left[0] = bobmgd-6
                kpz.handle_right[0] = bobmgd+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmgd+(frMGDC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opMGEL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormgel"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.003Action'
        data_path = 'modifiers["GeometryNodes"]["Input_34"]'
        index = 0
        stringMGEC = mytool.my_floatMGE
        frMGEC = bpy.context.scene.render.fps
        jeffmge = stringMGEC*frMGEC
        onemoremge =  (mytool.my_floatMGLE*frMGEC) + jeffmge
        bobmge = onemoremge 

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmge = int(bobmge)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmge
                kps.handle_left[0] = jeffmge-6
                kps.handle_right[0] = jeffmge
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmge
                kpz.handle_left[0] = bobmge-6
                kpz.handle_right[0] = bobmge+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmge+(frMGEC*2)


             
        return {'FINISHED'}

    
class ADDONNAME_OT_my_opMGFL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormgfl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.003Action'
        data_path = 'modifiers["GeometryNodes"]["Input_35"]'
        index = 0
        stringMGFC = mytool.my_floatMGF
        frMGFC = bpy.context.scene.render.fps
        jeffmgf = stringMGFC*frMGFC
        onemoremgf =  (mytool.my_floatMGLF*frMGFC) + jeffmgf
        bobmgf = onemoremgf    

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmgf = int(bobmgf)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmgf
                kps.handle_left[0] = jeffmgf-6
                kps.handle_right[0] = jeffmgf
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmgf
                kpz.handle_left[0] = bobmgf-6
                kpz.handle_right[0] = bobmgf+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmgf+(frMGFC*2)


             
        return {'FINISHED'}
    

class ADDONNAME_OT_my_opMGGL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormggl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.003Action'
        data_path = 'modifiers["GeometryNodes"]["Input_36"]'
        index = 0
        stringMGGC = mytool.my_floatMGG
        frMGGC = bpy.context.scene.render.fps
        jeffmgg = stringMGGC*frMGGC
        onemoremgg =  (mytool.my_floatMGLG*frMGGC) + jeffmgg
        bobmgg = onemoremgg 

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmgg = int(bobmgg)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmgg
                kps.handle_left[0] = jeffmgg-6
                kps.handle_right[0] = jeffmgg
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmgg
                kpz.handle_left[0] = bobmgg-6
                kpz.handle_right[0] = bobmgg+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = boblgg+(frMGGC*2)


             
        return {'FINISHED'}
    
    
class ADDONNAME_OT_my_opMGHL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormghl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.003Action'
        data_path = 'modifiers["GeometryNodes"]["Input_37"]'
        index = 0
        stringMGHC = mytool.my_floatMGH
        frMGHC = bpy.context.scene.render.fps
        jeffmgh = stringMGHC*frMGHC
        onemoremgh =  (mytool.my_floatMGLH*frMGHC) + jeffmgh
        bobmgh = onemoremgh   

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmgh = int(bobmgh)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmgh
                kps.handle_left[0] = jeffmgh-6
                kps.handle_right[0] = jeffmgh
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmgh
                kpz.handle_left[0] = bobmgh-6
                kpz.handle_right[0] = bobmgh+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmgh+(frMGHC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONAMOUNTA(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonamounta"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_46"]'
        index = 0
        stringCAMOUNTA = mytool.my_floatCOMPARISONAMOUNTA
        frCAMOUNTA = bpy.context.scene.render.fps
        jeffCAMOUNTa = stringCAMOUNTA * frCAMOUNTA
        onemoreamounta = (mytool.my_floatCOMPARISONAMOUNTLA * frCAMOUNTA) + jeffCAMOUNTa
        bobCAMOUNTa = onemoreamounta       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAMOUNTa = int(bobCAMOUNTa)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAMOUNTa
                kps.handle_left[0] = jeffCAMOUNTa - 6
                kps.handle_right[0] = jeffCAMOUNTa
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAMOUNTa
                kpz.handle_left[0] = bobCAMOUNTa - 6
                kpz.handle_right[0] = bobCAMOUNTa + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAMOUNTa + frCAMOUNTA

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONAMOUNTB(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonamountb"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_47"]'
        index = 0
        stringCAMOUNTB = mytool.my_floatCOMPARISONAMOUNTB
        frCAMOUNTB = bpy.context.scene.render.fps
        jeffCAMOUNTb = stringCAMOUNTB * frCAMOUNTB
        onemorecamountb = (mytool.my_floatCOMPARISONAMOUNTLB * frCAMOUNTB) + jeffCAMOUNTb
        bobCAMOUNTb = onemorecamountb       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAMOUNTb = int(bobCAMOUNTb)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAMOUNTb
                kps.handle_left[0] = jeffCAMOUNTb - 6
                kps.handle_right[0] = jeffCAMOUNTb
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAMOUNTb
                kpz.handle_left[0] = bobCAMOUNTb - 6
                kpz.handle_right[0] = bobCAMOUNTb + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAMOUNTb + frCAMOUNTB

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONAMOUNTC(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonamountc"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_48"]'
        index = 0
        stringCAMOUNTC = mytool.my_floatCOMPARISONAMOUNTC
        frCAMOUNTC = bpy.context.scene.render.fps
        jeffCAMOUNTc = stringCAMOUNTC * frCAMOUNTC
        onemorecamountc = (mytool.my_floatCOMPARISONAMOUNTLC * frCAMOUNTC) + jeffCAMOUNTc
        bobCAMOUNTc = onemorecamountc       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAMOUNTc = int(bobCAMOUNTc)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAMOUNTc
                kps.handle_left[0] = jeffCAMOUNTc - 6
                kps.handle_right[0] = jeffCAMOUNTc
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAMOUNTc
                kpz.handle_left[0] = bobCAMOUNTc - 6
                kpz.handle_right[0] = bobCAMOUNTc + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAMOUNTc + frCAMOUNTC

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONAMOUNTD(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonamountd"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_49"]'
        index = 0
        stringCAMOUNTD = mytool.my_floatCOMPARISONAMOUNTD
        frCAMOUNTD = bpy.context.scene.render.fps
        jeffCAMOUNTd = stringCAMOUNTD * frCAMOUNTD
        onemorecamountd = (mytool.my_floatCOMPARISONAMOUNTLD * frCAMOUNTD) + jeffCAMOUNTd
        bobCAMOUNTd = onemorecamountd       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAMOUNTd = int(bobCAMOUNTd)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAMOUNTd
                kps.handle_left[0] = jeffCAMOUNTd - 6
                kps.handle_right[0] = jeffCAMOUNTd
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAMOUNTd
                kpz.handle_left[0] = bobCAMOUNTd - 6
                kpz.handle_right[0] = bobCAMOUNTd + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAMOUNTd + frCAMOUNTD

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONAMOUNTE(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonamounte"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_50"]'
        index = 0
        stringCAMOUNTE = mytool.my_floatCOMPARISONAMOUNTE
        frCAMOUNTE = bpy.context.scene.render.fps
        jeffCAMOUNTe = stringCAMOUNTE * frCAMOUNTE
        onemorecamounte = (mytool.my_floatCOMPARISONAMOUNTLE * frCAMOUNTE) + jeffCAMOUNTe
        bobCAMOUNTe = onemorecamounte       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAMOUNTe = int(bobCAMOUNTe)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAMOUNTe
                kps.handle_left[0] = jeffCAMOUNTe - 6
                kps.handle_right[0] = jeffCAMOUNTe
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAMOUNTe
                kpz.handle_left[0] = bobCAMOUNTe - 6
                kpz.handle_right[0] = bobCAMOUNTe + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAMOUNTe + frCAMOUNTE

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONAMOUNTF(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonamountf"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_51"]'
        index = 0
        stringCAMOUNTF = mytool.my_floatCOMPARISONAMOUNTF
        frCAMOUNTF = bpy.context.scene.render.fps
        jeffCAMOUNTF = stringCAMOUNTF * frCAMOUNTF
        onemorecamountf = (mytool.my_floatCOMPARISONAMOUNTLF * frCAMOUNTF) + jeffCAMOUNTF
        bobCAMOUNTF = onemorecamountf       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAMOUNTF = int(bobCAMOUNTF)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAMOUNTF
                kps.handle_left[0] = jeffCAMOUNTF - 6
                kps.handle_right[0] = jeffCAMOUNTF
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAMOUNTF
                kpz.handle_left[0] = bobCAMOUNTF - 6
                kpz.handle_right[0] = bobCAMOUNTF + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAMOUNTF + frCAMOUNTF

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONAMOUNTG(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonamountg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_52"]'
        index = 0
        stringCAMOUNTG = mytool.my_floatCOMPARISONAMOUNTG
        frCAMOUNTG = bpy.context.scene.render.fps
        jeffCAMOUNTg = stringCAMOUNTG * frCAMOUNTG
        onemorecamountg = (mytool.my_floatCOMPARISONAMOUNTLG * frCAMOUNTG) + jeffCAMOUNTg
        bobCAMOUNTg = onemorecamountg       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAMOUNTg = int(bobCAMOUNTg)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAMOUNTg
                kps.handle_left[0] = jeffCAMOUNTg - 6
                kps.handle_right[0] = jeffCAMOUNTg
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAMOUNTg
                kpz.handle_left[0] = bobCAMOUNTg - 6
                kpz.handle_right[0] = bobCAMOUNTg + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAMOUNTg + frCAMOUNTG

        return {'FINISHED'}

    
class ADDONNAME_OT_my_opCOMPARISONAMOUNTH(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonamounth"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_53"]'
        index = 0
        stringCAMOUNTH = mytool.my_floatCOMPARISONAMOUNTH
        frCAMOUNTH = bpy.context.scene.render.fps
        jeffCAMOUNTh = stringCAMOUNTH * frCAMOUNTH
        onemorecamounth = (mytool.my_floatCOMPARISONAMOUNTLH * frCAMOUNTH) + jeffCAMOUNTh
        bobCAMOUNTh = onemorecamounth       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAMOUNTh = int(bobCAMOUNTh)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAMOUNTh
                kps.handle_left[0] = jeffCAMOUNTh - 6
                kps.handle_right[0] = jeffCAMOUNTh
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAMOUNTh
                kpz.handle_left[0] = bobCAMOUNTh - 6
                kpz.handle_right[0] = bobCAMOUNTh + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAMOUNTh + frCAMOUNTH

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBMOUNTA(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbmounta"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_77"]'
        index = 0
        stringCBMOUNTA = mytool.my_floatCOMPARISONBMOUNTA
        frCBMOUNTA = bpy.context.scene.render.fps
        jeffCBMOUNTa = stringCBMOUNTA * frCBMOUNTA
        onemorebmounta = (mytool.my_floatCOMPARISONBMOUNTLA * frCBMOUNTA) + jeffCBMOUNTa
        bobCBMOUNTa = onemorebmounta       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBMOUNTa = int(bobCBMOUNTa)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBMOUNTa
                kps.handle_left[0] = jeffCBMOUNTa - 6
                kps.handle_right[0] = jeffCBMOUNTa
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBMOUNTa
                kpz.handle_left[0] = bobCBMOUNTa - 6
                kpz.handle_right[0] = bobCBMOUNTa + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBMOUNTa + frCBMOUNTA

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONBMOUNTB(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbmountb"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_78"]'
        index = 0
        stringCBMOUNTB = mytool.my_floatCOMPARISONBMOUNTB
        frCBMOUNTB = bpy.context.scene.render.fps
        jeffCBMOUNTb = stringCBMOUNTB * frCBMOUNTB
        onemorecamountb = (mytool.my_floatCOMPARISONBMOUNTLB * frCBMOUNTB) + jeffCBMOUNTb
        bobCBMOUNTb = onemorecamountb       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBMOUNTb = int(bobCBMOUNTb)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBMOUNTb
                kps.handle_left[0] = jeffCBMOUNTb - 6
                kps.handle_right[0] = jeffCBMOUNTb
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBMOUNTb
                kpz.handle_left[0] = bobCBMOUNTb - 6
                kpz.handle_right[0] = bobCBMOUNTb + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBMOUNTb + frCBMOUNTB

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONBMOUNTC(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbmountc"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_79"]'
        index = 0
        stringCBMOUNTC = mytool.my_floatCOMPARISONBMOUNTC
        frCBMOUNTC = bpy.context.scene.render.fps
        jeffCBMOUNTc = stringCBMOUNTC * frCBMOUNTC
        onemorecamountc = (mytool.my_floatCOMPARISONBMOUNTLC * frCBMOUNTC) + jeffCBMOUNTc
        bobCBMOUNTc = onemorecamountc       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBMOUNTc = int(bobCBMOUNTc)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBMOUNTc
                kps.handle_left[0] = jeffCBMOUNTc - 6
                kps.handle_right[0] = jeffCBMOUNTc
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBMOUNTc
                kpz.handle_left[0] = bobCBMOUNTc - 6
                kpz.handle_right[0] = bobCBMOUNTc + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBMOUNTc + frCBMOUNTC

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBMOUNTD(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbmountd"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_80"]'
        index = 0
        stringCBMOUNTD = mytool.my_floatCOMPARISONBMOUNTD
        frCBMOUNTD = bpy.context.scene.render.fps
        jeffCBMOUNTd = stringCBMOUNTD * frCBMOUNTD
        onemorecamountd = (mytool.my_floatCOMPARISONBMOUNTLD * frCBMOUNTD) + jeffCBMOUNTd
        bobCBMOUNTd = onemorecamountd       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBMOUNTd = int(bobCBMOUNTd)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBMOUNTd
                kps.handle_left[0] = jeffCBMOUNTd - 6
                kps.handle_right[0] = jeffCBMOUNTd
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBMOUNTd
                kpz.handle_left[0] = bobCBMOUNTd - 6
                kpz.handle_right[0] = bobCBMOUNTd + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBMOUNTd + frCBMOUNTD

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBMOUNTE(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbmounte"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_81"]'
        index = 0
        stringCBMOUNTE = mytool.my_floatCOMPARISONBMOUNTE
        frCBMOUNTE = bpy.context.scene.render.fps
        jeffCBMOUNTe = stringCBMOUNTE * frCBMOUNTE
        onemorecbmounte = (mytool.my_floatCOMPARISONBMOUNTLE * frCBMOUNTE) + jeffCBMOUNTe
        bobCBMOUNTe = onemorecbmounte       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBMOUNTe = int(bobCBMOUNTe)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBMOUNTe
                kps.handle_left[0] = jeffCBMOUNTe - 6
                kps.handle_right[0] = jeffCBMOUNTe
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBMOUNTe
                kpz.handle_left[0] = bobCBMOUNTe - 6
                kpz.handle_right[0] = bobCBMOUNTe + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBMOUNTe + frCBMOUNTE

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBMOUNTF(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbmountf"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_82"]'
        index = 0
        stringCBMOUNTF = mytool.my_floatCOMPARISONBMOUNTF
        frCBMOUNTF = bpy.context.scene.render.fps
        jeffCBMOUNTF = stringCBMOUNTF * frCBMOUNTF
        onemorecbmountf = (mytool.my_floatCOMPARISONBMOUNTLF * frCBMOUNTF) + jeffCBMOUNTF
        bobCBMOUNTF = onemorecbmountf       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBMOUNTF = int(bobCBMOUNTF)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBMOUNTF
                kps.handle_left[0] = jeffCBMOUNTF - 6
                kps.handle_right[0] = jeffCBMOUNTF
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBMOUNTF
                kpz.handle_left[0] = bobCBMOUNTF - 6
                kpz.handle_right[0] = bobCBMOUNTF + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBMOUNTF + frCBMOUNTF

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBMOUNTG(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbmountg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_83"]'
        index = 0
        stringCBMOUNTG = mytool.my_floatCOMPARISONBMOUNTG
        frCBMOUNTG = bpy.context.scene.render.fps
        jeffCBMOUNTg = stringCBMOUNTG * frCBMOUNTG
        onemorecbmountg = (mytool.my_floatCOMPARISONBMOUNTLG * frCBMOUNTG) + jeffCBMOUNTg
        bobCBMOUNTg = onemorecbmountg       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBMOUNTg = int(bobCBMOUNTg)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBMOUNTg
                kps.handle_left[0] = jeffCBMOUNTg - 6
                kps.handle_right[0] = jeffCBMOUNTg
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBMOUNTg
                kpz.handle_left[0] = bobCBMOUNTg - 6
                kpz.handle_right[0] = bobCBMOUNTg + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBMOUNTg + frCBMOUNTG

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBMOUNTH(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbmounth"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Cube.004Action'
        data_path = 'modifiers["GeometryNodes"]["Input_84"]'
        index = 0
        stringCBMOUNTH = mytool.my_floatCOMPARISONBMOUNTH
        frCBMOUNTH = bpy.context.scene.render.fps
        jeffCBMOUNTh = stringCBMOUNTH * frCBMOUNTH
        onemorecbmounth = (mytool.my_floatCOMPARISONBMOUNTLH * frCBMOUNTH) + jeffCBMOUNTh
        bobCBMOUNTh = onemorecbmounth       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBMOUNTh = int(bobCBMOUNTh)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBMOUNTh
                kps.handle_left[0] = jeffCBMOUNTh - 6
                kps.handle_right[0] = jeffCBMOUNTh
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBMOUNTh
                kpz.handle_left[0] = bobCBMOUNTh - 6
                kpz.handle_right[0] = bobCBMOUNTh + 6
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBMOUNTh + frCBMOUNTH

        return {'FINISHED'}


class ADDONNAME_OT_my_opMCGAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormcgal"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.002Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_50"]'
        index = 0
        stringMCGAC = mytool.my_floatMCGA
        frMCGAC = bpy.context.scene.render.fps
        jeffmcga = stringMCGAC*frMCGAC
        onemoremcga =  (mytool.my_floatMCGLA*frMCGAC) + jeffmcga
        bobmcga = onemoremcga     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmcga = int(bobmcga)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmcga
                kps.handle_left[0] = jeffmcga-6
                kps.handle_right[0] = jeffmcga
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmcga
                kpz.handle_left[0] = bobmcga-6
                kpz.handle_right[0] = bobmcga+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmcga+(frMCGAC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opMCGBL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormcgbl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.002Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_51"]'
        index = 0
        stringMCGBC = mytool.my_floatMCGB
        frMCGBC = bpy.context.scene.render.fps
        jeffmcgb = stringMCGBC*frMCGBC
        onemoremcgb =  (mytool.my_floatMCGLB*frMCGBC) + jeffmcgb
        bobmcgb = onemoremcgb     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmcgb = int(bobmcgb)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmcgb
                kps.handle_left[0] = jeffmcgb-6
                kps.handle_right[0] = jeffmcgb
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmcgb
                kpz.handle_left[0] = bobmcgb-6
                kpz.handle_right[0] = bobmcgb+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmcgb+(frMCGBC*2)


             
        return {'FINISHED'}

class ADDONNAME_OT_my_opMCGCL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormcgcl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.002Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_52"]'
        index = 0
        stringMCGCC = mytool.my_floatMCGC
        frMCGCC = bpy.context.scene.render.fps
        jeffmcgc = stringMCGCC*frMCGCC
        onemoremcgc =  (mytool.my_floatMCGLC*frMCGCC) + jeffmcgc
        bobmcgc = onemoremcgc     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmcgc = int(bobmcgc)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmcgc
                kps.handle_left[0] = jeffmcgc-6
                kps.handle_right[0] = jeffmcgc
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmcgc
                kpz.handle_left[0] = bobmcgc-6
                kpz.handle_right[0] = bobmcgc+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmcgc+(frMCGCC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opMCGDL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormcgdl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.002Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_53"]'
        index = 0
        stringMCGDC = mytool.my_floatMCGD
        frMCGDC = bpy.context.scene.render.fps
        jeffmcgd = stringMCGDC*frMCGDC
        onemoremcgd =  (mytool.my_floatMCGLD*frMCGDC) + jeffmcgd
        bobmcgd = onemoremcgd     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmcgd = int(bobmcgd)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmcgd
                kps.handle_left[0] = jeffmcgd-6
                kps.handle_right[0] = jeffmcgd
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmcgd
                kpz.handle_left[0] = bobmcgd-6
                kpz.handle_right[0] = bobmcgd+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmcgd+(frMCGDC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opMCGEL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormcgel"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.002Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_54"]'
        index = 0
        stringMCGEC = mytool.my_floatMCGE
        frMCGEC = bpy.context.scene.render.fps
        jeffmcge = stringMCGEC*frMCGEC
        onemoremcge =  (mytool.my_floatMCGLE*frMCGEC) + jeffmcge
        bobmcge = onemoremcge     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmcge = int(bobmcge)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmcge
                kps.handle_left[0] = jeffmcge-6
                kps.handle_right[0] = jeffmcge
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmcge
                kpz.handle_left[0] = bobmcge-6
                kpz.handle_right[0] = bobmcge+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmcge+(frMCGEC*2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opMPGAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormpgal"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.005Action'
        data_path = 'modifiers["GeometryNodes"]["Input_49"]'
        index = 0
        stringMPGAC = mytool.my_floatMPGA
        frMPGAC = bpy.context.scene.render.fps
        jeffmpga = stringMPGAC * frMPGAC
        onemorempga = (mytool.my_floatMPGLA * frMPGAC) + jeffmpga
        bobmpga = onemorempga     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmpga = int(bobmpga)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmpga
                kps.handle_left[0] = jeffmpga - 6
                kps.handle_right[0] = jeffmpga
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmpga
                kpz.handle_left[0] = bobmpga - 6
                kpz.handle_right[0] = bobmpga + 6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmpga + (frMPGAC * 2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opMPGBL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormpgbl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.005Action'
        data_path = 'modifiers["GeometryNodes"]["Input_50"]'
        index = 0
        stringMPGBC = mytool.my_floatMPGB
        frMPGBC = bpy.context.scene.render.fps
        jeffmpgb = stringMPGBC * frMPGBC
        onemorempgb = (mytool.my_floatMPGLB * frMPGBC) + jeffmpgb
        bobmpgb = onemorempgb     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmpgb = int(bobmpgb)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmpgb
                kps.handle_left[0] = jeffmpgb - 6
                kps.handle_right[0] = jeffmpgb
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmpgb
                kpz.handle_left[0] = bobmpgb - 6
                kpz.handle_right[0] = bobmpgb + 6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmpgb + (frMPGBC * 2)


             
        return {'FINISHED'}

class ADDONNAME_OT_my_opMPGCL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormpgcl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.005Action'
        data_path = 'modifiers["GeometryNodes"]["Input_51"]'
        index = 0
        stringMPGCC = mytool.my_floatMPGC
        frMPGCC = bpy.context.scene.render.fps
        jeffmpgc = stringMPGCC * frMPGCC
        onemorempgc = (mytool.my_floatMPGLC * frMPGCC) + jeffmpgc
        bobmpgc = onemorempgc     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmpgc = int(bobmpgc)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmpgc
                kps.handle_left[0] = jeffmpgc - 6
                kps.handle_right[0] = jeffmpgc
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmpgc
                kpz.handle_left[0] = bobmpgc - 6
                kpz.handle_right[0] = bobmpgc + 6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmpgc + (frMPGCC * 2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opMPGDL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormpgdl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.005Action'
        data_path = 'modifiers["GeometryNodes"]["Input_52"]'
        index = 0
        stringMPGDC = mytool.my_floatMPGD
        frMPGDC = bpy.context.scene.render.fps
        jeffmpgd = stringMPGDC * frMPGDC
        onemorempgd = (mytool.my_floatMPGLD * frMPGDC) + jeffmpgd
        bobmpgd = onemorempgd     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmpgd = int(bobmpgd)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmpgd
                kps.handle_left[0] = jeffmpgd - 6
                kps.handle_right[0] = jeffmpgd
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmpgd
                kpz.handle_left[0] = bobmpgd - 6
                kpz.handle_right[0] = bobmpgd + 6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmpgd + (frMPGDC * 2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opMPGEL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormpgel"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Circle Graph.005Action'
        data_path = 'modifiers["GeometryNodes"]["Input_53"]'
        index = 0
        stringMPGEC = mytool.my_floatMPGE
        frMPGEC = bpy.context.scene.render.fps
        jeffmpge = stringMPGEC * frMPGEC
        onemorempge = (mytool.my_floatMPGLE * frMPGEC) + jeffmpge
        bobmpge = onemorempge     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmpge = int(bobmpge)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmpge
                kps.handle_left[0] = jeffmpge - 6
                kps.handle_right[0] = jeffmpge
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmpge
                kpz.handle_left[0] = bobmpge - 6
                kpz.handle_right[0] = bobmpge + 6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmpge + (frMPGEC * 2)


             
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
        stringpie = mytool.my_float2pie
        frpie = bpy.context.scene.render.fps
        jeffpie = stringpie*frpie
        onemorepie =  (mytool.my_floatpie*frpie) + jeffpie
        bobpie = onemorepie

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobpie = int(bobpie)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffpie
                kps.handle_left[0] = jeffpie-30
                kps.handle_right[0] = jeffpie
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobpie
                kpz.handle_left[0] = bobpie-60
                kpz.handle_right[0] = bobpie+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobpie+frpie


             
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
            data_paths = ['modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_49"]', 'modifiers["GeometryNodes"]["Input_50"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
            data_paths = ['modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_49"]', 'modifiers["GeometryNodes"]["Input_50"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
            data_paths = ['modifiers["GeometryNodes"]["Input_25"]', 'modifiers["GeometryNodes"]["Input_44"]', 'modifiers["GeometryNodes"]["Input_45"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
            data_paths = ['modifiers["GeometryNodes"]["Input_25"]', 'modifiers["GeometryNodes"]["Input_44"]', 'modifiers["GeometryNodes"]["Input_45"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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

        if mytool.my_enumLGpie in ('OPLG7pie', 'OPLG8pie'):
            fps = 24 if mytool.my_enumLGpie == 'OPLG7pie' else 30
            frame_end = 96 if mytool.my_enumLGpie == 'OPLG7pie' else 120
            bpy.context.scene.render.fps = fps
            bpy.context.scene.frame_end = frame_end

            for i in range(26, 34):
                action_name = 'CubeAction.001'
                data_path = f'modifiers["GeometryNodes"]["Input_{i}"]'
                index = 0  # Z axis

                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
                    if fcurve:
                        fcurve.keyframe_points[0].co.x = 24 if fps == 24 else 30
                        fcurve.keyframe_points[0].handle_left[0] = 16
                        fcurve.keyframe_points[0].handle_left[1] = 0
                        fcurve.keyframe_points[0].handle_right[0] = 32 if fps == 24 else 40
                        fcurve.keyframe_points[0].handle_right[1] = 0
                        fcurve.keyframe_points[1].co.x = 48 if fps == 24 else 60
                        fcurve.keyframe_points[1].handle_left[0] = 40 if fps == 24 else 50
                        fcurve.keyframe_points[1].handle_left[1] = 1
                        fcurve.keyframe_points[1].handle_right[0] = 56 if fps == 24 else 70
                        fcurve.keyframe_points[1].handle_right[1] = 1
                        print("changed")
                    else:
                        print("no fcurve")
                else:
                    print("no action")
                
            print("end")
        else:
            print("Invalid enum value")
        
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
            data_paths = ['modifiers["GeometryNodes"]["Input_26"]', 'modifiers["GeometryNodes"]["Input_27"]', 'modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]', 'modifiers["GeometryNodes"]["Input_32"]', 'modifiers["GeometryNodes"]["Input_33"]', 'modifiers["GeometryNodes"]["Input_46"]', 'modifiers["GeometryNodes"]["Input_47"]', 'modifiers["GeometryNodes"]["Input_48"]', 'modifiers["GeometryNodes"]["Input_49"]', 'modifiers["GeometryNodes"]["Input_50"]', 'modifiers["GeometryNodes"]["Input_51"]', 'modifiers["GeometryNodes"]["Input_52"]', 'modifiers["GeometryNodes"]["Input_53"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
            data_paths = ['modifiers["GeometryNodes"]["Input_26"]', 'modifiers["GeometryNodes"]["Input_27"]', 'modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]', 'modifiers["GeometryNodes"]["Input_32"]', 'modifiers["GeometryNodes"]["Input_33"]', 'modifiers["GeometryNodes"]["Input_46"]', 'modifiers["GeometryNodes"]["Input_47"]', 'modifiers["GeometryNodes"]["Input_48"]', 'modifiers["GeometryNodes"]["Input_49"]', 'modifiers["GeometryNodes"]["Input_50"]', 'modifiers["GeometryNodes"]["Input_51"]', 'modifiers["GeometryNodes"]["Input_52"]', 'modifiers["GeometryNodes"]["Input_53"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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

            action_name = 'Plane.004Action.002'
            data_paths = ['modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
            
            action_name = 'Plane.004Action.002'
            data_paths = ['modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
    
class ADDONNAME_OT_my_opHBGAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorhbgal"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.002'
        data_path = 'modifiers["GeometryNodes"]["Input_28"]'
        index = 0
        stringHBGA = mytool.my_floatHBGA
        frHBGA = bpy.context.scene.render.fps
        jeffHBGal = stringHBGA*frHBGA
        onemorehbgal =  (mytool.my_floatHBGLA*frHBGA) + jeffHBGal
        bobHBGal = onemorehbgal       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobHBGal = int(bobHBGal)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffHBGal
                kps.handle_left[0] = jeffHBGal-30
                kps.handle_right[0] = jeffHBGal
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobHBGal
                kpz.handle_left[0] = bobHBGal-30
                kpz.handle_right[0] = bobHBGal+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobHBGal+frHBGA


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opHBGBL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorhbgbl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.002'
        data_path = 'modifiers["GeometryNodes"]["Input_29"]'
        index = 0
        stringHBGB = mytool.my_floatHBGB
        frHBGB = bpy.context.scene.render.fps
        jeffHBGbl = stringHBGB*frHBGB
        onemorehbgbl =  (mytool.my_floatHBGLB*frHBGB) + jeffHBGbl
        bobHBGbl = onemorehbgbl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobHBGbl = int(bobHBGbl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffHBGbl
                kps.handle_left[0] = jeffHBGbl-30
                kps.handle_right[0] = jeffHBGbl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobHBGbl
                kpz.handle_left[0] = bobHBGbl-30
                kpz.handle_right[0] = bobHBGbl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobHBGbl+frHBGB


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opHBGCL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorhbgcl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.002'
        data_path = 'modifiers["GeometryNodes"]["Input_30"]'
        index = 0
        stringHBGC = mytool.my_floatHBGC
        frHBGC = bpy.context.scene.render.fps
        jeffHBGcl = stringHBGC*frHBGC
        onemorehbgcl =  (mytool.my_floatHBGLC*frHBGC) + jeffHBGcl
        bobHBGcl = onemorehbgcl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobHBGcl = int(bobHBGcl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffHBGcl
                kps.handle_left[0] = jeffHBGcl-30
                kps.handle_right[0] = jeffHBGcl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobHBGcl
                kpz.handle_left[0] = bobHBGcl-30
                kpz.handle_right[0] = bobHBGcl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobHBGcl+frHBGC


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opHBGDL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorhbgdl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.002'
        data_path = 'modifiers["GeometryNodes"]["Input_31"]'
        index = 0
        stringHBGD = mytool.my_floatHBGD
        frHBGD = bpy.context.scene.render.fps
        jeffHBGdl = stringHBGD*frHBGD
        onemorehbgdl =  (mytool.my_floatHBGLD*frHBGD) + jeffHBGdl
        bobHBGdl = onemorehbgdl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobHBGdl = int(bobHBGdl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffHBGdl
                kps.handle_left[0] = jeffHBGdl-30
                kps.handle_right[0] = jeffHBGdl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobHBGdl
                kpz.handle_left[0] = bobHBGdl-30
                kpz.handle_right[0] = bobHBGdl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobHBGdl+frHBGD


             
        return {'FINISHED'}
    

class ADDONNAME_OT_my_opCOMPARISONAHBARAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonahbara"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_28"]'
        index = 0
        stringCAHBARA = mytool.my_floatCOMPARISONAHBARA
        frCAHBARA = bpy.context.scene.render.fps
        jeffCAHBARal = stringCAHBARA * frCAHBARA
        onemorecahbaral = (mytool.my_floatCOMPARISONAHBARLA * frCAHBARA) + jeffCAHBARal
        bobCAHBARal = onemorecahbaral       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAHBARal = int(bobCAHBARal)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAHBARal
                kps.handle_left[0] = jeffCAHBARal - 30
                kps.handle_right[0] = jeffCAHBARal
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAHBARal
                kpz.handle_left[0] = bobCAHBARal - 30
                kpz.handle_right[0] = bobCAHBARal + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAHBARal + frCAHBARA

        return {'FINISHED'}
    



class ADDONNAME_OT_my_opCOMPARISONAHBARBL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonahbarb"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_29"]'
        index = 0
        stringCAHBARB = mytool.my_floatCOMPARISONAHBARB
        frCAHBARB = bpy.context.scene.render.fps
        jeffCAHBARBl = stringCAHBARB * frCAHBARB
        onemorecahbarbl = (mytool.my_floatCOMPARISONAHBARLB * frCAHBARB) + jeffCAHBARBl
        bobCAHBARBl = onemorecahbarbl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAHBARBl = int(bobCAHBARBl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAHBARBl
                kps.handle_left[0] = jeffCAHBARBl - 30
                kps.handle_right[0] = jeffCAHBARBl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAHBARBl
                kpz.handle_left[0] = bobCAHBARBl - 30
                kpz.handle_right[0] = bobCAHBARBl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAHBARBl + frCAHBARB

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONAHBARCL(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonahbarc"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_30"]'
        index = 0
        stringCAHBARC = mytool.my_floatCOMPARISONAHBARC
        frCAHBARC = bpy.context.scene.render.fps
        jeffCAHBARCl = stringCAHBARC * frCAHBARC
        onemorecahbarcl = (mytool.my_floatCOMPARISONAHBARLC * frCAHBARC) + jeffCAHBARCl
        bobCAHBARCl = onemorecahbarcl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAHBARCl = int(bobCAHBARCl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAHBARCl
                kps.handle_left[0] = jeffCAHBARCl - 30
                kps.handle_right[0] = jeffCAHBARCl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAHBARCl
                kpz.handle_left[0] = bobCAHBARCl - 30
                kpz.handle_right[0] = bobCAHBARCl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAHBARCl + frCAHBARC

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONAHBARD(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonahbard"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_31"]'
        index = 0
        stringCAHBARD = mytool.my_floatCOMPARISONAHBARD
        frCAHBARD = bpy.context.scene.render.fps
        jeffCAHBARDl = stringCAHBARD * frCAHBARD
        onemorecahbardl = (mytool.my_floatCOMPARISONAHBARLD * frCAHBARD) + jeffCAHBARDl
        bobCAHBARDl = onemorecahbardl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAHBARDl = int(bobCAHBARDl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAHBARDl
                kps.handle_left[0] = jeffCAHBARDl - 30
                kps.handle_right[0] = jeffCAHBARDl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAHBARDl
                kpz.handle_left[0] = bobCAHBARDl - 30
                kpz.handle_right[0] = bobCAHBARDl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAHBARDl + frCAHBARD

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBHBARAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonbhbara"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_55"]'
        index = 0
        stringCBHBARA = mytool.my_floatCOMPARISONBHBARA
        frCBHBARA = bpy.context.scene.render.fps
        jeffBHBARal = stringCBHBARA * frCBHBARA
        onemorebhbaral = (mytool.my_floatCOMPARISONBHBARLA * frCBHBARA) + jeffBHBARal
        bobBHBARal = onemorebhbaral       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobBHBARal = int(bobBHBARal)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffBHBARal
                kps.handle_left[0] = jeffBHBARal - 30
                kps.handle_right[0] = jeffBHBARal
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobBHBARal
                kpz.handle_left[0] = bobBHBARal - 30
                kpz.handle_right[0] = bobBHBARal + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobBHBARal + frCBHBARA

        return {'FINISHED'}



class ADDONNAME_OT_my_opCOMPARISONBHBARBL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonbhbarb"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_56"]'
        index = 0
        stringCBHBARB = mytool.my_floatCOMPARISONBHBARB
        frCBHBARB = bpy.context.scene.render.fps
        jeffBHBARBl = stringCBHBARB * frCBHBARB
        onemorebhbarbl = (mytool.my_floatCOMPARISONBHBARLB * frCBHBARB) + jeffBHBARBl
        bobBHBARBl = onemorebhbarbl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobBHBARBl = int(bobBHBARBl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffBHBARBl
                kps.handle_left[0] = jeffBHBARBl - 30
                kps.handle_right[0] = jeffBHBARBl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobBHBARBl
                kpz.handle_left[0] = bobBHBARBl - 30
                kpz.handle_right[0] = bobBHBARBl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobBHBARBl + frCBHBARB

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBHBARCL(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbhbarc"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_57"]'
        index = 0
        stringCBHBARC = mytool.my_floatCOMPARISONBHBARC
        frCBHBARC = bpy.context.scene.render.fps
        jeffBHBARCl = stringCBHBARC * frCBHBARC
        onemorebhbarcl = (mytool.my_floatCOMPARISONBHBARLC * frCBHBARC) + jeffBHBARCl
        bobBHBARCl = onemorebhbarcl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobBHBARCl = int(bobBHBARCl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffBHBARCl
                kps.handle_left[0] = jeffBHBARCl - 30
                kps.handle_right[0] = jeffBHBARCl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobBHBARCl
                kpz.handle_left[0] = bobBHBARCl - 30
                kpz.handle_right[0] = bobBHBARCl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobBHBARCl + frCBHBARC

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBHBARD(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonbhbard"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.001'
        data_path = 'modifiers["GeometryNodes"]["Input_58"]'
        index = 0
        stringCBHBARD = mytool.my_floatCOMPARISONBHBARD
        frCBHBARD = bpy.context.scene.render.fps
        jeffCBHBARDl = stringCBHBARD * frCBHBARD
        onemorebhbardl = (mytool.my_floatCOMPARISONBHBARDL * frCBHBARD) + jeffCBHBARDl
        bobCBHBARDl = onemorebhbardl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBHBARDl = int(bobCBHBARDl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBHBARDl
                kps.handle_left[0] = jeffCBHBARDl - 30
                kps.handle_right[0] = jeffCBHBARDl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBHBARDl
                kpz.handle_left[0] = bobCBHBARDl - 30
                kpz.handle_right[0] = bobCBHBARDl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBHBARDl + frCBHBARD

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
            data_paths = ['modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]', 'modifiers["GeometryNodes"]["Input_55"]', 'modifiers["GeometryNodes"]["Input_56"]', 'modifiers["GeometryNodes"]["Input_57"]', 'modifiers["GeometryNodes"]["Input_58"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
            data_paths = ['modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]', 'modifiers["GeometryNodes"]["Input_55"]', 'modifiers["GeometryNodes"]["Input_56"]', 'modifiers["GeometryNodes"]["Input_57"]', 'modifiers["GeometryNodes"]["Input_58"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
            data_paths = ['modifiers["GeometryNodes"]["Input_46"]', 'modifiers["GeometryNodes"]["Input_47"]', 'modifiers["GeometryNodes"]["Input_48"]', 'modifiers["GeometryNodes"]["Input_49"]', 'modifiers["GeometryNodes"]["Input_50"]', 'modifiers["GeometryNodes"]["Input_51"]', 'modifiers["GeometryNodes"]["Input_52"]', 'modifiers["GeometryNodes"]["Input_53"]', 'modifiers["GeometryNodes"]["Input_77"]', 'modifiers["GeometryNodes"]["Input_78"]', 'modifiers["GeometryNodes"]["Input_79"]', 'modifiers["GeometryNodes"]["Input_80"]', 'modifiers["GeometryNodes"]["Input_81"]', 'modifiers["GeometryNodes"]["Input_82"]', 'modifiers["GeometryNodes"]["Input_83"]', 'modifiers["GeometryNodes"]["Input_84"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
            data_paths = ['modifiers["GeometryNodes"]["Input_46"]', 'modifiers["GeometryNodes"]["Input_47"]', 'modifiers["GeometryNodes"]["Input_48"]', 'modifiers["GeometryNodes"]["Input_49"]', 'modifiers["GeometryNodes"]["Input_50"]', 'modifiers["GeometryNodes"]["Input_51"]', 'modifiers["GeometryNodes"]["Input_52"]', 'modifiers["GeometryNodes"]["Input_53"]', 'modifiers["GeometryNodes"]["Input_77"]', 'modifiers["GeometryNodes"]["Input_78"]', 'modifiers["GeometryNodes"]["Input_79"]', 'modifiers["GeometryNodes"]["Input_80"]', 'modifiers["GeometryNodes"]["Input_81"]', 'modifiers["GeometryNodes"]["Input_82"]', 'modifiers["GeometryNodes"]["Input_83"]', 'modifiers["GeometryNodes"]["Input_84"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
    
class ADDONNAME_OT_my_opVBGAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorvbgal"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.003'
        data_path = 'modifiers["GeometryNodes"]["Input_28"]'
        index = 0
        stringVBGA = mytool.my_floatVBGA
        frVBGA = bpy.context.scene.render.fps
        jeffVBGal = stringVBGA*frVBGA
        onemoreVBGal =  (mytool.my_floatVBGLA*frVBGA) + jeffVBGal
        bobVBGal = onemoreVBGal       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobVBGal = int(bobVBGal)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffVBGal
                kps.handle_left[0] = jeffVBGal-30
                kps.handle_right[0] = jeffVBGal
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobVBGal
                kpz.handle_left[0] = bobVBGal-30
                kpz.handle_right[0] = bobVBGal+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobVBGal+frVBGA


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opVBGBL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorvbgbl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.003'
        data_path = 'modifiers["GeometryNodes"]["Input_29"]'
        index = 0
        stringVBGB = mytool.my_floatVBGB
        frVBGB = bpy.context.scene.render.fps
        jeffVBGbl = stringVBGB*frVBGB
        onemoreVBGbl =  (mytool.my_floatVBGLB*frVBGB) + jeffVBGbl
        bobVBGbl = onemoreVBGbl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobVBGbl = int(bobVBGbl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffVBGbl
                kps.handle_left[0] = jeffVBGbl-30
                kps.handle_right[0] = jeffVBGbl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobVBGbl
                kpz.handle_left[0] = bobVBGbl-30
                kpz.handle_right[0] = bobVBGbl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobVBGbl+frVBGB


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opVBGCL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorvbgcl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.003'
        data_path = 'modifiers["GeometryNodes"]["Input_30"]'
        index = 0
        stringVBGC = mytool.my_floatVBGC
        frVBGC = bpy.context.scene.render.fps
        jeffVBGcl = stringVBGC*frVBGC
        onemoreVBGcl =  (mytool.my_floatVBGLC*frVBGC) + jeffVBGcl
        bobVBGcl = onemoreVBGcl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobVBGcl = int(bobVBGcl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffVBGcl
                kps.handle_left[0] = jeffVBGcl-30
                kps.handle_right[0] = jeffVBGcl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobVBGcl
                kpz.handle_left[0] = bobVBGcl-30
                kpz.handle_right[0] = bobVBGcl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobVBGcl+frVBGC


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opVBGDL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorvbgdl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.003'
        data_path = 'modifiers["GeometryNodes"]["Input_31"]'
        index = 0
        stringVBGD = mytool.my_floatVBGD
        frVBGD = bpy.context.scene.render.fps
        jeffVBGdl = stringVBGD*frVBGD
        onemoreVBGdl =  (mytool.my_floatVBGLD*frVBGD) + jeffVBGdl
        bobVBGdl = onemoreVBGdl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobVBGdl = int(bobVBGdl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffVBGdl
                kps.handle_left[0] = jeffVBGdl-30
                kps.handle_right[0] = jeffVBGdl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobVBGdl
                kpz.handle_left[0] = bobVBGdl-30
                kpz.handle_right[0] = bobVBGdl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobVBGdl+frVBGD


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opVBGEL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorvbgel"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.003'
        data_path = 'modifiers["GeometryNodes"]["Input_53"]'
        index = 0
        stringVBGE = mytool.my_floatVBGE
        frVBGE = bpy.context.scene.render.fps
        jeffVBGel = stringVBGE*frVBGE
        onemoreVBGel =  (mytool.my_floatVBGLE*frVBGE) + jeffVBGel
        bobVBGel = onemoreVBGel       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobVBGel = int(bobVBGel)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffVBGel
                kps.handle_left[0] = jeffVBGel-30
                kps.handle_right[0] = jeffVBGel
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobVBGel
                kpz.handle_left[0] = bobVBGel-30
                kpz.handle_right[0] = bobVBGel+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobVBGel+frVBGE


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opVBGFL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorvbgfl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.003'
        data_path = 'modifiers["GeometryNodes"]["Input_54"]'
        index = 0
        stringVBGF = mytool.my_floatVBGF
        frVBGF = bpy.context.scene.render.fps
        jeffVBGfl = stringVBGF*frVBGF
        onemoreVBGfl =  (mytool.my_floatVBGLF*frVBGF) + jeffVBGfl
        bobVBGfl = onemoreVBGfl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobVBGfl = int(bobVBGfl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffVBGfl
                kps.handle_left[0] = jeffVBGfl-30
                kps.handle_right[0] = jeffVBGfl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobVBGfl
                kpz.handle_left[0] = bobVBGfl-30
                kpz.handle_right[0] = bobVBGfl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobVBGfl+frVBGF


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opVBGGL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorvbggl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.003'
        data_path = 'modifiers["GeometryNodes"]["Input_55"]'
        index = 0
        stringVBGG = mytool.my_floatVBGG
        frVBGG = bpy.context.scene.render.fps
        jeffVBGgl = stringVBGG*frVBGG
        onemoreVBGgl =  (mytool.my_floatVBGLG*frVBGG) + jeffVBGgl
        bobVBGgl = onemoreVBGgl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobVBGgl = int(bobVBGgl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffVBGgl
                kps.handle_left[0] = jeffVBGgl-30
                kps.handle_right[0] = jeffVBGgl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobVBGgl
                kpz.handle_left[0] = bobVBGgl-30
                kpz.handle_right[0] = bobVBGgl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobVBGgl+frVBGG


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opVBGHL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorvbghl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.003'
        data_path = 'modifiers["GeometryNodes"]["Input_56"]'
        index = 0
        stringVBGH = mytool.my_floatVBGH
        frVBGH = bpy.context.scene.render.fps
        jeffVBGhl = stringVBGH*frVBGH
        onemoreVBGhl =  (mytool.my_floatVBGLH*frVBGH) + jeffVBGhl
        bobVBGhl = onemoreVBGhl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobVBGhl = int(bobVBGhl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffVBGhl
                kps.handle_left[0] = jeffVBGhl-30
                kps.handle_right[0] = jeffVBGhl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobVBGhl
                kpz.handle_left[0] = bobVBGhl-30
                kpz.handle_right[0] = bobVBGhl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobVBGhl+frVBGH


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONABARVA(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonabarva"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_28"]'
        index = 0
        stringCOMPARISONABARVA = mytool.my_floatCOMPARISONABARVA
        frCOMPARISONABARVA = bpy.context.scene.render.fps
        jeffCOMPARISONABARV = stringCOMPARISONABARVA * frCOMPARISONABARVA
        onemoreCOMPARISONABARV = (mytool.my_floatCOMPARISONABARVLA * frCOMPARISONABARVA) + jeffCOMPARISONABARV
        bobCOMPARISONABARV = onemoreCOMPARISONABARV       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONABARV = int(bobCOMPARISONABARV)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONABARV
                kps.handle_left[0] = jeffCOMPARISONABARV - 30
                kps.handle_right[0] = jeffCOMPARISONABARV
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONABARV
                kpz.handle_left[0] = bobCOMPARISONABARV - 30
                kpz.handle_right[0] = bobCOMPARISONABARV + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONABARV + frCOMPARISONABARVA

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONABARVB(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonabarvb"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_29"]'
        index = 0
        stringCOMPARISONABARV = mytool.my_floatCOMPARISONABARVB
        frCOMPARISONABARV = bpy.context.scene.render.fps
        jeffCOMPARISONABARVbl = stringCOMPARISONABARV*frCOMPARISONABARV
        onemoreCOMPARISONABARVbl =  (mytool.my_floatCOMPARISONABARVLB*frCOMPARISONABARV) + jeffCOMPARISONABARVbl
        bobCOMPARISONABARVbl = onemoreCOMPARISONABARVbl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONABARVbl = int(bobCOMPARISONABARVbl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONABARVbl
                kps.handle_left[0] = jeffCOMPARISONABARVbl - 30
                kps.handle_right[0] = jeffCOMPARISONABARVbl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONABARVbl
                kpz.handle_left[0] = bobCOMPARISONABARVbl - 30
                kpz.handle_right[0] = bobCOMPARISONABARVbl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONABARVbl + frCOMPARISONABARV

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONABARVC(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonabarvc"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_30"]'
        index = 0
        stringCOMPARISONABARVC = mytool.my_floatCOMPARISONABARVC
        frCOMPARISONABARVC = bpy.context.scene.render.fps
        jeffCOMPARISONABARVcl = stringCOMPARISONABARVC * frCOMPARISONABARVC
        onemoreCOMPARISONABARVcl = (mytool.my_floatCOMPARISONABARVLC * frCOMPARISONABARVC) + jeffCOMPARISONABARVcl
        bobCOMPARISONABARVcl = onemoreCOMPARISONABARVcl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONABARVcl = int(bobCOMPARISONABARVcl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONABARVcl
                kps.handle_left[0] = jeffCOMPARISONABARVcl - 30
                kps.handle_right[0] = jeffCOMPARISONABARVcl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONABARVcl
                kpz.handle_left[0] = bobCOMPARISONABARVcl - 30
                kpz.handle_right[0] = bobCOMPARISONABARVcl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONABARVcl + frCOMPARISONABARVC

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONABARVD(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonabarvd"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_31"]'
        index = 0
        stringCOMPARISONABARVD = mytool.my_floatCOMPARISONABARVD
        frCOMPARISONABARVD = bpy.context.scene.render.fps
        jeffCOMPARISONABARVdl = stringCOMPARISONABARVD * frCOMPARISONABARVD
        onemoreCOMPARISONABARVdl = (mytool.my_floatCOMPARISONABARVLD * frCOMPARISONABARVD) + jeffCOMPARISONABARVdl
        bobCOMPARISONABARVdl = onemoreCOMPARISONABARVdl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONABARVdl = int(bobCOMPARISONABARVdl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONABARVdl
                kps.handle_left[0] = jeffCOMPARISONABARVdl - 30
                kps.handle_right[0] = jeffCOMPARISONABARVdl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONABARVdl
                kpz.handle_left[0] = bobCOMPARISONABARVdl - 30
                kpz.handle_right[0] = bobCOMPARISONABARVdl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONABARVdl + frCOMPARISONABARVD

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONABARVE(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonabarve"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_53"]'
        index = 0
        stringCOMPARISONABARVE = mytool.my_floatCOMPARISONABARVE
        frCOMPARISONABARVE = bpy.context.scene.render.fps
        jeffCOMPARISONABARVel = stringCOMPARISONABARVE*frCOMPARISONABARVE
        onemoreCOMPARISONABARVel =  (mytool.my_floatCOMPARISONABARVLE*frCOMPARISONABARVE) + jeffCOMPARISONABARVel
        bobCOMPARISONABARVel = onemoreCOMPARISONABARVel       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONABARVel = int(bobCOMPARISONABARVel)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONABARVel
                kps.handle_left[0] = jeffCOMPARISONABARVel - 30
                kps.handle_right[0] = jeffCOMPARISONABARVel
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONABARVel
                kpz.handle_left[0] = bobCOMPARISONABARVel - 30
                kpz.handle_right[0] = bobCOMPARISONABARVel + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONABARVel + frCOMPARISONABARVE

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONABARVF(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonabarvf"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_54"]'
        index = 0
        stringCOMPARISONAFARVF = mytool.my_floatCOMPARISONABARVF
        frCOMPARISONAFARVF = bpy.context.scene.render.fps
        jeffCOMPARISONAFARVfl = stringCOMPARISONAFARVF * frCOMPARISONAFARVF
        onemoreCOMPARISONAFARVfl = (mytool.my_floatCOMPARISONABARVLF * frCOMPARISONAFARVF) + jeffCOMPARISONAFARVfl
        bobCOMPARISONAFARVfl = onemoreCOMPARISONAFARVfl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONAFARVfl = int(bobCOMPARISONAFARVfl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONAFARVfl
                kps.handle_left[0] = jeffCOMPARISONAFARVfl - 30
                kps.handle_right[0] = jeffCOMPARISONAFARVfl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONAFARVfl
                kpz.handle_left[0] = bobCOMPARISONAFARVfl - 30
                kpz.handle_right[0] = bobCOMPARISONAFARVfl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONAFARVfl + frCOMPARISONAFARVF

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONABARVG(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonabarvg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_55"]'
        index = 0
        stringCOMPARISONABARVG = mytool.my_floatCOMPARISONABARVG
        frCOMPARISONABARVG = bpy.context.scene.render.fps
        jeffCOMPARISONABARVgl = stringCOMPARISONABARVG * frCOMPARISONABARVG
        onemoreCOMPARISONABARVgl = (mytool.my_floatCOMPARISONABARVLG * frCOMPARISONABARVG) + jeffCOMPARISONABARVgl
        bobCOMPARISONABARVgl = onemoreCOMPARISONABARVgl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONABARVgl = int(bobCOMPARISONABARVgl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONABARVgl
                kps.handle_left[0] = jeffCOMPARISONABARVgl - 30
                kps.handle_right[0] = jeffCOMPARISONABARVgl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONABARVgl
                kpz.handle_left[0] = bobCOMPARISONABARVgl - 30
                kpz.handle_right[0] = bobCOMPARISONABARVgl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONABARVgl + frCOMPARISONABARVG

        return {'FINISHED'}


class ADDONNAME_OT_my_opCOMPARISONABARVH(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonabarvh"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_56"]'
        index = 0
        stringCOMPARISONABARVH = mytool.my_floatCOMPARISONABARVH
        frCOMPARISONABARVH = bpy.context.scene.render.fps
        jeffCOMPARISONABARVhl = stringCOMPARISONABARVH * frCOMPARISONABARVH
        onemoreCOMPARISONABARVhl = (mytool.my_floatCOMPARISONABARVLH * frCOMPARISONABARVH) + jeffCOMPARISONABARVhl
        bobCOMPARISONABARVhl = onemoreCOMPARISONABARVhl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONABARVhl = int(bobCOMPARISONABARVhl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONABARVhl
                kps.handle_left[0] = jeffCOMPARISONABARVhl - 30
                kps.handle_right[0] = jeffCOMPARISONABARVhl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONABARVhl
                kpz.handle_left[0] = bobCOMPARISONABARVhl - 30
                kpz.handle_right[0] = bobCOMPARISONABARVhl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONABARVhl + frCOMPARISONABARVH

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBBARVA(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonbbarva"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_82"]'
        index = 0
        stringCOMPARISONBBARVA = mytool.my_floatCOMPARISONBBARVA
        frCOMPARISONBBARVA = bpy.context.scene.render.fps
        jeffCOMPARISONBBARV = stringCOMPARISONBBARVA * frCOMPARISONBBARVA
        onemoreCOMPARISONBBARV = (mytool.my_floatCOMPARISONBBARVLA * frCOMPARISONBBARVA) + jeffCOMPARISONBBARV
        bobCOMPARISONBBARV = onemoreCOMPARISONBBARV       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONBBARV = int(bobCOMPARISONBBARV)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONBBARV
                kps.handle_left[0] = jeffCOMPARISONBBARV - 30
                kps.handle_right[0] = jeffCOMPARISONBBARV
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONBBARV
                kpz.handle_left[0] = bobCOMPARISONBBARV - 30
                kpz.handle_right[0] = bobCOMPARISONBBARV + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONBBARV + frCOMPARISONBBARVA

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONBBARVB(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbbarvb"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_83"]'
        index = 0
        stringCOMPARISONBBARV = mytool.my_floatCOMPARISONBBARVB
        frCOMPARISONBBARV = bpy.context.scene.render.fps
        jeffCOMPARISONBBARVbl = stringCOMPARISONBBARV * frCOMPARISONBBARV
        onemoreCOMPARISONBBARVbl = (mytool.my_floatCOMPARISONBBARVLB * frCOMPARISONBBARV) + jeffCOMPARISONBBARVbl
        bobCOMPARISONBBARVbl = onemoreCOMPARISONBBARVbl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONBBARVbl = int(bobCOMPARISONBBARVbl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONBBARVbl
                kps.handle_left[0] = jeffCOMPARISONBBARVbl - 30
                kps.handle_right[0] = jeffCOMPARISONBBARVbl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONBBARVbl
                kpz.handle_left[0] = bobCOMPARISONBBARVbl - 30
                kpz.handle_right[0] = bobCOMPARISONBBARVbl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONBBARVbl + frCOMPARISONBBARV

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONBBARVC(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbbarvc"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_84"]'
        index = 0
        stringCOMPARISONBBARVC = mytool.my_floatCOMPARISONBBARVC
        frCOMPARISONBBARVC = bpy.context.scene.render.fps
        jeffCOMPARISONBBARVcl = stringCOMPARISONBBARVC * frCOMPARISONBBARVC
        onemoreCOMPARISONBBARVcl = (mytool.my_floatCOMPARISONBBARVLC * frCOMPARISONBBARVC) + jeffCOMPARISONBBARVcl
        bobCOMPARISONBBARVcl = onemoreCOMPARISONBBARVcl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONBBARVcl = int(bobCOMPARISONBBARVcl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONBBARVcl
                kps.handle_left[0] = jeffCOMPARISONBBARVcl - 30
                kps.handle_right[0] = jeffCOMPARISONBBARVcl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONBBARVcl
                kpz.handle_left[0] = bobCOMPARISONBBARVcl - 30
                kpz.handle_right[0] = bobCOMPARISONBBARVcl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONBBARVcl + frCOMPARISONBBARVC

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBBARVD(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbbarvd"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_85"]'
        index = 0
        stringCOMPARISONBBARVD = mytool.my_floatCOMPARISONBBARVD
        frCOMPARISONBBARVD = bpy.context.scene.render.fps
        jeffCOMPARISONBBARVdl = stringCOMPARISONBBARVD * frCOMPARISONBBARVD
        onemoreCOMPARISONBBARVdl = (mytool.my_floatCOMPARISONBBARVLD * frCOMPARISONBBARVD) + jeffCOMPARISONBBARVdl
        bobCOMPARISONBBARVdl = onemoreCOMPARISONBBARVdl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONBBARVdl = int(bobCOMPARISONBBARVdl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONBBARVdl
                kps.handle_left[0] = jeffCOMPARISONBBARVdl - 30
                kps.handle_right[0] = jeffCOMPARISONBBARVdl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONBBARVdl
                kpz.handle_left[0] = bobCOMPARISONBBARVdl - 30
                kpz.handle_right[0] = bobCOMPARISONBBARVdl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONBBARVdl + frCOMPARISONBBARVD

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBBARVE(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbbarve"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_86"]'
        index = 0
        stringCOMPARISONBBARVE = mytool.my_floatCOMPARISONBBARVE
        frCOMPARISONBBARVE = bpy.context.scene.render.fps
        jeffCOMPARISONBBARVel = stringCOMPARISONBBARVE * frCOMPARISONBBARVE
        onemoreCOMPARISONBBARVel = (mytool.my_floatCOMPARISONBBARVLE * frCOMPARISONBBARVE) + jeffCOMPARISONBBARVel
        bobCOMPARISONBBARVel = onemoreCOMPARISONBBARVel       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONBBARVel = int(bobCOMPARISONBBARVel)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONBBARVel
                kps.handle_left[0] = jeffCOMPARISONBBARVel - 30
                kps.handle_right[0] = jeffCOMPARISONBBARVel
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONBBARVel
                kpz.handle_left[0] = bobCOMPARISONBBARVel - 30
                kpz.handle_right[0] = bobCOMPARISONBBARVel + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONBBARVel + frCOMPARISONBBARVE

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBBARVF(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbbarvf"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_87"]'
        index = 0
        stringCOMPARISONBFARVF = mytool.my_floatCOMPARISONBBARVF
        frCOMPARISONBFARVF = bpy.context.scene.render.fps
        jeffCOMPARISONBFARVfl = stringCOMPARISONBFARVF * frCOMPARISONBFARVF
        onemoreCOMPARISONBFARVfl = (mytool.my_floatCOMPARISONBBARVLF * frCOMPARISONBFARVF) + jeffCOMPARISONBFARVfl
        bobCOMPARISONBFARVfl = onemoreCOMPARISONBFARVfl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONBFARVfl = int(bobCOMPARISONBFARVfl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONBFARVfl
                kps.handle_left[0] = jeffCOMPARISONBFARVfl - 30
                kps.handle_right[0] = jeffCOMPARISONBFARVfl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONBFARVfl
                kpz.handle_left[0] = bobCOMPARISONBFARVfl - 30
                kpz.handle_right[0] = bobCOMPARISONBFARVfl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONBFARVfl + frCOMPARISONBFARVF

        return {'FINISHED'}

    
class ADDONNAME_OT_my_opCOMPARISONBBARVG(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbbarvg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_88"]'
        index = 0
        stringCOMPARISONBBARVG = mytool.my_floatCOMPARISONBBARVG
        frCOMPARISONBBARVG = bpy.context.scene.render.fps
        jeffCOMPARISONBBARVgl = stringCOMPARISONBBARVG * frCOMPARISONBBARVG
        onemoreCOMPARISONBBARVgl = (mytool.my_floatCOMPARISONBBARVLG * frCOMPARISONBBARVG) + jeffCOMPARISONBBARVgl
        bobCOMPARISONBBARVgl = onemoreCOMPARISONBBARVgl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONBBARVgl = int(bobCOMPARISONBBARVgl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONBBARVgl
                kps.handle_left[0] = jeffCOMPARISONBBARVgl - 30
                kps.handle_right[0] = jeffCOMPARISONBBARVgl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONBBARVgl
                kpz.handle_left[0] = bobCOMPARISONBBARVgl - 30
                kpz.handle_right[0] = bobCOMPARISONBBARVgl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONBBARVgl + frCOMPARISONBBARVG

        return {'FINISHED'}


class ADDONNAME_OT_my_opCOMPARISONBBARVH(bpy.types.Operator):
    bl_label = "Add Object"
    bl_idname = "addonname.myop_operatorcomparisonbbarvh"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = 'Plane.004Action.004'
        data_path = 'modifiers["GeometryNodes"]["Input_89"]'
        index = 0
        stringCOMPARISONBBARVH = mytool.my_floatCOMPARISONBBARVH
        frCOMPARISONBBARVH = bpy.context.scene.render.fps
        jeffCOMPARISONBBARVhl = stringCOMPARISONBBARVH * frCOMPARISONBBARVH
        onemoreCOMPARISONBBARVhl = (mytool.my_floatCOMPARISONBBARVLH * frCOMPARISONBBARVH) + jeffCOMPARISONBBARVhl
        bobCOMPARISONBBARVhl = onemoreCOMPARISONBBARVhl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCOMPARISONBBARVhl = int(bobCOMPARISONBBARVhl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCOMPARISONBBARVhl
                kps.handle_left[0] = jeffCOMPARISONBBARVhl - 30
                kps.handle_right[0] = jeffCOMPARISONBBARVhl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCOMPARISONBBARVhl
                kpz.handle_left[0] = bobCOMPARISONBBARVhl - 30
                kpz.handle_right[0] = bobCOMPARISONBBARVhl + 30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCOMPARISONBBARVhl + frCOMPARISONBBARVH

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
            data_paths = ['modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]', 'modifiers["GeometryNodes"]["Input_53"]', 'modifiers["GeometryNodes"]["Input_54"]', 'modifiers["GeometryNodes"]["Input_55"]', 'modifiers["GeometryNodes"]["Input_56"]', 'modifiers["GeometryNodes"]["Input_82"]', 'modifiers["GeometryNodes"]["Input_83"]', 'modifiers["GeometryNodes"]["Input_84"]', 'modifiers["GeometryNodes"]["Input_85"]', 'modifiers["GeometryNodes"]["Input_86"]', 'modifiers["GeometryNodes"]["Input_87"]', 'modifiers["GeometryNodes"]["Input_88"]', 'modifiers["GeometryNodes"]["Input_89"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
            data_paths = ['modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]', 'modifiers["GeometryNodes"]["Input_53"]', 'modifiers["GeometryNodes"]["Input_54"]', 'modifiers["GeometryNodes"]["Input_55"]', 'modifiers["GeometryNodes"]["Input_56"]', 'modifiers["GeometryNodes"]["Input_82"]', 'modifiers["GeometryNodes"]["Input_83"]', 'modifiers["GeometryNodes"]["Input_84"]', 'modifiers["GeometryNodes"]["Input_85"]', 'modifiers["GeometryNodes"]["Input_86"]', 'modifiers["GeometryNodes"]["Input_87"]', 'modifiers["GeometryNodes"]["Input_88"]', 'modifiers["GeometryNodes"]["Input_89"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
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
            bpy.context.scene.render.ffmpeg.audio_codec = 'AAC'
            bpy.context.scene.render.ffmpeg.codec = 'H264'
            bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'
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

classes = [MyProperties, MyoperatorCGcsv, MyoperatorCGCcsv, MyoperatorPGCcsv, MyoperatorPGcsv, MyoperatorLGcsv, MyoperatorLGCcsv, 
MyoperatorHBcsv, MyoperatorHBCcsv, MyoperatorMCcsv, MyoperatorMPcsv, MyoperatorMGcsv, MyoperatorMGCcsv, MyoperatorVBcsv, 
MyoperatorVBCcsv, RenderRender2, ADDONNAME_OT_my_opc, ADDONNAME_OT_my_op23cAL, ADDONNAME_OT_my_op23cBL, ADDONNAME_OT_my_op23cCL, 
ADDONNAME_OT_my_op23pAL, ADDONNAME_OT_my_op23pBL, ADDONNAME_OT_my_op23pCL, ADDONNAME_OT_my_opHBGAL, ADDONNAME_OT_my_opHBGBL, 
ADDONNAME_OT_my_opHBGCL, ADDONNAME_OT_my_opHBGDL, ADDONNAME_OT_my_opVBGAL, ADDONNAME_OT_my_opVBGBL, ADDONNAME_OT_my_opVBGCL, 
ADDONNAME_OT_my_opVBGDL, ADDONNAME_OT_my_opVBGEL, ADDONNAME_OT_my_opVBGFL, ADDONNAME_OT_my_opVBGGL, ADDONNAME_OT_my_opVBGHL,  
ADDONNAME_23C, ADDONNAME_23P, ADDONNAME_LGC, ADDONNAME_HBC, ADDONNAME_MG, ADDONNAME_MGC, ADDONNAME_VB, ADDONNAME_VBC, ADDONNAME_OT_my_opggpie, 
ADDONNAME_OT_my_op, ADDONNAME_OT_my_op2, ADDONNAME_OT_my_op2pie, ADDONNAME_OT_my_oplgpie, ADDONNAME_OT_my_ophbpie, ADDONNAME_OT_my_opmcpie, 
ADDONNAME_OT_my_opmppie, ADDONNAME_OT_my_op3, Fontchange, Fontchangepie, Fontrestore, Fontrestorepie, 
TestPanel, TestPanel2_panel_1, TestPanel2_panel_2, TestPanel2C_panel_1, TestPanel2C_panel_2, TestPanel3_panel_1, TestPanel3_panel_2, TestPanel3P_panel_1, 
TestPanel3P_panel_2,TestPanel4_panel_1, TestPanel4_panel_2, TestPanel4LGC_panel_1, TestPanel4LGC_panel_2, TestPanel5_panel_1, TestPanel5_panel_2 , 
TestPanel5c_panel_1, TestPanel5c_panel_2, TestPanel6_panel_1, TestPanel6_panel_2, TestPanel7_panel_1, TestPanel7_panel_2, TestPanel8_panel_1, TestPanel8_panel_2, 
TestPanel8C_panel_1, TestPanel8C_panel_2, Locationchange, TestPanel9_panel_1, TestPanel9_panel_2, TestPanel9vb_panel_1, TestPanel9vb_panel_2, ADDONNAME_OT_my_opLGAL, ADDONNAME_OT_my_opLGBL, ADDONNAME_OT_my_opLGCL, ADDONNAME_OT_my_opLGDL, ADDONNAME_OT_my_opLGEL, ADDONNAME_OT_my_opLGFL,ADDONNAME_OT_my_opLGGL, ADDONNAME_OT_my_opLGHL, ADDONNAME_OT_my_opMGAL, ADDONNAME_OT_my_opMGBL, ADDONNAME_OT_my_opMGCL, ADDONNAME_OT_my_opMGDL, ADDONNAME_OT_my_opMGEL, ADDONNAME_OT_my_opMGFL, ADDONNAME_OT_my_opMGGL, ADDONNAME_OT_my_opMGHL, ADDONNAME_OT_my_opMCGAL, ADDONNAME_OT_my_opMCGBL, ADDONNAME_OT_my_opMCGCL, ADDONNAME_OT_my_opMCGDL, ADDONNAME_OT_my_opMCGEL, ADDONNAME_OT_my_opMPGAL, ADDONNAME_OT_my_opMPGBL, ADDONNAME_OT_my_opMPGCL, ADDONNAME_OT_my_opMPGDL, ADDONNAME_OT_my_opMPGEL, ADDONNAME_OT_my_opCOMPARISONAHBARAL, ADDONNAME_OT_my_opCOMPARISONAHBARBL, ADDONNAME_OT_my_opCOMPARISONAHBARCL, ADDONNAME_OT_my_opCOMPARISONAHBARD, ADDONNAME_OT_my_opCOMPARISONBHBARAL, ADDONNAME_OT_my_opCOMPARISONBHBARBL, ADDONNAME_OT_my_opCOMPARISONBHBARCL, ADDONNAME_OT_my_opCOMPARISONBHBARD, ADDONNAME_OT_my_opCOMPARISONALINEAL, ADDONNAME_OT_my_opCOMPARISONALINEB, ADDONNAME_OT_my_opCOMPARISONALINEC, ADDONNAME_OT_my_opCOMPARISONALINED, ADDONNAME_OT_my_opCOMPARISONALINEE, ADDONNAME_OT_my_opCOMPARISONALINEF, ADDONNAME_OT_my_opCOMPARISONALINEH, ADDONNAME_OT_my_opCOMPARISONALINEG, ADDONNAME_OT_my_opCOMPARISONBLINEA, ADDONNAME_OT_my_opCOMPARISONBLINEB, ADDONNAME_OT_my_opCOMPARISONBLINEC, ADDONNAME_OT_my_opCOMPARISONBLINED, ADDONNAME_OT_my_opCOMPARISONBLINEE, ADDONNAME_OT_my_opCOMPARISONBLINEF, ADDONNAME_OT_my_opCOMPARISONBLINEG, ADDONNAME_OT_my_opCOMPARISONBLINEH, ADDONNAME_OT_my_opCOMPARISONAMOUNTA, ADDONNAME_OT_my_opCOMPARISONAMOUNTB, ADDONNAME_OT_my_opCOMPARISONAMOUNTC, ADDONNAME_OT_my_opCOMPARISONAMOUNTD, ADDONNAME_OT_my_opCOMPARISONAMOUNTE, ADDONNAME_OT_my_opCOMPARISONAMOUNTF, ADDONNAME_OT_my_opCOMPARISONAMOUNTG, ADDONNAME_OT_my_opCOMPARISONAMOUNTH, ADDONNAME_OT_my_opCOMPARISONBMOUNTA, ADDONNAME_OT_my_opCOMPARISONBMOUNTB, ADDONNAME_OT_my_opCOMPARISONBMOUNTC, ADDONNAME_OT_my_opCOMPARISONBMOUNTD, ADDONNAME_OT_my_opCOMPARISONBMOUNTE, ADDONNAME_OT_my_opCOMPARISONBMOUNTF, ADDONNAME_OT_my_opCOMPARISONBMOUNTG, ADDONNAME_OT_my_opCOMPARISONBMOUNTH, ADDONNAME_OT_my_opCOMPARISONABARVA, ADDONNAME_OT_my_opCOMPARISONABARVB, ADDONNAME_OT_my_opCOMPARISONABARVC, ADDONNAME_OT_my_opCOMPARISONABARVD, ADDONNAME_OT_my_opCOMPARISONABARVE, ADDONNAME_OT_my_opCOMPARISONABARVF, ADDONNAME_OT_my_opCOMPARISONABARVG, ADDONNAME_OT_my_opCOMPARISONABARVH, ADDONNAME_OT_my_opCOMPARISONBBARVA, ADDONNAME_OT_my_opCOMPARISONBBARVB, ADDONNAME_OT_my_opCOMPARISONBBARVC, ADDONNAME_OT_my_opCOMPARISONBBARVD, ADDONNAME_OT_my_opCOMPARISONBBARVE, ADDONNAME_OT_my_opCOMPARISONBBARVF, ADDONNAME_OT_my_opCOMPARISONBBARVG, ADDONNAME_OT_my_opCOMPARISONBBARVH]
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type= MyProperties)
        
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    
if __name__ == "__main__":
    register()


