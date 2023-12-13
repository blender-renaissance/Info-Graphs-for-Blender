bl_info = {
    "name": "Info_graphs_for_blender",
    "author": "Vikrant Jadhav, Blender Renaissance",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Renaissance tab",
    "description": "Quick Render Presets for Blender Renaissance Graphs.",
    "warning": "",
    "doc_url": "https://twitter.com/b3d_Renaissance",
    "category": "3D View",
}


import bpy
import os
import csv
import mysql.connector

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
    
    my_enum_candlestick : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPcandle7', "24 FPS (and reset)", "24 Frames per second"),
                ('OPcandle8', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandlestick()
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
    
    my_enum_usmap : bpy.props.EnumProperty(
        name= "",
        description= "Change Frame rate of the scene",
        items= [('OPUSM7', "24 FPS (and reset)", "24 Frames per second"),
                ('OPUSM8', "30 FPS (and reset)", "30 Frames per second"),
        ],
        update=lambda self, context: bpy.ops.addonname.myop_operatorusmap()
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
    
    my_stringhost : bpy.props.StringProperty(
    name= "",
    default="localhost",)
    
    my_stringuser : bpy.props.StringProperty(
    name= "",
    default="root",)
    
    my_stringpassword : bpy.props.StringProperty(
    name= "",
    subtype='PASSWORD',)
    
    my_stringcirclegraph : bpy.props.StringProperty(
    name= "",
    default="circle_graph",)
    
    my_stringpiegraph : bpy.props.StringProperty(
    name= "",
    default="pie_graph",)
    
    my_stringcircle23_graph : bpy.props.StringProperty(
    name= "",
    default="circle23_graph",)
    
    my_stringcandlestick_graph : bpy.props.StringProperty(
    name= "",
    default="candlestick_graph",)
    
    my_stringpie23_graph : bpy.props.StringProperty(
    name= "",
    default="pie23_graph",)
    
    my_stringhorizontal_bar_graph : bpy.props.StringProperty(
    name= "",
    default="horizontal_bar_graph",)
    
    my_stringhorizontal_bar_graph_comparison : bpy.props.StringProperty(
    name= "",
    default="horizontal_bar_graph_comparison",)
    
    my_stringvertical_bar_graph : bpy.props.StringProperty(
    name= "",
    default="vertical_bar_graph",)
    
    my_stringvertical_bar_graph_comparison : bpy.props.StringProperty(
    name= "",
    default="vertical_bar_graph_comparison",)
    
    my_stringline_graph : bpy.props.StringProperty(
    name= "",
    default="line_graph",)
    
    my_stringline_graph_comparison : bpy.props.StringProperty(
    name= "",
    default="line_graph_comparison",)    

    my_stringmountain_graph : bpy.props.StringProperty(
    name= "",
    default="mountain_graph",)
    
    my_stringmountain_graph_comparison : bpy.props.StringProperty(
    name= "",
    default="mountain_graph_comparison",)
    
    my_stringmultiple_circle_graph : bpy.props.StringProperty(
    name= "",
    default="multiple_circle_graph",)
    
    my_stringmultiple_pie_graph : bpy.props.StringProperty(
    name= "",
    default="multiple_pie_graph",)  
    
    my_stringusmap : bpy.props.StringProperty(
    name= "",
    default="us_map",)      
    
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

    my_floatcandlea1: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle1()
        )

    my_floatcandlea2: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle2()
        )

    my_floatcandlea3: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle3()
    )

    my_floatcandlea4: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle4()
    )

    my_floatcandlea5: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle5()
    )

    my_floatcandlea6: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle6()
    )

    my_floatcandlea7: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle7()
    )

    my_floatcandlea8: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle8()
    )

    my_floatcandlea9: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle9()
    )

    my_floatcandlea10: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle10()
    )

    my_floatcandlea11: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle11()
    )

    my_floatcandlea12: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle12()
    )

    my_floatcandlea13: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle13()
    )

    my_floatcandlea14: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle14()
    )

    my_floatcandlea15: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle15()
    )

    my_floatcandlea16: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle16()
    )

    my_floatcandlea17: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle17()
    )

    my_floatcandlea18: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle18()
    )

    my_floatcandlea19: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle19()
    )

    my_floatcandlea20: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle20()
    )

    my_floatcandlea21: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle21()
    )

    my_floatcandlea22: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle22()
    )

    my_floatcandlea23: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle23()
    )

    my_floatcandlea24: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle24()
    )

    my_floatcandlea25: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle25()
    )

    my_floatcandlea26: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle26()
    )

    my_floatcandlea27: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle27()
    )

    my_floatcandlea28: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle28()
    )

    my_floatcandlea29: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle29()
    )

    my_floatcandlea30: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle30()
    )

    my_floatcandlea31: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle31()
    )

    my_floatcandlea32: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle32()
    )

    my_floatcandleb1: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle1()
        )

    my_floatcandleb2: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle2()
        )

    my_floatcandleb3: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle3()
    )

    my_floatcandleb4: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle4()
    )

    my_floatcandleb5: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle5()
    )

    my_floatcandleb6: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle6()
    )

    my_floatcandleb7: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle7()
    )

    my_floatcandleb8: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle8()
    )

    my_floatcandleb9: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle9()
    )

    my_floatcandleb10: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle10()
    )

    my_floatcandleb11: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle11()
    )

    my_floatcandleb12: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle12()
    )

    my_floatcandleb13: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle13()
    )

    my_floatcandleb14: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle14()
    )

    my_floatcandleb15: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle15()
    )

    my_floatcandleb16: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle16()
    )

    my_floatcandleb17: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle17()
    )

    my_floatcandleb18: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle18()
    )

    my_floatcandleb19: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle19()
    )

    my_floatcandleb20: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle20()
    )

    my_floatcandleb21: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle21()
    )

    my_floatcandleb22: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle22()
    )

    my_floatcandleb23: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle23()
    )

    my_floatcandleb24: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle24()
    )

    my_floatcandleb25: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle25()
    )

    my_floatcandleb26: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle26()
    )

    my_floatcandleb27: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle27()
    )

    my_floatcandleb28: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle28()
    )

    my_floatcandleb29: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle29()
    )

    my_floatcandleb30: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle30()
    )

    my_floatcandleb31: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle31()
    )

    my_floatcandleb32: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcandle32()
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
        
    my_floatHBGE: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgel()
        )
        
    my_floatHBGLE: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgel()
        )

    my_floatHBGF: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgfl()
        )
        
    my_floatHBGLF: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgfl()
        )

    my_floatHBGG: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbggl()
        )
        
    my_floatHBGLG: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbggl()
        )

    my_floatHBGH: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbghl()
        )
        
    my_floatHBGLH: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbghl()
        )

    my_floatHBGI: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgil()
        )
        
    my_floatHBGLI: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgil()
        )

    my_floatHBGJ: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 1,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgjl()
        )
        
    my_floatHBGLJ: bpy.props.FloatProperty(
        name = "In seconds",
        description = "A float property",
        default = 4,
        min = 0.1,
        max = 300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorhbgjl()
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
    
    my_floatCOMPARISONAHBARE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbare()
    )
    
    my_floatCOMPARISONAHBARLE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbare()
    )

    my_floatCOMPARISONAHBARF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbarf()
    )
    
    my_floatCOMPARISONAHBARLF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbarf()
    )

    my_floatCOMPARISONAHBARG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbarg()
    )
    
    my_floatCOMPARISONAHBARLG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbarg()
    )

    my_floatCOMPARISONAHBARH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbarh()
    )
    
    my_floatCOMPARISONAHBARLH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbarh()
    )

    my_floatCOMPARISONAHBARI: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbari()
    )
    
    my_floatCOMPARISONAHBARLI: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonahbari()
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

    my_floatCOMPARISONBHBARE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbare()
    )
    
    my_floatCOMPARISONBHBARLE: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbare()
    )

    my_floatCOMPARISONBHBARF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbarf()
    )
    
    my_floatCOMPARISONBHBARLF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbarf()
    )

    my_floatCOMPARISONBHBARG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbarg()
    )
    
    my_floatCOMPARISONBHBARLG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbarg()
    )

    my_floatCOMPARISONBHBARH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbarh()
    )
    
    my_floatCOMPARISONBHBARLH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbarh()
    )

    my_floatCOMPARISONBHBARI: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbari()
    )
    
    my_floatCOMPARISONBHBARLI: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=4,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorcomparisonbhbari()
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
        default=2,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgal()
    )
        
    my_floatLGB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=2.5,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatorlgbl()
    )
        
    my_floatLGLB: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=0.5,
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
    
    my_floatMCGF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=6,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgfl()
    )

    my_floatMCGLF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcgfl()
    )
    
    my_floatMCGG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=7,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcggl()
    )

    my_floatMCGLG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcggl()
    )

    my_floatMCGH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=8,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcghl()
    )

    my_floatMCGLH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormcghl()
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
    
    my_floatMPGF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=6,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgfl()
    )

    my_floatMPGLF: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpgfl()
    )

    my_floatMPGG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=7,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpggl()
    )

    my_floatMPGLG: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpggl()
    )

    my_floatMPGH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=8,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpghl()
    )

    my_floatMPGLH: bpy.props.FloatProperty(
        name="In seconds",
        description="A float property",
        default=1,
        min=0.1,
        max=300.0,
        update=lambda self, context: bpy.ops.addonname.myop_operatormpghl()
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
        
    my_pathcandle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/candlestick_graph.csv",
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
        
    my_pathfontcg_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontcg_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontcg_value: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontcg_description: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontpg_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontpg_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontpg_value: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontpg_description: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfont23cg_title: bpy.props.StringProperty(
        name="",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfont23cg_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfont23cg_value: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfont23cg_description: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfont23cg_legend: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfont23pg_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfont23pg_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfont23pg_value: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfont23pg_description: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfont23pg_legend: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontbg_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontbg_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontbg_barvalue: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontbg_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontbg_rangenumbers: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontbg_texttotal: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontbg_valuetotal: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontbgc_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontbgc_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontbgc_barvalue: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontbgc_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontbgc_rangenumbers: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontbgc_legend: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontlg_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontlg_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontlg_barvalue: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontlg_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontlg_rangenumbers: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Semibold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontlgc_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontlgc_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontlgc_barvalue: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontlgc_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontlgc_rangenumbers: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Semibold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontlgc_legend: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontmg_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmg_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmg_barvalue: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmg_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontmg_rangenumbers: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Semibold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmgc_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmgc_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmgc_barvalue: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmgc_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontmgc_rangenumbers: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Semibold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontmgc_legend: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmcg_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmcg_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmcg_barvalue: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Semibold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmcg_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontmpg_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmpg_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmpg_barvalue: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Semibold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontmpg_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontvbg_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontvbg_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontvbg_barvalue: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontvbg_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontvbg_rangenumbers: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontvbg_texttotal: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontvbg_valuetotal: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
 
    my_pathfontvbgc_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontvbgc_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontvbgc_barvaluea: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontvbgc_barvalueb: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
             
    my_pathfontvbgc_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontvbgc_rangenumbers: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )

    my_pathfontvbgc_legend: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH', 
        )
        
    my_pathfontcandleg_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontcandleg_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontcandleg_rangenumbers: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Semibold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontcandleg_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathusmap: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//csv/us_map.csv",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontusmap_title: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-ExtraBold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontusmap_subtitle: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Light.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontusmap_rangenumbers: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Semibold.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )
        
    my_pathfontusmap_bartext: bpy.props.StringProperty(
        name = "",
        description="link to csv file:",
        default="//Fonts/Open sans/OpenSans-Regular.ttf",
        maxlen=1024,
        subtype='FILE_PATH',
        )


class NG_PT_QuickRenderPresets(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"} 
    
class NG_PT_QuickRenderPresets_1(NG_PT_QuickRenderPresets, bpy.types.Panel):    
    bl_label = "Quick Render Presets"
    bl_idname = "NG_PT_QuickRenderPresets_1"  
   
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
        
class NG_PT_QuickRenderPresets_2(NG_PT_QuickRenderPresets, bpy.types.Panel):
    bl_parent_id = "NG_PT_QuickRenderPresets_1"
    bl_label = "MySQL Login Details"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool 
        
        rowSH = layout.row()
        rowSH.label(text= "Hostname:")
        layout.prop(mytool, "my_stringhost")
        
        rowSU = layout.row()
        rowSU.label(text= "User:")
        layout.prop(mytool, "my_stringuser")
        
        rowSPW = layout.row()
        rowSPW.label(text= "Password:")
        layout.prop(mytool, "my_stringpassword")
        
        
class CIRCLE_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class CIRCLE_GRAPH_PT_panel_1(CIRCLE_GRAPH_panel, bpy.types.Panel):
    bl_idname = "CIRCLE_GRAPH_PT_panel_1"
    bl_label = "Circle Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowFPS = layout.row()
        rowFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enum2")

class CIRCLE_GRAPH_PT_panel_2(CIRCLE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "CIRCLE_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowCGcsv = layout.row()
        rowCGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_path")
        layout.operator("mesh.mycubeoperatorcgcsv")
        
class CIRCLE_GRAPH_PT_panel_3(CIRCLE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "CIRCLE_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringcirclegraph")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorcgsql")

class CIRCLE_GRAPH_PT_panel_4(CIRCLE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "CIRCLE_GRAPH_PT_panel_1"
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
        
class CIRCLE_GRAPH_PT_panel_5(CIRCLE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "CIRCLE_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlecg = layout.row()
        rowtitlecg.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontcg_title")

        rowsubtitlecg = layout.row()
        rowsubtitlecg.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontcg_subtitle")
        
        rowvaluecg = layout.row()
        rowvaluecg.label(text= "Value Font:")
        layout.prop(mytool, "my_pathfontcg_value")

        rowvaluecg = layout.row()
        rowvaluecg.label(text= "Description Font:")
        layout.prop(mytool, "my_pathfontcg_description")
        layout.operator("addonname.myop_operatorf")
        
        rowresetcg = layout.row()
        rowresetcg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatorres")
        
                
class CIRCLE_GRAPH_23_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class CIRCLE_GRAPH_23_PT_panel_1(CIRCLE_GRAPH_23_panel, bpy.types.Panel):
    bl_idname = "CIRCLE_GRAPH_23_PT_panel_1"
    bl_label = "2-3 Circle Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        row23FPS = layout.row()
        row23FPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enum23C")

class CIRCLE_GRAPH_23_PT_panel_2(CIRCLE_GRAPH_23_panel, bpy.types.Panel):
    bl_parent_id = "CIRCLE_GRAPH_23_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        row23CGcsv = layout.row()
        row23CGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_path23c")
        layout.operator("mesh.mycubeoperatorcgccsv")
        
class CIRCLE_GRAPH_23_PT_panel_3(CIRCLE_GRAPH_23_panel, bpy.types.Panel):
    bl_parent_id = "CIRCLE_GRAPH_23_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringcircle23_graph")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorcg23sql")

class CIRCLE_GRAPH_23_PT_panel_4(CIRCLE_GRAPH_23_panel, bpy.types.Panel):
    bl_parent_id = "CIRCLE_GRAPH_23_PT_panel_1"
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
        
class CIRCLE_GRAPH_23_PT_panel_5(CIRCLE_GRAPH_23_panel, bpy.types.Panel):
    bl_parent_id = "CIRCLE_GRAPH_23_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitle23cg = layout.row()
        rowtitle23cg.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfont23cg_title")

        rowsubtitle23cg = layout.row()
        rowsubtitle23cg.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfont23cg_subtitle")
        
        rowvalue23cg = layout.row()
        rowvalue23cg.label(text= "Value Font:")
        layout.prop(mytool, "my_pathfont23cg_value")

        rowdescription23cg = layout.row()
        rowdescription23cg.label(text= "Description Font:")
        layout.prop(mytool, "my_pathfont23cg_description")
        
        rowlegend23cg = layout.row()
        rowlegend23cg.label(text= "Legend Font:")
        layout.prop(mytool, "my_pathfont23cg_legend")                
        layout.operator("addonname.myop_operator23cgfont")
        
        rowreset23cg = layout.row()
        rowreset23cg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operator23cgresfont")

class CANDLESTICK_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class CANDLESTICK_GRAPH_PT_panel_1(CANDLESTICK_GRAPH_panel, bpy.types.Panel):
    bl_idname = "CANDLESTICK_GRAPH_PT_panel_1"
    bl_label = "Candlestick Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

class CANDLESTICK_GRAPH_PT_panel_2(CANDLESTICK_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "CANDLESTICK_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowCGcsv = layout.row()
        rowCGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathcandle")
        layout.operator("mesh.mycubeoperatorcandlecsv")
        
class CANDLESTICK_GRAPH_PT_panel_3(CANDLESTICK_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "CANDLESTICK_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringcandlestick_graph")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorcandlesql")

class CANDLESTICK_GRAPH_PT_panel_4(CANDLESTICK_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "CANDLESTICK_GRAPH_PT_panel_1"
    bl_label = "Note"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowcandlea1 = layout.row()
        rowcandlea1.label(text= "Duration Control is not applied")
        
        rowcandlea2 = layout.row()
        rowcandlea2.label(text= "for this graph,")
        
        rowcandlea3 = layout.row()
        rowcandlea3.label(text= "as its tedious to control")
        
        rowcandlea4 = layout.row()
        rowcandlea4.label(text= "32 data points individually.")

        rowcandlea5 = layout.row()
        rowcandlea5.label(text= "There is a tutorial in the help")
        
        rowcandlea6 = layout.row()
        rowcandlea6.label(text= "folder on how to increase duration")
        
        rowcandlea7 = layout.row()
        rowcandlea7.label(text= "in an easy way.")
        
class CANDLESTICK_GRAPH_PT_panel_5(CANDLESTICK_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "CANDLESTICK_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlecandleg = layout.row()
        rowtitlecandleg.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontcandleg_title")

        rowsubtitlecandleg = layout.row()
        rowsubtitlecandleg.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontcandleg_subtitle")
        
        rowrangenumberscandleg = layout.row()
        rowrangenumberscandleg.label(text= "Range Numbers Font:")
        layout.prop(mytool, "my_pathfontcandleg_rangenumbers")

        rowbartextcandleg = layout.row()
        rowbartextcandleg.label(text= "Point Name Font:")
        layout.prop(mytool, "my_pathfontcandleg_bartext")
        layout.operator("addonname.myop_operatorcandlegfont")
        
        rowresetcandleg = layout.row()
        rowresetcandleg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatorcandlegresfont")
        
class PIE_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class PIE_GRAPH_PT_panel_1(PIE_GRAPH_panel, bpy.types.Panel):
    bl_idname = "PIE_GRAPH_PT_panel_1"
    bl_label = "Pie Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowPFPS = layout.row()
        rowPFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enum2pie")

class PIE_GRAPH_PT_panel_2(PIE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "PIE_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowPGcsv = layout.row()
        rowPGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathpie")
        layout.operator("mesh.mycubeoperatorpgcsv")
        
class PIE_GRAPH_PT_panel_3(PIE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "PIE_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringpiegraph")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorpgsql")

class PIE_GRAPH_PT_panel_4(PIE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "PIE_GRAPH_PT_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowPG = layout.row()
        rowPG.label(text= "Start Animation:")
        layout.prop(mytool, "my_float2pie")

        rowPE = layout.row()
        rowPE.label(text= "Length of Animation:")
        layout.prop(mytool, "my_floatpie")
        
class PIE_GRAPH_PT_panel_5(PIE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "PIE_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
            
        rowtitlepg = layout.row()
        rowtitlepg.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontpg_title")

        rowsubtitlepg = layout.row()
        rowsubtitlepg.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontpg_subtitle")
        
        rowvaluepg = layout.row()
        rowvaluepg.label(text= "Value Font:")
        layout.prop(mytool, "my_pathfontpg_value")

        rowvaluepg = layout.row()
        rowvaluepg.label(text= "Description Font:")
        layout.prop(mytool, "my_pathfontpg_description")
        layout.operator("addonname.myop_operatorfpie")
        
        rowresetpg = layout.row()
        rowresetpg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatorrespie")

        
class PIE_GRAPH_23_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class PIE_GRAPH_23_PT_panel_1(PIE_GRAPH_23_panel, bpy.types.Panel):
    bl_idname = "PIE_GRAPH_23_PT_panel_1"
    bl_label = "2-3 Pie Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        row23PFPS = layout.row()
        row23PFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enum23P")

class PIE_GRAPH_23_PT_panel_2(PIE_GRAPH_23_panel, bpy.types.Panel):
    bl_parent_id = "PIE_GRAPH_23_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        row23PGcsv = layout.row()
        row23PGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_path23p")
        layout.operator("mesh.mycubeoperatorpgccsv")
        
class PIE_GRAPH_23_PT_panel_3(PIE_GRAPH_23_panel, bpy.types.Panel):
    bl_parent_id = "PIE_GRAPH_23_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringpie23_graph")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorpg23sql")

class PIE_GRAPH_23_PT_panel_4(PIE_GRAPH_23_panel, bpy.types.Panel):
    bl_parent_id = "PIE_GRAPH_23_PT_panel_1"
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
        
class PIE_GRAPH_23_PT_panel_5(PIE_GRAPH_23_panel, bpy.types.Panel):
    bl_parent_id = "PIE_GRAPH_23_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitle23pg = layout.row()
        rowtitle23pg.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfont23pg_title")

        rowsubtitle23pg = layout.row()
        rowsubtitle23pg.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfont23pg_subtitle")
        
        rowvalue23pg = layout.row()
        rowvalue23pg.label(text= "Value Font:")
        layout.prop(mytool, "my_pathfont23pg_value")

        rowvalue23pg = layout.row()
        rowvalue23pg.label(text= "Description Font:")
        layout.prop(mytool, "my_pathfont23pg_description")
        
        rowlegend23pg = layout.row()
        rowlegend23pg.label(text= "Legend Font:")
        layout.prop(mytool, "my_pathfont23pg_legend")                
        layout.operator("addonname.myop_operator23pgfont")
        
        rowreset23pg = layout.row()
        rowreset23pg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operator23pgresfont")
        
class LINE_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class LINE_GRAPH_PT_panel_1(LINE_GRAPH_panel, bpy.types.Panel):
    bl_idname = "LINE_GRAPH_PT_panel_1"
    bl_label = "Line Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowLG = layout.row()
        rowLG.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumLGpie")

class LINE_GRAPH_PT_panel_2(LINE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "LINE_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowLGcsv = layout.row()
        rowLGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathline")
        layout.operator("mesh.mycubeoperatorlgcsv")
        
class LINE_GRAPH_PT_panel_3(LINE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "LINE_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringline_graph")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorlgsql")

class LINE_GRAPH_PT_panel_4(LINE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "LINE_GRAPH_PT_panel_1"
    bl_label = "Duration Control"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowLGA = layout.row()
        rowLGA.label(text= "Start Length of Curve:")
        layout.prop(mytool, "my_floatLGA")

        rowLGLA = layout.row()
        rowLGLA.label(text= "Length of Animation of Length of Curve:")
        layout.prop(mytool, "my_floatLGLA")

        rowLGB = layout.row()
        rowLGB.label(text= "Start Shader Display:")
        layout.prop(mytool, "my_floatLGB")

        rowLGLB = layout.row()
        rowLGLB.label(text= "Length of Animation of Shader Display:")
        layout.prop(mytool, "my_floatLGLB")

        
class LINE_GRAPH_PT_panel_5(LINE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "LINE_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlelg = layout.row()
        rowtitlelg.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontlg_title")

        rowsubtitlelg = layout.row()
        rowsubtitlelg.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontlg_subtitle")
        
        rowvaluelg = layout.row()
        rowvaluelg.label(text= "Bar Value Font:")
        layout.prop(mytool, "my_pathfontlg_barvalue")

        rowlinetextlg = layout.row()
        rowlinetextlg.label(text= "Bar Text Font:")
        layout.prop(mytool, "my_pathfontlg_bartext")
        
        rowlegendlg = layout.row()
        rowlegendlg.label(text= "Range Numbers Font:")
        layout.prop(mytool, "my_pathfontlg_rangenumbers")                
        layout.operator("addonname.myop_operatorlinegfont")
        
        rowresetlg = layout.row()
        rowresetlg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatorlinegresfont")

        
class COMPARISON_LINE_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class COMPARISON_LINE_GRAPH_PT_panel_1(COMPARISON_LINE_GRAPH_panel, bpy.types.Panel):
    bl_idname = "COMPARISON_LINE_GRAPH_PT_panel_1"
    bl_label = "Line Graph Comparison"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowLGCFPS = layout.row()
        rowLGCFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumLGC")

class COMPARISON_LINE_GRAPH_PT_panel_2(COMPARISON_LINE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_LINE_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowLGCcsv = layout.row()
        rowLGCcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathlinec")
        layout.operator("mesh.mycubeoperatorlgccsv")
        
class COMPARISON_LINE_GRAPH_PT_panel_3(COMPARISON_LINE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_LINE_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringline_graph_comparison")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorlgcsql")

class COMPARISON_LINE_GRAPH_PT_panel_4(COMPARISON_LINE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_LINE_GRAPH_PT_panel_1"
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

class COMPARISON_LINE_GRAPH_PT_panel_5(COMPARISON_LINE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_LINE_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlelgc = layout.row()
        rowtitlelgc.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontlgc_title")

        rowsubtitlelgc = layout.row()
        rowsubtitlelgc.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontlgc_subtitle")
        
        rowvaluelgc = layout.row()
        rowvaluelgc.label(text= "Bar Value Font:")
        layout.prop(mytool, "my_pathfontlgc_barvalue")

        rowvaluelgc = layout.row()
        rowvaluelgc.label(text= "Bar Text Font:")
        layout.prop(mytool, "my_pathfontlgc_bartext")
        
        rowlegendlgc = layout.row()
        rowlegendlgc.label(text= "Range Numbers Font:")
        layout.prop(mytool, "my_pathfontlgc_rangenumbers")
        
        rowlegendlgc = layout.row()
        rowlegendlgc.label(text= "Legend Font:")
        layout.prop(mytool, "my_pathfontlgc_legend")                 
        layout.operator("addonname.myop_operatorlinegcfont")
        
        rowresetlgc = layout.row()
        rowresetlgc.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatorlinegcresfont")


class HORIZONTAL_BAR_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class HORIZONTAL_BAR_GRAPH_PT_panel_1(HORIZONTAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_idname = "HORIZONTAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Horizontal Bar Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowHB = layout.row()
        rowHB.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumHBpie")

class HORIZONTAL_BAR_GRAPH_PT_panel_2(HORIZONTAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "HORIZONTAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowHBcsv = layout.row()
        rowHBcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathhbar")
        layout.operator("mesh.mycubeoperatorhbcsv")
        
class HORIZONTAL_BAR_GRAPH_PT_panel_3(HORIZONTAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "HORIZONTAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringhorizontal_bar_graph")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorhbgsql")

class HORIZONTAL_BAR_GRAPH_PT_panel_4(HORIZONTAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "HORIZONTAL_BAR_GRAPH_PT_panel_1"
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
        
        rowHBGD = layout.row()
        rowHBGD.label(text= "Start E:")
        layout.prop(mytool, "my_floatHBGE")
        
        rowHBGLD = layout.row()
        rowHBGLD.label(text= "Length of Animation E:")
        layout.prop(mytool, "my_floatHBGLE")
        
        rowHBGD = layout.row()
        rowHBGD.label(text= "Start F:")
        layout.prop(mytool, "my_floatHBGF")
        
        rowHBGLD = layout.row()
        rowHBGLD.label(text= "Length of Animation F:")
        layout.prop(mytool, "my_floatHBGLF")
        
        rowHBGD = layout.row()
        rowHBGD.label(text= "Start G:")
        layout.prop(mytool, "my_floatHBGG")
        
        rowHBGLD = layout.row()
        rowHBGLD.label(text= "Length of Animation G:")
        layout.prop(mytool, "my_floatHBGLG")
        
        rowHBGD = layout.row()
        rowHBGD.label(text= "Start H:")
        layout.prop(mytool, "my_floatHBGH")
        
        rowHBGLD = layout.row()
        rowHBGLD.label(text= "Length of Animation H:")
        layout.prop(mytool, "my_floatHBGLH")
        
        rowHBGD = layout.row()
        rowHBGD.label(text= "Start I:")
        layout.prop(mytool, "my_floatHBGI")
        
        rowHBGLD = layout.row()
        rowHBGLD.label(text= "Length of Animation I:")
        layout.prop(mytool, "my_floatHBGLI")
        
        rowHBGD = layout.row()
        rowHBGD.label(text= "Start J:")
        layout.prop(mytool, "my_floatHBGJ")
        
        rowHBGLD = layout.row()
        rowHBGLD.label(text= "Length of Animation J:")
        layout.prop(mytool, "my_floatHBGLJ")
        
class HORIZONTAL_BAR_GRAPH_PT_panel_5(HORIZONTAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "HORIZONTAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlebg = layout.row()
        rowtitlebg.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontbg_title")

        rowsubtitlebg = layout.row()
        rowsubtitlebg.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontbg_subtitle")
        
        rowvaluebg = layout.row()
        rowvaluebg.label(text= "Bar Value Font:")
        layout.prop(mytool, "my_pathfontbg_barvalue")

        rowvaluebg = layout.row()
        rowvaluebg.label(text= "Bar Text Font:")
        layout.prop(mytool, "my_pathfontbg_bartext")
        
        rowlegendbg = layout.row()
        rowlegendbg.label(text= "Range Numbers Font:")
        layout.prop(mytool, "my_pathfontbg_rangenumbers")
        
        rowlegendbg = layout.row()
        rowlegendbg.label(text= "Text Total Font:")
        layout.prop(mytool, "my_pathfontbg_texttotal")

        rowlegendbg = layout.row()
        rowlegendbg.label(text= "Value Total Font:")
        layout.prop(mytool, "my_pathfontbg_valuetotal")                  
        layout.operator("addonname.myop_operatorbgfont")
        
        rowresetbg = layout.row()
        rowresetbg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatorbgresfont")
        
class COMPARISON_HORIZONTAL_BAR_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_1(COMPARISON_HORIZONTAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_idname = "COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Horizontal Bar Graph Comparison"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowHBCFPS = layout.row()
        rowHBCFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumHBC")

class COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_2(COMPARISON_HORIZONTAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowHBCcsv = layout.row()
        rowHBCcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathhbarc")
        layout.operator("mesh.mycubeoperatorhbccsv")
        
class COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_3(COMPARISON_HORIZONTAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringhorizontal_bar_graph_comparison")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorhbgcsql")

class COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_4(COMPARISON_HORIZONTAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_1"
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
        
        rowCOMPARISONAHBARE = layout.row()
        rowCOMPARISONAHBARE.label(text= "Start A5:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARE")

        rowCOMPARISONAHBARLE = layout.row()
        rowCOMPARISONAHBARLE.label(text= "Length of Animation A5:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARLE")
        
        rowCOMPARISONBHBARE = layout.row()
        rowCOMPARISONBHBARE.label(text= "Start B5:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARE")

        rowCOMPARISONBHBARLE = layout.row()
        rowCOMPARISONBHBARLE.label(text= "Length of Animation B5:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARLE")

        rowCOMPARISONAHBARF = layout.row()
        rowCOMPARISONAHBARF.label(text= "Start A6:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARF")

        rowCOMPARISONAHBARLF = layout.row()
        rowCOMPARISONAHBARLF.label(text= "Length of Animation A6:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARLF")
        
        rowCOMPARISONBHBARF = layout.row()
        rowCOMPARISONBHBARF.label(text= "Start B6:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARF")

        rowCOMPARISONBHBARLF = layout.row()
        rowCOMPARISONBHBARLF.label(text= "Length of Animation B6:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARLF")
        
        rowCOMPARISONAHBARG = layout.row()
        rowCOMPARISONAHBARG.label(text= "Start A7:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARG")

        rowCOMPARISONAHBARLG = layout.row()
        rowCOMPARISONAHBARLG.label(text= "Length of Animation A7:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARLG")
        
        rowCOMPARISONBHBARG = layout.row()
        rowCOMPARISONBHBARG.label(text= "Start B7:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARG")

        rowCOMPARISONBHBARLG = layout.row()
        rowCOMPARISONBHBARLG.label(text= "Length of Animation B7:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARLG")
        
        rowCOMPARISONAHBARH = layout.row()
        rowCOMPARISONAHBARH.label(text= "Start A8:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARH")

        rowCOMPARISONAHBARLH = layout.row()
        rowCOMPARISONAHBARLH.label(text= "Length of Animation A8:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARLH")
        
        rowCOMPARISONBHBARH = layout.row()
        rowCOMPARISONBHBARH.label(text= "Start B8:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARH")

        rowCOMPARISONBHBARLH = layout.row()
        rowCOMPARISONBHBARLH.label(text= "Length of Animation B8:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARLH")
        
        rowCOMPARISONAHBARI = layout.row()
        rowCOMPARISONAHBARI.label(text= "Start A9:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARI")

        rowCOMPARISONAHBARLI = layout.row()
        rowCOMPARISONAHBARLI.label(text= "Length of Animation A9:")
        layout.prop(mytool, "my_floatCOMPARISONAHBARLI")
        
        rowCOMPARISONBHBARI = layout.row()
        rowCOMPARISONBHBARI.label(text= "Start B9:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARI")

        rowCOMPARISONBHBARLI = layout.row()
        rowCOMPARISONBHBARLI.label(text= "Length of Animation B9:")
        layout.prop(mytool, "my_floatCOMPARISONBHBARLI")

class COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_5(COMPARISON_HORIZONTAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlebgc = layout.row()
        rowtitlebgc.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontbgc_title")

        rowsubtitlebgc = layout.row()
        rowsubtitlebgc.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontbgc_subtitle")
        
        rowvaluebgc = layout.row()
        rowvaluebgc.label(text= "Bar Value Font:")
        layout.prop(mytool, "my_pathfontbgc_barvalue")

        rowvaluebgc = layout.row()
        rowvaluebgc.label(text= "Bar Text Font:")
        layout.prop(mytool, "my_pathfontbgc_bartext")
        
        rowlegendbgc = layout.row()
        rowlegendbgc.label(text= "Range Numbers Font:")
        layout.prop(mytool, "my_pathfontbgc_rangenumbers")
        
        rowlegendbgc = layout.row()
        rowlegendbgc.label(text= "Legend Font:")
        layout.prop(mytool, "my_pathfontbgc_legend")                 
        layout.operator("addonname.myop_operatorbgcfont")
        
        rowresetbgc = layout.row()
        rowresetbgc.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatorbgcresfont")

class MULTIPLE_CIRCLE_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class MULTIPLE_CIRCLE_GRAPH_PT_panel_1(MULTIPLE_CIRCLE_GRAPH_panel, bpy.types.Panel):
    bl_idname = "MULTIPLE_CIRCLE_GRAPH_PT_panel_1"
    bl_label = "Multiple Circle Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowMC = layout.row()
        rowMC.label(text= "Frames per second:")       
        layout.prop(mytool, "my_enumMCpie")

class MULTIPLE_CIRCLE_GRAPH_PT_panel_2(MULTIPLE_CIRCLE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MULTIPLE_CIRCLE_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowMCcsv = layout.row()
        rowMCcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathmcircle")
        layout.operator("mesh.mycubeoperatormccsv")
        
class MULTIPLE_CIRCLE_GRAPH_PT_panel_3(MULTIPLE_CIRCLE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MULTIPLE_CIRCLE_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringmultiple_circle_graph")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatormcgsql")

class MULTIPLE_CIRCLE_GRAPH_PT_panel_4(MULTIPLE_CIRCLE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MULTIPLE_CIRCLE_GRAPH_PT_panel_1"
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
        
        rowMCGE = layout.row()
        rowMCGE.label(text= "Start F:")
        layout.prop(mytool, "my_floatMCGF")

        rowMCGLE = layout.row()
        rowMCGLE.label(text= "Length of Animation F:")
        layout.prop(mytool, "my_floatMCGLF")
        
        rowMCGE = layout.row()
        rowMCGE.label(text= "Start G:")
        layout.prop(mytool, "my_floatMCGG")

        rowMCGLE = layout.row()
        rowMCGLE.label(text= "Length of Animation G:")
        layout.prop(mytool, "my_floatMCGLG")
        
        rowMCGE = layout.row()
        rowMCGE.label(text= "Start H:")
        layout.prop(mytool, "my_floatMCGH")

        rowMCGLE = layout.row()
        rowMCGLE.label(text= "Length of Animation H:")
        layout.prop(mytool, "my_floatMCGLH")

class MULTIPLE_CIRCLE_GRAPH_PT_panel_5(MULTIPLE_CIRCLE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MULTIPLE_CIRCLE_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlemcg = layout.row()
        rowtitlemcg.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontmcg_title")

        rowsubtitlemcg = layout.row()
        rowsubtitlemcg.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontmcg_subtitle")
        
        rowvaluemcg = layout.row()
        rowvaluemcg.label(text= "Value Font:")
        layout.prop(mytool, "my_pathfontmcg_barvalue")

        rowvaluemcg = layout.row()
        rowvaluemcg.label(text= "Description Font:")
        layout.prop(mytool, "my_pathfontmcg_bartext")
        layout.operator("addonname.myop_operatormcgfont")
        
        rowresetmcg = layout.row()
        rowresetmcg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatormcgresfont")

        
class MULTIPLE_PIE_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class MULTIPLE_PIE_GRAPH_PT_panel_1(MULTIPLE_PIE_GRAPH_panel, bpy.types.Panel):
    bl_idname = "MULTIPLE_PIE_GRAPH_PT_panel_1"
    bl_label = "Multiple Pie Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowMP = layout.row()
        rowMP.label(text= "Frames per second:")       
        layout.prop(mytool, "my_enumMPpie")

class MULTIPLE_PIE_GRAPH_PT_panel_2(MULTIPLE_PIE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MULTIPLE_PIE_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowMPcsv = layout.row()
        rowMPcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathmpie")
        layout.operator("mesh.mycubeoperatormpcsv")
        
class MULTIPLE_PIE_GRAPH_PT_panel_3(MULTIPLE_PIE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MULTIPLE_PIE_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringmultiple_pie_graph")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatormpgsql")

class MULTIPLE_PIE_GRAPH_PT_panel_4(MULTIPLE_PIE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MULTIPLE_PIE_GRAPH_PT_panel_1"
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
        
        rowMPF = layout.row()
        rowMPF.label(text="Start F:")
        layout.prop(mytool, "my_floatMPGF")

        rowMPLF = layout.row()
        rowMPLF.label(text="Length of Animation F:")
        layout.prop(mytool, "my_floatMPGLF")
        
        rowMPF = layout.row()
        rowMPF.label(text="Start G:")
        layout.prop(mytool, "my_floatMPGG")

        rowMPLF = layout.row()
        rowMPLF.label(text="Length of Animation G:")
        layout.prop(mytool, "my_floatMPGLG")
        
        rowMPF = layout.row()
        rowMPF.label(text="Start H:")
        layout.prop(mytool, "my_floatMPGH")

        rowMPLF = layout.row()
        rowMPLF.label(text="Length of Animation H:")
        layout.prop(mytool, "my_floatMPGLH")

class MULTIPLE_PIE_GRAPH_PT_panel_5(MULTIPLE_PIE_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MULTIPLE_PIE_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlempg = layout.row()
        rowtitlempg.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontmpg_title")

        rowsubtitlempg = layout.row()
        rowsubtitlempg.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontmpg_subtitle")
        
        rowvaluempg = layout.row()
        rowvaluempg.label(text= "Value Font:")
        layout.prop(mytool, "my_pathfontmpg_barvalue")

        rowvaluempg = layout.row()
        rowvaluempg.label(text= "Description Font:")
        layout.prop(mytool, "my_pathfontmpg_bartext")
        layout.operator("addonname.myop_operatormpgfont")
        
        rowresetmpg = layout.row()
        rowresetmpg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatormpgresfont")

        
class MOUNTAIN_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class MOUNTAIN_GRAPH_PT_panel_1(MOUNTAIN_GRAPH_panel, bpy.types.Panel):
    bl_idname = "MOUNTAIN_GRAPH_PT_panel_1"
    bl_label = "Mountain Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowMGFPS = layout.row()
        rowMGFPS.label(text= "Frames per second:")  
        layout.prop(mytool, "my_enumMG") 

class MOUNTAIN_GRAPH_PT_panel_2(MOUNTAIN_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MOUNTAIN_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowMGcsv = layout.row()
        rowMGcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathmg")
        layout.operator("mesh.mycubeoperatormgcsv")
        
class MOUNTAIN_GRAPH_PT_panel_3(MOUNTAIN_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MOUNTAIN_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringmountain_graph")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatormgsql")

class MOUNTAIN_GRAPH_PT_panel_4(MOUNTAIN_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MOUNTAIN_GRAPH_PT_panel_1"
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
        
class MOUNTAIN_GRAPH_PT_panel_5(MOUNTAIN_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "MOUNTAIN_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlemg = layout.row()
        rowtitlemg.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontmg_title")

        rowsubtitlemg = layout.row()
        rowsubtitlemg.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontmg_subtitle")
        
        rowvaluemg = layout.row()
        rowvaluemg.label(text= "Bar Value Font:")
        layout.prop(mytool, "my_pathfontmg_barvalue")

        rowvaluemg = layout.row()
        rowvaluemg.label(text= "Bar Text Font:")
        layout.prop(mytool, "my_pathfontmg_bartext")
        
        rowlegendmg = layout.row()
        rowlegendmg.label(text= "Range Numbers Font:")
        layout.prop(mytool, "my_pathfontmg_rangenumbers")                
        layout.operator("addonname.myop_operatormgfont")
        
        rowresetmg = layout.row()
        rowresetmg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatormgresfont")
        
class COMPARISON_MOUNTAIN_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class COMPARISON_MOUNTAIN_GRAPH_PT_panel_1(COMPARISON_MOUNTAIN_GRAPH_panel, bpy.types.Panel):
    bl_idname = "COMPARISON_MOUNTAIN_GRAPH_PT_panel_1"
    bl_label = "Mountain Graph Comparison"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowMGCFPS = layout.row()
        rowMGCFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumMGC")  

class COMPARISON_MOUNTAIN_GRAPH_PT_panel_2(COMPARISON_MOUNTAIN_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_MOUNTAIN_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowMGCcsv = layout.row()
        rowMGCcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathmgc")
        layout.operator("mesh.mycubeoperatormgccsv")
        
class COMPARISON_MOUNTAIN_GRAPH_PT_panel_3(COMPARISON_MOUNTAIN_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_MOUNTAIN_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringmountain_graph_comparison")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatormgcsql")

class COMPARISON_MOUNTAIN_GRAPH_PT_panel_4(COMPARISON_MOUNTAIN_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_MOUNTAIN_GRAPH_PT_panel_1"
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
        
class COMPARISON_MOUNTAIN_GRAPH_PT_panel_5(COMPARISON_MOUNTAIN_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_MOUNTAIN_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlemgc = layout.row()
        rowtitlemgc.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontmgc_title")

        rowsubtitlemgc = layout.row()
        rowsubtitlemgc.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontmgc_subtitle")
        
        rowvaluemgc = layout.row()
        rowvaluemgc.label(text= "Bar Value Font:")
        layout.prop(mytool, "my_pathfontmgc_barvalue")

        rowvaluemgc = layout.row()
        rowvaluemgc.label(text= "Bar Text Font:")
        layout.prop(mytool, "my_pathfontmgc_bartext")
        
        rowlegendmgc = layout.row()
        rowlegendmgc.label(text= "Range Numbers Font:")
        layout.prop(mytool, "my_pathfontmgc_rangenumbers")
        
        rowlegendmgc = layout.row()
        rowlegendmgc.label(text= "Legend Font:")
        layout.prop(mytool, "my_pathfontmgc_legend")                 
        layout.operator("addonname.myop_operatormgcfont")
        
        rowresetmgc = layout.row()
        rowresetmgc.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatormgcresfont")
        
class US_MAP_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class US_MAP_PT_panel_1(US_MAP_panel, bpy.types.Panel):
    bl_idname = "US_MAP_PT_panel_1"
    bl_label = "US Map"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowusmFPS = layout.row()
        rowusmFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enum_usmap")

class US_MAP_PT_panel_2(US_MAP_panel, bpy.types.Panel):
    bl_parent_id = "US_MAP_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowusmcsv = layout.row()
        rowusmcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathusmap")
        layout.operator("mesh.mycubeoperatorusmapcsv")
        
class US_MAP_PT_panel_3(US_MAP_panel, bpy.types.Panel):
    bl_parent_id = "US_MAP_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowusmsql = layout.row()
        rowusmsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringusmap")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorusmapsql")

class US_MAP_PT_panel_4(US_MAP_panel, bpy.types.Panel):
    bl_parent_id = "US_MAP_PT_panel_1"
    bl_label = "Note"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowcandlea1 = layout.row()
        rowcandlea1.label(text= "Duration Control is not applied")
        
        rowcandlea2 = layout.row()
        rowcandlea2.label(text= "for this map,")
        
        rowcandlea3 = layout.row()
        rowcandlea3.label(text= "as its tedious to control")
        
        rowcandlea4 = layout.row()
        rowcandlea4.label(text= "50+ data points individually.")

        rowcandlea5 = layout.row()
        rowcandlea5.label(text= "There is a tutorial in the help")
        
        rowcandlea6 = layout.row()
        rowcandlea6.label(text= "folder on how to increase duration")
        
        rowcandlea7 = layout.row()
        rowcandlea7.label(text= "in an easy way.")
        
class US_MAP_PT_panel_5(US_MAP_panel, bpy.types.Panel):
    bl_parent_id = "US_MAP_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitleusmap = layout.row()
        rowtitleusmap.label(text= "Title Font: (also Credit and Source Title)")
        layout.prop(mytool, "my_pathfontusmap_title")

        rowsubtitleusmap = layout.row()
        rowsubtitleusmap.label(text= "Subtitle Font: (Credit and Source Subtitle)")
        layout.prop(mytool, "my_pathfontusmap_subtitle")
        layout.operator("addonname.myop_operatorusmapfont")
        
        rowresetusmap = layout.row()
        rowresetusmap.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatorusmapresfont")
        
class VERTICAL_BAR_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class VERTICAL_BAR_GRAPH_PT_panel_1(VERTICAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_idname = "VERTICAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Vertical Bar Graph"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowVBFPS = layout.row()
        rowVBFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumVB") 

class VERTICAL_BAR_GRAPH_PT_panel_2(VERTICAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "VERTICAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowVBcsv = layout.row()
        rowVBcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathvb")
        layout.operator("mesh.mycubeoperatorvbcsv")
        
class VERTICAL_BAR_GRAPH_PT_panel_3(VERTICAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "VERTICAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringvertical_bar_graph")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorvbgsql")

class VERTICAL_BAR_GRAPH_PT_panel_4(VERTICAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "VERTICAL_BAR_GRAPH_PT_panel_1"
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
 
class VERTICAL_BAR_GRAPH_PT_panel_5(VERTICAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "VERTICAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlevbg = layout.row()
        rowtitlevbg.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontvbg_title")

        rowsubtitlevbg = layout.row()
        rowsubtitlevbg.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontvbg_subtitle")
        
        rowvaluevbg = layout.row()
        rowvaluevbg.label(text= "Bar Value Font:")
        layout.prop(mytool, "my_pathfontvbg_barvalue")

        rowvaluevbg = layout.row()
        rowvaluevbg.label(text= "Bar Text Font:")
        layout.prop(mytool, "my_pathfontvbg_bartext")
        
        rowlegendvbg = layout.row()
        rowlegendvbg.label(text= "Range Numbers Font:")
        layout.prop(mytool, "my_pathfontvbg_rangenumbers")
        
        rowlegendvbg = layout.row()
        rowlegendvbg.label(text= "Text Total Font:")
        layout.prop(mytool, "my_pathfontvbg_texttotal")

        rowlegendvbg = layout.row()
        rowlegendvbg.label(text= "Value Total Font:")
        layout.prop(mytool, "my_pathfontvbg_valuetotal")                  
        layout.operator("addonname.myop_operatorvbgfont")
        
        rowresetvbg = layout.row()
        rowresetvbg.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatorvbgresfont")

        
class COMPARISON_VERTICAL_BAR_GRAPH_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Renaissance'
    bl_options = {"DEFAULT_CLOSED"}

class COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_1(COMPARISON_VERTICAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_idname = "COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Vertical Bar Graph Comparison"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowVBCFPS = layout.row()
        rowVBCFPS.label(text= "Frames per second:")
        layout.prop(mytool, "my_enumVBC") 

class COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_2(COMPARISON_VERTICAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Import CSV"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        rowVBCcsv = layout.row()
        rowVBCcsv.label(text= "Link to csv file")
        layout.prop(mytool, "my_pathvbc")
        layout.operator("mesh.mycubeoperatorvbccsv")
        
class COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_3(COMPARISON_VERTICAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Import MySQL Data"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowCGsql = layout.row()
        rowCGsql.label(text= "DATABASE name:")
        layout.prop(mytool, "my_stringvertical_bar_graph_comparison")
        
        layout.label(text="Import data from MySQL database:")
        layout.operator("mesh.mycubeoperatorvbgcsql")

class COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_4(COMPARISON_VERTICAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_1"
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
        
class COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_5(COMPARISON_VERTICAL_BAR_GRAPH_panel, bpy.types.Panel):
    bl_parent_id = "COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_1"
    bl_label = "Font"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        rowtitlevbgc = layout.row()
        rowtitlevbgc.label(text= "Title Font:")
        layout.prop(mytool, "my_pathfontvbgc_title")

        rowsubtitlevbgc = layout.row()
        rowsubtitlevbgc.label(text= "Subtitle Font:")
        layout.prop(mytool, "my_pathfontvbgc_subtitle")
        
        rowvalueavbgc = layout.row()
        rowvalueavbgc.label(text= "Bar Value A Font:")
        layout.prop(mytool, "my_pathfontvbgc_barvaluea")
        
        rowvaluebvbgc = layout.row()
        rowvaluebvbgc.label(text= "Bar Value B Font:")
        layout.prop(mytool, "my_pathfontvbgc_barvalueb")

        rowvaluevbgc = layout.row()
        rowvaluevbgc.label(text= "Bar Text Font:")
        layout.prop(mytool, "my_pathfontvbgc_bartext")
        
        rowlegendvbgc = layout.row()
        rowlegendvbgc.label(text= "Range Numbers Font:")
        layout.prop(mytool, "my_pathfontvbgc_rangenumbers")
        
        rowlegendvbgc = layout.row()
        rowlegendvbgc.label(text= "Legend Font:")
        layout.prop(mytool, "my_pathfontvbgc_legend")                 
        layout.operator("addonname.myop_operatorvbgcfont")
        
        rowresetvbgc = layout.row()
        rowresetvbgc.label(text= "Reset all Fonts:")
        layout.operator("addonname.myop_operatorvbgcresfont")
        
class MyoperatorCGsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorcgsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringcirclegraph
        )
            
        mycursor = mydb.cursor()

        mycursor.execute("SELECT `Max Value` FROM circlegtable")
        maxvalue = mycursor.fetchone()
        my_float_maxvalue = float(maxvalue[0])

        mycursor.execute("SELECT `Min Value` FROM circlegtable")
        minvalue = mycursor.fetchone()
        my_float_minvalue = float(minvalue[0])

        mycursor.execute("SELECT `Value` FROM circlegtable")
        value = mycursor.fetchone()
        my_float_value = float(value[0])
        my_float_percentage = my_float_value/my_float_maxvalue

        mycursor.execute("SELECT `TITLE (in caps)` FROM circlegtable")
        my_string_title = mycursor.fetchone()
        my_string_title = str(my_string_title)
        my_string_title = my_string_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM circlegtable")
        my_string_subtitle = mycursor.fetchone()
        my_string_subtitle = str(my_string_subtitle)
        my_string_subtitle = my_string_subtitle.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Text description` FROM circlegtable")
        my_string_description = mycursor.fetchone()
        my_string_description = str(my_string_description)
        my_string_description = my_string_description.strip("(").strip(")").strip(",").strip("'")
            
            # Ensure an object is selected
        if bpy.context.selected_objects:
            selected_obj = bpy.context.active_object  # Get the active (selected) object

            if selected_obj.type == 'MESH':
                mesh_name = selected_obj.name

                # Check if the selected object has modifiers
                if selected_obj.modifiers:
                    modifier_name = selected_obj.modifiers.active.name  # Get the name of the active modifier



                    selected_obj.modifiers[modifier_name]["Input_11"] = my_float_maxvalue
                    selected_obj.modifiers[modifier_name]["Input_10"] = my_float_minvalue
                    selected_obj.modifiers[modifier_name]["Input_2"] = my_float_percentage
                    selected_obj.modifiers[modifier_name]["Input_22"] = str(my_string_title)
                    selected_obj.modifiers[modifier_name]["Input_23"] = str(my_string_subtitle)
                    selected_obj.modifiers[modifier_name]["Input_16"] = str(my_string_description)
        

                    print(f"Set modifier input for object '{mesh_name}' and modifier '{modifier_name}'.")
                else:
                    print(f"Selected object '{mesh_name}' has no modifiers.")
            else:
                print("Selected object is not a mesh.")
        else:
            print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}

class MyoperatorPGsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorpgsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringpiegraph
        )
            
        mycursor = mydb.cursor()

        mycursor.execute("SELECT `Max Value` FROM piegtable")
        maxvalue = mycursor.fetchone()
        my_floatpie_maxvalue = float(maxvalue[0])

        mycursor.execute("SELECT `Min Value` FROM piegtable")
        minvalue = mycursor.fetchone()
        my_floatpie_minvalue = float(minvalue[0])

        mycursor.execute("SELECT `Value` FROM piegtable")
        value = mycursor.fetchone()
        my_floatpie_value = float(value[0])
        my_floatpie_percentage = my_floatpie_value/my_floatpie_maxvalue

        mycursor.execute("SELECT `TITLE (in caps)` FROM piegtable")
        my_stringpie_title = mycursor.fetchone()
        my_stringpie_title = str(my_stringpie_title)
        my_stringpie_title = my_stringpie_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM piegtable")
        my_stringpie_subtitle = mycursor.fetchone()
        my_stringpie_subtitle = str(my_stringpie_subtitle)
        my_stringpie_subtitle = my_stringpie_subtitle.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Text description` FROM piegtable")
        my_stringpie_description = mycursor.fetchone()
        my_stringpie_description = str(my_stringpie_description)
        my_stringpie_description = my_stringpie_description.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_pg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_pg.type == 'MESH':
                        mesh_name_pg = selected_obj_pg.name

                        # Check if the selected object has modifiers
                        if selected_obj_pg.modifiers:
                                modifier_name_pg = selected_obj_pg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_pg.modifiers[modifier_name_pg]["Input_11"] = my_floatpie_maxvalue
                                selected_obj_pg.modifiers[modifier_name_pg]["Input_10"] = my_floatpie_minvalue
                                selected_obj_pg.modifiers[modifier_name_pg]["Input_2"] = my_floatpie_percentage
                                selected_obj_pg.modifiers[modifier_name_pg]["Input_15"] = str(my_stringpie_title)
                                selected_obj_pg.modifiers[modifier_name_pg]["Input_17"] = str(my_stringpie_subtitle)
                                selected_obj_pg.modifiers[modifier_name_pg]["Input_19"] = str(my_stringpie_description)

                                print(f"Set modifier input for object '{mesh_name_pg}' and modifier '{modifier_name_pg}'.")
                        else:
                                print(f"Selected object '{mesh_name_pg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}


    
class Myoperator23CGsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorcg23sql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringcircle23_graph
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of Graphs` FROM circle23gtable")
        numberofgraphs23cg = mycursor.fetchone()
        my_float23cg_numberofgraphs = int(numberofgraphs23cg[0])
        
        mycursor.execute("SELECT `Wheel Text` FROM circle23gtable")
        my_string23cg_wheeltext = mycursor.fetchall()
        my_string23cg_wheeltext1 = str(my_string23cg_wheeltext[0])
        my_string23cg_wheeltext2 = str(my_string23cg_wheeltext[1])
        my_string23cg_wheeltext3 = str(my_string23cg_wheeltext[2])
        my_string23cg_wheeltext1 = my_string23cg_wheeltext1.strip("(").strip(")").strip(",").strip("'")
        my_string23cg_wheeltext2 = my_string23cg_wheeltext2.strip("(").strip(")").strip(",").strip("'")
        my_string23cg_wheeltext3 = my_string23cg_wheeltext3.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Max Value` FROM circle23gtable")
        maxvalue = mycursor.fetchone()
        my_float23cg_maxvalue = float(maxvalue[0])

        mycursor.execute("SELECT `Value` FROM circle23gtable")
        value23cg = mycursor.fetchall()
        value23cg1, value23cg2, value23cg3 = value23cg
        value23cg1 = str(value23cg1)
        value23cg2 = str(value23cg2)
        value23cg3 = str(value23cg3)        
        value23cg1 = value23cg1.strip("(").strip(")").strip(",").strip("'")
        value23cg1 = float(value23cg1)
        value23cg2 = value23cg2.strip("(").strip(")").strip(",").strip("'")
        value23cg2 = float(value23cg2)
        value23cg3 = value23cg3.strip("(").strip(")").strip(",").strip("'")
        value23cg3 = float(value23cg3)
        my_float23cg_value1 = value23cg1/my_float23cg_maxvalue
        my_float23cg_value2 = value23cg2/my_float23cg_maxvalue
        my_float23cg_value3 = value23cg3/my_float23cg_maxvalue

        mycursor.execute("SELECT `Min Value` FROM circle23gtable")
        minvalue = mycursor.fetchone()
        my_float23cg_minvalue = float(minvalue[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM circle23gtable")
        my_string23cg_title = mycursor.fetchone()
        my_string23cg_title = str(my_string23cg_title)
        my_string23cg_title = my_string23cg_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM circle23gtable")
        my_string23cg_subtitle = mycursor.fetchone()
        my_string23cg_subtitle = str(my_string23cg_subtitle)
        my_string23cg_subtitle = my_string23cg_subtitle.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Text description` FROM circle23gtable")
        my_string23cg_textdescription = mycursor.fetchone()
        my_string23cg_textdescription = str(my_string23cg_textdescription)
        my_string23cg_textdescription = my_string23cg_textdescription.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_23cg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_23cg.type == 'MESH':
                        mesh_name_23cg = selected_obj_23cg.name

                        # Check if the selected object has modifiers
                        if selected_obj_23cg.modifiers:
                                modifier_name_23cg = selected_obj_23cg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_31"] = my_float23cg_numberofgraphs
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_39"] = my_string23cg_wheeltext1
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_40"] = my_string23cg_wheeltext2
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_38"] = my_string23cg_wheeltext3
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_2"] = my_float23cg_value1
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_41"] = my_float23cg_value2
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_42"] = my_float23cg_value3
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_10"] = my_float23cg_minvalue
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_11"] = my_float23cg_maxvalue
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_22"] = my_string23cg_title
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_23"] = my_string23cg_subtitle
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_16"] = my_string23cg_textdescription

                                print(f"Set modifier input for object '{mesh_name_23cg}' and modifier '{modifier_name_23cg}'.")
                        else:
                                print(f"Selected object '{mesh_name_23cg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}

    
class Myoperatorcandlesql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorcandlesql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        candle_object = bpy.context.view_layer.objects.active
        candle_object_name = candle_object.name
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringcandlestick_graph
        )
            
        mycursor = mydb.cursor(buffered=True)
        
        mycursor.execute("SELECT `Number of Points` FROM candlestickgtable")
        numberofpointscandleg = mycursor.fetchone()
        my_floatcandleg_numberofpoints = int(numberofpointscandleg[0])

        mycursor.execute("SELECT `Point High` FROM candlestickgtable")
        pointhighvaluecandleg = mycursor.fetchall()
        # Convert the fetched data to a list of floats in one line
        pointhighvaluecandleg = [float(str(point).strip("(), '")) for point in pointhighvaluecandleg]

        mycursor.execute("SELECT `Point Open` FROM candlestickgtable")
        pointopenvaluecandleg = mycursor.fetchall()
        # Convert the fetched data to a list of floats in one line
        pointopenvaluecandleg = [float(str(point).strip("(), '")) for point in pointopenvaluecandleg]

        mycursor.execute("SELECT `Point Close` FROM candlestickgtable")
        pointclosevaluecandleg = mycursor.fetchall()
        # Convert the fetched data to a list of floats in one line
        pointclosevaluecandleg = [float(str(point).strip("(), '")) for point in pointclosevaluecandleg]

        mycursor.execute("SELECT `Point Low` FROM candlestickgtable")
        pointlowvaluecandleg = mycursor.fetchall()
        # Convert the fetched data to a list of floats in one line
        pointlowvaluecandleg = [float(str(point).strip("(), '")) for point in pointlowvaluecandleg]

        mycursor.execute("SELECT `Point Text` FROM candlestickgtable")
        my_stringcandleg_pointtext = mycursor.fetchall()
        pointtext_list = [str(item).strip("(").strip(")").strip(",").strip("'") for item in my_stringcandleg_pointtext]

        mycursor.execute("SELECT `Min Value` FROM candlestickgtable")
        minpointvalue = mycursor.fetchone()
        my_floatcandleg_minpointvalue = float(minpointvalue[0])
        
        mycursor.execute("SELECT `Max Value` FROM candlestickgtable")
        maxpointvalue = mycursor.fetchone()
        my_floatcandleg_maxpointvalue = float(maxpointvalue[0])

        mycursor.execute("SELECT `Decimals` FROM candlestickgtable")
        decvalue = mycursor.fetchone()
        my_floatcandleg_decvalue = int(decvalue[0])

        mycursor.execute("SELECT `Range Numbers` FROM candlestickgtable")
        rangenumber = mycursor.fetchone()
        my_floatcandleg_rangenumber = int(rangenumber[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM candlestickgtable")
        my_stringcandleg_title = mycursor.fetchone()
        my_stringcandleg_title = str(my_stringcandleg_title)
        my_stringcandleg_title = my_stringcandleg_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM candlestickgtable")
        my_stringcandleg_subtitle = mycursor.fetchone()
        my_stringcandleg_subtitle = str(my_stringcandleg_subtitle)
        my_stringcandleg_subtitle = my_stringcandleg_subtitle.strip("(").strip(")").strip(",").strip("'")
            
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_3"] = my_floatcandleg_numberofpoints
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_12"] = my_floatcandleg_minpointvalue
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_13"] = my_floatcandleg_maxpointvalue
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_14"] = my_floatcandleg_decvalue
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_15"] = my_floatcandleg_rangenumber


        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_4"] = pointtext_list[0]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_5"] = pointtext_list[1]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_6"] = pointtext_list[2]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_7"] = pointtext_list[3]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_8"] = pointtext_list[4]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_9"] = pointtext_list[5]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_10"] = pointtext_list[6]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_11"] = pointtext_list[7]
        
        cube_objecttextcandle = bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]
        for i in range(8, 32):
            input_index = i - 8 + 71
            input_name = f"Input_{input_index:02d}"
            cube_objecttextcandle[input_name] = pointtext_list[i]
        
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_38"] = pointhighvaluecandleg[0]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_103"] = pointhighvaluecandleg[1] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_107"] = pointhighvaluecandleg[2]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_168"] = pointhighvaluecandleg[3] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_172"] = pointhighvaluecandleg[4]          
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_176"] = pointhighvaluecandleg[5]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_99"] = pointhighvaluecandleg[6]
        for i in range(7, 32):
            input_numpointhighvaluecandleg = 180 + (i - 7) * 4
            bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_" + str(input_numpointhighvaluecandleg)] = pointhighvaluecandleg[i]  
            
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_97"] = pointopenvaluecandleg[0]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_104"] = pointopenvaluecandleg[1] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_108"] = pointopenvaluecandleg[2]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_169"] = pointopenvaluecandleg[3] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_173"] = pointopenvaluecandleg[4]          
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_177"] = pointopenvaluecandleg[5]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_100"] = pointopenvaluecandleg[6]
        for i in range(7, 32):
            input_numpointopenvaluecandleg = 181 + (i - 7) * 4
            bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_" + str(input_numpointopenvaluecandleg)] = pointopenvaluecandleg[i]
            
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_98"] = pointclosevaluecandleg[0]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_105"] = pointclosevaluecandleg[1] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_109"] = pointclosevaluecandleg[2]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_170"] = pointclosevaluecandleg[3] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_174"] = pointclosevaluecandleg[4]          
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_178"] = pointclosevaluecandleg[5]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_101"] = pointclosevaluecandleg[6]
        for i in range(7, 32):
            input_numpointclosevaluecandleg = 182 + (i - 7) * 4
            bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_" + str(input_numpointclosevaluecandleg)] = pointclosevaluecandleg[i]
            
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_96"] = pointlowvaluecandleg[0]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_106"] = pointlowvaluecandleg[1] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_110"] = pointlowvaluecandleg[2]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_171"] = pointlowvaluecandleg[3] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_175"] = pointlowvaluecandleg[4]          
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_179"] = pointlowvaluecandleg[5]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_102"] = pointlowvaluecandleg[6]
        for i in range(7, 32):
            input_numpointlowvaluecandleg = 183 + (i - 7) * 4
            bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_" + str(input_numpointlowvaluecandleg)] = pointlowvaluecandleg[i]    


        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_23"] = my_stringcandleg_title
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_22"] = my_stringcandleg_subtitle
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class Myoperator23PGsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorpg23sql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringpie23_graph
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of Graphs` FROM pie23gtable")
        numberofgraphs23pg = mycursor.fetchone()
        my_float23pg_numberofgraphs = int(numberofgraphs23pg[0])
        
        mycursor.execute("SELECT `Wheel Text` FROM pie23gtable")
        my_string23pg_wheeltext = mycursor.fetchall()
        my_string23pg_wheeltext1 = str(my_string23pg_wheeltext[0])
        my_string23pg_wheeltext2 = str(my_string23pg_wheeltext[1])
        my_string23pg_wheeltext3 = str(my_string23pg_wheeltext[2])
        my_string23pg_wheeltext1 = my_string23pg_wheeltext1.strip("(").strip(")").strip(",").strip("'")
        my_string23pg_wheeltext2 = my_string23pg_wheeltext2.strip("(").strip(")").strip(",").strip("'")
        my_string23pg_wheeltext3 = my_string23pg_wheeltext3.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Max Value` FROM pie23gtable")
        maxvalue = mycursor.fetchone()
        my_float23pg_maxvalue = float(maxvalue[0])

        mycursor.execute("SELECT `Value` FROM pie23gtable")
        value23pg = mycursor.fetchall()
        value23pg1, value23pg2, value23pg3 = value23pg
        value23pg1 = str(value23pg1)
        value23pg2 = str(value23pg2)
        value23pg3 = str(value23pg3)        
        value23pg1 = value23pg1.strip("(").strip(")").strip(",").strip("'")
        value23pg1 = float(value23pg1)
        value23pg2 = value23pg2.strip("(").strip(")").strip(",").strip("'")
        value23pg2 = float(value23pg2)
        value23pg3 = value23pg3.strip("(").strip(")").strip(",").strip("'")
        value23pg3 = float(value23pg3)
        my_float23pg_value1 = value23pg1/my_float23pg_maxvalue
        my_float23pg_value2 = value23pg2/my_float23pg_maxvalue
        my_float23pg_value3 = value23pg3/my_float23pg_maxvalue

        mycursor.execute("SELECT `Min Value` FROM pie23gtable")
        minvalue = mycursor.fetchone()
        my_float23pg_minvalue = float(minvalue[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM pie23gtable")
        my_string23pg_title = mycursor.fetchone()
        my_string23pg_title = str(my_string23pg_title)
        my_string23pg_title = my_string23pg_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM pie23gtable")
        my_string23pg_subtitle = mycursor.fetchone()
        my_string23pg_subtitle = str(my_string23pg_subtitle)
        my_string23pg_subtitle = my_string23pg_subtitle.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Text description` FROM pie23gtable")
        my_string23pg_textdescription = mycursor.fetchone()
        my_string23pg_textdescription = str(my_string23pg_textdescription)
        my_string23pg_textdescription = my_string23pg_textdescription.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_23pg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_23pg.type == 'MESH':
                        mesh_name_23pg = selected_obj_23pg.name

                        # Check if the selected object has modifiers
                        if selected_obj_23pg.modifiers:
                                modifier_name_23pg = selected_obj_23pg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_26"] = my_float23pg_numberofgraphs
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_31"] = my_string23pg_wheeltext1
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_32"] = my_string23pg_wheeltext2
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_33"] = my_string23pg_wheeltext3
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_2"] = my_float23pg_value1
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_27"] = my_float23pg_value2
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_28"] = my_float23pg_value3
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_10"] = my_float23pg_minvalue
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_11"] = my_float23pg_maxvalue
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_15"] = my_string23pg_title
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_17"] = my_string23pg_subtitle
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_19"] = my_string23pg_textdescription

                                print(f"Set modifier input for object '{mesh_name_23pg}' and modifier '{modifier_name_23pg}'.")
                        else:
                                print(f"Selected object '{mesh_name_23pg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}

    
class MyoperatorHBGsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorhbgsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringhorizontal_bar_graph
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of bars (1-10)` FROM horizontal_bargtable")
        numberofbarshbg = mycursor.fetchone()
        my_floathbg_numberofbars = int(numberofbarshbg[0])
        
        mycursor.execute("SELECT `Bar Text` FROM horizontal_bargtable")
        my_stringhbg_bartext = mycursor.fetchall()
        my_stringhbg_bartext1 = str(my_stringhbg_bartext[0])
        my_stringhbg_bartext2 = str(my_stringhbg_bartext[1])
        my_stringhbg_bartext3 = str(my_stringhbg_bartext[2])
        my_stringhbg_bartext4 = str(my_stringhbg_bartext[3])
        my_stringhbg_bartext5 = str(my_stringhbg_bartext[4])
        my_stringhbg_bartext6 = str(my_stringhbg_bartext[5])
        my_stringhbg_bartext7 = str(my_stringhbg_bartext[6])
        my_stringhbg_bartext8 = str(my_stringhbg_bartext[7])
        my_stringhbg_bartext9 = str(my_stringhbg_bartext[8])
        my_stringhbg_bartext10 = str(my_stringhbg_bartext[9])
        my_stringhbg_bartext1 = my_stringhbg_bartext1.strip("(").strip(")").strip(",").strip("'")
        my_stringhbg_bartext2 = my_stringhbg_bartext2.strip("(").strip(")").strip(",").strip("'")
        my_stringhbg_bartext3 = my_stringhbg_bartext3.strip("(").strip(")").strip(",").strip("'")
        my_stringhbg_bartext4 = my_stringhbg_bartext4.strip("(").strip(")").strip(",").strip("'")
        my_stringhbg_bartext5 = my_stringhbg_bartext5.strip("(").strip(")").strip(",").strip("'")
        my_stringhbg_bartext6 = my_stringhbg_bartext6.strip("(").strip(")").strip(",").strip("'")
        my_stringhbg_bartext7 = my_stringhbg_bartext7.strip("(").strip(")").strip(",").strip("'")
        my_stringhbg_bartext8 = my_stringhbg_bartext8.strip("(").strip(")").strip(",").strip("'")
        my_stringhbg_bartext9 = my_stringhbg_bartext9.strip("(").strip(")").strip(",").strip("'")
        my_stringhbg_bartext10 = my_stringhbg_bartext10.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Max Value` FROM horizontal_bargtable")
        maxvalue = mycursor.fetchone()
        my_floathbg_maxvalue = float(maxvalue[0])

        mycursor.execute("SELECT `Bar Value` FROM horizontal_bargtable")
        valuehbg = mycursor.fetchall()
        valuehbg1, valuehbg2, valuehbg3, valuehbg4, valuehbg5, valuehbg6, valuehbg7, valuehbg8, valuehbg9, valuehbg10 = valuehbg
        valuehbg1 = str(valuehbg1)
        valuehbg2 = str(valuehbg2)
        valuehbg3 = str(valuehbg3)
        valuehbg4 = str(valuehbg4)    
        valuehbg5 = str(valuehbg5)
        valuehbg6 = str(valuehbg6)
        valuehbg7 = str(valuehbg7)
        valuehbg8 = str(valuehbg8)
        valuehbg9 = str(valuehbg9)
        valuehbg10 = str(valuehbg10)         
        valuehbg1 = valuehbg1.strip("(").strip(")").strip(",").strip("'")
        valuehbg1 = float(valuehbg1)
        valuehbg2 = valuehbg2.strip("(").strip(")").strip(",").strip("'")
        valuehbg2 = float(valuehbg2)
        valuehbg3 = valuehbg3.strip("(").strip(")").strip(",").strip("'")
        valuehbg3 = float(valuehbg3)
        valuehbg4 = valuehbg4.strip("(").strip(")").strip(",").strip("'")
        valuehbg4 = float(valuehbg4)
        valuehbg5 = valuehbg5.strip("(").strip(")").strip(",").strip("'")
        valuehbg5 = float(valuehbg5)
        valuehbg6 = valuehbg6.strip("(").strip(")").strip(",").strip("'")
        valuehbg6 = float(valuehbg6)
        valuehbg7 = valuehbg7.strip("(").strip(")").strip(",").strip("'")
        valuehbg7 = float(valuehbg7)
        valuehbg8 = valuehbg8.strip("(").strip(")").strip(",").strip("'")
        valuehbg8 = float(valuehbg8)
        valuehbg9 = valuehbg9.strip("(").strip(")").strip(",").strip("'")
        valuehbg9 = float(valuehbg9)
        valuehbg10 = valuehbg10.strip("(").strip(")").strip(",").strip("'")
        valuehbg10 = float(valuehbg10)


        mycursor.execute("SELECT `Min Value` FROM horizontal_bargtable")
        minvalue = mycursor.fetchone()
        my_floathbg_minvalue = float(minvalue[0])

        mycursor.execute("SELECT `Decimals` FROM horizontal_bargtable")
        decvalue = mycursor.fetchone()
        my_floathbg_decvalue = float(decvalue[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM horizontal_bargtable")
        my_stringhbg_title = mycursor.fetchone()
        my_stringhbg_title = str(my_stringhbg_title)
        my_stringhbg_title = my_stringhbg_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM horizontal_bargtable")
        my_stringhbg_subtitle = mycursor.fetchone()
        my_stringhbg_subtitle = str(my_stringhbg_subtitle)
        my_stringhbg_subtitle = my_stringhbg_subtitle.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Text for total` FROM horizontal_bargtable")
        my_stringhbg_textfortotal = mycursor.fetchone()
        my_stringhbg_textfortotal = str(my_stringhbg_textfortotal)
        my_stringhbg_textfortotal = my_stringhbg_textfortotal.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_hbg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_hbg.type == 'MESH':
                        mesh_name_hbg = selected_obj_hbg.name

                        # Check if the selected object has modifiers
                        if selected_obj_hbg.modifiers:
                                modifier_name_hbg = selected_obj_hbg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_36"] = my_floathbg_numberofbars
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_2"] = my_stringhbg_bartext1
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_3"] = my_stringhbg_bartext2
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_4"] = my_stringhbg_bartext3
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_5"] = my_stringhbg_bartext4
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_10"] = my_stringhbg_bartext5
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_11"] = my_stringhbg_bartext6
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_12"] = my_stringhbg_bartext7
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_13"] = my_stringhbg_bartext8
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_14"] = my_stringhbg_bartext9
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_15"] = my_stringhbg_bartext10
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_14"] = valuehbg1
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_15"] = valuehbg2
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_16"] = valuehbg3
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_17"] = valuehbg4
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_16"] = valuehbg5
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_17"] = valuehbg6
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_18"] = valuehbg7
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_19"] = valuehbg8
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_20"] = valuehbg9
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_21"] = valuehbg10
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_10"] = my_floathbg_minvalue
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_11"] = my_floathbg_maxvalue
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_7"] = my_stringhbg_title
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_8"] = my_stringhbg_subtitle
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_6"] = my_stringhbg_textfortotal

                                print(f"Set modifier input for object '{mesh_name_hbg}' and modifier '{modifier_name_hbg}'.")
                        else:
                                print(f"Selected object '{mesh_name_hbg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}

    
class MyoperatorHBGCsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorhbgcsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringhorizontal_bar_graph_comparison
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of bars (1-9)` FROM horizontal_bar_comparison_gtable")
        numberofbarshbgc = mycursor.fetchone()
        my_floathbgc_numberofbars = int(numberofbarshbgc[0])
        
        mycursor.execute("SELECT `Bar Text` FROM horizontal_bar_comparison_gtable")
        my_stringhbgc_bartext = mycursor.fetchall()
        my_stringhbgc_bartext1 = str(my_stringhbgc_bartext[0])
        my_stringhbgc_bartext2 = str(my_stringhbgc_bartext[1])
        my_stringhbgc_bartext3 = str(my_stringhbgc_bartext[2])
        my_stringhbgc_bartext4 = str(my_stringhbgc_bartext[3])
        my_stringhbgc_bartext5 = str(my_stringhbgc_bartext[4])
        my_stringhbgc_bartext6 = str(my_stringhbgc_bartext[5])
        my_stringhbgc_bartext7 = str(my_stringhbgc_bartext[6])
        my_stringhbgc_bartext8 = str(my_stringhbgc_bartext[7])
        my_stringhbgc_bartext9 = str(my_stringhbgc_bartext[8])
        my_stringhbgc_bartext1 = my_stringhbgc_bartext1.strip("(").strip(")").strip(",").strip("'")
        my_stringhbgc_bartext2 = my_stringhbgc_bartext2.strip("(").strip(")").strip(",").strip("'")
        my_stringhbgc_bartext3 = my_stringhbgc_bartext3.strip("(").strip(")").strip(",").strip("'")
        my_stringhbgc_bartext4 = my_stringhbgc_bartext4.strip("(").strip(")").strip(",").strip("'")
        my_stringhbgc_bartext5 = my_stringhbgc_bartext5.strip("(").strip(")").strip(",").strip("'")
        my_stringhbgc_bartext6 = my_stringhbgc_bartext6.strip("(").strip(")").strip(",").strip("'")
        my_stringhbgc_bartext7 = my_stringhbgc_bartext7.strip("(").strip(")").strip(",").strip("'")
        my_stringhbgc_bartext8 = my_stringhbgc_bartext8.strip("(").strip(")").strip(",").strip("'")
        my_stringhbgc_bartext9 = my_stringhbgc_bartext9.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Max Value` FROM horizontal_bar_comparison_gtable")
        maxvalue = mycursor.fetchone()
        my_floathbgc_maxvalue = float(maxvalue[0])

        mycursor.execute("SELECT `Bar Value A` FROM horizontal_bar_comparison_gtable")
        valueahbgc = mycursor.fetchall()
        valueahbgc1, valueahbgc2, valueahbgc3, valueahbgc4, valueahbgc5, valueahbgc6, valueahbgc7, valueahbgc8, valueahbgc9  = valueahbgc
        valueahbgc1 = str(valueahbgc1)
        valueahbgc2 = str(valueahbgc2)
        valueahbgc3 = str(valueahbgc3)
        valueahbgc4 = str(valueahbgc4)
        valueahbgc5 = str(valueahbgc5)
        valueahbgc6 = str(valueahbgc6)
        valueahbgc7 = str(valueahbgc7)
        valueahbgc8 = str(valueahbgc8)  
        valueahbgc9 = str(valueahbgc9)         
        valueahbgc1 = valueahbgc1.strip("(").strip(")").strip(",").strip("'")
        valueahbgc1 = float(valueahbgc1)
        valueahbgc2 = valueahbgc2.strip("(").strip(")").strip(",").strip("'")
        valueahbgc2 = float(valueahbgc2)
        valueahbgc3 = valueahbgc3.strip("(").strip(")").strip(",").strip("'")
        valueahbgc3 = float(valueahbgc3)
        valueahbgc4 = valueahbgc4.strip("(").strip(")").strip(",").strip("'")
        valueahbgc4 = float(valueahbgc4)
        valueahbgc5 = valueahbgc5.strip("(").strip(")").strip(",").strip("'")
        valueahbgc5 = float(valueahbgc5)
        valueahbgc6 = valueahbgc6.strip("(").strip(")").strip(",").strip("'")
        valueahbgc6 = float(valueahbgc6)
        valueahbgc7 = valueahbgc7.strip("(").strip(")").strip(",").strip("'")
        valueahbgc7 = float(valueahbgc7)
        valueahbgc8 = valueahbgc8.strip("(").strip(")").strip(",").strip("'")
        valueahbgc8 = float(valueahbgc8)
        valueahbgc9 = valueahbgc9.strip("(").strip(")").strip(",").strip("'")
        valueahbgc9 = float(valueahbgc9)

        mycursor.execute("SELECT `Bar Value B` FROM horizontal_bar_comparison_gtable")
        valuebhbgc = mycursor.fetchall()
        valuebhbgc1, valuebhbgc2, valuebhbgc3, valuebhbgc4, valuebhbgc5, valuebhbgc6, valuebhbgc7, valuebhbgc8, valuebhbgc9 = valuebhbgc
        valuebhbgc1 = str(valuebhbgc1)
        valuebhbgc2 = str(valuebhbgc2)
        valuebhbgc3 = str(valuebhbgc3)
        valuebhbgc4 = str(valuebhbgc4)  
        valuebhbgc5 = str(valuebhbgc5)
        valuebhbgc6 = str(valuebhbgc6)
        valuebhbgc7 = str(valuebhbgc7)
        valuebhbgc8 = str(valuebhbgc8) 
        valuebhbgc9 = str(valuebhbgc9)        
        valuebhbgc1 = valuebhbgc1.strip("(").strip(")").strip(",").strip("'")
        valuebhbgc1 = float(valuebhbgc1)
        valuebhbgc2 = valuebhbgc2.strip("(").strip(")").strip(",").strip("'")
        valuebhbgc2 = float(valuebhbgc2)
        valuebhbgc3 = valuebhbgc3.strip("(").strip(")").strip(",").strip("'")
        valuebhbgc3 = float(valuebhbgc3)
        valuebhbgc4 = valuebhbgc4.strip("(").strip(")").strip(",").strip("'")
        valuebhbgc4 = float(valuebhbgc4)
        valuebhbgc5 = valuebhbgc5.strip("(").strip(")").strip(",").strip("'")
        valuebhbgc5 = float(valuebhbgc5)
        valuebhbgc6 = valuebhbgc6.strip("(").strip(")").strip(",").strip("'")
        valuebhbgc6 = float(valuebhbgc6)
        valuebhbgc7 = valuebhbgc7.strip("(").strip(")").strip(",").strip("'")
        valuebhbgc7 = float(valuebhbgc7)
        valuebhbgc8 = valuebhbgc8.strip("(").strip(")").strip(",").strip("'")
        valuebhbgc8 = float(valuebhbgc8)
        valuebhbgc9 = valuebhbgc9.strip("(").strip(")").strip(",").strip("'")
        valuebhbgc9 = float(valuebhbgc9)

        mycursor.execute("SELECT `Min Value` FROM horizontal_bar_comparison_gtable")
        minvalue = mycursor.fetchone()
        my_floathbgc_minvalue = float(minvalue[0])

        mycursor.execute("SELECT `Decimals` FROM horizontal_bar_comparison_gtable")
        decvalue = mycursor.fetchone()
        my_floathbgc_decvalue = int(decvalue[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM horizontal_bar_comparison_gtable")
        my_stringhbgc_title = mycursor.fetchone()
        my_stringhbgc_title = str(my_stringhbgc_title)
        my_stringhbgc_title = my_stringhbgc_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM horizontal_bar_comparison_gtable")
        my_stringhbgc_subtitle = mycursor.fetchone()
        my_stringhbgc_subtitle = str(my_stringhbgc_subtitle)
        my_stringhbgc_subtitle = my_stringhbgc_subtitle.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Legend Text` FROM horizontal_bar_comparison_gtable")
        my_stringhbgc_legendtext = mycursor.fetchall()
        my_stringhbgc_legendtext1 = str(my_stringhbgc_legendtext[0])
        my_stringhbgc_legendtext2 = str(my_stringhbgc_legendtext[1])
        my_stringhbgc_legendtext1 = my_stringhbgc_legendtext1.strip("(").strip(")").strip(",").strip("'")
        my_stringhbgc_legendtext2 = my_stringhbgc_legendtext2.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_hbgc = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_hbgc.type == 'MESH':
                        mesh_name_hbgc = selected_obj_hbgc.name

                        # Check if the selected object has modifiers
                        if selected_obj_hbgc.modifiers:
                                modifier_name_hbgc = selected_obj_hbgc.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_45"] = my_floathbgc_numberofbars
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_2"] = my_stringhbgc_bartext1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_3"] = my_stringhbgc_bartext2
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_4"] = my_stringhbgc_bartext3
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_5"] = my_stringhbgc_bartext4
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_66"] = my_stringhbgc_bartext5
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_67"] = my_stringhbgc_bartext6
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_68"] = my_stringhbgc_bartext7
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_69"] = my_stringhbgc_bartext8
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_70"] = my_stringhbgc_bartext9
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_14"] = valueahbgc1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_15"] = valueahbgc2
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_16"] = valueahbgc3
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_17"] = valueahbgc4
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_71"] = valueahbgc5
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_73"] = valueahbgc6
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_75"] = valueahbgc7
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_77"] = valueahbgc8
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_79"] = valueahbgc9
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_36"] = valuebhbgc1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_37"] = valuebhbgc2
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_38"] = valuebhbgc3
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_39"] = valuebhbgc4
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_72"] = valuebhbgc5
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_74"] = valuebhbgc6
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_76"] = valuebhbgc7
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_78"] = valuebhbgc8
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_80"] = valuebhbgc9
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_10"] = my_floathbgc_minvalue
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_11"] = my_floathbgc_maxvalue
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_12"] = my_floathbgc_decvalue
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_7"] = my_stringhbgc_title
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_8"] = my_stringhbgc_subtitle
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_6"] = my_stringhbgc_legendtext1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_40"] = my_stringhbgc_legendtext2

                                print(f"Set modifier input for object '{mesh_name_hbgc}' and modifier '{modifier_name_hbgc}'.")
                        else:
                                print(f"Selected object '{mesh_name_hbgc}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}

class MyoperatorMCGsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatormcgsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringmultiple_circle_graph
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of sliders (1-8)` FROM multiple_circlegtable")
        numberofslidersmcg = mycursor.fetchone()
        my_floatmcg_numberofsliders = int(numberofslidersmcg[0])
        
        mycursor.execute("SELECT `Bar Text` FROM multiple_circlegtable")
        my_stringmcg_bartext = mycursor.fetchall()
        my_stringmcg_bartext1 = str(my_stringmcg_bartext[0])
        my_stringmcg_bartext2 = str(my_stringmcg_bartext[1])
        my_stringmcg_bartext3 = str(my_stringmcg_bartext[2])
        my_stringmcg_bartext4 = str(my_stringmcg_bartext[3])
        my_stringmcg_bartext5 = str(my_stringmcg_bartext[4])
        my_stringmcg_bartext6 = str(my_stringmcg_bartext[5])
        my_stringmcg_bartext7 = str(my_stringmcg_bartext[6])
        my_stringmcg_bartext8 = str(my_stringmcg_bartext[7])
        my_stringmcg_bartext1 = my_stringmcg_bartext1.strip("(").strip(")").strip(",").strip("'")
        my_stringmcg_bartext2 = my_stringmcg_bartext2.strip("(").strip(")").strip(",").strip("'")
        my_stringmcg_bartext3 = my_stringmcg_bartext3.strip("(").strip(")").strip(",").strip("'")
        my_stringmcg_bartext4 = my_stringmcg_bartext4.strip("(").strip(")").strip(",").strip("'")
        my_stringmcg_bartext5 = my_stringmcg_bartext5.strip("(").strip(")").strip(",").strip("'")
        my_stringmcg_bartext6 = my_stringmcg_bartext6.strip("(").strip(")").strip(",").strip("'")
        my_stringmcg_bartext7 = my_stringmcg_bartext7.strip("(").strip(")").strip(",").strip("'")
        my_stringmcg_bartext8 = my_stringmcg_bartext8.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Max Value` FROM multiple_circlegtable")
        maxbarvalue = mycursor.fetchone()
        my_floatmcg_maxbarvalue = float(maxbarvalue[0])

        mycursor.execute("SELECT `Bar Value` FROM multiple_circlegtable")
        barvaluemcg = mycursor.fetchall()
        barvaluemcg1, barvaluemcg2, barvaluemcg3, barvaluemcg4, barvaluemcg5, barvaluemcg6, barvaluemcg7, barvaluemcg8 = barvaluemcg
        barvaluemcg1 = str(barvaluemcg1)
        barvaluemcg2 = str(barvaluemcg2)
        barvaluemcg3 = str(barvaluemcg3)
        barvaluemcg4 = str(barvaluemcg4)
        barvaluemcg5 = str(barvaluemcg5)
        barvaluemcg6 = str(barvaluemcg6)
        barvaluemcg7 = str(barvaluemcg7)
        barvaluemcg8 = str(barvaluemcg8)            
        barvaluemcg1 = barvaluemcg1.strip("(").strip(")").strip(",").strip("'")
        barvaluemcg1 = float(barvaluemcg1)
        barvaluemcg2 = barvaluemcg2.strip("(").strip(")").strip(",").strip("'")
        barvaluemcg2 = float(barvaluemcg2)
        barvaluemcg3 = barvaluemcg3.strip("(").strip(")").strip(",").strip("'")
        barvaluemcg3 = float(barvaluemcg3)
        barvaluemcg4 = barvaluemcg4.strip("(").strip(")").strip(",").strip("'")
        barvaluemcg4 = float(barvaluemcg4)
        barvaluemcg5 = barvaluemcg5.strip("(").strip(")").strip(",").strip("'")
        barvaluemcg5 = float(barvaluemcg5)
        barvaluemcg6 = barvaluemcg6.strip("(").strip(")").strip(",").strip("'")
        barvaluemcg6 = float(barvaluemcg6)
        barvaluemcg7 = barvaluemcg7.strip("(").strip(")").strip(",").strip("'")
        barvaluemcg7 = float(barvaluemcg7)
        barvaluemcg8 = barvaluemcg8.strip("(").strip(")").strip(",").strip("'")
        barvaluemcg8 = float(barvaluemcg8)
        my_floatmcg_barvalue1 = barvaluemcg1/my_floatmcg_maxbarvalue
        my_floatmcg_barvalue2 = barvaluemcg2/my_floatmcg_maxbarvalue
        my_floatmcg_barvalue3 = barvaluemcg3/my_floatmcg_maxbarvalue
        my_floatmcg_barvalue4 = barvaluemcg4/my_floatmcg_maxbarvalue
        my_floatmcg_barvalue5 = barvaluemcg5/my_floatmcg_maxbarvalue
        my_floatmcg_barvalue6 = barvaluemcg6/my_floatmcg_maxbarvalue
        my_floatmcg_barvalue7 = barvaluemcg7/my_floatmcg_maxbarvalue
        my_floatmcg_barvalue8 = barvaluemcg8/my_floatmcg_maxbarvalue

        mycursor.execute("SELECT `Min Value` FROM multiple_circlegtable")
        minbarvalue = mycursor.fetchone()
        my_floatmcg_minbarvalue = float(minbarvalue[0])

        mycursor.execute("SELECT `Decimals` FROM multiple_circlegtable")
        decvalue = mycursor.fetchone()
        my_floatmcg_decvalue = int(decvalue[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM multiple_circlegtable")
        my_stringmcg_title = mycursor.fetchone()
        my_stringmcg_title = str(my_stringmcg_title)
        my_stringmcg_title = my_stringmcg_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM multiple_circlegtable")
        my_stringmcg_subtitle = mycursor.fetchone()
        my_stringmcg_subtitle = str(my_stringmcg_subtitle)
        my_stringmcg_subtitle = my_stringmcg_subtitle.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_mcg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_mcg.type == 'MESH':
                        mesh_name_mcg = selected_obj_mcg.name

                        # Check if the selected object has modifiers
                        if selected_obj_mcg.modifiers:
                                modifier_name_mcg = selected_obj_mcg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_55"] = my_floatmcg_numberofsliders
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_42"] = my_stringmcg_bartext1
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_43"] = my_stringmcg_bartext2
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_44"] = my_stringmcg_bartext3
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_46"] = my_stringmcg_bartext4
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_45"] = my_stringmcg_bartext5
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_13"] = my_stringmcg_bartext6
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_18"] = my_stringmcg_bartext7
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_23"] = my_stringmcg_bartext8
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_2"] = my_floatmcg_barvalue1
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_12"] = my_floatmcg_barvalue2
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_14"] = my_floatmcg_barvalue3
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_15"] = my_floatmcg_barvalue4
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_16"] = my_floatmcg_barvalue5
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_7"] = my_floatmcg_barvalue6
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_8"] = my_floatmcg_barvalue7
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_9"] = my_floatmcg_barvalue8
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_10"] = my_floatmcg_minbarvalue
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_11"] = my_floatmcg_maxbarvalue
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_18"] = my_floatmcg_decvalue
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_40"] = my_stringmcg_title
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_41"] = my_stringmcg_subtitle

                                print(f"Set modifier input for object '{mesh_name_mcg}' and modifier '{modifier_name_mcg}'.")
                        else:
                                print(f"Selected object '{mesh_name_mcg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}
       
class MyoperatorMPGsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatormpgsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringmultiple_pie_graph
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of sliders (1-8)` FROM multiple_piegtable")
        numberofslidersmpg = mycursor.fetchone()
        my_floatmpg_numberofsliders = int(numberofslidersmpg[0])
        
        mycursor.execute("SELECT `Bar Text` FROM multiple_piegtable")
        my_stringmpg_bartext = mycursor.fetchall()
        my_stringmpg_bartext1 = str(my_stringmpg_bartext[0])
        my_stringmpg_bartext2 = str(my_stringmpg_bartext[1])
        my_stringmpg_bartext3 = str(my_stringmpg_bartext[2])
        my_stringmpg_bartext4 = str(my_stringmpg_bartext[3])
        my_stringmpg_bartext5 = str(my_stringmpg_bartext[4])
        my_stringmpg_bartext6 = str(my_stringmpg_bartext[5])
        my_stringmpg_bartext7 = str(my_stringmpg_bartext[6])
        my_stringmpg_bartext8 = str(my_stringmpg_bartext[7])
        my_stringmpg_bartext1 = my_stringmpg_bartext1.strip("(").strip(")").strip(",").strip("'")
        my_stringmpg_bartext2 = my_stringmpg_bartext2.strip("(").strip(")").strip(",").strip("'")
        my_stringmpg_bartext3 = my_stringmpg_bartext3.strip("(").strip(")").strip(",").strip("'")
        my_stringmpg_bartext4 = my_stringmpg_bartext4.strip("(").strip(")").strip(",").strip("'")
        my_stringmpg_bartext5 = my_stringmpg_bartext5.strip("(").strip(")").strip(",").strip("'")
        my_stringmpg_bartext6 = my_stringmpg_bartext6.strip("(").strip(")").strip(",").strip("'")
        my_stringmpg_bartext7 = my_stringmpg_bartext7.strip("(").strip(")").strip(",").strip("'")
        my_stringmpg_bartext8 = my_stringmpg_bartext8.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Max Value` FROM multiple_piegtable")
        maxbarvalue = mycursor.fetchone()
        my_floatmpg_maxbarvalue = float(maxbarvalue[0])

        mycursor.execute("SELECT `Bar Value` FROM multiple_piegtable")
        barvaluempg = mycursor.fetchall()
        barvaluempg1, barvaluempg2, barvaluempg3, barvaluempg4, barvaluempg5, barvaluempg6, barvaluempg7, barvaluempg8 = barvaluempg
        barvaluempg1 = str(barvaluempg1)
        barvaluempg2 = str(barvaluempg2)
        barvaluempg3 = str(barvaluempg3)
        barvaluempg4 = str(barvaluempg4)
        barvaluempg5 = str(barvaluempg5)   
        barvaluempg6 = str(barvaluempg6)  
        barvaluempg7 = str(barvaluempg7) 
        barvaluempg8 = str(barvaluempg8)      
        barvaluempg1 = barvaluempg1.strip("(").strip(")").strip(",").strip("'")
        barvaluempg1 = float(barvaluempg1)
        barvaluempg2 = barvaluempg2.strip("(").strip(")").strip(",").strip("'")
        barvaluempg2 = float(barvaluempg2)
        barvaluempg3 = barvaluempg3.strip("(").strip(")").strip(",").strip("'")
        barvaluempg3 = float(barvaluempg3)
        barvaluempg4 = barvaluempg4.strip("(").strip(")").strip(",").strip("'")
        barvaluempg4 = float(barvaluempg4)
        barvaluempg5 = barvaluempg5.strip("(").strip(")").strip(",").strip("'")
        barvaluempg5 = float(barvaluempg5)
        barvaluempg6 = barvaluempg6.strip("(").strip(")").strip(",").strip("'")
        barvaluempg6 = float(barvaluempg6)
        barvaluempg7 = barvaluempg7.strip("(").strip(")").strip(",").strip("'")
        barvaluempg7 = float(barvaluempg7)
        barvaluempg8 = barvaluempg8.strip("(").strip(")").strip(",").strip("'")
        barvaluempg8 = float(barvaluempg8)
        my_floatmpg_barvalue1 = barvaluempg1/my_floatmpg_maxbarvalue
        my_floatmpg_barvalue2 = barvaluempg2/my_floatmpg_maxbarvalue
        my_floatmpg_barvalue3 = barvaluempg3/my_floatmpg_maxbarvalue
        my_floatmpg_barvalue4 = barvaluempg4/my_floatmpg_maxbarvalue
        my_floatmpg_barvalue5 = barvaluempg5/my_floatmpg_maxbarvalue
        my_floatmpg_barvalue6 = barvaluempg6/my_floatmpg_maxbarvalue
        my_floatmpg_barvalue7 = barvaluempg7/my_floatmpg_maxbarvalue
        my_floatmpg_barvalue8 = barvaluempg8/my_floatmpg_maxbarvalue

        mycursor.execute("SELECT `Min Value` FROM multiple_piegtable")
        minbarvalue = mycursor.fetchone()
        my_floatmpg_minbarvalue = float(minbarvalue[0])

        mycursor.execute("SELECT `Decimals` FROM multiple_piegtable")
        decvalue = mycursor.fetchone()
        my_floatmpg_decvalue = int(decvalue[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM multiple_piegtable")
        my_stringmpg_title = mycursor.fetchone()
        my_stringmpg_title = str(my_stringmpg_title)
        my_stringmpg_title = my_stringmpg_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM multiple_piegtable")
        my_stringmpg_subtitle = mycursor.fetchone()
        my_stringmpg_subtitle = str(my_stringmpg_subtitle)
        my_stringmpg_subtitle = my_stringmpg_subtitle.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_mpg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_mpg.type == 'MESH':
                        mesh_name_mpg = selected_obj_mpg.name

                        # Check if the selected object has modifiers
                        if selected_obj_mpg.modifiers:
                                modifier_name_mpg = selected_obj_mpg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_54"] = my_floatmpg_numberofsliders
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_42"] = my_stringmpg_bartext1
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_43"] = my_stringmpg_bartext2
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_44"] = my_stringmpg_bartext3
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_46"] = my_stringmpg_bartext4
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_45"] = my_stringmpg_bartext5
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_88"] = my_stringmpg_bartext6
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Socket_4"] = my_stringmpg_bartext7
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Socket_9"] = my_stringmpg_bartext8
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_2"] = my_floatmpg_barvalue1
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_12"] = my_floatmpg_barvalue2
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_14"] = my_floatmpg_barvalue3
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_15"] = my_floatmpg_barvalue4
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_16"] = my_floatmpg_barvalue5
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_93"] = my_floatmpg_barvalue6
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Socket_0"] = my_floatmpg_barvalue7
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Socket_1"] = my_floatmpg_barvalue8
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_10"] = my_floatmpg_minbarvalue
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_11"] = my_floatmpg_maxbarvalue
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_18"] = my_floatmpg_decvalue
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_40"] = my_stringmpg_title
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_41"] = my_stringmpg_subtitle

                                print(f"Set modifier input for object '{mesh_name_mpg}' and modifier '{modifier_name_mpg}'.")
                        else:
                                print(f"Selected object '{mesh_name_mpg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class MyoperatorLGsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorlgsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringline_graph
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of points (1-30)` FROM linegtable")
        numberofpointslg = mycursor.fetchone()
        my_floatlg_numberofpoints = int(numberofpointslg[0])

        mycursor.execute("SELECT `Value` FROM linegtable")
        pointvaluelg = mycursor.fetchall()
        pointvaluelg1, pointvaluelg2, pointvaluelg3, pointvaluelg4, pointvaluelg5, pointvaluelg6, pointvaluelg7, pointvaluelg8, pointvaluelg9, pointvaluelg10, pointvaluelg11, pointvaluelg12, pointvaluelg13, pointvaluelg14, pointvaluelg15, pointvaluelg16, pointvaluelg17, pointvaluelg18, pointvaluelg19, pointvaluelg20, pointvaluelg21, pointvaluelg22, pointvaluelg23, pointvaluelg24, pointvaluelg25, pointvaluelg26, pointvaluelg27, pointvaluelg28, pointvaluelg29, pointvaluelg30 = pointvaluelg
        pointvaluelg1 = str(pointvaluelg1)
        pointvaluelg2 = str(pointvaluelg2)
        pointvaluelg3 = str(pointvaluelg3)
        pointvaluelg4 = str(pointvaluelg4)
        pointvaluelg5 = str(pointvaluelg5)
        pointvaluelg6 = str(pointvaluelg6)
        pointvaluelg7 = str(pointvaluelg7)
        pointvaluelg8 = str(pointvaluelg8) 
        pointvaluelg1 = str(pointvaluelg1)
        pointvaluelg2 = str(pointvaluelg2)
        pointvaluelg3 = str(pointvaluelg3)
        pointvaluelg4 = str(pointvaluelg4)
        pointvaluelg5 = str(pointvaluelg5)
        pointvaluelg6 = str(pointvaluelg6)
        pointvaluelg7 = str(pointvaluelg7)
        pointvaluelg8 = str(pointvaluelg8)
        pointvaluelg9 = str(pointvaluelg9)
        pointvaluelg10 = str(pointvaluelg10)
        pointvaluelg11 = str(pointvaluelg11)
        pointvaluelg12 = str(pointvaluelg12)
        pointvaluelg13 = str(pointvaluelg13)
        pointvaluelg14 = str(pointvaluelg14)
        pointvaluelg15 = str(pointvaluelg15)
        pointvaluelg16 = str(pointvaluelg16)
        pointvaluelg17 = str(pointvaluelg17)
        pointvaluelg18 = str(pointvaluelg18)
        pointvaluelg19 = str(pointvaluelg19)
        pointvaluelg20 = str(pointvaluelg20)
        pointvaluelg21 = str(pointvaluelg21)
        pointvaluelg22 = str(pointvaluelg22)
        pointvaluelg23 = str(pointvaluelg23)
        pointvaluelg24 = str(pointvaluelg24)
        pointvaluelg25 = str(pointvaluelg25)
        pointvaluelg26 = str(pointvaluelg26)
        pointvaluelg27 = str(pointvaluelg27)
        pointvaluelg28 = str(pointvaluelg28)
        pointvaluelg29 = str(pointvaluelg29)
        pointvaluelg30 = str(pointvaluelg30)         
        pointvaluelg1 = pointvaluelg1.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg1 = float(pointvaluelg1)
        pointvaluelg2 = pointvaluelg2.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg2 = float(pointvaluelg2)
        pointvaluelg3 = pointvaluelg3.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg3 = float(pointvaluelg3)
        pointvaluelg4 = pointvaluelg4.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg4 = float(pointvaluelg4)
        pointvaluelg5 = pointvaluelg5.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg5 = float(pointvaluelg5)
        pointvaluelg6 = pointvaluelg6.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg6 = float(pointvaluelg6)
        pointvaluelg7 = pointvaluelg7.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg7 = float(pointvaluelg7)
        pointvaluelg8 = pointvaluelg8.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg8 = float(pointvaluelg8)
        pointvaluelg9 = pointvaluelg9.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg9 = float(pointvaluelg9)

        pointvaluelg10 = pointvaluelg10.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg10 = float(pointvaluelg10)

        pointvaluelg11 = pointvaluelg11.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg11 = float(pointvaluelg11)

        pointvaluelg12 = pointvaluelg12.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg12 = float(pointvaluelg12)

        pointvaluelg13 = pointvaluelg13.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg13 = float(pointvaluelg13)

        pointvaluelg14 = pointvaluelg14.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg14 = float(pointvaluelg14)

        pointvaluelg15 = pointvaluelg15.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg15 = float(pointvaluelg15)

        pointvaluelg16 = pointvaluelg16.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg16 = float(pointvaluelg16)

        pointvaluelg17 = pointvaluelg17.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg17 = float(pointvaluelg17)

        pointvaluelg18 = pointvaluelg18.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg18 = float(pointvaluelg18)

        pointvaluelg19 = pointvaluelg19.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg19 = float(pointvaluelg19)

        pointvaluelg20 = pointvaluelg20.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg20 = float(pointvaluelg20)

        pointvaluelg21 = pointvaluelg21.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg21 = float(pointvaluelg21)

        pointvaluelg22 = pointvaluelg22.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg22 = float(pointvaluelg22)

        pointvaluelg23 = pointvaluelg23.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg23 = float(pointvaluelg23)

        pointvaluelg24 = pointvaluelg24.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg24 = float(pointvaluelg24)

        pointvaluelg25 = pointvaluelg25.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg25 = float(pointvaluelg25)

        pointvaluelg26 = pointvaluelg26.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg26 = float(pointvaluelg26)

        pointvaluelg27 = pointvaluelg27.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg27 = float(pointvaluelg27)

        pointvaluelg28 = pointvaluelg28.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg28 = float(pointvaluelg28)

        pointvaluelg29 = pointvaluelg29.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg29 = float(pointvaluelg29)

        pointvaluelg30 = pointvaluelg30.strip("(").strip(")").strip(",").strip("'")
        pointvaluelg30 = float(pointvaluelg30)

        mycursor.execute("SELECT `Point Text` FROM linegtable")
        my_stringlg_pointtext = mycursor.fetchall()
        my_stringlg_pointtext1 = str(my_stringlg_pointtext[0])
        my_stringlg_pointtext2 = str(my_stringlg_pointtext[1])
        my_stringlg_pointtext3 = str(my_stringlg_pointtext[2])
        my_stringlg_pointtext4 = str(my_stringlg_pointtext[3])
        my_stringlg_pointtext5 = str(my_stringlg_pointtext[4])
        my_stringlg_pointtext6 = str(my_stringlg_pointtext[5])
        my_stringlg_pointtext7 = str(my_stringlg_pointtext[6])
        my_stringlg_pointtext8 = str(my_stringlg_pointtext[7])
        my_stringlg_pointtext9 = str(my_stringlg_pointtext[8])
        my_stringlg_pointtext10 = str(my_stringlg_pointtext[9])
        my_stringlg_pointtext11 = str(my_stringlg_pointtext[10])
        my_stringlg_pointtext12 = str(my_stringlg_pointtext[11])
        my_stringlg_pointtext13 = str(my_stringlg_pointtext[12])
        my_stringlg_pointtext14 = str(my_stringlg_pointtext[13])
        my_stringlg_pointtext15 = str(my_stringlg_pointtext[14])
        my_stringlg_pointtext16 = str(my_stringlg_pointtext[15])
        my_stringlg_pointtext17 = str(my_stringlg_pointtext[16])
        my_stringlg_pointtext18 = str(my_stringlg_pointtext[17])
        my_stringlg_pointtext19 = str(my_stringlg_pointtext[18])
        my_stringlg_pointtext20 = str(my_stringlg_pointtext[19])
        my_stringlg_pointtext21 = str(my_stringlg_pointtext[20])
        my_stringlg_pointtext22 = str(my_stringlg_pointtext[21])
        my_stringlg_pointtext23 = str(my_stringlg_pointtext[22])
        my_stringlg_pointtext24 = str(my_stringlg_pointtext[23])
        my_stringlg_pointtext25 = str(my_stringlg_pointtext[24])
        my_stringlg_pointtext26 = str(my_stringlg_pointtext[25])
        my_stringlg_pointtext27 = str(my_stringlg_pointtext[26])
        my_stringlg_pointtext28 = str(my_stringlg_pointtext[27])
        my_stringlg_pointtext29 = str(my_stringlg_pointtext[28])
        my_stringlg_pointtext30 = str(my_stringlg_pointtext[29])
        my_stringlg_pointtext1 = my_stringlg_pointtext1.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext2 = my_stringlg_pointtext2.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext3 = my_stringlg_pointtext3.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext4 = my_stringlg_pointtext4.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext5 = my_stringlg_pointtext5.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext6 = my_stringlg_pointtext6.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext7 = my_stringlg_pointtext7.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext8 = my_stringlg_pointtext8.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext9 = my_stringlg_pointtext9.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext10 = my_stringlg_pointtext10.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext11 = my_stringlg_pointtext11.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext12 = my_stringlg_pointtext12.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext13 = my_stringlg_pointtext13.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext14 = my_stringlg_pointtext14.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext15 = my_stringlg_pointtext15.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext16 = my_stringlg_pointtext16.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext17 = my_stringlg_pointtext17.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext18 = my_stringlg_pointtext18.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext19 = my_stringlg_pointtext19.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext20 = my_stringlg_pointtext20.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext21 = my_stringlg_pointtext21.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext22 = my_stringlg_pointtext22.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext23 = my_stringlg_pointtext23.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext24 = my_stringlg_pointtext24.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext25 = my_stringlg_pointtext25.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext26 = my_stringlg_pointtext26.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext27 = my_stringlg_pointtext27.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext28 = my_stringlg_pointtext28.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext29 = my_stringlg_pointtext29.strip("(").strip(")").strip(",").strip("'")
        my_stringlg_pointtext30 = my_stringlg_pointtext30.strip("(").strip(")").strip(",").strip("'")


        mycursor.execute("SELECT `Min Value` FROM linegtable")
        minpointvalue = mycursor.fetchone()
        my_floatlg_minpointvalue = float(minpointvalue[0])
        
        mycursor.execute("SELECT `Max Value` FROM linegtable")
        maxpointvalue = mycursor.fetchone()
        my_floatlg_maxpointvalue = float(maxpointvalue[0])

        mycursor.execute("SELECT `Decimals` FROM linegtable")
        decvalue = mycursor.fetchone()
        my_floatlg_decvalue = int(decvalue[0])

        mycursor.execute("SELECT `Range Numbers` FROM linegtable")
        rangenumber = mycursor.fetchone()
        my_floatlg_rangenumber = int(rangenumber[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM linegtable")
        my_stringlg_title = mycursor.fetchone()
        my_stringlg_title = str(my_stringlg_title)
        my_stringlg_title = my_stringlg_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM linegtable")
        my_stringlg_subtitle = mycursor.fetchone()
        my_stringlg_subtitle = str(my_stringlg_subtitle)
        my_stringlg_subtitle = my_stringlg_subtitle.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj = bpy.context.active_object  # Get the active (selected) object

                if selected_obj.type == 'MESH':
                        mesh_name = selected_obj.name

                        # Check if the selected object has modifiers
                        if selected_obj.modifiers:
                                if len(selected_obj.modifiers) >= 2:  # Ensure at least two modifiers exist
                                        modifier_0 = selected_obj.modifiers.get("GeometryNodes")
                                        modifier_1 = selected_obj.modifiers.get("GeometryNodes.001")

                                if modifier_0 and modifier_1:
                                        modifier_0["Input_2"] = my_floatlg_numberofpoints
                                        modifier_0["Input_13"] = my_floatlg_minpointvalue
                                        modifier_0["Input_14"] = my_floatlg_maxpointvalue
                                        modifier_0["Input_15"] = my_floatlg_decvalue
                                        modifier_0["Input_18"] = my_floatlg_rangenumber
                                        modifier_0["Input_4"] = pointvaluelg1
                                        modifier_0["Input_5"] = pointvaluelg2
                                        modifier_0["Input_6"] = pointvaluelg3
                                        modifier_0["Input_7"] = pointvaluelg4
                                        modifier_0["Input_8"] = pointvaluelg5
                                        modifier_0["Input_9"] = pointvaluelg6
                                        modifier_0["Input_10"] = pointvaluelg7
                                        modifier_0["Input_11"] = pointvaluelg8
                                        modifier_0["Socket_0"] = pointvaluelg9
                                        modifier_0["Socket_1"] = pointvaluelg10
                                        modifier_0["Socket_2"] = pointvaluelg11
                                        modifier_0["Socket_3"] = pointvaluelg12
                                        modifier_0["Socket_4"] = pointvaluelg13
                                        modifier_0["Socket_5"] = pointvaluelg14
                                        modifier_0["Socket_6"] = pointvaluelg15
                                        modifier_0["Socket_7"] = pointvaluelg16
                                        modifier_0["Socket_8"] = pointvaluelg17
                                        modifier_0["Socket_9"] = pointvaluelg18
                                        modifier_0["Socket_10"] = pointvaluelg19
                                        modifier_0["Socket_11"] = pointvaluelg20
                                        modifier_0["Socket_12"] = pointvaluelg21
                                        modifier_0["Socket_13"] = pointvaluelg22
                                        modifier_0["Socket_14"] = pointvaluelg23
                                        modifier_0["Socket_15"] = pointvaluelg24
                                        modifier_0["Socket_16"] = pointvaluelg25
                                        modifier_0["Socket_17"] = pointvaluelg26
                                        modifier_0["Socket_18"] = pointvaluelg27
                                        modifier_0["Socket_19"] = pointvaluelg28
                                        modifier_0["Socket_20"] = pointvaluelg29
                                        modifier_0["Socket_21"] = pointvaluelg30

                                        modifier_1["Input_4"] = my_stringlg_pointtext1
                                        modifier_1["Input_5"] = my_stringlg_pointtext2
                                        modifier_1["Input_6"] = my_stringlg_pointtext3
                                        modifier_1["Input_7"] = my_stringlg_pointtext4
                                        modifier_1["Input_8"] = my_stringlg_pointtext5
                                        modifier_1["Input_9"] = my_stringlg_pointtext6
                                        modifier_1["Input_10"] = my_stringlg_pointtext7
                                        modifier_1["Input_11"] = my_stringlg_pointtext8
                                        modifier_1["Socket_0"] = my_stringlg_pointtext9
                                        modifier_1["Socket_1"] = my_stringlg_pointtext10
                                        modifier_1["Socket_2"] = my_stringlg_pointtext11
                                        modifier_1["Socket_3"] = my_stringlg_pointtext12
                                        modifier_1["Socket_4"] = my_stringlg_pointtext13
                                        modifier_1["Socket_5"] = my_stringlg_pointtext14
                                        modifier_1["Socket_6"] = my_stringlg_pointtext15
                                        modifier_1["Socket_7"] = my_stringlg_pointtext16
                                        modifier_1["Socket_8"] = my_stringlg_pointtext17
                                        modifier_1["Socket_9"] = my_stringlg_pointtext18
                                        modifier_1["Socket_10"] = my_stringlg_pointtext19
                                        modifier_1["Socket_11"] = my_stringlg_pointtext20
                                        modifier_1["Socket_12"] = my_stringlg_pointtext21
                                        modifier_1["Socket_13"] = my_stringlg_pointtext22
                                        modifier_1["Socket_14"] = my_stringlg_pointtext23
                                        modifier_1["Socket_15"] = my_stringlg_pointtext24
                                        modifier_1["Socket_16"] = my_stringlg_pointtext25
                                        modifier_1["Socket_17"] = my_stringlg_pointtext26
                                        modifier_1["Socket_18"] = my_stringlg_pointtext27
                                        modifier_1["Socket_19"] = my_stringlg_pointtext28
                                        modifier_1["Socket_20"] = my_stringlg_pointtext29
                                        modifier_1["Socket_21"] = my_stringlg_pointtext30
                                        modifier_1["Input_23"] = my_stringlg_title
                                        modifier_1["Input_22"] = my_stringlg_subtitle

                                        print(f"Set modifier input for object '{mesh_name}'.")
                                else:
                                        print("Selected object does not have both modifiers.")
                        else:
                                print(f"Selected object '{mesh_name}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")

        # Optionally, you can update the mesh data if needed.
        bpy.context.object.data.update()
        return {'FINISHED'}

    
class MyoperatorLGCsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorlgcsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringline_graph_comparison
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of points (1-8)` FROM linegcomparison_table")
        numberofpointslgc = mycursor.fetchone()
        my_floatlgc_numberofpoints = int(numberofpointslgc[0])

        mycursor.execute("SELECT `Point Text` FROM linegcomparison_table")
        my_stringlgc_pointtext = mycursor.fetchall()
        my_stringlgc_pointtext1 = str(my_stringlgc_pointtext[0])
        my_stringlgc_pointtext2 = str(my_stringlgc_pointtext[1])
        my_stringlgc_pointtext3 = str(my_stringlgc_pointtext[2])
        my_stringlgc_pointtext4 = str(my_stringlgc_pointtext[3])
        my_stringlgc_pointtext5 = str(my_stringlgc_pointtext[4])
        my_stringlgc_pointtext6 = str(my_stringlgc_pointtext[5])
        my_stringlgc_pointtext7 = str(my_stringlgc_pointtext[6])
        my_stringlgc_pointtext8 = str(my_stringlgc_pointtext[7])
        my_stringlgc_pointtext1 = my_stringlgc_pointtext1.strip("(").strip(")").strip(",").strip("'")
        my_stringlgc_pointtext2 = my_stringlgc_pointtext2.strip("(").strip(")").strip(",").strip("'")
        my_stringlgc_pointtext3 = my_stringlgc_pointtext3.strip("(").strip(")").strip(",").strip("'")
        my_stringlgc_pointtext4 = my_stringlgc_pointtext4.strip("(").strip(")").strip(",").strip("'")
        my_stringlgc_pointtext5 = my_stringlgc_pointtext5.strip("(").strip(")").strip(",").strip("'")
        my_stringlgc_pointtext6 = my_stringlgc_pointtext6.strip("(").strip(")").strip(",").strip("'")
        my_stringlgc_pointtext7 = my_stringlgc_pointtext7.strip("(").strip(")").strip(",").strip("'")
        my_stringlgc_pointtext8 = my_stringlgc_pointtext8.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Value A` FROM linegcomparison_table")
        pointvaluealgc = mycursor.fetchall()
        pointvaluealgc1, pointvaluealgc2, pointvaluealgc3, pointvaluealgc4, pointvaluealgc5, pointvaluealgc6, pointvaluealgc7, pointvaluealgc8 = pointvaluealgc
        pointvaluealgc1 = str(pointvaluealgc1)
        pointvaluealgc2 = str(pointvaluealgc2)
        pointvaluealgc3 = str(pointvaluealgc3)
        pointvaluealgc4 = str(pointvaluealgc4)
        pointvaluealgc5 = str(pointvaluealgc5)
        pointvaluealgc6 = str(pointvaluealgc6)
        pointvaluealgc7 = str(pointvaluealgc7)
        pointvaluealgc8 = str(pointvaluealgc8)          
        pointvaluealgc1 = pointvaluealgc1.strip("(").strip(")").strip(",").strip("'")
        pointvaluealgc1 = float(pointvaluealgc1)
        pointvaluealgc2 = pointvaluealgc2.strip("(").strip(")").strip(",").strip("'")
        pointvaluealgc2 = float(pointvaluealgc2)
        pointvaluealgc3 = pointvaluealgc3.strip("(").strip(")").strip(",").strip("'")
        pointvaluealgc3 = float(pointvaluealgc3)
        pointvaluealgc4 = pointvaluealgc4.strip("(").strip(")").strip(",").strip("'")
        pointvaluealgc4 = float(pointvaluealgc4)
        pointvaluealgc5 = pointvaluealgc5.strip("(").strip(")").strip(",").strip("'")
        pointvaluealgc5 = float(pointvaluealgc5)
        pointvaluealgc6 = pointvaluealgc6.strip("(").strip(")").strip(",").strip("'")
        pointvaluealgc6 = float(pointvaluealgc6)
        pointvaluealgc7 = pointvaluealgc7.strip("(").strip(")").strip(",").strip("'")
        pointvaluealgc7 = float(pointvaluealgc7)
        pointvaluealgc8 = pointvaluealgc8.strip("(").strip(")").strip(",").strip("'")
        pointvaluealgc8 = float(pointvaluealgc8)

        mycursor.execute("SELECT `Value B` FROM linegcomparison_table")
        pointvalueblgc = mycursor.fetchall()
        pointvalueblgc1, pointvalueblgc2, pointvalueblgc3, pointvalueblgc4, pointvalueblgc5, pointvalueblgc6, pointvalueblgc7, pointvalueblgc8 = pointvalueblgc
        pointvalueblgc1 = str(pointvalueblgc1)
        pointvalueblgc2 = str(pointvalueblgc2)
        pointvalueblgc3 = str(pointvalueblgc3)
        pointvalueblgc4 = str(pointvalueblgc4)
        pointvalueblgc5 = str(pointvalueblgc5)
        pointvalueblgc6 = str(pointvalueblgc6)
        pointvalueblgc7 = str(pointvalueblgc7)
        pointvalueblgc8 = str(pointvalueblgc8)          
        pointvalueblgc1 = pointvalueblgc1.strip("(").strip(")").strip(",").strip("'")
        pointvalueblgc1 = float(pointvalueblgc1)
        pointvalueblgc2 = pointvalueblgc2.strip("(").strip(")").strip(",").strip("'")
        pointvalueblgc2 = float(pointvalueblgc2)
        pointvalueblgc3 = pointvalueblgc3.strip("(").strip(")").strip(",").strip("'")
        pointvalueblgc3 = float(pointvalueblgc3)
        pointvalueblgc4 = pointvalueblgc4.strip("(").strip(")").strip(",").strip("'")
        pointvalueblgc4 = float(pointvalueblgc4)
        pointvalueblgc5 = pointvalueblgc5.strip("(").strip(")").strip(",").strip("'")
        pointvalueblgc5 = float(pointvalueblgc5)
        pointvalueblgc6 = pointvalueblgc6.strip("(").strip(")").strip(",").strip("'")
        pointvalueblgc6 = float(pointvalueblgc6)
        pointvalueblgc7 = pointvalueblgc7.strip("(").strip(")").strip(",").strip("'")
        pointvalueblgc7 = float(pointvalueblgc7)
        pointvalueblgc8 = pointvalueblgc8.strip("(").strip(")").strip(",").strip("'")
        pointvalueblgc8 = float(pointvalueblgc8)


        mycursor.execute("SELECT `Min Value` FROM linegcomparison_table")
        minpointvalue = mycursor.fetchone()
        my_floatlgc_minpointvalue = float(minpointvalue[0])
        
        mycursor.execute("SELECT `Max Value` FROM linegcomparison_table")
        maxpointvalue = mycursor.fetchone()
        my_floatlgc_maxpointvalue = float(maxpointvalue[0])

        mycursor.execute("SELECT `Decimals` FROM linegcomparison_table")
        decvalue = mycursor.fetchone()
        my_floatlgc_decvalue = int(decvalue[0])

        mycursor.execute("SELECT `Range Numbers` FROM linegcomparison_table")
        rangenumber = mycursor.fetchone()
        my_floatlgc_rangenumber = int(rangenumber[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM linegcomparison_table")
        my_stringlgc_title = mycursor.fetchone()
        my_stringlgc_title = str(my_stringlgc_title)
        my_stringlgc_title = my_stringlgc_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM linegcomparison_table")
        my_stringlgc_subtitle = mycursor.fetchone()
        my_stringlgc_subtitle = str(my_stringlgc_subtitle)
        my_stringlgc_subtitle = my_stringlgc_subtitle.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Legend` FROM linegcomparison_table")
        my_stringlgc_legendtext = mycursor.fetchall()
        my_stringlgc_legendtext1 = str(my_stringlgc_legendtext[0])
        my_stringlgc_legendtext2 = str(my_stringlgc_legendtext[1])
        my_stringlgc_legendtext1 = my_stringlgc_legendtext1.strip("(").strip(")").strip(",").strip("'")
        my_stringlgc_legendtext2 = my_stringlgc_legendtext2.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj = bpy.context.active_object  # Get the active (selected) object

                if selected_obj.type == 'MESH':
                        mesh_name = selected_obj.name

                        # Check if the selected object has modifiers
                        if selected_obj.modifiers:
                                if len(selected_obj.modifiers) >= 2:  # Ensure at least two modifiers exist
                                        modifier_0c = selected_obj.modifiers.get("GeometryNodes")
                                        modifier_1c = selected_obj.modifiers.get("GeometryNodes.001")

                                if modifier_0c and modifier_1c:
                                        modifier_0c["Input_2"] = my_floatlgc_numberofpoints
                                        modifier_0c["Input_13"] = my_floatlgc_minpointvalue
                                        modifier_0c["Input_14"] = my_floatlgc_maxpointvalue
                                        modifier_0c["Input_15"] = my_floatlgc_decvalue
                                        modifier_0c["Input_18"] = my_floatlgc_rangenumber
                                        modifier_0c["Input_4"] = pointvaluealgc1
                                        modifier_0c["Input_5"] = pointvaluealgc2
                                        modifier_0c["Input_6"] = pointvaluealgc3
                                        modifier_0c["Input_7"] = pointvaluealgc4
                                        modifier_0c["Input_8"] = pointvaluealgc5
                                        modifier_0c["Input_9"] = pointvaluealgc6
                                        modifier_0c["Input_10"] = pointvaluealgc7
                                        modifier_0c["Input_11"] = pointvaluealgc8
                                        modifier_0c["Input_34"] = pointvalueblgc1
                                        modifier_0c["Input_35"] = pointvalueblgc2
                                        modifier_0c["Input_36"] = pointvalueblgc3
                                        modifier_0c["Input_37"] = pointvalueblgc4
                                        modifier_0c["Input_38"] = pointvalueblgc5
                                        modifier_0c["Input_39"] = pointvalueblgc6
                                        modifier_0c["Input_40"] = pointvalueblgc7
                                        modifier_0c["Input_41"] = pointvalueblgc8

                                        modifier_1c["Input_4"] = my_stringlgc_pointtext1
                                        modifier_1c["Input_5"] = my_stringlgc_pointtext2
                                        modifier_1c["Input_6"] = my_stringlgc_pointtext3
                                        modifier_1c["Input_7"] = my_stringlgc_pointtext4
                                        modifier_1c["Input_8"] = my_stringlgc_pointtext5
                                        modifier_1c["Input_9"] = my_stringlgc_pointtext6
                                        modifier_1c["Input_10"] = my_stringlgc_pointtext7
                                        modifier_1c["Input_11"] = my_stringlgc_pointtext8
                                        modifier_1c["Input_23"] = my_stringlgc_title
                                        modifier_1c["Input_22"] = my_stringlgc_subtitle
                                        modifier_1c["Input_29"] = my_stringlgc_legendtext1
                                        modifier_1c["Input_30"] = my_stringlgc_legendtext2

                                        print(f"Set modifier input for object '{mesh_name}'.")
                                else:
                                        print("Selected object does not have both modifiers.")
                        else:
                                print(f"Selected object '{mesh_name}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")

        # Optionally, you can update the mesh data if needed.
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class MyoperatorMGsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatormgsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringmountain_graph
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of points (1-8)` FROM mountaingtable")
        numberofpointsmg = mycursor.fetchone()
        my_floatmg_numberofpoints = int(numberofpointsmg[0])

        mycursor.execute("SELECT `Value` FROM mountaingtable")
        pointvaluemg = mycursor.fetchall()
        pointvaluemg1, pointvaluemg2, pointvaluemg3, pointvaluemg4, pointvaluemg5, pointvaluemg6, pointvaluemg7, pointvaluemg8 = pointvaluemg
        pointvaluemg1 = str(pointvaluemg1)
        pointvaluemg2 = str(pointvaluemg2)
        pointvaluemg3 = str(pointvaluemg3)
        pointvaluemg4 = str(pointvaluemg4)
        pointvaluemg5 = str(pointvaluemg5)
        pointvaluemg6 = str(pointvaluemg6)
        pointvaluemg7 = str(pointvaluemg7)
        pointvaluemg8 = str(pointvaluemg8)          
        pointvaluemg1 = pointvaluemg1.strip("(").strip(")").strip(",").strip("'")
        pointvaluemg1 = float(pointvaluemg1)
        pointvaluemg2 = pointvaluemg2.strip("(").strip(")").strip(",").strip("'")
        pointvaluemg2 = float(pointvaluemg2)
        pointvaluemg3 = pointvaluemg3.strip("(").strip(")").strip(",").strip("'")
        pointvaluemg3 = float(pointvaluemg3)
        pointvaluemg4 = pointvaluemg4.strip("(").strip(")").strip(",").strip("'")
        pointvaluemg4 = float(pointvaluemg4)
        pointvaluemg5 = pointvaluemg5.strip("(").strip(")").strip(",").strip("'")
        pointvaluemg5 = float(pointvaluemg5)
        pointvaluemg6 = pointvaluemg6.strip("(").strip(")").strip(",").strip("'")
        pointvaluemg6 = float(pointvaluemg6)
        pointvaluemg7 = pointvaluemg7.strip("(").strip(")").strip(",").strip("'")
        pointvaluemg7 = float(pointvaluemg7)
        pointvaluemg8 = pointvaluemg8.strip("(").strip(")").strip(",").strip("'")
        pointvaluemg8 = float(pointvaluemg8)

        mycursor.execute("SELECT `Point Text` FROM mountaingtable")
        my_stringmg_pointtext = mycursor.fetchall()
        my_stringmg_pointtext1 = str(my_stringmg_pointtext[0])
        my_stringmg_pointtext2 = str(my_stringmg_pointtext[1])
        my_stringmg_pointtext3 = str(my_stringmg_pointtext[2])
        my_stringmg_pointtext4 = str(my_stringmg_pointtext[3])
        my_stringmg_pointtext5 = str(my_stringmg_pointtext[4])
        my_stringmg_pointtext6 = str(my_stringmg_pointtext[5])
        my_stringmg_pointtext7 = str(my_stringmg_pointtext[6])
        my_stringmg_pointtext8 = str(my_stringmg_pointtext[7])
        my_stringmg_pointtext1 = my_stringmg_pointtext1.strip("(").strip(")").strip(",").strip("'")
        my_stringmg_pointtext2 = my_stringmg_pointtext2.strip("(").strip(")").strip(",").strip("'")
        my_stringmg_pointtext3 = my_stringmg_pointtext3.strip("(").strip(")").strip(",").strip("'")
        my_stringmg_pointtext4 = my_stringmg_pointtext4.strip("(").strip(")").strip(",").strip("'")
        my_stringmg_pointtext5 = my_stringmg_pointtext5.strip("(").strip(")").strip(",").strip("'")
        my_stringmg_pointtext6 = my_stringmg_pointtext6.strip("(").strip(")").strip(",").strip("'")
        my_stringmg_pointtext7 = my_stringmg_pointtext7.strip("(").strip(")").strip(",").strip("'")
        my_stringmg_pointtext8 = my_stringmg_pointtext8.strip("(").strip(")").strip(",").strip("'")


        mycursor.execute("SELECT `Min Value` FROM mountaingtable")
        minpointvalue = mycursor.fetchone()
        my_floatmg_minpointvalue = float(minpointvalue[0])
        
        mycursor.execute("SELECT `Max Value` FROM mountaingtable")
        maxpointvalue = mycursor.fetchone()
        my_floatmg_maxpointvalue = float(maxpointvalue[0])

        mycursor.execute("SELECT `Decimals` FROM mountaingtable")
        decvalue = mycursor.fetchone()
        my_floatmg_decvalue = int(decvalue[0])

        mycursor.execute("SELECT `Range Numbers` FROM mountaingtable")
        rangenumber = mycursor.fetchone()
        my_floatmg_rangenumber = int(rangenumber[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM mountaingtable")
        my_stringmg_title = mycursor.fetchone()
        my_stringmg_title = str(my_stringmg_title)
        my_stringmg_title = my_stringmg_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM mountaingtable")
        my_stringmg_subtitle = mycursor.fetchone()
        my_stringmg_subtitle = str(my_stringmg_subtitle)
        my_stringmg_subtitle = my_stringmg_subtitle.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_mg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_mg.type == 'MESH':
                        mesh_name_mg = selected_obj_mg.name

                        # Check if the selected object has modifiers
                        if selected_obj_mg.modifiers:
                                modifier_name_mg = selected_obj_mg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_mg.modifiers[modifier_name_mg]["Input_2"] = my_floatmg_numberofpoints
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_22"] = my_floatmg_minpointvalue
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_24"] = my_floatmg_maxpointvalue
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_23"] = my_floatmg_decvalue
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_21"] = my_floatmg_rangenumber
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_3"] = pointvaluemg1
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_4"] = pointvaluemg2
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_5"] = pointvaluemg3
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_6"] = pointvaluemg4
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_7"] = pointvaluemg5
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_8"] = pointvaluemg6
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_9"] = pointvaluemg7
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_10"] = pointvaluemg8
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_13"] = my_stringmg_pointtext1
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_14"] = my_stringmg_pointtext2
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_15"] = my_stringmg_pointtext3
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_16"] = my_stringmg_pointtext4
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_17"] = my_stringmg_pointtext5
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_18"] = my_stringmg_pointtext6
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_19"] = my_stringmg_pointtext7
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_20"] = my_stringmg_pointtext8
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_38"] = my_stringmg_title
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_39"] = my_stringmg_subtitle

                                print(f"Set modifier input for object '{mesh_name_mg}' and modifier '{modifier_name_mg}'.")
                        else:
                                print(f"Selected object '{mesh_name_mg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class MyoperatorMGCsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatormgcsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringmountain_graph_comparison
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of points (1-8)` FROM mountaingcomparison_table")
        numberofpointsmgc = mycursor.fetchone()
        my_floatmgc_numberofpoints = int(numberofpointsmgc[0])

        mycursor.execute("SELECT `Point Text` FROM mountaingcomparison_table")
        my_stringmgc_pointtext = mycursor.fetchall()
        my_stringmgc_pointtext1 = str(my_stringmgc_pointtext[0])
        my_stringmgc_pointtext2 = str(my_stringmgc_pointtext[1])
        my_stringmgc_pointtext3 = str(my_stringmgc_pointtext[2])
        my_stringmgc_pointtext4 = str(my_stringmgc_pointtext[3])
        my_stringmgc_pointtext5 = str(my_stringmgc_pointtext[4])
        my_stringmgc_pointtext6 = str(my_stringmgc_pointtext[5])
        my_stringmgc_pointtext7 = str(my_stringmgc_pointtext[6])
        my_stringmgc_pointtext8 = str(my_stringmgc_pointtext[7])
        my_stringmgc_pointtext1 = my_stringmgc_pointtext1.strip("(").strip(")").strip(",").strip("'")
        my_stringmgc_pointtext2 = my_stringmgc_pointtext2.strip("(").strip(")").strip(",").strip("'")
        my_stringmgc_pointtext3 = my_stringmgc_pointtext3.strip("(").strip(")").strip(",").strip("'")
        my_stringmgc_pointtext4 = my_stringmgc_pointtext4.strip("(").strip(")").strip(",").strip("'")
        my_stringmgc_pointtext5 = my_stringmgc_pointtext5.strip("(").strip(")").strip(",").strip("'")
        my_stringmgc_pointtext6 = my_stringmgc_pointtext6.strip("(").strip(")").strip(",").strip("'")
        my_stringmgc_pointtext7 = my_stringmgc_pointtext7.strip("(").strip(")").strip(",").strip("'")
        my_stringmgc_pointtext8 = my_stringmgc_pointtext8.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Value A` FROM mountaingcomparison_table")
        pointvalueamgc = mycursor.fetchall()
        pointvalueamgc1, pointvalueamgc2, pointvalueamgc3, pointvalueamgc4, pointvalueamgc5, pointvalueamgc6, pointvalueamgc7, pointvalueamgc8 = pointvalueamgc
        pointvalueamgc1 = str(pointvalueamgc1)
        pointvalueamgc2 = str(pointvalueamgc2)
        pointvalueamgc3 = str(pointvalueamgc3)
        pointvalueamgc4 = str(pointvalueamgc4)
        pointvalueamgc5 = str(pointvalueamgc5)
        pointvalueamgc6 = str(pointvalueamgc6)
        pointvalueamgc7 = str(pointvalueamgc7)
        pointvalueamgc8 = str(pointvalueamgc8)          
        pointvalueamgc1 = pointvalueamgc1.strip("(").strip(")").strip(",").strip("'")
        pointvalueamgc1 = float(pointvalueamgc1)
        pointvalueamgc2 = pointvalueamgc2.strip("(").strip(")").strip(",").strip("'")
        pointvalueamgc2 = float(pointvalueamgc2)
        pointvalueamgc3 = pointvalueamgc3.strip("(").strip(")").strip(",").strip("'")
        pointvalueamgc3 = float(pointvalueamgc3)
        pointvalueamgc4 = pointvalueamgc4.strip("(").strip(")").strip(",").strip("'")
        pointvalueamgc4 = float(pointvalueamgc4)
        pointvalueamgc5 = pointvalueamgc5.strip("(").strip(")").strip(",").strip("'")
        pointvalueamgc5 = float(pointvalueamgc5)
        pointvalueamgc6 = pointvalueamgc6.strip("(").strip(")").strip(",").strip("'")
        pointvalueamgc6 = float(pointvalueamgc6)
        pointvalueamgc7 = pointvalueamgc7.strip("(").strip(")").strip(",").strip("'")
        pointvalueamgc7 = float(pointvalueamgc7)
        pointvalueamgc8 = pointvalueamgc8.strip("(").strip(")").strip(",").strip("'")
        pointvalueamgc8 = float(pointvalueamgc8)

        mycursor.execute("SELECT `Value B` FROM mountaingcomparison_table")
        pointvaluebmgc = mycursor.fetchall()
        pointvaluebmgc1, pointvaluebmgc2, pointvaluebmgc3, pointvaluebmgc4, pointvaluebmgc5, pointvaluebmgc6, pointvaluebmgc7, pointvaluebmgc8 = pointvaluebmgc
        pointvaluebmgc1 = str(pointvaluebmgc1)
        pointvaluebmgc2 = str(pointvaluebmgc2)
        pointvaluebmgc3 = str(pointvaluebmgc3)
        pointvaluebmgc4 = str(pointvaluebmgc4)
        pointvaluebmgc5 = str(pointvaluebmgc5)
        pointvaluebmgc6 = str(pointvaluebmgc6)
        pointvaluebmgc7 = str(pointvaluebmgc7)
        pointvaluebmgc8 = str(pointvaluebmgc8)          
        pointvaluebmgc1 = pointvaluebmgc1.strip("(").strip(")").strip(",").strip("'")
        pointvaluebmgc1 = float(pointvaluebmgc1)
        pointvaluebmgc2 = pointvaluebmgc2.strip("(").strip(")").strip(",").strip("'")
        pointvaluebmgc2 = float(pointvaluebmgc2)
        pointvaluebmgc3 = pointvaluebmgc3.strip("(").strip(")").strip(",").strip("'")
        pointvaluebmgc3 = float(pointvaluebmgc3)
        pointvaluebmgc4 = pointvaluebmgc4.strip("(").strip(")").strip(",").strip("'")
        pointvaluebmgc4 = float(pointvaluebmgc4)
        pointvaluebmgc5 = pointvaluebmgc5.strip("(").strip(")").strip(",").strip("'")
        pointvaluebmgc5 = float(pointvaluebmgc5)
        pointvaluebmgc6 = pointvaluebmgc6.strip("(").strip(")").strip(",").strip("'")
        pointvaluebmgc6 = float(pointvaluebmgc6)
        pointvaluebmgc7 = pointvaluebmgc7.strip("(").strip(")").strip(",").strip("'")
        pointvaluebmgc7 = float(pointvaluebmgc7)
        pointvaluebmgc8 = pointvaluebmgc8.strip("(").strip(")").strip(",").strip("'")
        pointvaluebmgc8 = float(pointvaluebmgc8)


        mycursor.execute("SELECT `Min Value` FROM mountaingcomparison_table")
        minpointvalue = mycursor.fetchone()
        my_floatmgc_minpointvalue = float(minpointvalue[0])
        
        mycursor.execute("SELECT `Max Value` FROM mountaingcomparison_table")
        maxpointvalue = mycursor.fetchone()
        my_floatmgc_maxpointvalue = float(maxpointvalue[0])

        mycursor.execute("SELECT `Decimals` FROM mountaingcomparison_table")
        decvalue = mycursor.fetchone()
        my_floatmgc_decvalue = int(decvalue[0])

        mycursor.execute("SELECT `Range Numbers` FROM mountaingcomparison_table")
        rangenumber = mycursor.fetchone()
        my_floatmgc_rangenumber = int(rangenumber[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM mountaingcomparison_table")
        my_stringmgc_title = mycursor.fetchone()
        my_stringmgc_title = str(my_stringmgc_title)
        my_stringmgc_title = my_stringmgc_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM mountaingcomparison_table")
        my_stringmgc_subtitle = mycursor.fetchone()
        my_stringmgc_subtitle = str(my_stringmgc_subtitle)
        my_stringmgc_subtitle = my_stringmgc_subtitle.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Legend` FROM mountaingcomparison_table")
        my_stringmgc_legendtext = mycursor.fetchall()
        my_stringmgc_legendtext1 = str(my_stringmgc_legendtext[0])
        my_stringmgc_legendtext2 = str(my_stringmgc_legendtext[1])
        my_stringmgc_legendtext1 = my_stringmgc_legendtext1.strip("(").strip(")").strip(",").strip("'")
        my_stringmgc_legendtext2 = my_stringmgc_legendtext2.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_mgc = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_mgc.type == 'MESH':
                        mesh_name_mgc = selected_obj_mgc.name

                        # Check if the selected object has modifiers
                        if selected_obj_mgc.modifiers:
                                modifier_name_mgc = selected_obj_mgc.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_2"] = my_floatmgc_numberofpoints
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_22"] = my_floatmgc_minpointvalue
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_24"] = my_floatmgc_maxpointvalue
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_23"] = my_floatmgc_decvalue
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_21"] = my_floatmgc_rangenumber
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_3"] = pointvalueamgc1
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_4"] = pointvalueamgc2
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_67"] = pointvalueamgc3
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_6"] = pointvalueamgc4
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_7"] = pointvalueamgc5
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_8"] = pointvalueamgc6
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_9"] = pointvalueamgc7
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_10"] = pointvalueamgc8
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_30"] = pointvaluebmgc1
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_39"] = pointvaluebmgc2
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_40"] = pointvaluebmgc3
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_41"] = pointvaluebmgc4
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_42"] = pointvaluebmgc5
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_43"] = pointvaluebmgc6
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_44"] = pointvaluebmgc7
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_45"] = pointvaluebmgc8
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_13"] = my_stringmgc_pointtext1
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_14"] = my_stringmgc_pointtext2
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_15"] = my_stringmgc_pointtext3
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_16"] = my_stringmgc_pointtext4
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_17"] = my_stringmgc_pointtext5
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_18"] = my_stringmgc_pointtext6
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_19"] = my_stringmgc_pointtext7
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_20"] = my_stringmgc_pointtext8
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_54"] = my_stringmgc_title
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_55"] = my_stringmgc_subtitle
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_57"] = my_stringmgc_legendtext1
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_56"] = my_stringmgc_legendtext2

                                print(f"Set modifier input for object '{mesh_name_mgc}' and modifier '{modifier_name_mgc}'.")
                        else:
                                print(f"Selected object '{mesh_name_mgc}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class Myoperatorusmapsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorusmapsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        usmap_object = bpy.context.view_layer.objects.active
        usmap_object_name = usmap_object.name
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringusmap
        )
            
        mycursor = mydb.cursor(buffered=True)

        mycursor.execute("SELECT `US State Name` FROM usmaptable")
        my_stringusmapg_usstatename = mycursor.fetchall()
        usstatename_list = [str(item).strip("(").strip(")").strip(",").strip("'") for item in my_stringusmapg_usstatename]
 
        mycursor.execute("SELECT `Data` FROM usmaptable")
        datausmapg = mycursor.fetchall()
        # Convert the fetched data to a list of floats in one line
        datausmapg = [float(str(point).strip("(), '")) for point in datausmapg]

        mycursor.execute("SELECT `Min Value` FROM usmaptable")
        minpointvalue = mycursor.fetchone()
        my_floatusmapg_minpointvalue = float(minpointvalue[0])
        
        mycursor.execute("SELECT `Max Value` FROM usmaptable")
        maxpointvalue = mycursor.fetchone()
        my_floatusmapg_maxpointvalue = float(maxpointvalue[0])

        mycursor.execute("SELECT `Decimals` FROM usmaptable")
        decvalue = mycursor.fetchone()
        my_floatusmapg_decvalue = int(decvalue[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM usmaptable")
        my_stringusmapg_title = mycursor.fetchone()
        my_stringusmapg_title = str(my_stringusmapg_title)
        my_stringusmapg_title = my_stringusmapg_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM usmaptable")
        my_stringusmapg_subtitle = mycursor.fetchone()
        my_stringusmapg_subtitle = str(my_stringusmapg_subtitle)
        my_stringusmapg_subtitle = my_stringusmapg_subtitle.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Source Title` FROM usmaptable")
        my_stringusmapg_sourcetitle = mycursor.fetchone()
        my_stringusmapg_sourcetitle = str(my_stringusmapg_sourcetitle)
        my_stringusmapg_sourcetitle = my_stringusmapg_sourcetitle.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Source Text` FROM usmaptable")
        my_stringusmapg_sourcesubtitle = mycursor.fetchone()
        my_stringusmapg_sourcesubtitle = str(my_stringusmapg_sourcesubtitle)
        my_stringusmapg_sourcesubtitle = my_stringusmapg_sourcesubtitle.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Credit Title` FROM usmaptable")
        my_stringusmapg_credittitle = mycursor.fetchone()
        my_stringusmapg_credittitle = str(my_stringusmapg_credittitle)
        my_stringusmapg_credittitle = my_stringusmapg_credittitle.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Credit Text` FROM usmaptable")
        my_stringusmapg_creditsubtitle = mycursor.fetchone()
        my_stringusmapg_creditsubtitle = str(my_stringusmapg_creditsubtitle)
        my_stringusmapg_creditsubtitle = my_stringusmapg_creditsubtitle.strip("(").strip(")").strip(",").strip("'")
            
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_112"] = my_floatusmapg_minpointvalue
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_113"] = my_floatusmapg_maxpointvalue
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_168"] = my_floatusmapg_decvalue
        
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_185"] = usstatename_list[0]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_184"] = usstatename_list[1]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_183"] = usstatename_list[2]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_182"] = usstatename_list[3]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_181"] = usstatename_list[4]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_180"] = usstatename_list[5]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_179"] = usstatename_list[6]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_178"] = usstatename_list[7]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_177"] = usstatename_list[8]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_176"] = usstatename_list[9]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_175"] = usstatename_list[10]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_174"] = usstatename_list[11]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_173"] = usstatename_list[12]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_172"] = usstatename_list[13]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_171"] = usstatename_list[14]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_170"] = usstatename_list[15]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_167"] = usstatename_list[16]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_186"] = usstatename_list[17]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_187"] = usstatename_list[18]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_188"] = usstatename_list[19]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_189"] = usstatename_list[20]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_190"] = usstatename_list[21]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_191"] = usstatename_list[22]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_192"] = usstatename_list[23]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_193"] = usstatename_list[24]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_194"] = usstatename_list[25]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_195"] = usstatename_list[26]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_196"] = usstatename_list[27]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_197"] = usstatename_list[28]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_198"] = usstatename_list[29]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_199"] = usstatename_list[30]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_200"] = usstatename_list[31]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_201"] = usstatename_list[32]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_202"] = usstatename_list[33]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_203"] = usstatename_list[34]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_204"] = usstatename_list[35]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_205"] = usstatename_list[36]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_206"] = usstatename_list[37]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_207"] = usstatename_list[38]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_208"] = usstatename_list[39]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_209"] = usstatename_list[40]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_210"] = usstatename_list[41]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_211"] = usstatename_list[42]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_212"] = usstatename_list[43]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_213"] = usstatename_list[44]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_214"] = usstatename_list[45]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_215"] = usstatename_list[46]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_216"] = usstatename_list[47]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_217"] = usstatename_list[48]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_218"] = usstatename_list[49]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_219"] = usstatename_list[50]



            
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_13"] = datausmapg[0]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_14"] = datausmapg[1] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_15"] = datausmapg[2]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_16"] = datausmapg[3] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_17"] = datausmapg[4]          
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_18"] = datausmapg[5]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_19"] = datausmapg[6] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_20"] = datausmapg[7] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_62"] = datausmapg[8]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_21"] = datausmapg[9]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_22"] = datausmapg[10] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_23"] = datausmapg[11] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_24"] = datausmapg[12] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_25"] = datausmapg[13] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_26"] = datausmapg[14] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_27"] = datausmapg[15]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_12"] = datausmapg[16]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_28"] = datausmapg[17]  
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_29"] = datausmapg[18] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_30"] = datausmapg[19]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_31"] = datausmapg[20]  
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_32"] = datausmapg[21]  
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_33"] = datausmapg[22]  
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_34"] = datausmapg[23] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_166"] = datausmapg[24]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_35"] = datausmapg[25] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_36"] = datausmapg[26]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_37"] = datausmapg[27]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_38"] = datausmapg[28]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_39"] = datausmapg[29]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_40"] = datausmapg[30]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_41"] = datausmapg[31]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_42"] = datausmapg[32]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_43"] = datausmapg[33]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_44"] = datausmapg[34]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_45"] = datausmapg[35]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_46"] = datausmapg[36]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_47"] = datausmapg[37]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_48"] = datausmapg[38]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_49"] = datausmapg[39]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_50"] = datausmapg[40]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_51"] = datausmapg[41]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_52"] = datausmapg[42]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_53"] = datausmapg[43]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_54"] = datausmapg[44]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_55"] = datausmapg[45]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_56"] = datausmapg[46]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_57"] = datausmapg[47]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_58"] = datausmapg[48]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_59"] = datausmapg[49]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_60"] = datausmapg[50]
           
    
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_232"] = my_stringusmapg_title
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_233"] = my_stringusmapg_subtitle
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_234"] = my_stringusmapg_sourcetitle
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_235"] = my_stringusmapg_sourcesubtitle
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_236"] = my_stringusmapg_credittitle
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_237"] = my_stringusmapg_creditsubtitle
        
        bpy.context.object.data.update()
        return {'FINISHED'}   
    
class MyoperatorVBGsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorvbgsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringvertical_bar_graph
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of bars (1-8)` FROM vertical_bargtable")
        numberofbarsvbg = mycursor.fetchone()
        my_floatvbg_numberofbars = int(numberofbarsvbg[0])
        
        mycursor.execute("SELECT `Bar Text` FROM vertical_bargtable")
        my_stringvbg_bartext = mycursor.fetchall()
        my_stringvbg_bartext1 = str(my_stringvbg_bartext[0])
        my_stringvbg_bartext2 = str(my_stringvbg_bartext[1])
        my_stringvbg_bartext3 = str(my_stringvbg_bartext[2])
        my_stringvbg_bartext4 = str(my_stringvbg_bartext[3])
        my_stringvbg_bartext5 = str(my_stringvbg_bartext[4])
        my_stringvbg_bartext6 = str(my_stringvbg_bartext[5])
        my_stringvbg_bartext7 = str(my_stringvbg_bartext[6])
        my_stringvbg_bartext8 = str(my_stringvbg_bartext[7])
        my_stringvbg_bartext1 = my_stringvbg_bartext1.strip("(").strip(")").strip(",").strip("'")
        my_stringvbg_bartext2 = my_stringvbg_bartext2.strip("(").strip(")").strip(",").strip("'")
        my_stringvbg_bartext3 = my_stringvbg_bartext3.strip("(").strip(")").strip(",").strip("'")
        my_stringvbg_bartext4 = my_stringvbg_bartext4.strip("(").strip(")").strip(",").strip("'")
        my_stringvbg_bartext5 = my_stringvbg_bartext5.strip("(").strip(")").strip(",").strip("'")
        my_stringvbg_bartext6 = my_stringvbg_bartext6.strip("(").strip(")").strip(",").strip("'")
        my_stringvbg_bartext7 = my_stringvbg_bartext7.strip("(").strip(")").strip(",").strip("'")
        my_stringvbg_bartext8 = my_stringvbg_bartext8.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Max Value` FROM vertical_bargtable")
        maxvalue = mycursor.fetchone()
        my_floatvbg_maxvalue = float(maxvalue[0])

        mycursor.execute("SELECT `Bar Value` FROM vertical_bargtable")
        valuevbg = mycursor.fetchall()
        valuevbg1, valuevbg2, valuevbg3, valuevbg4, valuevbg5, valuevbg6, valuevbg7, valuevbg8 = valuevbg
        valuevbg1 = str(valuevbg1)
        valuevbg2 = str(valuevbg2)
        valuevbg3 = str(valuevbg3)
        valuevbg4 = str(valuevbg4)  
        valuevbg5 = str(valuevbg5)
        valuevbg6 = str(valuevbg6)
        valuevbg7 = str(valuevbg7)
        valuevbg8 = str(valuevbg8)        
        valuevbg1 = valuevbg1.strip("(").strip(")").strip(",").strip("'")
        valuevbg1 = float(valuevbg1)
        valuevbg2 = valuevbg2.strip("(").strip(")").strip(",").strip("'")
        valuevbg2 = float(valuevbg2)
        valuevbg3 = valuevbg3.strip("(").strip(")").strip(",").strip("'")
        valuevbg3 = float(valuevbg3)
        valuevbg4 = valuevbg4.strip("(").strip(")").strip(",").strip("'")
        valuevbg4 = float(valuevbg4)
        valuevbg5 = valuevbg5.strip("(").strip(")").strip(",").strip("'")
        valuevbg5 = float(valuevbg5)
        valuevbg6 = valuevbg6.strip("(").strip(")").strip(",").strip("'")
        valuevbg6 = float(valuevbg6)
        valuevbg7 = valuevbg7.strip("(").strip(")").strip(",").strip("'")
        valuevbg7 = float(valuevbg7)
        valuevbg8 = valuevbg8.strip("(").strip(")").strip(",").strip("'")
        valuevbg8 = float(valuevbg8)

        mycursor.execute("SELECT `Min Value` FROM vertical_bargtable")
        minvalue = mycursor.fetchone()
        my_floatvbg_minvalue = float(minvalue[0])

        mycursor.execute("SELECT `Decimals` FROM vertical_bargtable")
        decvalue = mycursor.fetchone()
        my_floatvbg_decvalue = float(decvalue[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM vertical_bargtable")
        my_stringvbg_title = mycursor.fetchone()
        my_stringvbg_title = str(my_stringvbg_title)
        my_stringvbg_title = my_stringvbg_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM vertical_bargtable")
        my_stringvbg_subtitle = mycursor.fetchone()
        my_stringvbg_subtitle = str(my_stringvbg_subtitle)
        my_stringvbg_subtitle = my_stringvbg_subtitle.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Text for total` FROM vertical_bargtable")
        my_stringvbg_textfortotal = mycursor.fetchone()
        my_stringvbg_textfortotal = str(my_stringvbg_textfortotal)
        my_stringvbg_textfortotal = my_stringvbg_textfortotal.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_vbg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_vbg.type == 'MESH':
                        mesh_name_vbg = selected_obj_vbg.name

                        # Check if the selected object has modifiers
                        if selected_obj_vbg.modifiers:
                                modifier_name_vbg = selected_obj_vbg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_57"] = my_floatvbg_numberofbars
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_14"] = valuevbg1
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_41"] = valuevbg2
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_15"] = valuevbg3
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_44"] = valuevbg4
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_16"] = valuevbg5
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_48"] = valuevbg6
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_17"] = valuevbg7
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_50"] = valuevbg8
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_10"] = my_floatvbg_minvalue
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_11"] = my_floatvbg_maxvalue
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_12"] = my_floatvbg_decvalue
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_2"] = my_stringvbg_bartext1
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_42"] = my_stringvbg_bartext2
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_3"] = my_stringvbg_bartext3
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_45"] = my_stringvbg_bartext4
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_4"] = my_stringvbg_bartext5
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_47"] = my_stringvbg_bartext6
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_5"] = my_stringvbg_bartext7
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_49"] = my_stringvbg_bartext8
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_7"] = my_stringvbg_title
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_8"] = my_stringvbg_subtitle
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_6"] = my_stringvbg_textfortotal

                                print(f"Set modifier input for object '{mesh_name_vbg}' and modifier '{modifier_name_vbg}'.")
                        else:
                                print(f"Selected object '{mesh_name_vbg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class MyoperatorVBGCsql(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorvbgcsql"
    bl_label = "Import MySQL Data"
    
    def execute(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        mydb = mysql.connector.connect(
        host= mytool.my_stringhost,
        user= mytool.my_stringuser,
        password= mytool.my_stringpassword,
        database= mytool.my_stringvertical_bar_graph_comparison
        )
            
        mycursor = mydb.cursor(buffered=True)

        
        mycursor.execute("SELECT `Number of bars (1-8)` FROM vertical_bar_comparison_gtable")
        numberofbarsvbgc = mycursor.fetchone()
        my_floatvbgc_numberofbars = int(numberofbarsvbgc[0])
        
        mycursor.execute("SELECT `Bar Text` FROM vertical_bar_comparison_gtable")
        my_stringvbgc_bartext = mycursor.fetchall()
        my_stringvbgc_bartext1 = str(my_stringvbgc_bartext[0])
        my_stringvbgc_bartext2 = str(my_stringvbgc_bartext[1])
        my_stringvbgc_bartext3 = str(my_stringvbgc_bartext[2])
        my_stringvbgc_bartext4 = str(my_stringvbgc_bartext[3])
        my_stringvbgc_bartext5 = str(my_stringvbgc_bartext[4])
        my_stringvbgc_bartext6 = str(my_stringvbgc_bartext[5])
        my_stringvbgc_bartext7 = str(my_stringvbgc_bartext[6])
        my_stringvbgc_bartext8 = str(my_stringvbgc_bartext[7])
        my_stringvbgc_bartext1 = my_stringvbgc_bartext1.strip("(").strip(")").strip(",").strip("'")
        my_stringvbgc_bartext2 = my_stringvbgc_bartext2.strip("(").strip(")").strip(",").strip("'")
        my_stringvbgc_bartext3 = my_stringvbgc_bartext3.strip("(").strip(")").strip(",").strip("'")
        my_stringvbgc_bartext4 = my_stringvbgc_bartext4.strip("(").strip(")").strip(",").strip("'")
        my_stringvbgc_bartext5 = my_stringvbgc_bartext5.strip("(").strip(")").strip(",").strip("'")
        my_stringvbgc_bartext6 = my_stringvbgc_bartext6.strip("(").strip(")").strip(",").strip("'")
        my_stringvbgc_bartext7 = my_stringvbgc_bartext7.strip("(").strip(")").strip(",").strip("'")
        my_stringvbgc_bartext8 = my_stringvbgc_bartext8.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Max Value` FROM vertical_bar_comparison_gtable")
        maxvalue = mycursor.fetchone()
        my_floatvbgc_maxvalue = float(maxvalue[0])

        mycursor.execute("SELECT `Bar Value A` FROM vertical_bar_comparison_gtable")
        valueavbgc = mycursor.fetchall()
        valueavbgc1, valueavbgc2, valueavbgc3, valueavbgc4, valueavbgc5, valueavbgc6, valueavbgc7, valueavbgc8 = valueavbgc
        valueavbgc1 = str(valueavbgc1)
        valueavbgc2 = str(valueavbgc2)
        valueavbgc3 = str(valueavbgc3)
        valueavbgc4 = str(valueavbgc4)  
        valueavbgc5 = str(valueavbgc5)
        valueavbgc6 = str(valueavbgc6)
        valueavbgc7 = str(valueavbgc7)
        valueavbgc8 = str(valueavbgc8)        
        valueavbgc1 = valueavbgc1.strip("(").strip(")").strip(",").strip("'")
        valueavbgc1 = float(valueavbgc1)
        valueavbgc2 = valueavbgc2.strip("(").strip(")").strip(",").strip("'")
        valueavbgc2 = float(valueavbgc2)
        valueavbgc3 = valueavbgc3.strip("(").strip(")").strip(",").strip("'")
        valueavbgc3 = float(valueavbgc3)
        valueavbgc4 = valueavbgc4.strip("(").strip(")").strip(",").strip("'")
        valueavbgc4 = float(valueavbgc4)
        valueavbgc5 = valueavbgc5.strip("(").strip(")").strip(",").strip("'")
        valueavbgc5 = float(valueavbgc5)
        valueavbgc6 = valueavbgc6.strip("(").strip(")").strip(",").strip("'")
        valueavbgc6 = float(valueavbgc6)
        valueavbgc7 = valueavbgc7.strip("(").strip(")").strip(",").strip("'")
        valueavbgc7 = float(valueavbgc7)
        valueavbgc8 = valueavbgc8.strip("(").strip(")").strip(",").strip("'")
        valueavbgc8 = float(valueavbgc8)

        mycursor.execute("SELECT `Bar Value B` FROM vertical_bar_comparison_gtable")
        valuebvbgc = mycursor.fetchall()
        valuebvbgc1, valuebvbgc2, valuebvbgc3, valuebvbgc4, valuebvbgc5, valuebvbgc6, valuebvbgc7, valuebvbgc8 = valuebvbgc
        valuebvbgc1 = str(valuebvbgc1)
        valuebvbgc2 = str(valuebvbgc2)
        valuebvbgc3 = str(valuebvbgc3)
        valuebvbgc4 = str(valuebvbgc4)  
        valuebvbgc5 = str(valuebvbgc5)
        valuebvbgc6 = str(valuebvbgc6)
        valuebvbgc7 = str(valuebvbgc7)
        valuebvbgc8 = str(valuebvbgc8)        
        valuebvbgc1 = valuebvbgc1.strip("(").strip(")").strip(",").strip("'")
        valuebvbgc1 = float(valuebvbgc1)
        valuebvbgc2 = valuebvbgc2.strip("(").strip(")").strip(",").strip("'")
        valuebvbgc2 = float(valuebvbgc2)
        valuebvbgc3 = valuebvbgc3.strip("(").strip(")").strip(",").strip("'")
        valuebvbgc3 = float(valuebvbgc3)
        valuebvbgc4 = valuebvbgc4.strip("(").strip(")").strip(",").strip("'")
        valuebvbgc4 = float(valuebvbgc4)
        valuebvbgc5 = valuebvbgc5.strip("(").strip(")").strip(",").strip("'")
        valuebvbgc5 = float(valuebvbgc5)
        valuebvbgc6 = valuebvbgc6.strip("(").strip(")").strip(",").strip("'")
        valuebvbgc6 = float(valuebvbgc6)
        valuebvbgc7 = valuebvbgc7.strip("(").strip(")").strip(",").strip("'")
        valuebvbgc7 = float(valuebvbgc7)
        valuebvbgc8 = valuebvbgc8.strip("(").strip(")").strip(",").strip("'")
        valuebvbgc8 = float(valuebvbgc8)

        mycursor.execute("SELECT `Min Value` FROM vertical_bar_comparison_gtable")
        minvalue = mycursor.fetchone()
        my_floatvbgc_minvalue = float(minvalue[0])

        mycursor.execute("SELECT `Decimals` FROM vertical_bar_comparison_gtable")
        decvalue = mycursor.fetchone()
        my_floatvbgc_decvalue = float(decvalue[0])

        mycursor.execute("SELECT `TITLE (in caps)` FROM vertical_bar_comparison_gtable")
        my_stringvbgc_title = mycursor.fetchone()
        my_stringvbgc_title = str(my_stringvbgc_title)
        my_stringvbgc_title = my_stringvbgc_title.strip("(").strip(")").strip(",").strip("'")

        mycursor.execute("SELECT `Subtitle` FROM vertical_bar_comparison_gtable")
        my_stringvbgc_subtitle = mycursor.fetchone()
        my_stringvbgc_subtitle = str(my_stringvbgc_subtitle)
        my_stringvbgc_subtitle = my_stringvbgc_subtitle.strip("(").strip(")").strip(",").strip("'")
        
        mycursor.execute("SELECT `Legend Text` FROM vertical_bar_comparison_gtable")
        my_stringvbgc_legendtext = mycursor.fetchall()
        my_stringvbgc_legendtext1 = str(my_stringvbgc_legendtext[0])
        my_stringvbgc_legendtext2 = str(my_stringvbgc_legendtext[1])
        my_stringvbgc_legendtext1 = my_stringvbgc_legendtext1.strip("(").strip(")").strip(",").strip("'")
        my_stringvbgc_legendtext2 = my_stringvbgc_legendtext2.strip("(").strip(")").strip(",").strip("'")
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_vbgc = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_vbgc.type == 'MESH':
                        mesh_name_vbgc = selected_obj_vbgc.name

                        # Check if the selected object has modifiers
                        if selected_obj_vbgc.modifiers:
                                modifier_name_vbgc = selected_obj_vbgc.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_71"] = my_floatvbgc_numberofbars
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_2"] = my_stringvbgc_bartext1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_42"] = my_stringvbgc_bartext2
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_3"] = my_stringvbgc_bartext3
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_45"] = my_stringvbgc_bartext4
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_4"] = my_stringvbgc_bartext5
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_47"] = my_stringvbgc_bartext6
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_5"] = my_stringvbgc_bartext7
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_49"] = my_stringvbgc_bartext8
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_10"] = my_floatvbgc_minvalue
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_11"] = my_floatvbgc_maxvalue
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_12"] = my_floatvbgc_decvalue
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_14"] = valueavbgc1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_41"] = valueavbgc2
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_15"] = valueavbgc3
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_44"] = valueavbgc4
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_16"] = valueavbgc5
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_48"] = valueavbgc6
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_17"] = valueavbgc7
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_50"] = valueavbgc8
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_57"] = valuebvbgc1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_58"] = valuebvbgc2
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_59"] = valuebvbgc3
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_64"] = valuebvbgc4
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_60"] = valuebvbgc5
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_61"] = valuebvbgc6
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_62"] = valuebvbgc7
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_63"] = valuebvbgc8
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_7"] = my_stringvbgc_title
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_8"] = my_stringvbgc_subtitle
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_70"] = my_stringvbgc_legendtext1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_69"] = my_stringvbgc_legendtext2


                                print(f"Set modifier input for object '{mesh_name_vbgc}' and modifier '{modifier_name_vbgc}'.")
                        else:
                                print(f"Selected object '{mesh_name_vbgc}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}

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
            
            # Ensure an object is selected
        if bpy.context.selected_objects:
            selected_obj = bpy.context.active_object  # Get the active (selected) object

            if selected_obj.type == 'MESH':
                mesh_name = selected_obj.name

                # Check if the selected object has modifiers
                if selected_obj.modifiers:
                    modifier_name = selected_obj.modifiers.active.name  # Get the name of the active modifier



                    selected_obj.modifiers[modifier_name]["Input_11"] = olatunji
                    selected_obj.modifiers[modifier_name]["Input_10"] = mallory
                    selected_obj.modifiers[modifier_name]["Input_2"] = gregorypercentage
                    selected_obj.modifiers[modifier_name]["Input_22"] = titlecirclegraph
                    selected_obj.modifiers[modifier_name]["Input_23"] = subtitlecirclegraph
                    selected_obj.modifiers[modifier_name]["Input_16"] = descriptioncirclegraph
        

                    print(f"Set modifier input for object '{mesh_name}' and modifier '{modifier_name}'.")
                else:
                    print(f"Selected object '{mesh_name}' has no modifiers.")
            else:
                print("Selected object is not a mesh.")
        else:
            print("No object selected.")
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


        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_23cg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_23cg.type == 'MESH':
                        mesh_name_23cg = selected_obj_23cg.name

                        # Check if the selected object has modifiers
                        if selected_obj_23cg.modifiers:
                                modifier_name_23cg = selected_obj_23cg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_31"] = ncg23c
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_39"] = wta23c
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_40"] = wtb23c
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_38"] = wtc23c
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_2"] = wtpa23c
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_41"] = wtpb23c
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_42"] = wtpc23c
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_10"] = minv23c
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_11"] = maxv23c
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_22"] = title23c
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_23"] = subtitle23c
                                selected_obj_23cg.modifiers[modifier_name_23cg]["Input_16"] = desc23c

                                print(f"Set modifier input for object '{mesh_name_23cg}' and modifier '{modifier_name_23cg}'.")
                        else:
                                print(f"Selected object '{mesh_name_23cg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class MyoperatorCANDLEcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorcandlecsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        candle_object = bpy.context.view_layer.objects.active
        candle_object_name = candle_object.name
        filepath_fullcandle = bpy.path.abspath(mytool.my_pathcandle)
        with open(filepath_fullcandle) as f:
            readout = list(csv.reader(f))
            npcandleg = int(readout[1][0])
            minvcandleg = float(readout[1][6])
            maxvcandleg = float(readout[1][7])
            decimalcandleg = int(readout[1][8])
            rncandleg = int(readout[1][9])

            num_elementspointhigh = 32
            pointhigh_candleg = []
            for i in range(1, num_elementspointhigh + 1):
                pointhigh_candleg.append(float(readout[i][1]))
                
            num_elementspointopen = 32
            pointopen_candleg = []
            for i in range(1, num_elementspointopen + 1):
                pointopen_candleg.append(float(readout[i][2]))
                
            num_elementspointclose = 32
            pointclose_candleg = []
            for i in range(1, num_elementspointclose + 1):
                pointclose_candleg.append(float(readout[i][3]))
                
            num_elementspointlow = 32
            pointlow_candleg = []
            for i in range(1, num_elementspointlow + 1):
                pointlow_candleg.append(float(readout[i][4]))
            
            num_elementstexts = 32
            texts_candleg = []
            for i in range(1, num_elementstexts + 1):
                texts_candleg.append(str(readout[i][5]))
                
            titlecandleg = str(readout[1][10])
            subtitlecandleg = str(readout[1][11])

            
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_3"] = npcandleg
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_12"] = minvcandleg
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_13"] = maxvcandleg
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_14"] = decimalcandleg
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_15"] = rncandleg
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_4"] = texts_candleg[0]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_5"] = texts_candleg[1]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_6"] = texts_candleg[2]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_7"] = texts_candleg[3]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_8"] = texts_candleg[4]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_9"] = texts_candleg[5]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_10"] = texts_candleg[6]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_11"] = texts_candleg[7]
        
        cube_objecttextcandle = bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]
        for i in range(8, 32):
            input_index = i - 8 + 71
            input_name = f"Input_{input_index:02d}"
            cube_objecttextcandle[input_name] = texts_candleg[i]
        
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_38"] = pointhigh_candleg[0]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_103"] = pointhigh_candleg[1] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_107"] = pointhigh_candleg[2]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_168"] = pointhigh_candleg[3] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_172"] = pointhigh_candleg[4]          
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_176"] = pointhigh_candleg[5]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_99"] = pointhigh_candleg[6]
        for i in range(7, 32):
            input_numpointhigh_candleg = 180 + (i - 7) * 4
            bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_" + str(input_numpointhigh_candleg)] = pointhigh_candleg[i]  
            
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_97"] = pointopen_candleg[0]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_104"] = pointopen_candleg[1] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_108"] = pointopen_candleg[2]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_169"] = pointopen_candleg[3] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_173"] = pointopen_candleg[4]          
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_177"] = pointopen_candleg[5]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_100"] = pointopen_candleg[6]
        for i in range(7, 32):
            input_numpointopen_candleg = 181 + (i - 7) * 4
            bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_" + str(input_numpointopen_candleg)] = pointopen_candleg[i]
            
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_98"] = pointclose_candleg[0]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_105"] = pointclose_candleg[1] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_109"] = pointclose_candleg[2]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_170"] = pointclose_candleg[3] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_174"] = pointclose_candleg[4]          
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_178"] = pointclose_candleg[5]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_101"] = pointclose_candleg[6]
        for i in range(7, 32):
            input_numpointclose_candleg = 182 + (i - 7) * 4
            bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_" + str(input_numpointclose_candleg)] = pointclose_candleg[i]
            
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_96"] = pointlow_candleg[0]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_106"] = pointlow_candleg[1] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_110"] = pointlow_candleg[2]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_171"] = pointlow_candleg[3] 
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_175"] = pointlow_candleg[4]          
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_179"] = pointlow_candleg[5]
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_102"] = pointlow_candleg[6]
        for i in range(7, 32):
            input_numpointlow_candleg = 183 + (i - 7) * 4
            bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_" + str(input_numpointlow_candleg)] = pointlow_candleg[i]        
    
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_23"] = titlecandleg
        bpy.data.objects[candle_object_name].modifiers["GeometryNodes"]["Input_22"] = subtitlecandleg
        
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
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_23pg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_23pg.type == 'MESH':
                        mesh_name_23pg = selected_obj_23pg.name

                        # Check if the selected object has modifiers
                        if selected_obj_23pg.modifiers:
                                modifier_name_23pg = selected_obj_23pg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_26"] = ncg23p
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_31"] = wta23p
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_32"] = wtb23p
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_33"] = wtc23p
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_2"] = wtpa23p
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_27"] = wtpb23p
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_28"] = wtpc23p
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_10"] = minv23p
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_11"] = maxv23p
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_15"] = title23p
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_17"] = subtitle23p
                                selected_obj_23pg.modifiers[modifier_name_23pg]["Input_19"] = desc23p

                                print(f"Set modifier input for object '{mesh_name_23pg}' and modifier '{modifier_name_23pg}'.")
                        else:
                                print(f"Selected object '{mesh_name_23pg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
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
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_pg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_pg.type == 'MESH':
                        mesh_name_pg = selected_obj_pg.name

                        # Check if the selected object has modifiers
                        if selected_obj_pg.modifiers:
                                modifier_name_pg = selected_obj_pg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_pg.modifiers[modifier_name_pg]["Input_2"] = gregorypercentagepg
                                selected_obj_pg.modifiers[modifier_name_pg]["Input_10"] = mallorypg
                                selected_obj_pg.modifiers[modifier_name_pg]["Input_11"] = olatunjipg
                                selected_obj_pg.modifiers[modifier_name_pg]["Input_15"] = titlepg
                                selected_obj_pg.modifiers[modifier_name_pg]["Input_17"] = subtitlepg
                                selected_obj_pg.modifiers[modifier_name_pg]["Input_19"] = percentpg

                                print(f"Set modifier input for object '{mesh_name_pg}' and modifier '{modifier_name_pg}'.")
                        else:
                                print(f"Selected object '{mesh_name_pg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
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
            value9lg = float(readout[9][1])
            value10lg = float(readout[10][1])
            value11lg = float(readout[11][1])
            value12lg = float(readout[12][1])
            value13lg = float(readout[13][1])
            value14lg = float(readout[14][1])
            value15lg = float(readout[15][1])
            value16lg = float(readout[16][1])
            value17lg = float(readout[17][1])
            value18lg = float(readout[18][1])
            value19lg = float(readout[19][1])
            value20lg = float(readout[20][1])
            value21lg = float(readout[21][1])
            value22lg = float(readout[22][1])
            value23lg = float(readout[23][1])
            value24lg = float(readout[24][1])
            value25lg = float(readout[25][1])
            value26lg = float(readout[26][1])
            value27lg = float(readout[27][1])
            value28lg = float(readout[28][1])
            value29lg = float(readout[29][1])
            value30lg = float(readout[30][1])
            text1lg = str(readout[1][2])
            text2lg = str(readout[2][2])
            text3lg = str(readout[3][2])
            text4lg = str(readout[4][2])
            text5lg = str(readout[5][2])
            text6lg = str(readout[6][2])
            text7lg = str(readout[7][2])
            text8lg = str(readout[8][2])
            text9lg = str(readout[9][2])
            text10lg = str(readout[10][2])
            text11lg = str(readout[11][2])
            text12lg = str(readout[12][2])
            text13lg = str(readout[13][2])
            text14lg = str(readout[14][2])
            text15lg = str(readout[15][2])
            text16lg = str(readout[16][2])
            text17lg = str(readout[17][2])
            text18lg = str(readout[18][2])
            text19lg = str(readout[19][2])
            text20lg = str(readout[20][2])
            text21lg = str(readout[21][2])
            text22lg = str(readout[22][2])
            text23lg = str(readout[23][2])
            text24lg = str(readout[24][2])
            text25lg = str(readout[25][2])
            text26lg = str(readout[26][2])
            text27lg = str(readout[27][2])
            text28lg = str(readout[28][2])
            text29lg = str(readout[29][2])
            text30lg = str(readout[30][2])
            titlelg = str(readout[1][7])
            subtitlelg = str(readout[1][8])
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj = bpy.context.active_object  # Get the active (selected) object

                if selected_obj.type == 'MESH':
                        mesh_name = selected_obj.name

                        # Check if the selected object has modifiers
                        if selected_obj.modifiers:
                                if len(selected_obj.modifiers) >= 2:  # Ensure at least two modifiers exist
                                        modifier_0 = selected_obj.modifiers.get("GeometryNodes")
                                        modifier_1 = selected_obj.modifiers.get("GeometryNodes.001")

                                if modifier_0 and modifier_1:
                                        modifier_0["Input_2"] = nplg
                                        modifier_0["Input_13"] = minvlg
                                        modifier_0["Input_14"] = maxvlg
                                        modifier_0["Input_15"] = decimallg
                                        modifier_0["Input_18"] = rnlg
                                        modifier_0["Input_4"] = value1lg
                                        modifier_0["Input_5"] = value2lg
                                        modifier_0["Input_6"] = value3lg
                                        modifier_0["Input_7"] = value4lg
                                        modifier_0["Input_8"] = value5lg
                                        modifier_0["Input_9"] = value6lg
                                        modifier_0["Input_10"] = value7lg
                                        modifier_0["Input_11"] = value8lg
                                        modifier_0["Socket_0"] = value9lg
                                        modifier_0["Socket_1"] = value10lg
                                        modifier_0["Socket_2"] = value11lg
                                        modifier_0["Socket_3"] = value12lg
                                        modifier_0["Socket_4"] = value13lg
                                        modifier_0["Socket_5"] = value14lg
                                        modifier_0["Socket_6"] = value15lg
                                        modifier_0["Socket_7"] = value16lg
                                        modifier_0["Socket_8"] = value17lg
                                        modifier_0["Socket_9"] = value18lg
                                        modifier_0["Socket_10"] = value19lg
                                        modifier_0["Socket_11"] = value20lg
                                        modifier_0["Socket_12"] = value21lg
                                        modifier_0["Socket_13"] = value22lg
                                        modifier_0["Socket_14"] = value23lg
                                        modifier_0["Socket_15"] = value24lg
                                        modifier_0["Socket_16"] = value25lg
                                        modifier_0["Socket_17"] = value26lg
                                        modifier_0["Socket_18"] = value27lg
                                        modifier_0["Socket_19"] = value28lg
                                        modifier_0["Socket_20"] = value29lg
                                        modifier_0["Socket_21"] = value30lg

                                        modifier_1["Input_4"] = text1lg
                                        modifier_1["Input_5"] = text2lg
                                        modifier_1["Input_6"] = text3lg
                                        modifier_1["Input_7"] = text4lg
                                        modifier_1["Input_8"] = text5lg
                                        modifier_1["Input_9"] = text6lg
                                        modifier_1["Input_10"] = text7lg
                                        modifier_1["Input_11"] = text8lg
                                        modifier_1["Socket_0"] = text9lg
                                        modifier_1["Socket_1"] = text10lg
                                        modifier_1["Socket_2"] = text11lg
                                        modifier_1["Socket_3"] = text12lg
                                        modifier_1["Socket_4"] = text13lg
                                        modifier_1["Socket_5"] = text14lg
                                        modifier_1["Socket_6"] = text15lg
                                        modifier_1["Socket_7"] = text16lg
                                        modifier_1["Socket_8"] = text17lg
                                        modifier_1["Socket_9"] = text18lg
                                        modifier_1["Socket_10"] = text19lg
                                        modifier_1["Socket_11"] = text20lg
                                        modifier_1["Socket_12"] = text21lg
                                        modifier_1["Socket_13"] = text22lg
                                        modifier_1["Socket_14"] = text23lg
                                        modifier_1["Socket_15"] = text24lg
                                        modifier_1["Socket_16"] = text25lg
                                        modifier_1["Socket_17"] = text26lg
                                        modifier_1["Socket_18"] = text27lg
                                        modifier_1["Socket_19"] = text28lg
                                        modifier_1["Socket_20"] = text29lg
                                        modifier_1["Socket_21"] = text30lg
                                        modifier_1["Input_23"] = titlelg
                                        modifier_1["Input_22"] = subtitlelg

                                        print(f"Set modifier input for object '{mesh_name}'.")
                                else:
                                        print("Selected object does not have both modifiers.")
                        else:
                                print(f"Selected object '{mesh_name}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        
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
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj = bpy.context.active_object  # Get the active (selected) object

                if selected_obj.type == 'MESH':
                        mesh_name = selected_obj.name

                        # Check if the selected object has modifiers
                        if selected_obj.modifiers:
                                if len(selected_obj.modifiers) >= 2:  # Ensure at least two modifiers exist
                                        modifier_0c = selected_obj.modifiers.get("GeometryNodes")
                                        modifier_1c = selected_obj.modifiers.get("GeometryNodes.001")

                                if modifier_0c and modifier_1c:
                                        modifier_0c["Input_2"] = nplgc
                                        modifier_0c["Input_13"] = minvlgc
                                        modifier_0c["Input_14"] = maxvlgc
                                        modifier_0c["Input_15"] = decimallgc
                                        modifier_0c["Input_18"] = rnlgc
                                        modifier_0c["Input_4"] = valuea1lgc
                                        modifier_0c["Input_5"] = valuea2lgc
                                        modifier_0c["Input_6"] = valuea3lgc
                                        modifier_0c["Input_7"] = valuea4lgc
                                        modifier_0c["Input_8"] = valuea5lgc
                                        modifier_0c["Input_9"] = valuea6lgc
                                        modifier_0c["Input_10"] = valuea7lgc
                                        modifier_0c["Input_11"] = valuea8lgc
                                        modifier_0c["Input_34"] = valueb1lgc
                                        modifier_0c["Input_35"] = valueb2lgc
                                        modifier_0c["Input_36"] = valueb3lgc
                                        modifier_0c["Input_37"] = valueb4lgc
                                        modifier_0c["Input_38"] = valueb5lgc
                                        modifier_0c["Input_39"] = valueb6lgc
                                        modifier_0c["Input_40"] = valueb7lgc
                                        modifier_0c["Input_41"] = valueb8lgc

                                        modifier_1c["Input_4"] = text1lgc
                                        modifier_1c["Input_5"] = text2lgc
                                        modifier_1c["Input_6"] = text3lgc
                                        modifier_1c["Input_7"] = text4lgc
                                        modifier_1c["Input_8"] = text5lgc
                                        modifier_1c["Input_9"] = text6lgc
                                        modifier_1c["Input_10"] = text7lgc
                                        modifier_1c["Input_11"] = text8lgc
                                        modifier_1c["Input_23"] = titlelgc
                                        modifier_1c["Input_22"] = subtitlelgc
                                        modifier_1c["Input_29"] = legendalgc
                                        modifier_1c["Input_30"] = legendblgc

                                        print(f"Set modifier input for object '{mesh_name}'.")
                                else:
                                        print("Selected object does not have both modifiers.")
                        else:
                                print(f"Selected object '{mesh_name}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")

        # Optionally, you can update the mesh data if needed.
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
            malloryhbar5 = float(readout[5][2])
            malloryhbar6 = float(readout[6][2])
            malloryhbar7 = float(readout[7][2])
            malloryhbar8 = float(readout[8][2])
            malloryhbar9 = float(readout[9][2])
            malloryhbar10 = float(readout[10][2])
            
            olatunjihbar1 = float(readout[1][3])
            olatunjihbar2 = float(readout[1][4])
            
            jeopardyhbar1 = int(readout[1][5])
            
            hogwashhbar1 = str(readout[1][1])
            hogwashhbar2 = str(readout[2][1])
            hogwashhbar3 = str(readout[3][1])
            hogwashhbar4 = str(readout[4][1])
            hogwashhbar5 = str(readout[5][1])
            hogwashhbar6 = str(readout[6][1])
            hogwashhbar7 = str(readout[7][1])
            hogwashhbar8 = str(readout[8][1])
            hogwashhbar9 = str(readout[9][1])
            hogwashhbar10 = str(readout[10][1])

            titlehbar1 = str(readout[1][6])
            subtitlehbar1 = str(readout[1][7])
            totalhbar1 = str(readout[1][8])
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_hbg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_hbg.type == 'MESH':
                        mesh_name_hbg = selected_obj_hbg.name

                        # Check if the selected object has modifiers
                        if selected_obj_hbg.modifiers:
                                modifier_name_hbg = selected_obj_hbg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_36"] = gregoryhbar
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_14"] = malloryhbar1
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_15"] = malloryhbar2
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_16"] = malloryhbar3
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_17"] = malloryhbar4
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_16"] = malloryhbar5
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_17"] = malloryhbar6
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_18"] = malloryhbar7
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_19"] = malloryhbar8
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_20"] = malloryhbar9
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_21"] = malloryhbar10
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_10"] = olatunjihbar1
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_11"] = olatunjihbar2
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_12"] = jeopardyhbar1
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_2"] = hogwashhbar1
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_3"] = hogwashhbar2
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_4"] = hogwashhbar3
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_5"] = hogwashhbar4
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_10"] = hogwashhbar5
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_11"] = hogwashhbar6
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_12"] = hogwashhbar7
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_13"] = hogwashhbar8
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_14"] = hogwashhbar9
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Socket_15"] = hogwashhbar10
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_7"] = titlehbar1
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_8"] = subtitlehbar1
                                selected_obj_hbg.modifiers[modifier_name_hbg]["Input_6"] = totalhbar1

                                print(f"Set modifier input for object '{mesh_name_hbg}' and modifier '{modifier_name_hbg}'.")
                        else:
                                print(f"Selected object '{mesh_name_hbg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
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
            bthbarc5 = str(readout[5][1])
            bthbarc6 = str(readout[6][1])
            bthbarc7 = str(readout[7][1])
            bthbarc8 = str(readout[8][1])
            bthbarc9 = str(readout[9][1])
            minvhbarc1 = float(readout[1][4])
            maxvhbarc2 = float(readout[1][5])
            decimalhbarc1 = int(readout[1][6])
            bvahbarc1 = float(readout[1][2])
            bvahbarc2 = float(readout[2][2])
            bvahbarc3 = float(readout[3][2])
            bvahbarc4 = float(readout[4][2])
            bvahbarc5 = float(readout[5][2])
            bvahbarc6 = float(readout[6][2])
            bvahbarc7 = float(readout[7][2])
            bvahbarc8 = float(readout[8][2])
            bvahbarc9 = float(readout[9][2])
            bvbhbarc1 = float(readout[1][3])
            bvbhbarc2 = float(readout[2][3])
            bvbhbarc3 = float(readout[3][3])
            bvbhbarc4 = float(readout[4][3])
            bvbhbarc5 = float(readout[5][3])
            bvbhbarc6 = float(readout[6][3])
            bvbhbarc7 = float(readout[7][3])
            bvbhbarc8 = float(readout[8][3])
            bvbhbarc9 = float(readout[9][3])
            titlehbarc1 = str(readout[1][7])
            subtitlehbarc1 = str(readout[1][8])
            legendhbarc1 = str(readout[1][9])
            legendhbarc2 = str(readout[2][9])
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_hbgc = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_hbgc.type == 'MESH':
                        mesh_name_hbgc = selected_obj_hbgc.name

                        # Check if the selected object has modifiers
                        if selected_obj_hbgc.modifiers:
                                modifier_name_hbgc = selected_obj_hbgc.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_45"] = nbhbarc
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_2"] = bthbarc1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_3"] = bthbarc2
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_4"] = bthbarc3
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_5"] = bthbarc4
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_66"] = bthbarc5
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_67"] = bthbarc6
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_68"] = bthbarc7
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_69"] = bthbarc8
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_70"] = bthbarc9
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_10"] = minvhbarc1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_11"] = maxvhbarc2
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_12"] = decimalhbarc1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_14"] = bvahbarc1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_15"] = bvahbarc2
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_16"] = bvahbarc3
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_17"] = bvahbarc4
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_71"] = bvahbarc5
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_73"] = bvahbarc6
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_75"] = bvahbarc7
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_77"] = bvahbarc8
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_79"] = bvahbarc9
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_36"] = bvbhbarc1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_37"] = bvbhbarc2
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_38"] = bvbhbarc3
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_39"] = bvbhbarc4
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_72"] = bvbhbarc5
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_74"] = bvbhbarc6
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_76"] = bvbhbarc7
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_78"] = bvbhbarc8
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_80"] = bvbhbarc9
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_7"] = titlehbarc1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_8"] = subtitlehbarc1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_6"] = legendhbarc1
                                selected_obj_hbgc.modifiers[modifier_name_hbgc]["Input_40"] = legendhbarc2

                                print(f"Set modifier input for object '{mesh_name_hbgc}' and modifier '{modifier_name_hbgc}'.")
                        else:
                                print(f"Selected object '{mesh_name_hbgc}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
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
            mallorymcircle6 = float(readout[6][2])
            mallorymcircle7 = float(readout[7][2])
            mallorymcircle8 = float(readout[8][2])
            hogwashmcircle1 = str(readout[1][1])
            hogwashmcircle2 = str(readout[2][1])
            hogwashmcircle3 = str(readout[3][1])
            hogwashmcircle4 = str(readout[4][1])
            hogwashmcircle5 = str(readout[5][1])
            hogwashmcircle6 = str(readout[6][1])
            hogwashmcircle7 = str(readout[7][1])
            hogwashmcircle8 = str(readout[8][1])
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
            mallorympercentage6 = float(mallorymcircle6/maxvaluemcircle)
            mallorympercentage7 = float(mallorymcircle7/maxvaluemcircle)
            mallorympercentage8 = float(mallorymcircle8/maxvaluemcircle)
             

            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_mcg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_mcg.type == 'MESH':
                        mesh_name_mcg = selected_obj_mcg.name

                        # Check if the selected object has modifiers
                        if selected_obj_mcg.modifiers:
                                modifier_name_mcg = selected_obj_mcg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_55"] = gregorymcircle
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_2"] = mallorympercentage1
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_12"] = mallorympercentage2
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_14"] = mallorympercentage3
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_15"] = mallorympercentage4
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_16"] = mallorympercentage5
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_7"] = mallorympercentage6
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_8"] = mallorympercentage7                               
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_9"] = mallorympercentage8                                
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_10"] = minvaluemcircle
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_11"] = maxvaluemcircle
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_18"] = decimalmcircle
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_40"] = titlemcircle
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_41"] = subtitlemcircle
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_42"] = hogwashmcircle1
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_43"] = hogwashmcircle2
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_44"] = hogwashmcircle3
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_46"] = hogwashmcircle4
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Input_45"] = hogwashmcircle5
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_13"] = hogwashmcircle6
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_18"] = hogwashmcircle7
                                selected_obj_mcg.modifiers[modifier_name_mcg]["Socket_23"] = hogwashmcircle8

                                print(f"Set modifier input for object '{mesh_name_mcg}' and modifier '{modifier_name_mcg}'.")
                        else:
                                print(f"Selected object '{mesh_name_mcg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
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
            mallorympie6 = float(readout[6][2])
            mallorympie7 = float(readout[7][2])
            mallorympie8 = float(readout[8][2])
            hogwashmpie1 = str(readout[1][1])
            hogwashmpie2 = str(readout[2][1])
            hogwashmpie3 = str(readout[3][1])
            hogwashmpie4 = str(readout[4][1])
            hogwashmpie5 = str(readout[5][1])
            hogwashmpie6 = str(readout[6][1])
            hogwashmpie7 = str(readout[7][1])
            hogwashmpie8 = str(readout[8][1])
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
            mallorympiepercentage6 = float(mallorympie6/maxvaluempie)
            mallorympiepercentage7 = float(mallorympie7/maxvaluempie)  
            mallorympiepercentage8 = float(mallorympie8/maxvaluempie)              
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_mpg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_mpg.type == 'MESH':
                        mesh_name_mpg = selected_obj_mpg.name

                        # Check if the selected object has modifiers
                        if selected_obj_mpg.modifiers:
                                modifier_name_mpg = selected_obj_mpg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_54"] = gregorympie
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_2"] = mallorympiepercentage1
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_12"] = mallorympiepercentage2
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_14"] = mallorympiepercentage3
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_15"] = mallorympiepercentage4
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_16"] = mallorympiepercentage5
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_93"] = mallorympiepercentage6
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Socket_0"] = mallorympiepercentage7
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Socket_1"] = mallorympiepercentage8
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_10"] = minvaluempie
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_11"] = maxvaluempie
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_18"] = decimalmpie
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_40"] = titlempie
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_41"] = subtitlempie
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_42"] = hogwashmpie1
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_43"] = hogwashmpie2
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_44"] = hogwashmpie3
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_46"] = hogwashmpie4
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_45"] = hogwashmpie5
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Input_88"] = hogwashmpie6
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Socket_4"] = hogwashmpie7
                                selected_obj_mpg.modifiers[modifier_name_mpg]["Socket_9"] = hogwashmpie8

                                print(f"Set modifier input for object '{mesh_name_mpg}' and modifier '{modifier_name_mpg}'.")
                        else:
                                print(f"Selected object '{mesh_name_mpg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
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
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_mg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_mg.type == 'MESH':
                        mesh_name_mg = selected_obj_mg.name

                        # Check if the selected object has modifiers
                        if selected_obj_mg.modifiers:
                                modifier_name_mg = selected_obj_mg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_mg.modifiers[modifier_name_mg]["Input_2"] = npmg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_22"] = minvmg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_24"] = maxvmg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_23"] = decimalmg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_21"] = rnmg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_3"] = value1mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_4"] = value2mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_5"] = value3mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_6"] = value4mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_7"] = value5mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_8"] = value6mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_9"] = value7mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_10"] = value8mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_13"] = text1mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_14"] = text2mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_15"] = text3mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_16"] = text4mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_17"] = text5mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_18"] = text6mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_19"] = text7mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_20"] = text8mg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_38"] = titlemg
                                selected_obj_mg.modifiers[modifier_name_mg]["Input_39"] = subtitlemg

                                print(f"Set modifier input for object '{mesh_name_mg}' and modifier '{modifier_name_mg}'.")
                        else:
                                print(f"Selected object '{mesh_name_mg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
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
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_mgc = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_mgc.type == 'MESH':
                        mesh_name_mgc = selected_obj_mgc.name

                        # Check if the selected object has modifiers
                        if selected_obj_mgc.modifiers:
                                modifier_name_mgc = selected_obj_mgc.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_2"] = npmgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_22"] = minvmgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_24"] = maxvmgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_23"] = decimalmgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_21"] = rnmgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_3"] = valuea1mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_4"] = valuea2mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_67"] = valuea3mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_6"] = valuea4mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_7"] = valuea5mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_8"] = valuea6mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_9"] = valuea7mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_10"] = valuea8mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_30"] = valueb1mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_39"] = valueb2mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_40"] = valueb3mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_41"] = valueb4mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_42"] = valueb5mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_43"] = valueb6mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_44"] = valueb7mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_45"] = valueb8mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_13"] = text1mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_14"] = text2mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_15"] = text3mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_16"] = text4mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_17"] = text5mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_18"] = text6mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_19"] = text7mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_20"] = text8mgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_54"] = titlemgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_55"] = subtitlemgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_57"] = legendamgc
                                selected_obj_mgc.modifiers[modifier_name_mgc]["Input_56"] = legendbmgc

                                print(f"Set modifier input for object '{mesh_name_mgc}' and modifier '{modifier_name_mgc}'.")
                        else:
                                print(f"Selected object '{mesh_name_mgc}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}
    
class MyoperatorUSMcsv(bpy.types.Operator):
    bl_idname = "mesh.mycubeoperatorusmapcsv"
    bl_label = "Import csv"
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        usmap_object = bpy.context.view_layer.objects.active
        usmap_object_name = usmap_object.name
        filepath_fullusmap = bpy.path.abspath(mytool.my_pathusmap)
        with open(filepath_fullusmap) as f:
            readout = list(csv.reader(f))
            minvusmap = float(readout[1][2])
            maxvusmap = float(readout[1][3])
            decimalusmap = int(readout[1][4])

            num_elementsstatename = 50
            statename_usmap = []
            for i in range(1, num_elementsstatename + 2):
                statename_usmap.append(str(readout[i][0]))
                
            num_elementsstatevalue = 50
            statevalue_usmap = []
            for i in range(1, num_elementsstatevalue + 2):
                statevalue_usmap.append(float(readout[i][1]))              
                
            titleusmap = str(readout[1][5])
            subtitleusmap = str(readout[1][6])
            sourcetitleusmap = str(readout[1][7])
            sourcesubtitleusmap = str(readout[1][8])
            credittitleusmap = str(readout[1][9])
            creditsubtitleusmap = str(readout[1][10])

            
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_112"] = minvusmap
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_113"] = maxvusmap
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_168"] = decimalusmap
        
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_185"] = statename_usmap[0]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_184"] = statename_usmap[1]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_183"] = statename_usmap[2]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_182"] = statename_usmap[3]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_181"] = statename_usmap[4]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_180"] = statename_usmap[5]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_179"] = statename_usmap[6]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_178"] = statename_usmap[7]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_177"] = statename_usmap[8]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_176"] = statename_usmap[9]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_175"] = statename_usmap[10]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_174"] = statename_usmap[11]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_173"] = statename_usmap[12]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_172"] = statename_usmap[13]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_171"] = statename_usmap[14]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_170"] = statename_usmap[15]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_167"] = statename_usmap[16]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_186"] = statename_usmap[17]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_187"] = statename_usmap[18]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_188"] = statename_usmap[19]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_189"] = statename_usmap[20]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_190"] = statename_usmap[21]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_191"] = statename_usmap[22]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_192"] = statename_usmap[23]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_193"] = statename_usmap[24]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_194"] = statename_usmap[25]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_195"] = statename_usmap[26]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_196"] = statename_usmap[27]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_197"] = statename_usmap[28]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_198"] = statename_usmap[29]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_199"] = statename_usmap[30]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_200"] = statename_usmap[31]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_201"] = statename_usmap[32]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_202"] = statename_usmap[33]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_203"] = statename_usmap[34]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_204"] = statename_usmap[35]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_205"] = statename_usmap[36]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_206"] = statename_usmap[37]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_207"] = statename_usmap[38]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_208"] = statename_usmap[39]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_209"] = statename_usmap[40]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_210"] = statename_usmap[41]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_211"] = statename_usmap[42]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_212"] = statename_usmap[43]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_213"] = statename_usmap[44]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_214"] = statename_usmap[45]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_215"] = statename_usmap[46]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_216"] = statename_usmap[47]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_217"] = statename_usmap[48]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_218"] = statename_usmap[49]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_219"] = statename_usmap[50]



            
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_13"] = statevalue_usmap[0]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_14"] = statevalue_usmap[1] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_15"] = statevalue_usmap[2]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_16"] = statevalue_usmap[3] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_17"] = statevalue_usmap[4]          
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_18"] = statevalue_usmap[5]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_19"] = statevalue_usmap[6] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_20"] = statevalue_usmap[7] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_62"] = statevalue_usmap[8]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_21"] = statevalue_usmap[9]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_22"] = statevalue_usmap[10] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_23"] = statevalue_usmap[11] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_24"] = statevalue_usmap[12] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_25"] = statevalue_usmap[13] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_26"] = statevalue_usmap[14] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_27"] = statevalue_usmap[15]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_12"] = statevalue_usmap[16]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_28"] = statevalue_usmap[17]  
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_29"] = statevalue_usmap[18] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_30"] = statevalue_usmap[19]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_31"] = statevalue_usmap[20]  
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_32"] = statevalue_usmap[21]  
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_33"] = statevalue_usmap[22]  
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_34"] = statevalue_usmap[23] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_166"] = statevalue_usmap[24]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_35"] = statevalue_usmap[25] 
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_36"] = statevalue_usmap[26]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_37"] = statevalue_usmap[27]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_38"] = statevalue_usmap[28]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_39"] = statevalue_usmap[29]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_40"] = statevalue_usmap[30]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_41"] = statevalue_usmap[31]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_42"] = statevalue_usmap[32]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_43"] = statevalue_usmap[33]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_44"] = statevalue_usmap[34]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_45"] = statevalue_usmap[35]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_46"] = statevalue_usmap[36]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_47"] = statevalue_usmap[37]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_48"] = statevalue_usmap[38]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_49"] = statevalue_usmap[39]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_50"] = statevalue_usmap[40]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_51"] = statevalue_usmap[41]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_52"] = statevalue_usmap[42]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_53"] = statevalue_usmap[43]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_54"] = statevalue_usmap[44]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_55"] = statevalue_usmap[45]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_56"] = statevalue_usmap[46]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_57"] = statevalue_usmap[47]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_58"] = statevalue_usmap[48]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_59"] = statevalue_usmap[49]
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_60"] = statevalue_usmap[50]
           
    
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_232"] = titleusmap
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_233"] = subtitleusmap
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_234"] = sourcetitleusmap
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_235"] = sourcesubtitleusmap
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_236"] = credittitleusmap
        bpy.data.objects[usmap_object_name].modifiers["GeometryNodes"]["Input_237"] = creditsubtitleusmap
        
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
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_vbg = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_vbg.type == 'MESH':
                        mesh_name_vbg = selected_obj_vbg.name

                        # Check if the selected object has modifiers
                        if selected_obj_vbg.modifiers:
                                modifier_name_vbg = selected_obj_vbg.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_57"] = gregoryvb
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_14"] = malloryvb1
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_41"] = malloryvb2
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_15"] = malloryvb3
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_44"] = malloryvb4
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_16"] = malloryvb5
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_48"] = malloryvb6
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_17"] = malloryvb7
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_50"] = malloryvb8
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_10"] = olatunjivb1
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_11"] = olatunjivb2
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_12"] = jeopardyvb1
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_2"] = hogwashvb1
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_42"] = hogwashvb2
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_3"] = hogwashvb3
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_45"] = hogwashvb4
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_4"] = hogwashvb5
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_47"] = hogwashvb6
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_5"] = hogwashvb7
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_49"] = hogwashvb8
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_7"] = titlevb1
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_8"] = subtitlevb1
                                selected_obj_vbg.modifiers[modifier_name_vbg]["Input_6"] = totalvb1

                                print(f"Set modifier input for object '{mesh_name_vbg}' and modifier '{modifier_name_vbg}'.")
                        else:
                                print(f"Selected object '{mesh_name_vbg}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
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
            
        # Ensure an object is selected
        if bpy.context.selected_objects:
                selected_obj_vbgc = bpy.context.active_object  # Get the active (selected) object

                if selected_obj_vbgc.type == 'MESH':
                        mesh_name_vbgc = selected_obj_vbgc.name

                        # Check if the selected object has modifiers
                        if selected_obj_vbgc.modifiers:
                                modifier_name_vbgc = selected_obj_vbgc.modifiers.active.name  # Get the name of the active modifier

                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_71"] = nbvbc
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_2"] = btvbc1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_42"] = btvbc2
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_3"] = btvbc3
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_45"] = btvbc4
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_4"] = btvbc5
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_47"] = btvbc6
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_5"] = btvbc7
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_49"] = btvbc8
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_10"] = minvvbc1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_11"] = maxvvbc2
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_12"] = decimalvbc1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_14"] = bvavbc1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_41"] = bvavbc2
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_15"] = bvavbc3
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_44"] = bvavbc4
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_16"] = bvavbc5
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_48"] = bvavbc6
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_17"] = bvavbc7
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_50"] = bvavbc8
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_57"] = bvbvbc1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_58"] = bvbvbc2
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_59"] = bvbvbc3
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_64"] = bvbvbc4
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_60"] = bvbvbc5
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_61"] = bvbvbc6
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_62"] = bvbvbc7
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_63"] = bvbvbc8
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_7"] = titlevbc1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_8"] = subtitlevbc1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_70"] = legendvbc1
                                selected_obj_vbgc.modifiers[modifier_name_vbgc]["Input_69"] = legendvbc2


                                print(f"Set modifier input for object '{mesh_name_vbgc}' and modifier '{modifier_name_vbgc}'.")
                        else:
                                print(f"Selected object '{mesh_name_vbgc}' has no modifiers.")
                else:
                        print("Selected object is not a mesh.")
        else:
                print("No object selected.")
        bpy.context.object.data.update()
        return {'FINISHED'}   
        
class ADDONNAME_OT_my_opc(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorgg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_44"]'
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
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_89"]'
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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

class ADDONNAME_OT_my_opMCGFL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormcgfl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_4"]'
        index = 0
        stringMCGFC = mytool.my_floatMCGF
        frMCGFC = bpy.context.scene.render.fps
        jeffmcgf = stringMCGFC*frMCGFC
        onemoremcgf =  (mytool.my_floatMCGLF*frMCGFC) + jeffmcgf
        bobmcgf = onemoremcgf     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmcgf = int(bobmcgf)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmcgf
                kps.handle_left[0] = jeffmcgf-6
                kps.handle_right[0] = jeffmcgf
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmcgf
                kpz.handle_left[0] = bobmcgf-6
                kpz.handle_right[0] = bobmcgf+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmcgf+(frMCGFC*2)
                
class ADDONNAME_OT_my_opMCGGL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormcggl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_5"]'
        index = 0
        stringMCGGC = mytool.my_floatMCGG
        frMCGGC = bpy.context.scene.render.fps
        jeffmcgg = stringMCGGC*frMCGGC
        onemoremcgg =  (mytool.my_floatMCGLG*frMCGGC) + jeffmcgg
        bobmcgg = onemoremcgg     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmcgg = int(bobmcgg)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmcgg
                kps.handle_left[0] = jeffmcgg-6
                kps.handle_right[0] = jeffmcgg
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmcgg
                kpz.handle_left[0] = bobmcgg-6
                kpz.handle_right[0] = bobmcgg+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmcgg+(frMCGGC*2)
                
class ADDONNAME_OT_my_opMCGHL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormcghl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_6"]'
        index = 0
        stringMCGHC = mytool.my_floatMCGH
        frMCGHC = bpy.context.scene.render.fps
        jeffmcgh = stringMCGHC*frMCGHC
        onemoremcgh =  (mytool.my_floatMCGLH*frMCGHC) + jeffmcgh
        bobmcgh = onemoremcgh     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmcgh = int(bobmcgh)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmcgh
                kps.handle_left[0] = jeffmcgh-6
                kps.handle_right[0] = jeffmcgh
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmcgh
                kpz.handle_left[0] = bobmcgh-6
                kpz.handle_right[0] = bobmcgh+6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmcgh+(frMCGHC*2)

             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opMPGAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormpgal"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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

class ADDONNAME_OT_my_opMPGFL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormpgfl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_95"]'
        index = 0
        stringMPGFC = mytool.my_floatMPGF
        frMPGFC = bpy.context.scene.render.fps
        jeffmpgf = stringMPGFC * frMPGFC
        onemorempgf = (mytool.my_floatMPGLF * frMPGFC) + jeffmpgf
        bobmpgf = onemorempgf     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmpgf = int(bobmpgf)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmpgf
                kps.handle_left[0] = jeffmpgf - 6
                kps.handle_right[0] = jeffmpgf
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmpgf
                kpz.handle_left[0] = bobmpgf - 6
                kpz.handle_right[0] = bobmpgf + 6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmpgf + (frMPGFC * 2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opMPGGL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormpggl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_2"]'
        index = 0
        stringMPGGC = mytool.my_floatMPGG
        frMPGGC = bpy.context.scene.render.fps
        jeffmpgg = stringMPGGC * frMPGGC
        onemorempgg = (mytool.my_floatMPGLG * frMPGGC) + jeffmpgg
        bobmpgg = onemorempgg     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmpgg = int(bobmpgg)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmpgg
                kps.handle_left[0] = jeffmpgg - 6
                kps.handle_right[0] = jeffmpgg
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmpgg
                kpz.handle_left[0] = bobmpgg - 6
                kpz.handle_right[0] = bobmpgg + 6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmpgg + (frMPGGC * 2)


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opMPGHL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatormpghl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_3"]'
        index = 0
        stringMPGHC = mytool.my_floatMPGH
        frMPGHC = bpy.context.scene.render.fps
        jeffmpgh = stringMPGHC * frMPGHC
        onemorempgh = (mytool.my_floatMPGLH * frMPGHC) + jeffmpgh
        bobmpgh = onemorempgh     

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobmpgh = int(bobmpgh)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffmpgh
                kps.handle_left[0] = jeffmpgh - 6
                kps.handle_right[0] = jeffmpgh
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobmpgh
                kpz.handle_left[0] = bobmpgh - 6
                kpz.handle_right[0] = bobmpgh + 6
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobmpgh + (frMPGHC * 2)


             
        return {'FINISHED'}

    
class ADDONNAME_OT_my_opggpie(bpy.types.Operator):
    bl_label = "Add Objecggggggtpie"
    bl_idname = "addonname.myop_operatorggpie"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
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
    
        if mytool.my_enumLGpie == 'OPLG7pie':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 96

            action_name = 'Line GraphAction'
            data_paths = ['modifiers["GeometryNodes"]["Socket_44"]']
            index = 0              # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
                    if fcurve:
                        fcurve.keyframe_points[0].co.x = 24
                        fcurve.keyframe_points[0].handle_left[0] = 8
                        fcurve.keyframe_points[0].handle_left[1] = 0
                        fcurve.keyframe_points[0].handle_right[0] = 37
                        fcurve.keyframe_points[0].handle_right[1] = 0
                        fcurve.keyframe_points[1].co.x = 72
                        fcurve.keyframe_points[1].handle_left[0] = 47
                        fcurve.keyframe_points[1].handle_left[1] = 0.976
                        fcurve.keyframe_points[1].handle_right[0] = 77
                        fcurve.keyframe_points[1].handle_right[1] = 1.005

                        print("changed")
                    else:
                        print("no fcurve")
                else:
                    print("no action")

            print("end")

            action_name = 'Line GraphAction'
            data_paths = ['modifiers["GeometryNodes"]["Socket_89"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
                    if fcurve:
                        fcurve.keyframe_points[0].co.x = 60
                        fcurve.keyframe_points[0].handle_left[0] = 56
                        fcurve.keyframe_points[0].handle_left[1] = 1
                        fcurve.keyframe_points[0].handle_right[0] = 64
                        fcurve.keyframe_points[0].handle_right[1] = 1
                        fcurve.keyframe_points[1].co.x = 72
                        fcurve.keyframe_points[1].handle_left[0] = 68
                        fcurve.keyframe_points[1].handle_left[1] = 0
                        fcurve.keyframe_points[1].handle_right[0] = 79
                        fcurve.keyframe_points[1].handle_right[1] = 0

                        print("changed")
                    else:
                        print("no fcurve")
                else:
                    print("no action")

            print("end")

            
        if mytool.my_enumLGpie == 'OPLG8pie':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 120
            
            action_name = 'Line GraphAction'
            data_paths = ['modifiers["GeometryNodes"]["Socket_44"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
                    if fcurve:
                        fcurve.keyframe_points[0].co.x = 30
                        fcurve.keyframe_points[0].handle_left[0] = 8
                        fcurve.keyframe_points[0].handle_left[1] = 0
                        fcurve.keyframe_points[0].handle_right[0] = 54.597
                        fcurve.keyframe_points[0].handle_right[1] = 0
                        fcurve.keyframe_points[1].co.x = 90
                        fcurve.keyframe_points[1].handle_left[0] = 65.419
                        fcurve.keyframe_points[1].handle_left[1] = 1
                        fcurve.keyframe_points[1].handle_right[0] = 90.005
                        fcurve.keyframe_points[1].handle_right[1] = 1

                        print("changed")
                    else:
                        print("no fcurve")
                else:
                    print("no action")

            print("end")

            action_name = 'Line GraphAction'
            data_paths = ['modifiers["GeometryNodes"]["Socket_89"]']
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
                    if fcurve:
                        fcurve.keyframe_points[0].co.x = 75
                        fcurve.keyframe_points[0].handle_left[0] = 70
                        fcurve.keyframe_points[0].handle_left[1] = 0.995
                        fcurve.keyframe_points[0].handle_right[0] = 83.275
                        fcurve.keyframe_points[0].handle_right[1] = 1.009
                        fcurve.keyframe_points[1].co.x = 90
                        fcurve.keyframe_points[1].handle_left[0] = 80.733
                        fcurve.keyframe_points[1].handle_left[1] = 0
                        fcurve.keyframe_points[1].handle_right[0] = 95
                        fcurve.keyframe_points[1].handle_right[1] = 0

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

            action_name = 'Plane.004Action.005'
            data_paths = ['modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]', 'modifiers["GeometryNodes"]["Socket_0"]', 'modifiers["GeometryNodes"]["Socket_3"]', 'modifiers["GeometryNodes"]["Socket_4"]', 'modifiers["GeometryNodes"]["Socket_5"]', 'modifiers["GeometryNodes"]["Socket_6"]', 'modifiers["GeometryNodes"]["Socket_7"]']
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
            
            action_name = 'Plane.004Action.005'
            data_paths = ['modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]', 'modifiers["GeometryNodes"]["Socket_0"]', 'modifiers["GeometryNodes"]["Socket_3"]', 'modifiers["GeometryNodes"]["Socket_4"]', 'modifiers["GeometryNodes"]["Socket_5"]', 'modifiers["GeometryNodes"]["Socket_6"]', 'modifiers["GeometryNodes"]["Socket_7"]']
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
    
class ADDONNAME_OT_my_opHBGEL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorhbgel"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_0"]'
        index = 0
        stringHBGE = mytool.my_floatHBGE
        frHBGE = bpy.context.scene.render.fps
        jeffHBGEl = stringHBGE*frHBGE
        onemoreHBGEl =  (mytool.my_floatHBGLE*frHBGE) + jeffHBGEl
        bobHBGEl = onemoreHBGEl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobHBGEl = int(bobHBGEl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffHBGEl
                kps.handle_left[0] = jeffHBGEl-30
                kps.handle_right[0] = jeffHBGEl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobHBGEl
                kpz.handle_left[0] = bobHBGEl-30
                kpz.handle_right[0] = bobHBGEl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobHBGEl+frHBGE


             
        return {'FINISHED'}

class ADDONNAME_OT_my_opHBGFL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorhbgfl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_3"]'
        index = 0
        stringHBGF = mytool.my_floatHBGF
        frHBGF = bpy.context.scene.render.fps
        jeffHBGFl = stringHBGF*frHBGF
        onemoreHBGFl =  (mytool.my_floatHBGLF*frHBGF) + jeffHBGFl
        bobHBGFl = onemoreHBGFl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobHBGFl = int(bobHBGFl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffHBGFl
                kps.handle_left[0] = jeffHBGFl-30
                kps.handle_right[0] = jeffHBGFl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobHBGFl
                kpz.handle_left[0] = bobHBGFl-30
                kpz.handle_right[0] = bobHBGFl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobHBGFl+frHBGF


             
        return {'FINISHED'}   
    
class ADDONNAME_OT_my_opHBGGL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorhbggl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_4"]'
        index = 0
        stringHBGG = mytool.my_floatHBGG
        frHBGG = bpy.context.scene.render.fps
        jeffHBGGl = stringHBGG*frHBGG
        onemoreHBGGl =  (mytool.my_floatHBGLG*frHBGG) + jeffHBGGl
        bobHBGGl = onemoreHBGGl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobHBGGl = int(bobHBGGl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffHBGGl
                kps.handle_left[0] = jeffHBGGl-30
                kps.handle_right[0] = jeffHBGGl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobHBGGl
                kpz.handle_left[0] = bobHBGGl-30
                kpz.handle_right[0] = bobHBGGl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobHBGGl+frHBGG


             
        return {'FINISHED'} 
    
class ADDONNAME_OT_my_opHBGHL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorhbghl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_5"]'
        index = 0
        stringHBGH = mytool.my_floatHBGH
        frHBGH = bpy.context.scene.render.fps
        jeffHBGHl = stringHBGH*frHBGH
        onemoreHBGHl =  (mytool.my_floatHBGLH*frHBGH) + jeffHBGHl
        bobHBGHl = onemoreHBGHl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobHBGHl = int(bobHBGHl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffHBGHl
                kps.handle_left[0] = jeffHBGHl-30
                kps.handle_right[0] = jeffHBGHl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobHBGHl
                kpz.handle_left[0] = bobHBGHl-30
                kpz.handle_right[0] = bobHBGHl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobHBGHl+frHBGH


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opHBGIL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorhbgil"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_6"]'
        index = 0
        stringHBGI = mytool.my_floatHBGI
        frHBGI = bpy.context.scene.render.fps
        jeffHBGIl = stringHBGI*frHBGI
        onemoreHBGIl =  (mytool.my_floatHBGLI*frHBGI) + jeffHBGIl
        bobHBGIl = onemoreHBGIl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobHBGIl = int(bobHBGIl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffHBGIl
                kps.handle_left[0] = jeffHBGIl-30
                kps.handle_right[0] = jeffHBGIl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobHBGIl
                kpz.handle_left[0] = bobHBGIl-30
                kpz.handle_right[0] = bobHBGIl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobHBGIl+frHBGI


             
        return {'FINISHED'}
    
class ADDONNAME_OT_my_opHBGJL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorhbgjl"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Socket_7"]'
        index = 0
        stringHBGJ = mytool.my_floatHBGJ
        frHBGJ = bpy.context.scene.render.fps
        jeffHBGJl = stringHBGJ*frHBGJ
        onemoreHBGJl =  (mytool.my_floatHBGLJ*frHBGJ) + jeffHBGJl
        bobHBGJl = onemoreHBGJl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path = data_path, index = index)
            if fcurve:
                # Iterate over all keyframes
                
                bobHBGJl = int(bobHBGJl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffHBGJl
                kps.handle_left[0] = jeffHBGJl-30
                kps.handle_right[0] = jeffHBGJl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobHBGJl
                kpz.handle_left[0] = bobHBGJl-30
                kpz.handle_right[0] = bobHBGJl+30
                                               
                #fcurve.keyframe_points[0].co.x = 1
                #fcurve.keyframe_points[1].co.x = bob
                
                
                
                bpy.context.scene.frame_end = bobHBGJl+frHBGJ


             
        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONAHBARAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonahbara"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
    
class ADDONNAME_OT_my_opCOMPARISONAHBARE(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonahbare"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_81"]'
        index = 0
        stringCAHBARE = mytool.my_floatCOMPARISONAHBARE
        frCAHBARE = bpy.context.scene.render.fps
        jeffCAHBAREl = stringCAHBARE * frCAHBARE
        onemorecahbarel = (mytool.my_floatCOMPARISONAHBARLE * frCAHBARE) + jeffCAHBAREl
        bobCAHBAREl = onemorecahbarel       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAHBAREl = int(bobCAHBAREl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAHBAREl
                kps.handle_left[0] = jeffCAHBAREl - 30
                kps.handle_right[0] = jeffCAHBAREl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAHBAREl
                kpz.handle_left[0] = bobCAHBAREl - 30
                kpz.handle_right[0] = bobCAHBAREl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAHBAREl + frCAHBARE

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONAHBARF(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonahbarf"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_82"]'
        index = 0
        stringCAHBARF = mytool.my_floatCOMPARISONAHBARF
        frCAHBARF = bpy.context.scene.render.fps
        jeffCAHBARFl = stringCAHBARF * frCAHBARF
        onemorecahbarfl = (mytool.my_floatCOMPARISONAHBARLF * frCAHBARF) + jeffCAHBARFl
        bobCAHBARFl = onemorecahbarfl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAHBARFl = int(bobCAHBARFl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAHBARFl
                kps.handle_left[0] = jeffCAHBARFl - 30
                kps.handle_right[0] = jeffCAHBARFl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAHBARFl
                kpz.handle_left[0] = bobCAHBARFl - 30
                kpz.handle_right[0] = bobCAHBARFl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAHBARFl + frCAHBARF

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONAHBARG(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonahbarg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_83"]'
        index = 0
        stringCAHBARG = mytool.my_floatCOMPARISONAHBARG
        frCAHBARG = bpy.context.scene.render.fps
        jeffCAHBARGl = stringCAHBARG * frCAHBARG
        onemorecahbargl = (mytool.my_floatCOMPARISONAHBARLG * frCAHBARG) + jeffCAHBARGl
        bobCAHBARGl = onemorecahbargl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAHBARGl = int(bobCAHBARGl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAHBARGl
                kps.handle_left[0] = jeffCAHBARGl - 30
                kps.handle_right[0] = jeffCAHBARGl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAHBARGl
                kpz.handle_left[0] = bobCAHBARGl - 30
                kpz.handle_right[0] = bobCAHBARGl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAHBARGl + frCAHBARG

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONAHBARH(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonahbarh"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_84"]'
        index = 0
        stringCAHBARH = mytool.my_floatCOMPARISONAHBARH
        frCAHBARH = bpy.context.scene.render.fps
        jeffCAHBARHl = stringCAHBARH * frCAHBARH
        onemorecahbarhl = (mytool.my_floatCOMPARISONAHBARLH * frCAHBARH) + jeffCAHBARHl
        bobCAHBARHl = onemorecahbarhl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAHBARHl = int(bobCAHBARHl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAHBARHl
                kps.handle_left[0] = jeffCAHBARHl - 30
                kps.handle_right[0] = jeffCAHBARHl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAHBARHl
                kpz.handle_left[0] = bobCAHBARHl - 30
                kpz.handle_right[0] = bobCAHBARHl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAHBARHl + frCAHBARH

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONAHBARI(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonahbari"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_85"]'
        index = 0
        stringCAHBARI = mytool.my_floatCOMPARISONAHBARI
        frCAHBARI = bpy.context.scene.render.fps
        jeffCAHBARIl = stringCAHBARI * frCAHBARI
        onemorecahbaril = (mytool.my_floatCOMPARISONAHBARLI * frCAHBARI) + jeffCAHBARIl
        bobCAHBARIl = onemorecahbaril       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCAHBARIl = int(bobCAHBARIl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCAHBARIl
                kps.handle_left[0] = jeffCAHBARIl - 30
                kps.handle_right[0] = jeffCAHBARIl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCAHBARIl
                kpz.handle_left[0] = bobCAHBARIl - 30
                kpz.handle_right[0] = bobCAHBARIl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCAHBARIl + frCAHBARI

        return {'FINISHED'}

class ADDONNAME_OT_my_opCOMPARISONBHBARAL(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonbhbara"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
    
class ADDONNAME_OT_my_opCOMPARISONBHBARE(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonbhbare"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_81"]'
        index = 0
        stringCBHBARE = mytool.my_floatCOMPARISONBHBARE
        frCBHBARE = bpy.context.scene.render.fps
        jeffCBHBAREl = stringCBHBARE * frCBHBARE
        onemorecbhbarel = (mytool.my_floatCOMPARISONBHBARLE * frCBHBARE) + jeffCBHBAREl
        bobCBHBAREl = onemorecbhbarel       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBHBAREl = int(bobCBHBAREl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBHBAREl
                kps.handle_left[0] = jeffCBHBAREl - 30
                kps.handle_right[0] = jeffCBHBAREl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBHBAREl
                kpz.handle_left[0] = bobCBHBAREl - 30
                kpz.handle_right[0] = bobCBHBAREl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBHBAREl + frCBHBARE

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONBHBARF(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonbhbarf"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_82"]'
        index = 0
        stringCBHBARF = mytool.my_floatCOMPARISONBHBARF
        frCBHBARF = bpy.context.scene.render.fps
        jeffCBHBARFl = stringCBHBARF * frCBHBARF
        onemorecbhbarfl = (mytool.my_floatCOMPARISONBHBARLF * frCBHBARF) + jeffCBHBARFl
        bobCBHBARFl = onemorecbhbarfl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBHBARFl = int(bobCBHBARFl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBHBARFl
                kps.handle_left[0] = jeffCBHBARFl - 30
                kps.handle_right[0] = jeffCBHBARFl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBHBARFl
                kpz.handle_left[0] = bobCBHBARFl - 30
                kpz.handle_right[0] = bobCBHBARFl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBHBARFl + frCBHBARF

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONBHBARG(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonbhbarg"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_83"]'
        index = 0
        stringCBHBARG = mytool.my_floatCOMPARISONBHBARG
        frCBHBARG = bpy.context.scene.render.fps
        jeffCBHBARGl = stringCBHBARG * frCBHBARG
        onemorecbhbargl = (mytool.my_floatCOMPARISONBHBARLG * frCBHBARG) + jeffCBHBARGl
        bobCBHBARGl = onemorecbhbargl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBHBARGl = int(bobCBHBARGl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBHBARGl
                kps.handle_left[0] = jeffCBHBARGl - 30
                kps.handle_right[0] = jeffCBHBARGl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBHBARGl
                kpz.handle_left[0] = bobCBHBARGl - 30
                kpz.handle_right[0] = bobCBHBARGl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBHBARGl + frCBHBARG

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONBHBARH(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonbhbarh"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_84"]'
        index = 0
        stringCBHBARH = mytool.my_floatCOMPARISONBHBARH
        frCBHBARH = bpy.context.scene.render.fps
        jeffCBHBARHl = stringCBHBARH * frCBHBARH
        onemorecbhbarhl = (mytool.my_floatCOMPARISONBHBARLH * frCBHBARH) + jeffCBHBARHl
        bobCBHBARHl = onemorecbhbarhl       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBHBARHl = int(bobCBHBARHl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBHBARHl
                kps.handle_left[0] = jeffCBHBARHl - 30
                kps.handle_right[0] = jeffCBHBARHl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBHBARHl
                kpz.handle_left[0] = bobCBHBARHl - 30
                kpz.handle_right[0] = bobCBHBARHl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBHBARHl + frCBHBARH

        return {'FINISHED'}
    
class ADDONNAME_OT_my_opCOMPARISONBHBARI(bpy.types.Operator):
    bl_label = "Add Objecggggggt"
    bl_idname = "addonname.myop_operatorcomparisonbhbari"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        action_name = bpy.context.active_object.animation_data.action.name
        data_path = 'modifiers["GeometryNodes"]["Input_85"]'
        index = 0
        stringCBHBARI = mytool.my_floatCOMPARISONBHBARI
        frCBHBARI = bpy.context.scene.render.fps
        jeffCBHBARIl = stringCBHBARI * frCBHBARI
        onemorecbhbaril = (mytool.my_floatCOMPARISONBHBARLI * frCBHBARI) + jeffCBHBARIl
        bobCBHBARIl = onemorecbhbaril       

        # Find the appropriate action
        action = bpy.data.actions.get(action_name)
        if action:
            # From this action, retrieve the appropriate F-Curve
            fcurve = action.fcurves.find(data_path=data_path, index=index)
            if fcurve:
                # Iterate over all keyframes
                
                bobCBHBARIl = int(bobCBHBARIl)
                
                kps = fcurve.keyframe_points[0]
                kps.co.x = jeffCBHBARIl
                kps.handle_left[0] = jeffCBHBARIl - 30
                kps.handle_right[0] = jeffCBHBARIl
                kps.handle_right[1] = 0.6        
                
                kpz = fcurve.keyframe_points[1]
                kpz.co.x = bobCBHBARIl
                kpz.handle_left[0] = bobCBHBARIl - 30
                kpz.handle_right[0] = bobCBHBARIl + 30
                                               
                # fcurve.keyframe_points[0].co.x = 1
                # fcurve.keyframe_points[1].co.x = bob
                
                bpy.context.scene.frame_end = bobCBHBARIl + frCBHBARI

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
            data_paths = ['modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]', 'modifiers["GeometryNodes"]["Input_55"]', 'modifiers["GeometryNodes"]["Input_56"]', 'modifiers["GeometryNodes"]["Input_57"]', 'modifiers["GeometryNodes"]["Input_58"]', 'modifiers["GeometryNodes"]["Input_81"]', 'modifiers["GeometryNodes"]["Input_82"]', 'modifiers["GeometryNodes"]["Input_83"]', 'modifiers["GeometryNodes"]["Input_84"]', 'modifiers["GeometryNodes"]["Input_85"]', 'modifiers["GeometryNodes"]["Input_86"]', 'modifiers["GeometryNodes"]["Input_87"]', 'modifiers["GeometryNodes"]["Input_88"]', 'modifiers["GeometryNodes"]["Input_89"]', 'modifiers["GeometryNodes"]["Input_90"]']
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
            data_paths = ['modifiers["GeometryNodes"]["Input_28"]', 'modifiers["GeometryNodes"]["Input_29"]', 'modifiers["GeometryNodes"]["Input_30"]', 'modifiers["GeometryNodes"]["Input_31"]', 'modifiers["GeometryNodes"]["Input_55"]', 'modifiers["GeometryNodes"]["Input_56"]', 'modifiers["GeometryNodes"]["Input_57"]', 'modifiers["GeometryNodes"]["Input_58"]', 'modifiers["GeometryNodes"]["Input_81"]', 'modifiers["GeometryNodes"]["Input_82"]', 'modifiers["GeometryNodes"]["Input_83"]', 'modifiers["GeometryNodes"]["Input_84"]', 'modifiers["GeometryNodes"]["Input_85"]', 'modifiers["GeometryNodes"]["Input_86"]', 'modifiers["GeometryNodes"]["Input_87"]', 'modifiers["GeometryNodes"]["Input_88"]', 'modifiers["GeometryNodes"]["Input_89"]', 'modifiers["GeometryNodes"]["Input_90"]']
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
    
class ADDONNAME_USM(bpy.types.Operator):
    bl_label = "Add Ob33jectusm"
    bl_idname = "addonname.myop_operatorusmap"  
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool       
    
        if mytool.my_enum_usmap == 'OPUSM7':
            bpy.context.scene.render.fps = 24
            bpy.context.scene.frame_end = 120

            action_name = 'KSAction'

            data_paths = []

            # Add paths from 'Input_114' to 'Input_137'
            start_index_1 = 114
            end_index_1 = 137

            for i in range(start_index_1, end_index_1 + 1):
                path = 'modifiers["GeometryNodes"]["Input_' + str(i) + '"]'
                data_paths.append(path)

            # Add paths from 'Input_138' to 'Input_163'
            start_index_2 = 138
            end_index_2 = 163

            # Add "Input_164" to the list
            data_paths.append('modifiers["GeometryNodes"]["Input_164"]')

            for i in range(start_index_2, end_index_2 + 1):
                path = 'modifiers["GeometryNodes"]["Input_' + str(i) + '"]'
                data_paths.append(path)

            print(data_paths)

            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
                    if fcurve:
                        fcurve.keyframe_points[0].co.x = 18
                        fcurve.keyframe_points[0].handle_left[0] = 16
                        fcurve.keyframe_points[0].handle_left[1] = 0
                        fcurve.keyframe_points[0].handle_right[0] = 32
                        fcurve.keyframe_points[0].handle_right[1] = 0
                        fcurve.keyframe_points[1].co.x = 90
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

            
        if mytool.my_enum_usmap == 'OPUSM8':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 143
            
            action_name = 'KSAction'
            data_paths = []

            # Add paths from 'Input_114' to 'Input_137'
            start_index_1 = 114
            end_index_1 = 137

            for i in range(start_index_1, end_index_1 + 1):
                path = 'modifiers["GeometryNodes"]["Input_' + str(i) + '"]'
                data_paths.append(path)

            # Add paths from 'Input_138' to 'Input_163'
            start_index_2 = 138
            end_index_2 = 163

            # Add "Input_164" to the list
            data_paths.append('modifiers["GeometryNodes"]["Input_164"]')

            for i in range(start_index_2, end_index_2 + 1):
                path = 'modifiers["GeometryNodes"]["Input_' + str(i) + '"]'
                data_paths.append(path)

            print(data_paths)
            index = 0               # Z axis

            for data_path in data_paths:
                # Find the appropriate action
                action = bpy.data.actions.get(action_name)
                if action:
                    # From this action, retrieve the appropriate F-Curve
                    fcurve = action.fcurves.find(data_path=data_path, index=index)
                    if fcurve:
                        fcurve.keyframe_points[0].co.x = 23
                        fcurve.keyframe_points[0].handle_left[0] = 16
                        fcurve.keyframe_points[0].handle_left[1] = 0
                        fcurve.keyframe_points[0].handle_right[0] = 40
                        fcurve.keyframe_points[0].handle_right[1] = 0
                        fcurve.keyframe_points[1].co.x = 113
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
        
        action_name = bpy.context.active_object.animation_data.action.name
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
            bpy.context.scene.frame_end = 264
            
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
            
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Socket_4"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 144
                    fcurve.keyframe_points[0].handle_left[0] = 144
                    fcurve.keyframe_points[0].handle_left[1] = -0.896
                    fcurve.keyframe_points[0].handle_right[0] = 144
                    fcurve.keyframe_points[0].handle_right[1] = 0.727
                    fcurve.keyframe_points[1].co.x = 168
                    fcurve.keyframe_points[1].handle_left[0] = 160
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 176
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Socket_5"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 168
                    fcurve.keyframe_points[0].handle_left[0] = 168
                    fcurve.keyframe_points[0].handle_left[1] = -0.896
                    fcurve.keyframe_points[0].handle_right[0] = 168
                    fcurve.keyframe_points[0].handle_right[1] = 0.659
                    fcurve.keyframe_points[1].co.x = 192
                    fcurve.keyframe_points[1].handle_left[0] = 184
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 200
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Socket_6"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 192
                    fcurve.keyframe_points[0].handle_left[0] = 192
                    fcurve.keyframe_points[0].handle_left[1] = -0.896
                    fcurve.keyframe_points[0].handle_right[0] = 192
                    fcurve.keyframe_points[0].handle_right[1] = 0.606
                    fcurve.keyframe_points[1].co.x = 216
                    fcurve.keyframe_points[1].handle_left[0] = 206
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 224
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

        if mytool.my_enumMCpie == 'OPMC8pie':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 330
            
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
   
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Socket_4"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 180
                    fcurve.keyframe_points[0].handle_left[0] = 180
                    fcurve.keyframe_points[0].handle_left[1] = -0.864
                    fcurve.keyframe_points[0].handle_right[0] = 180
                    fcurve.keyframe_points[0].handle_right[1] = 0.727
                    fcurve.keyframe_points[1].co.x = 210
                    fcurve.keyframe_points[1].handle_left[0] = 200
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 220
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Socket_5"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 210
                    fcurve.keyframe_points[0].handle_left[0] = 210
                    fcurve.keyframe_points[0].handle_left[1] = -0.864
                    fcurve.keyframe_points[0].handle_right[0] = 210
                    fcurve.keyframe_points[0].handle_right[1] = 0.659
                    fcurve.keyframe_points[1].co.x = 240
                    fcurve.keyframe_points[1].handle_left[0] = 230
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 250
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.002Action.001'
            data_path = 'modifiers["GeometryNodes"]["Socket_6"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 240
                    fcurve.keyframe_points[0].handle_left[0] = 240
                    fcurve.keyframe_points[0].handle_left[1] = -0.864
                    fcurve.keyframe_points[0].handle_right[0] = 240
                    fcurve.keyframe_points[0].handle_right[1] = 0.606
                    fcurve.keyframe_points[1].co.x = 270
                    fcurve.keyframe_points[1].handle_left[0] = 260
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 280
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
            bpy.context.scene.frame_end = 264
            
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
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_95"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 144
                    fcurve.keyframe_points[0].handle_left[0] = 144
                    fcurve.keyframe_points[0].handle_left[1] = -0.896
                    fcurve.keyframe_points[0].handle_right[0] = 144
                    fcurve.keyframe_points[0].handle_right[1] = 0.762
                    fcurve.keyframe_points[1].co.x = 168
                    fcurve.keyframe_points[1].handle_left[0] = 160
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 176
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Socket_2"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 168
                    fcurve.keyframe_points[0].handle_left[0] = 168
                    fcurve.keyframe_points[0].handle_left[1] = -0.896
                    fcurve.keyframe_points[0].handle_right[0] = 168
                    fcurve.keyframe_points[0].handle_right[1] = 0.762
                    fcurve.keyframe_points[1].co.x = 192
                    fcurve.keyframe_points[1].handle_left[0] = 184
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 200
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Socket_3"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 192
                    fcurve.keyframe_points[0].handle_left[0] = 192
                    fcurve.keyframe_points[0].handle_left[1] = -0.896
                    fcurve.keyframe_points[0].handle_right[0] = 192
                    fcurve.keyframe_points[0].handle_right[1] = 0.762
                    fcurve.keyframe_points[1].co.x = 216
                    fcurve.keyframe_points[1].handle_left[0] = 208
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 224
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

        if mytool.my_enumMPpie == 'OPMP8pie':
            bpy.context.scene.render.fps = 30
            bpy.context.scene.frame_end = 300
            
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
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Input_95"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 180
                    fcurve.keyframe_points[0].handle_left[0] = 180
                    fcurve.keyframe_points[0].handle_left[1] = -0.722
                    fcurve.keyframe_points[0].handle_right[0] = 180
                    fcurve.keyframe_points[0].handle_right[1] = 0.762
                    fcurve.keyframe_points[1].co.x = 210
                    fcurve.keyframe_points[1].handle_left[0] = 194.3
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 211
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Socket_2"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 210
                    fcurve.keyframe_points[0].handle_left[0] = 210
                    fcurve.keyframe_points[0].handle_left[1] = -0.722
                    fcurve.keyframe_points[0].handle_right[0] = 210
                    fcurve.keyframe_points[0].handle_right[1] = 0.639
                    fcurve.keyframe_points[1].co.x = 240
                    fcurve.keyframe_points[1].handle_left[0] = 230
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 250
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")
            
            action_name = 'Circle Graph.005Action'
            data_path = 'modifiers["GeometryNodes"]["Socket_3"]'
            index = 0               # Z axis

            # Find the appropriate action
            action = bpy.data.actions.get(action_name)
            if action:
                # From this action, retrieve the appropriate F-Curve
                fcurve = action.fcurves.find(data_path = data_path, index = index)
                if fcurve:

                    fcurve.keyframe_points[0].co.x = 240
                    fcurve.keyframe_points[0].handle_left[0] = 240
                    fcurve.keyframe_points[0].handle_left[1] = -0.722
                    fcurve.keyframe_points[0].handle_right[0] = 240
                    fcurve.keyframe_points[0].handle_right[1] = 0.762
                    fcurve.keyframe_points[1].co.x = 270
                    fcurve.keyframe_points[1].handle_left[0] = 260
                    fcurve.keyframe_points[1].handle_left[1] = 1
                    fcurve.keyframe_points[1].handle_right[0] = 280
                    fcurve.keyframe_points[1].handle_right[1] = 1
            
                    print("changed")
                else:
                    print("no fcurve")
            else:
                print("no action")
    
            print("end")

        return {'FINISHED'}

class FontchangeCG(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatorf"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        node_groupcg = modifier.node_group
        
        nodecgtitle = node_groupcg.nodes['String to Curves.005']
        datacgtitle_font = bpy.data.fonts.load(mytool.my_pathfontcg_title)
        nodecgtitle.font = datacgtitle_font
        
        nodecgsubtitle = node_groupcg.nodes['String to Curves.006']
        datacgsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontcg_subtitle)
        nodecgsubtitle.font = datacgsubtitle_font
        
        nodecgvalue = node_groupcg.nodes['String to Curves']
        datacgvalue_font = bpy.data.fonts.load(mytool.my_pathfontcg_value)
        nodecgvalue.font = datacgvalue_font        
        
        nodecgdescription = node_groupcg.nodes['String to Curves.001']
        datacgdescription_font = bpy.data.fonts.load(mytool.my_pathfontcg_description)
        nodecgdescription.font = datacgdescription_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreCG(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorres"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestorecg_group = modifier.node_group
        
        noderestorecgtitle = noderestorecg_group.nodes['String to Curves.005']
        datarestorecgtitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestorecgtitle.font = datarestorecgtitle_font
        
        noderestorecgsubtitle = noderestorecg_group.nodes['String to Curves.006']
        datarestorecgsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestorecgsubtitle.font = datarestorecgsubtitle_font
        
        noderestorecgvalue = noderestorecg_group.nodes['String to Curves']
        datarestorecgvalue_font = bpy.data.fonts["Open Sans Regular"]
        noderestorecgvalue.font = datarestorecgvalue_font        
        
        noderestorecgdescription = noderestorecg_group.nodes['String to Curves.001']
        datarestorecgdescription_font = bpy.data.fonts["Open Sans Regular"]
        noderestorecgdescription.font = datarestorecgdescription_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}

    
class Fontchange23CG(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operator23cgfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        node23_group = modifier.node_group
        
        node23cgtitle = node23_group.nodes['String to Curves.005']
        data23cgtitle_font = bpy.data.fonts.load(mytool.my_pathfont23cg_title)
        node23cgtitle.font = data23cgtitle_font
        
        node23cgsubtitle = node23_group.nodes['String to Curves.006']
        data23cgsubtitle_font = bpy.data.fonts.load(mytool.my_pathfont23cg_subtitle)
        node23cgsubtitle.font = data23cgsubtitle_font
        
        node23cgvalue_names = ['String to Curves', 'String to Curves.001', 'String to Curves.002']
        for name in node23cgvalue_names:
            node23cgvalue = node23_group.nodes.get(name)
            if node23cgvalue:
                data23cgvalue_font = bpy.data.fonts.load(mytool.my_pathfont23cg_value)
                node23cgvalue.font = data23cgvalue_font

        node23cgdescription_names = ['String to Curves.004', 'String to Curves.007', 'String to Curves.008']
        for name in node23cgdescription_names:
            node23cgdescription = node23_group.nodes.get(name)
            if node23cgdescription:
                data23cgdescription_font = bpy.data.fonts.load(mytool.my_pathfont23cg_description)
                node23cgdescription.font = data23cgdescription_font    
        
        node23cglegend_names = ['String to Curves.037', 'String to Curves.036', 'String to Curves.035']
        for name in node23cglegend_names:
            node23cglegend = node23_group.nodes.get(name)
            if node23cglegend:
                data23cglegend_font = bpy.data.fonts.load(mytool.my_pathfont23cg_legend)
                node23cglegend.font = data23cglegend_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class Fontrestore23CG(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operator23cgresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj23cg = bpy.context.view_layer.objects.active
        modifier23cg = obj23cg.modifiers.active 
        noderestore23cg_group = modifier23cg.node_group
        
        noderestore23cgtitle = noderestore23cg_group.nodes['String to Curves.005']
        datarestore23cgtitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestore23cgtitle.font = datarestore23cgtitle_font
        
        noderestore23cgsubtitle = noderestore23cg_group.nodes['String to Curves.006']
        datarestore23cgsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestore23cgsubtitle.font = datarestore23cgsubtitle_font
        
        node23cgvalue_names = ['String to Curves', 'String to Curves.001', 'String to Curves.002']
        for name in node23cgvalue_names:
            node23cgvalue = noderestore23cg_group.nodes.get(name)
            if node23cgvalue:
                data23cgvalue_font = bpy.data.fonts["Open Sans Regular"]
                node23cgvalue.font = data23cgvalue_font     
        
        node23cgdescription_names = ['String to Curves.004', 'String to Curves.007', 'String to Curves.008']
        for name in node23cgdescription_names:
            node23cgdescription = noderestore23cg_group.nodes.get(name)
            if node23cgdescription:
                data23cgdescription_font = bpy.data.fonts["Open Sans Regular"]
                node23cgdescription.font = data23cgdescription_font  

        node23cglegend_names = ['String to Curves.037', 'String to Curves.036', 'String to Curves.035']
        for name in node23cglegend_names:
            node23cglegend = noderestore23cg_group.nodes.get(name)
            if node23cglegend:
                data23cglegend_font = bpy.data.fonts["Open Sans Regular"]
                node23cglegend.font = data23cglegend_font  
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class Fontchange23PG(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operator23pgfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        node23pg_group = modifier.node_group
        
        node23pgtitle = node23pg_group.nodes['String to Curves.005']
        data23pgtitle_font = bpy.data.fonts.load(mytool.my_pathfont23pg_title)
        node23pgtitle.font = data23pgtitle_font
        
        node23pgsubtitle = node23pg_group.nodes['String to Curves.006']
        data23pgsubtitle_font = bpy.data.fonts.load(mytool.my_pathfont23pg_subtitle)
        node23pgsubtitle.font = data23pgsubtitle_font
        
        node23pgvalue_names = ['String to Curves', 'String to Curves.001', 'String to Curves.002']
        for name in node23pgvalue_names:
            node23pgvalue = node23pg_group.nodes.get(name)
            if node23pgvalue:
                data23pgvalue_font = bpy.data.fonts.load(mytool.my_pathfont23pg_value)
                node23pgvalue.font = data23pgvalue_font

        node23pgdescription_names = ['String to Curves.009', 'String to Curves.007', 'String to Curves.008']
        for name in node23pgdescription_names:
            node23pgdescription = node23pg_group.nodes.get(name)
            if node23pgdescription:
                data23pgdescription_font = bpy.data.fonts.load(mytool.my_pathfont23pg_description)
                node23pgdescription.font = data23pgdescription_font    
        
        node23pglegend_names = ['String to Curves.037', 'String to Curves.036', 'String to Curves.035']
        for name in node23pglegend_names:
            node23pglegend = node23pg_group.nodes.get(name)
            if node23pglegend:
                data23pglegend_font = bpy.data.fonts.load(mytool.my_pathfont23pg_legend)
                node23pglegend.font = data23pglegend_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class Fontrestore23PG(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operator23pgresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestore23pg_group = modifier.node_group
        
        noderestore23pgtitle = noderestore23pg_group.nodes['String to Curves.005']
        datarestore23pgtitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestore23pgtitle.font = datarestore23pgtitle_font
        
        noderestore23pgsubtitle = noderestore23pg_group.nodes['String to Curves.006']
        datarestore23pgsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestore23pgsubtitle.font = datarestore23pgsubtitle_font
        
        node23pgvalue_names = ['String to Curves', 'String to Curves.001', 'String to Curves.002']
        for name in node23pgvalue_names:
            node23pgvalue = noderestore23pg_group.nodes.get(name)
            if node23pgvalue:
                data23pgvalue_font = bpy.data.fonts["Open Sans Regular"]
                node23pgvalue.font = data23pgvalue_font     
        
        node23pgdescription_names = ['String to Curves.004', 'String to Curves.007', 'String to Curves.008']
        for name in node23pgdescription_names:
            node23pgdescription = noderestore23pg_group.nodes.get(name)
            if node23pgdescription:
                data23pgdescription_font = bpy.data.fonts["Open Sans Regular"]
                node23pgdescription.font = data23pgdescription_font  

        node23pglegend_names = ['String to Curves.037', 'String to Curves.036', 'String to Curves.035']
        for name in node23pglegend_names:
            node23pglegend = noderestore23pg_group.nodes.get(name)
            if node23pglegend:
                data23pglegend_font = bpy.data.fonts["Open Sans Regular"]
                node23pglegend.font = data23pglegend_font  
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontchangePG(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatorfpie"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        node_grouppg = modifier.node_group
        
        nodepgtitle = node_grouppg.nodes['String to Curves.005']
        datapgtitle_font = bpy.data.fonts.load(mytool.my_pathfontpg_title)
        nodepgtitle.font = datapgtitle_font
        
        nodepgsubtitle = node_grouppg.nodes['String to Curves.006']
        datapgsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontpg_subtitle)
        nodepgsubtitle.font = datapgsubtitle_font
        
        nodepgvalue = node_grouppg.nodes['String to Curves']
        datapgvalue_font = bpy.data.fonts.load(mytool.my_pathfontpg_value)
        nodepgvalue.font = datapgvalue_font        
        
        nodepgdescription = node_grouppg.nodes['String to Curves.001']
        datapgdescription_font = bpy.data.fonts.load(mytool.my_pathfontpg_description)
        nodepgdescription.font = datapgdescription_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestorePG(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorrespie"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestorepg_group = modifier.node_group
        
        noderestorepgtitle = noderestorepg_group.nodes['String to Curves.005']
        datarestorepgtitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestorepgtitle.font = datarestorepgtitle_font
        
        noderestorepgsubtitle = noderestorepg_group.nodes['String to Curves.006']
        datarestorepgsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestorepgsubtitle.font = datarestorepgsubtitle_font
        
        noderestorepgvalue = noderestorepg_group.nodes['String to Curves']
        datarestorepgvalue_font = bpy.data.fonts["Open Sans Regular"]
        noderestorepgvalue.font = datarestorepgvalue_font        
        
        noderestorepgdescription = noderestorepg_group.nodes['String to Curves.001']
        datarestorepgdescription_font = bpy.data.fonts["Open Sans Regular"]
        noderestorepgdescription.font = datarestorepgdescription_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
 
class FontchangeCANDLEG(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatorcandlegfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        nodecandleg_group = modifier.node_group
        nestedcandlegrn_node_group = bpy.data.node_groups["NodeGroup.174"]
        nestedcandlegpointtext_node_group = bpy.data.node_groups["NodeGroup.173"]
        
        nodecandlegtitle = nodecandleg_group.nodes['String to Curves.014']
        datacandlegtitle_font = bpy.data.fonts.load(mytool.my_pathfontcandleg_title)
        nodecandlegtitle.font = datacandlegtitle_font
        
        nodecandlegsubtitle = nodecandleg_group.nodes['String to Curves.015']
        datacandlegsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontcandleg_subtitle)
        nodecandlegsubtitle.font = datacandlegsubtitle_font
        
        nodecandlegrangenumbers = nestedcandlegrn_node_group.nodes['String to Curves.013']
        datacandlegrangenumbers_font = bpy.data.fonts.load(mytool.my_pathfontcandleg_rangenumbers)
        nodecandlegrangenumbers.font = datacandlegrangenumbers_font 

        nodecandlegpointtext = nestedcandlegpointtext_node_group.nodes['String to Curves.005']
        datacandlegpointtext_font = bpy.data.fonts.load(mytool.my_pathfontcandleg_bartext)
        nodecandlegpointtext.font = datacandlegpointtext_font       
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreCANDLEG(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorcandlegresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestore23_group = modifier.node_group
        nestedcandlegrn_node_group = bpy.data.node_groups["NodeGroup.174"]
        nestedcandlegpointtext_node_group = bpy.data.node_groups["NodeGroup.173"]
        
        noderestorecandlegtitle = noderestore23_group.nodes['String to Curves.014']
        datarestorecandlegtitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestorecandlegtitle.font = datarestorecandlegtitle_font
        
        noderestorecandlegsubtitle = noderestore23_group.nodes['String to Curves.015']
        datarestorecandlegsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestorecandlegsubtitle.font = datarestorecandlegsubtitle_font
        
        noderestorecandlegrangenumbers = nestedcandlegrn_node_group.nodes['String to Curves.013']
        datarestorecandlegrangenumbers_font = bpy.data.fonts["Open Sans Regular"]
        noderestorecandlegrangenumbers.font = datarestorecandlegrangenumbers_font        
        
        noderestorecandlegpointtext = nestedcandlegpointtext_node_group.nodes['String to Curves.005']
        datarestorecandlegpointtext_font = bpy.data.fonts["Open Sans Regular"]
        noderestorecandlegpointtext.font = datarestorecandlegpointtext_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    

class FontchangeLINEG(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatorlinegfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes.001"]
        nodelineg_group = modifier.node_group
        
        nodelinegtitle = nodelineg_group.nodes['String to Curves.014']
        datalinegtitle_font = bpy.data.fonts.load(mytool.my_pathfontlg_title)
        nodelinegtitle.font = datalinegtitle_font
        
        nodelinegsubtitle = nodelineg_group.nodes['String to Curves.015']
        datalinegsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontlg_subtitle)
        nodelinegsubtitle.font = datalinegsubtitle_font

        nodelinegvalue = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.022', 'String to Curves.023', 'String to Curves.025','String to Curves.027','String to Curves.029','String to Curves.031','String to Curves.033','String to Curves.035','String to Curves.037','String to Curves.039','String to Curves.041','String to Curves.043','String to Curves.045','String to Curves.047','String to Curves.049','String to Curves.051','String to Curves.053','String to Curves.055','String to Curves.057','String to Curves.059','String to Curves.061','String to Curves.063','String to Curves.065','String to Curves.067']
        for name in nodelinegvalue:
            nodelinegvalue = nodelineg_group.nodes.get(name)
            if nodelinegvalue:
                datalinegvalue_font = bpy.data.fonts.load(mytool.my_pathfontlg_barvalue)
                nodelinegvalue.font = datalinegvalue_font

        nodelinegrangenumbers = ['String to Curves.009', 'String to Curves.010', 'String to Curves.008', 'String to Curves.011', 'String to Curves.012', 'String to Curves.013']
        for name in nodelinegrangenumbers:
            nodelinegrangenumbers = nodelineg_group.nodes.get(name)
            if nodelinegrangenumbers:
                datalinegrangenumbers_font = bpy.data.fonts.load(mytool.my_pathfontlg_rangenumbers)
                nodelinegrangenumbers.font = datalinegrangenumbers_font    
        
        nodelinegpointtext = ['String to Curves.005', 'String to Curves.003', 'String to Curves', 'String to Curves.001', 'String to Curves.006', 'String to Curves.007', 'String to Curves.004', 'String to Curves.002', 'String to Curves.024', 'String to Curves.026','String to Curves.028','String to Curves.030','String to Curves.032','String to Curves.034','String to Curves.036','String to Curves.038','String to Curves.040', 'String to Curves.042','String to Curves.044','String to Curves.046','String to Curves.048','String to Curves.050','String to Curves.052','String to Curves.054','String to Curves.056', 'String to Curves.058','String to Curves.060','String to Curves.062','String to Curves.064','String to Curves.066']
        for name in nodelinegpointtext:
            nodelinegpointtext = nodelineg_group.nodes.get(name)
            if nodelinegpointtext:
                datalinegpointtext_font = bpy.data.fonts.load(mytool.my_pathfontlg_bartext)
                nodelinegpointtext.font = datalinegpointtext_font     
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreLINEG(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorlinegresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes.001"]
        noderestoreline_group = modifier.node_group
        
        noderestorelinegtitle = noderestoreline_group.nodes['String to Curves.014']
        datarestorelinegtitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestorelinegtitle.font = datarestorelinegtitle_font
        
        noderestorelinegsubtitle = noderestoreline_group.nodes['String to Curves.015']
        datarestorelinegsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestorelinegsubtitle.font = datarestorelinegsubtitle_font

        noderestorelinegvalue = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.022', 'String to Curves.023', 'String to Curves.025','String to Curves.027','String to Curves.029','String to Curves.031','String to Curves.033','String to Curves.035','String to Curves.037','String to Curves.039','String to Curves.041','String to Curves.043','String to Curves.045','String to Curves.047','String to Curves.049','String to Curves.051','String to Curves.053','String to Curves.055','String to Curves.057','String to Curves.059','String to Curves.061','String to Curves.063','String to Curves.065','String to Curves.067']
        for name in noderestorelinegvalue:
            noderestorelinegvalue = noderestoreline_group.nodes.get(name)
            if noderestorelinegvalue:
                datalinegvalue_font = bpy.data.fonts["Open Sans Regular"]
                noderestorelinegvalue.font = datalinegvalue_font     
        
        noderestorelinegrangenumbers = ['String to Curves.009', 'String to Curves.010', 'String to Curves.008', 'String to Curves.011', 'String to Curves.012', 'String to Curves.013']
        for name in noderestorelinegrangenumbers:
            noderestorelinegrangenumbers = noderestoreline_group.nodes.get(name)
            if noderestorelinegrangenumbers:
                datalinegrangenumbers_font = bpy.data.fonts["Open Sans Regular"]
                noderestorelinegrangenumbers.font = datalinegrangenumbers_font  

        noderestorelinegpointtext = nodelinegpointtext = ['String to Curves.005', 'String to Curves.003', 'String to Curves', 'String to Curves.001', 'String to Curves.006', 'String to Curves.007', 'String to Curves.004', 'String to Curves.002', 'String to Curves.024', 'String to Curves.026','String to Curves.028','String to Curves.030','String to Curves.032','String to Curves.034','String to Curves.036','String to Curves.038','String to Curves.040', 'String to Curves.042','String to Curves.044','String to Curves.046','String to Curves.048','String to Curves.050','String to Curves.052','String to Curves.054','String to Curves.056', 'String to Curves.058','String to Curves.060','String to Curves.062','String to Curves.064','String to Curves.066']
        for name in noderestorelinegpointtext:
            noderestorelinegpointtext = noderestoreline_group.nodes.get(name)
            if noderestorelinegpointtext:
                datalinegpointtext_font = bpy.data.fonts["Open Sans Regular"]
                noderestorelinegpointtext.font = datalinegpointtext_font  
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'} 
    
class FontchangeLINEGC(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatorlinegcfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes.001"]
        nodelinegc_group = modifier.node_group
        
        nodelinegctitle = nodelinegc_group.nodes['String to Curves.014']
        datalinegctitle_font = bpy.data.fonts.load(mytool.my_pathfontlgc_title)
        nodelinegctitle.font = datalinegctitle_font
        
        nodelinegcsubtitle = nodelinegc_group.nodes['String to Curves.015']
        datalinegcsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontlgc_subtitle)
        nodelinegcsubtitle.font = datalinegcsubtitle_font

        nodelinegcvalue = ['String to Curves.021','String to Curves.022','String to Curves.023','String to Curves.024','String to Curves.025', 'String to Curves.026', 'String to Curves.027','String to Curves.028','String to Curves.029','String to Curves.030','String to Curves.031','String to Curves.032', 'String to Curves.033','String to Curves.034','String to Curves.035','String to Curves.036']
        for name in nodelinegcvalue:
            nodelinegcvalue = nodelinegc_group.nodes.get(name)
            if nodelinegcvalue:
                datalinegcvalue_font = bpy.data.fonts.load(mytool.my_pathfontlgc_barvalue)
                nodelinegcvalue.font = datalinegcvalue_font

        nodelinegcrangenumbers = ['String to Curves.013', 'String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020']
        for name in nodelinegcrangenumbers:
            nodelinegcrangenumbers = nodelinegc_group.nodes.get(name)
            if nodelinegcrangenumbers:
                datalinegcrangenumbers_font = bpy.data.fonts.load(mytool.my_pathfontlgc_rangenumbers)
                nodelinegcrangenumbers.font = datalinegcrangenumbers_font    
        
        nodelinegcpointtext = ['String to Curves.005', 'String to Curves.006', 'String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010', 'String to Curves.011', 'String to Curves.012']
        for name in nodelinegcpointtext:
            nodelinegcpointtext = nodelinegc_group.nodes.get(name)
            if nodelinegcpointtext:
                datalinegcpointtext_font = bpy.data.fonts.load(mytool.my_pathfontlgc_bartext)
                nodelinegcpointtext.font = datalinegcpointtext_font

        nodelinegclegend = ['String to Curves.0162', 'String to Curves.163']
        for name in nodelinegclegend:
            nodelinegclegend = nodelinegc_group.nodes.get(name)
            if nodelinegclegend:
                datalinegclegend_font = bpy.data.fonts.load(mytool.my_pathfontlgc_legend)
                nodelinegclegend.font = datalinegclegend_font    
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreLINEGC(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorlinegcresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes.001"]
        noderestorelinec_group = modifier.node_group
        
        noderestorelinegctitle = noderestorelinec_group.nodes['String to Curves.014']
        datarestorelinegctitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestorelinegctitle.font = datarestorelinegctitle_font
        
        noderestorelinegcsubtitle = noderestorelinec_group.nodes['String to Curves.015']
        datarestorelinegcsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestorelinegcsubtitle.font = datarestorelinegcsubtitle_font

        nodelinegcvalue = ['String to Curves.021','String to Curves.022','String to Curves.023','String to Curves.024','String to Curves.025', 'String to Curves.026', 'String to Curves.027','String to Curves.028','String to Curves.029','String to Curves.030','String to Curves.031','String to Curves.032', 'String to Curves.033','String to Curves.034','String to Curves.035','String to Curves.036']
        for name in nodelinegcvalue:
            nodelinegcvalue = noderestorelinec_group.nodes.get(name)
            if nodelinegcvalue:
                datalinegcvalue_font = bpy.data.fonts["Open Sans Regular"]
                nodelinegcvalue.font = datalinegcvalue_font     
        
        nodelinegcrangenumbers = ['String to Curves.013', 'String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020']
        for name in nodelinegcrangenumbers:
            nodelinegcrangenumbers = noderestorelinec_group.nodes.get(name)
            if nodelinegcrangenumbers:
                datalinegcrangenumbers_font = bpy.data.fonts["Open Sans Semibold"]
                nodelinegcrangenumbers.font = datalinegcrangenumbers_font  

        nodelinegcpointtext = ['String to Curves.005', 'String to Curves.006', 'String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010', 'String to Curves.011', 'String to Curves.012']
        for name in nodelinegcpointtext:
            nodelinegcpointtext = noderestorelinec_group.nodes.get(name)
            if nodelinegcpointtext:
                datalinegcpointtext_font = bpy.data.fonts["Open Sans Regular"]
                nodelinegcpointtext.font = datalinegcpointtext_font  

        nodelinegclegend = ['String to Curves.0162', 'String to Curves.163']
        for name in nodelinegclegend:
            nodelinegclegend = noderestorelinec_group.nodes.get(name)
            if nodelinegclegend:
                datalinegclegend_font = bpy.data.fonts["Open Sans Light"]
                nodelinegclegend.font = datalinegclegend_font  
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontchangeMOUNTAING(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatormgfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        nodemountain_group = modifier.node_group
        
        nodemountaintitle = nodemountain_group.nodes['String to Curves.029']
        datamountaintitle_font = bpy.data.fonts.load(mytool.my_pathfontmg_title)
        nodemountaintitle.font = datamountaintitle_font
        
        nodemountainsubtitle = nodemountain_group.nodes['String to Curves.028']
        datamountainsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontmg_subtitle)
        nodemountainsubtitle.font = datamountainsubtitle_font

        nodemountainvalue = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.022', 'String to Curves.023']
        for name in nodemountainvalue:
            nodemountainvalue = nodemountain_group.nodes.get(name)
            if nodemountainvalue:
                datamountainvalue_font = bpy.data.fonts.load(mytool.my_pathfontmg_barvalue)
                nodemountainvalue.font = datamountainvalue_font

        nodemountainrangenumbers = ['String to Curves.001','String to Curves.002', 'String to Curves.003', 'String to Curves.004', 'String to Curves.013', 'String to Curves.014' ]
        for name in nodemountainrangenumbers:
            nodemountainrangenumbers = nodemountain_group.nodes.get(name)
            if nodemountainrangenumbers:
                datamountainrangenumbers_font = bpy.data.fonts.load(mytool.my_pathfontmg_rangenumbers)
                nodemountainrangenumbers.font = datamountainrangenumbers_font    
        
        nodemountainpointtext = ['String to Curves.005', 'String to Curves.006', 'String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010', 'String to Curves.011', 'String to Curves.012']
        for name in nodemountainpointtext:
            nodemountainpointtext = nodemountain_group.nodes.get(name)
            if nodemountainpointtext:
                datamountainpointtext_font = bpy.data.fonts.load(mytool.my_pathfontmg_bartext)
                nodemountainpointtext.font = datamountainpointtext_font     
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreMOUNTAING(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatormgresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestoremountain_group = modifier.node_group
        
        noderestoremountaintitle = noderestoremountain_group.nodes['String to Curves.029']
        datarestoremountaintitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestoremountaintitle.font = datarestoremountaintitle_font
        
        noderestoremountainsubtitle = noderestoremountain_group.nodes['String to Curves.028']
        datarestoremountainsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestoremountainsubtitle.font = datarestoremountainsubtitle_font

        nodemountainvalue = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.022', 'String to Curves.023']
        for name in nodemountainvalue:
            nodemountainvalue = noderestoremountain_group.nodes.get(name)
            if nodemountainvalue:
                datamountainvalue_font = bpy.data.fonts["Open Sans Regular"]
                nodemountainvalue.font = datamountainvalue_font     
        
        nodemountainrangenumbers = ['String to Curves.001','String to Curves.002', 'String to Curves.003', 'String to Curves.004', 'String to Curves.013', 'String to Curves.014' ]
        for name in nodemountainrangenumbers:
            nodemountainrangenumbers = noderestoremountain_group.nodes.get(name)
            if nodemountainrangenumbers:
                datamountainrangenumbers_font = bpy.data.fonts["Open Sans Regular"]
                nodemountainrangenumbers.font = datamountainrangenumbers_font  

        nodemountainpointtext = ['String to Curves.005', 'String to Curves.006', 'String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010', 'String to Curves.011', 'String to Curves.012']
        for name in nodemountainpointtext:
            nodemountainpointtext = noderestoremountain_group.nodes.get(name)
            if nodemountainpointtext:
                datamountainpointtext_font = bpy.data.fonts["Open Sans Regular"]
                nodemountainpointtext.font = datamountainpointtext_font  
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'} 
    
class FontchangeMOUNTAINGC(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatormgcfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        nodemountainc_group = modifier.node_group
        
        nodemountainctitle = nodemountainc_group.nodes['String to Curves.029']
        datamountainctitle_font = bpy.data.fonts.load(mytool.my_pathfontmgc_title)
        nodemountainctitle.font = datamountainctitle_font
        
        nodemountaincsubtitle = nodemountainc_group.nodes['String to Curves.028']
        datamountaincsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontmgc_subtitle)
        nodemountaincsubtitle.font = datamountaincsubtitle_font

        nodemountaincvalue = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.034', 'String to Curves.035', 'String to Curves.036', 'String to Curves.037', 'String to Curves.038', 'String to Curves.039', 'String to Curves.040', 'String to Curves.041', 'String to Curves.042', 'String to Curves.043']
        for name in nodemountaincvalue:
            nodemountaincvalue = nodemountainc_group.nodes.get(name)
            if nodemountaincvalue:
                datamountaincvalue_font = bpy.data.fonts.load(mytool.my_pathfontmgc_barvalue)
                nodemountaincvalue.font = datamountaincvalue_font

        nodemountaincrangenumbers = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.004', 'String to Curves.005']
        for name in nodemountaincrangenumbers:
            nodemountaincrangenumbers = nodemountainc_group.nodes.get(name)
            if nodemountaincrangenumbers:
                datamountaincrangenumbers_font = bpy.data.fonts.load(mytool.my_pathfontmgc_rangenumbers)
                nodemountaincrangenumbers.font = datamountaincrangenumbers_font    
        
        nodemountaincpointtext = ['String to Curves.022', 'String to Curves.023', 'String to Curves.024', 'String to Curves.025', 'String to Curves.026', 'String to Curves.028', 'String to Curves.030', 'String to Curves.031']
        for name in nodemountaincpointtext:
            nodemountaincpointtext = nodemountainc_group.nodes.get(name)
            if nodemountaincpointtext:
                datamountaincpointtext_font = bpy.data.fonts.load(mytool.my_pathfontmgc_bartext)
                nodemountaincpointtext.font = datamountaincpointtext_font

        nodemountainclegend = ['String to Curves.032', 'String to Curves.033']
        for name in nodemountainclegend:
            nodemountainclegend = nodemountainc_group.nodes.get(name)
            if nodemountainclegend:
                datamountainclegend_font = bpy.data.fonts.load(mytool.my_pathfontmgc_legend)
                nodemountainclegend.font = datamountainclegend_font    
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreMOUNTAINGC(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatormgcresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestoremountainc_group = modifier.node_group
        
        noderestoremountainctitle = noderestoremountainc_group.nodes['String to Curves.029']
        datarestoremountainctitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestoremountainctitle.font = datarestoremountainctitle_font
        
        noderestoremountaincsubtitle = noderestoremountainc_group.nodes['String to Curves.028']
        datarestoremountaincsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestoremountaincsubtitle.font = datarestoremountaincsubtitle_font

        nodemountaincvalue = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.034', 'String to Curves.035', 'String to Curves.036', 'String to Curves.037', 'String to Curves.038', 'String to Curves.039', 'String to Curves.040', 'String to Curves.041', 'String to Curves.042', 'String to Curves.043']
        for name in nodemountaincvalue:
            nodemountaincvalue = noderestoremountainc_group.nodes.get(name)
            if nodemountaincvalue:
                datamountaincvalue_font = bpy.data.fonts["Open Sans Regular"]
                nodemountaincvalue.font = datamountaincvalue_font     
        
        nodemountaincrangenumbers = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.004', 'String to Curves.005']
        for name in nodemountaincrangenumbers:
            nodemountaincrangenumbers = noderestoremountainc_group.nodes.get(name)
            if nodemountaincrangenumbers:
                datamountaincrangenumbers_font = bpy.data.fonts["Open Sans Semibold"]
                nodemountaincrangenumbers.font = datamountaincrangenumbers_font  

        nodemountaincpointtext = ['String to Curves.022', 'String to Curves.023', 'String to Curves.024', 'String to Curves.025', 'String to Curves.026', 'String to Curves.028', 'String to Curves.030', 'String to Curves.031']
        for name in nodemountaincpointtext:
            nodemountaincpointtext = noderestoremountainc_group.nodes.get(name)
            if nodemountaincpointtext:
                datamountaincpointtext_font = bpy.data.fonts["Open Sans Regular"]
                nodemountaincpointtext.font = datamountaincpointtext_font  

        nodemountainclegend = ['String to Curves.032', 'String to Curves.033']
        for name in nodemountainclegend:
            nodemountainclegend = noderestoremountainc_group.nodes.get(name)
            if nodemountainclegend:
                datamountainclegend_font = bpy.data.fonts["Open Sans Light"]
                nodemountainclegend.font = datamountainclegend_font  
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontchangeHBG(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatorbgfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        nodehbg_group = modifier.node_group
        
        nodehbgtitle = nodehbg_group.nodes['String to Curves.005']
        datahbgtitle_font = bpy.data.fonts.load(mytool.my_pathfontbg_title)
        nodehbgtitle.font = datahbgtitle_font
        
        nodehbgsubtitle = nodehbg_group.nodes['String to Curves.006']
        datahbgsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontbg_subtitle)
        nodehbgsubtitle.font = datahbgsubtitle_font

        nodehbgvalue = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.023', 'String to Curves.024', 'String to Curves.025', 'String to Curves.026', 'String to Curves.027', 'String to Curves.028']
        for name in nodehbgvalue:
            nodehbgvalue = nodehbg_group.nodes.get(name)
            if nodehbgvalue:
                datahbgvalue_font = bpy.data.fonts.load(mytool.my_pathfontbg_barvalue)
                nodehbgvalue.font = datahbgvalue_font

        nodehbgrangenumbers = ['String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010', 'String to Curves.011']
        for name in nodehbgrangenumbers:
            nodehbgrangenumbers = nodehbg_group.nodes.get(name)
            if nodehbgrangenumbers:
                datahbgrangenumbers_font = bpy.data.fonts.load(mytool.my_pathfontbg_rangenumbers)
                nodehbgrangenumbers.font = datahbgrangenumbers_font    
        
        nodehbgpointtext = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.022', 'String to Curves.021', 'String to Curves.020', 'String to Curves.015', 'String to Curves.014', 'String to Curves.013']
        for name in nodehbgpointtext:
            nodehbgpointtext = nodehbg_group.nodes.get(name)
            if nodehbgpointtext:
                datahbgpointtext_font = bpy.data.fonts.load(mytool.my_pathfontbg_bartext)
                nodehbgpointtext.font = datahbgpointtext_font

        nodehbgtexttotal = ['String to Curves.004']
        for name in nodehbgtexttotal:
            nodehbgtexttotal = nodehbg_group.nodes.get(name)
            if nodehbgtexttotal:
                datahbgtexttotal_font = bpy.data.fonts.load(mytool.my_pathfontbg_texttotal)
                nodehbgtexttotal.font = datahbgtexttotal_font   

        nodehbgvaluetotal = ['String to Curves.012']
        for name in nodehbgvaluetotal:
            nodehbgvaluetotal = nodehbg_group.nodes.get(name)
            if nodehbgvaluetotal:
                datahbgvaluetotal_font = bpy.data.fonts.load(mytool.my_pathfontbg_valuetotal)
                nodehbgvaluetotal.font = datahbgvaluetotal_font    
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreHBG(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorbgresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestorehbg_group = modifier.node_group
        
        noderestorehbgtitle = noderestorehbg_group.nodes['String to Curves.005']
        datarestorehbgtitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestorehbgtitle.font = datarestorehbgtitle_font
        
        noderestorehbgsubtitle = noderestorehbg_group.nodes['String to Curves.006']
        datarestorehbgsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestorehbgsubtitle.font = datarestorehbgsubtitle_font

        nodehbgvalue = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.023', 'String to Curves.024', 'String to Curves.025', 'String to Curves.026', 'String to Curves.027', 'String to Curves.028']
        for name in nodehbgvalue:
            nodehbgvalue = noderestorehbg_group.nodes.get(name)
            if nodehbgvalue:
                datahbgvalue_font = bpy.data.fonts["Open Sans Regular"]
                nodehbgvalue.font = datahbgvalue_font     
        
        nodehbgrangenumbers = ['String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010', 'String to Curves.011']
        for name in nodehbgrangenumbers:
            nodehbgrangenumbers = noderestorehbg_group.nodes.get(name)
            if nodehbgrangenumbers:
                datahbgrangenumbers_font = bpy.data.fonts["Open Sans Semibold"]
                nodehbgrangenumbers.font = datahbgrangenumbers_font  

        nodehbgpointtext = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.022', 'String to Curves.021', 'String to Curves.020', 'String to Curves.015', 'String to Curves.014', 'String to Curves.013' ]
        for name in nodehbgpointtext:
            nodehbgpointtext = noderestorehbg_group.nodes.get(name)
            if nodehbgpointtext:
                datahbgpointtext_font = bpy.data.fonts["Open Sans Regular"]
                nodehbgpointtext.font = datahbgpointtext_font  

        nodehbgtexttotal = ['String to Curves.004']
        for name in nodehbgtexttotal:
            nodehbgtexttotal = noderestorehbg_group.nodes.get(name)
            if nodehbgtexttotal:
                datahbgtexttotal_font = bpy.data.fonts["Open Sans Light"]
                nodehbgtexttotal.font = datahbgtexttotal_font  

        nodehbgvaluetotal = ['String to Curves.012']
        for name in nodehbgvaluetotal:
            nodehbgvaluetotal = noderestorehbg_group.nodes.get(name)
            if nodehbgvaluetotal:
                datahbgvaluetotal_font = bpy.data.fonts["Open Sans Light"]
                nodehbgvaluetotal.font = datahbgvaluetotal_font 
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontchangeHBGC(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatorbgcfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        nodehbg_group = modifier.node_group
        
        nodehbgtitle = nodehbg_group.nodes['String to Curves.005']
        datahbgtitle_font = bpy.data.fonts.load(mytool.my_pathfontbgc_title)
        nodehbgtitle.font = datahbgtitle_font
        
        nodehbgsubtitle = nodehbg_group.nodes['String to Curves.006']
        datahbgsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontbgc_subtitle)
        nodehbgsubtitle.font = datahbgsubtitle_font

        nodehbgvalue = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.022', 'String to Curves.023', 'String to Curves.027','String to Curves.026', 'String to Curves.029', 'String to Curves.028', 'String to Curves.031', 'String to Curves.030', 'String to Curves.033', 'String to Curves.032', 'String to Curves.035', 'String to Curves.034']
        for name in nodehbgvalue:
            nodehbgvalue = nodehbg_group.nodes.get(name)
            if nodehbgvalue:
                datahbgvalue_font = bpy.data.fonts.load(mytool.my_pathfontbgc_barvalue)
                nodehbgvalue.font = datahbgvalue_font

        nodehbgrangenumbers = ['String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010', 'String to Curves.011']
        for name in nodehbgrangenumbers:
            nodehbgrangenumbers = nodehbg_group.nodes.get(name)
            if nodehbgrangenumbers:
                datahbgrangenumbers_font = bpy.data.fonts.load(mytool.my_pathfontbgc_rangenumbers)
                nodehbgrangenumbers.font = datahbgrangenumbers_font    
        
        nodehbgpointtext = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.025', 'String to Curves.024', 'String to Curves.015', 'String to Curves.014', 'String to Curves.013']
        for name in nodehbgpointtext:
            nodehbgpointtext = nodehbg_group.nodes.get(name)
            if nodehbgpointtext:
                datahbgpointtext_font = bpy.data.fonts.load(mytool.my_pathfontbgc_bartext)
                nodehbgpointtext.font = datahbgpointtext_font

        nodehbglegend = ['String to Curves.004', 'String to Curves.012']
        for name in nodehbglegend:
            nodehbglegend = nodehbg_group.nodes.get(name)
            if nodehbglegend:
                datahbglegend_font = bpy.data.fonts.load(mytool.my_pathfontbgc_legend)
                nodehbglegend.font = datahbglegend_font     
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreHBGC(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorbgcresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestorehbg_group = modifier.node_group
        
        noderestorehbgtitle = noderestorehbg_group.nodes['String to Curves.005']
        datarestorehbgtitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestorehbgtitle.font = datarestorehbgtitle_font
        
        noderestorehbgsubtitle = noderestorehbg_group.nodes['String to Curves.006']
        datarestorehbgsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestorehbgsubtitle.font = datarestorehbgsubtitle_font

        nodehbgvalue = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.022', 'String to Curves.023', 'String to Curves.027','String to Curves.026', 'String to Curves.029', 'String to Curves.028', 'String to Curves.031', 'String to Curves.030', 'String to Curves.033', 'String to Curves.032', 'String to Curves.035', 'String to Curves.034']
        for name in nodehbgvalue:
            nodehbgvalue = noderestorehbg_group.nodes.get(name)
            if nodehbgvalue:
                datahbgvalue_font = bpy.data.fonts["Open Sans Regular"]
                nodehbgvalue.font = datahbgvalue_font     
        
        nodehbgrangenumbers = ['String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010', 'String to Curves.011']
        for name in nodehbgrangenumbers:
            nodehbgrangenumbers = noderestorehbg_group.nodes.get(name)
            if nodehbgrangenumbers:
                datahbgrangenumbers_font = bpy.data.fonts["Open Sans Semibold"]
                nodehbgrangenumbers.font = datahbgrangenumbers_font  

        nodehbgpointtext = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.025', 'String to Curves.024', 'String to Curves.015', 'String to Curves.014', 'String to Curves.013']
        for name in nodehbgpointtext:
            nodehbgpointtext = noderestorehbg_group.nodes.get(name)
            if nodehbgpointtext:
                datahbgpointtext_font = bpy.data.fonts["Open Sans Regular"]
                nodehbgpointtext.font = datahbgpointtext_font  

        nodehbglegend = ['String to Curves.004', 'String to Curves.012']
        for name in nodehbglegend:
            nodehbglegend = noderestorehbg_group.nodes.get(name)
            if nodehbglegend:
                datahbglegend_font = bpy.data.fonts["Open Sans Light"]
                nodehbglegend.font = datahbglegend_font  
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'} 
    
class FontchangeMCG(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatormcgfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        nodemcg_group = modifier.node_group
        
        nodemcgtitle = nodemcg_group.nodes['String to Curves.005']
        datamcgtitle_font = bpy.data.fonts.load(mytool.my_pathfontmcg_title)
        nodemcgtitle.font = datamcgtitle_font
        
        nodemcgsubtitle = nodemcg_group.nodes['String to Curves.006']
        datamcgsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontmcg_subtitle)
        nodemcgsubtitle.font = datamcgsubtitle_font

        nodemcgvalue = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.004', 'String to Curves.009', 'String to Curves.008', 'String to Curves.007']
        for name in nodemcgvalue:
            nodemcgvalue = nodemcg_group.nodes.get(name)
            if nodemcgvalue:
                datamcgvalue_font = bpy.data.fonts.load(mytool.my_pathfontmcg_barvalue)
                nodemcgvalue.font = datamcgvalue_font

        nodemcgdescription = nodemcgdescription = ['String to Curves.011', 'String to Curves.012', 'String to Curves.013', 'String to Curves.014', 'String to Curves.015', 'String to Curves.018', 'String to Curves.017', 'String to Curves.016']
        for name in nodemcgdescription:
            nodemcgdescription = nodemcg_group.nodes.get(name)
            if nodemcgdescription:
                datamcgdescription_font = bpy.data.fonts.load(mytool.my_pathfontmcg_bartext)
                nodemcgdescription.font = datamcgdescription_font      
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreMCG(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatormcgresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestoremcg_group = modifier.node_group
        
        noderestoremcgtitle = noderestoremcg_group.nodes['String to Curves.005']
        datarestoremcgtitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestoremcgtitle.font = datarestoremcgtitle_font
        
        noderestoremcgsubtitle = noderestoremcg_group.nodes['String to Curves.006']
        datarestoremcgsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestoremcgsubtitle.font = datarestoremcgsubtitle_font

        nodemcgvalue = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.004', 'String to Curves.009', 'String to Curves.008', 'String to Curves.007']
        for name in nodemcgvalue:
            nodemcgvalue = noderestoremcg_group.nodes.get(name)
            if nodemcgvalue:
                datamcgvalue_font = bpy.data.fonts["Open Sans Semibold"]
                nodemcgvalue.font = datamcgvalue_font     
        
        nodemcgdescription = nodemcgdescription = ['String to Curves.011', 'String to Curves.012', 'String to Curves.013', 'String to Curves.014', 'String to Curves.015', 'String to Curves.018', 'String to Curves.017', 'String to Curves.016']
        for name in nodemcgdescription:
            nodemcgdescription = noderestoremcg_group.nodes.get(name)
            if nodemcgdescription:
                datamcgdescription_font = bpy.data.fonts["Open Sans Light"]
                nodemcgdescription.font = datamcgdescription_font  
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
         
class FontchangeMPG(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatormpgfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        nodempg_group = modifier.node_group
        
        nodempgtitle = nodempg_group.nodes['String to Curves.005']
        datampgtitle_font = bpy.data.fonts.load(mytool.my_pathfontmpg_title)
        nodempgtitle.font = datampgtitle_font
        
        nodempgsubtitle = nodempg_group.nodes['String to Curves.006']
        datampgsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontmpg_subtitle)
        nodempgsubtitle.font = datampgsubtitle_font

        nodempgvalue = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.004', 'String to Curves.007', 'String to Curves.009', 'String to Curves.008']
        for name in nodempgvalue:
            nodempgvalue = nodempg_group.nodes.get(name)
            if nodempgvalue:
                datampgvalue_font = bpy.data.fonts.load(mytool.my_pathfontmpg_barvalue)
                nodempgvalue.font = datampgvalue_font

        nodempgdescription = ['String to Curves.011', 'String to Curves.012', 'String to Curves.013', 'String to Curves.014', 'String to Curves.015', 'String to Curves.016', 'String to Curves.018', 'String to Curves.017']
        for name in nodempgdescription:
            nodempgdescription = nodempg_group.nodes.get(name)
            if nodempgdescription:
                datampgdescription_font = bpy.data.fonts.load(mytool.my_pathfontmpg_bartext)
                nodempgdescription.font = datampgdescription_font      
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreMPG(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatormpgresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestorempg_group = modifier.node_group
        
        noderestorempgtitle = noderestorempg_group.nodes['String to Curves.005']
        datarestorempgtitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestorempgtitle.font = datarestorempgtitle_font
        
        noderestorempgsubtitle = noderestorempg_group.nodes['String to Curves.006']
        datarestorempgsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestorempgsubtitle.font = datarestorempgsubtitle_font

        nodempgvalue = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.004', 'String to Curves.007', 'String to Curves.009', 'String to Curves.008']
        for name in nodempgvalue:
            nodempgvalue = noderestorempg_group.nodes.get(name)
            if nodempgvalue:
                datampgvalue_font = bpy.data.fonts["Open Sans Semibold"]
                nodempgvalue.font = datampgvalue_font     
        
        nodempgdescription = ['String to Curves.011', 'String to Curves.012', 'String to Curves.013', 'String to Curves.014', 'String to Curves.015', 'String to Curves.016', 'String to Curves.018', 'String to Curves.017']
        for name in nodempgdescription:
            nodempgdescription = noderestorempg_group.nodes.get(name)
            if nodempgdescription:
                datampgdescription_font = bpy.data.fonts["Open Sans Light"]
                nodempgdescription.font = datampgdescription_font  
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontchangeUSM(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatorusmapfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        nodeusmap_group = modifier.node_group
        nestedcandlegrn_node_group = bpy.data.node_groups["NodeGroup.174"]
        nestedcandlegpointtext_node_group = bpy.data.node_groups["NodeGroup.173"]
        
        nodeusmaptitle = ['String to Curves', 'String to Curves.002', 'String to Curves.004']
        for name in nodeusmaptitle:
            nodeusmaptitle = nodeusmap_group.nodes.get(name)
            if nodeusmaptitle:
                datausmaptitle_font = bpy.data.fonts.load(mytool.my_pathfontusmap_title)
                nodeusmaptitle.font = datausmaptitle_font
        
        nodeusmapsubtitle = ['String to Curves.005', 'String to Curves.001', 'String to Curves.003']
        for name in nodeusmapsubtitle:
            nodeusmapsubtitle = nodeusmap_group.nodes.get(name)
            if nodeusmapsubtitle:
                datausmapsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontusmap_subtitle)
                nodeusmapsubtitle.font = datausmapsubtitle_font
    
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreUSM(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorusmapresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestoreusmap_group = modifier.node_group
        nestedcandlegrn_node_group = bpy.data.node_groups["NodeGroup.174"]
        nestedcandlegpointtext_node_group = bpy.data.node_groups["NodeGroup.173"]

        noderestoreusmaptitle = ['String to Curves', 'String to Curves.002', 'String to Curves.004']
        for name in noderestoreusmaptitle:
            noderestoreusmaptitle = noderestoreusmap_group.nodes.get(name)
            if noderestoreusmaptitle:
                datausmaptitle_font = bpy.data.fonts["Open Sans Extrabold"]
                noderestoreusmaptitle.font = datausmaptitle_font   

        noderestoreusmapsubtitle = ['String to Curves.005', 'String to Curves.001', 'String to Curves.003']
        for name in noderestoreusmapsubtitle:
            noderestoreusmapsubtitle = noderestoreusmap_group.nodes.get(name)
            if noderestoreusmapsubtitle:
                datausmapsubtitle_font = bpy.data.fonts["Open Sans Light"]
                noderestoreusmapsubtitle.font = datausmapsubtitle_font
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
         
class FontchangeVBG(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatorvbgfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        nodevvbg_group = modifier.node_group
        
        nodevvbgtitle = nodevvbg_group.nodes['String to Curves.005']
        datavvbgtitle_font = bpy.data.fonts.load(mytool.my_pathfontvbg_title)
        nodevvbgtitle.font = datavvbgtitle_font
        
        nodevvbgsubtitle = nodevvbg_group.nodes['String to Curves.006']
        datavvbgsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontvbg_subtitle)
        nodevvbgsubtitle.font = datavvbgsubtitle_font

        nodevvbgvalue = ['String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.022', 'String to Curves.023', 'String to Curves.024']
        for name in nodevvbgvalue:
            nodevvbgvalue = nodevvbg_group.nodes.get(name)
            if nodevvbgvalue:
                datavvbgvalue_font = bpy.data.fonts.load(mytool.my_pathfontvbg_barvalue)
                nodevvbgvalue.font = datavvbgvalue_font

        nodevvbgrangenumbers = ['String to Curves.011', 'String to Curves.013', 'String to Curves.014', 'String to Curves.015', 'String to Curves.016']
        for name in nodevvbgrangenumbers:
            nodevvbgrangenumbers = nodevvbg_group.nodes.get(name)
            if nodevvbgrangenumbers:
                datavvbgrangenumbers_font = bpy.data.fonts.load(mytool.my_pathfontvbg_rangenumbers)
                nodevvbgrangenumbers.font = datavvbgrangenumbers_font    
        
        nodevvbgpointtext = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010']
        for name in nodevvbgpointtext:
            nodevvbgpointtext = nodevvbg_group.nodes.get(name)
            if nodevvbgpointtext:
                datavvbgpointtext_font = bpy.data.fonts.load(mytool.my_pathfontvbg_bartext)
                nodevvbgpointtext.font = datavvbgpointtext_font

        nodevvbgtexttotal = ['String to Curves.004']
        for name in nodevvbgtexttotal:
            nodevvbgtexttotal = nodevvbg_group.nodes.get(name)
            if nodevvbgtexttotal:
                datavvbgtexttotal_font = bpy.data.fonts.load(mytool.my_pathfontvbg_texttotal)
                nodevvbgtexttotal.font = datavvbgtexttotal_font   

        nodevvbgvaluetotal = ['String to Curves.012']
        for name in nodevvbgvaluetotal:
            nodevvbgvaluetotal = nodevvbg_group.nodes.get(name)
            if nodevvbgvaluetotal:
                datavvbgvaluetotal_font = bpy.data.fonts.load(mytool.my_pathfontvbg_valuetotal)
                nodevvbgvaluetotal.font = datavvbgvaluetotal_font    
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreVBG(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorvbgresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestorevvbg_group = modifier.node_group
        
        noderestorevvbgtitle = noderestorevvbg_group.nodes['String to Curves.005']
        datarestorevvbgtitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestorevvbgtitle.font = datarestorevvbgtitle_font
        
        noderestorevvbgsubtitle = noderestorevvbg_group.nodes['String to Curves.006']
        datarestorevvbgsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestorevvbgsubtitle.font = datarestorevvbgsubtitle_font

        nodevvbgvalue = ['String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.022', 'String to Curves.023', 'String to Curves.024']
        for name in nodevvbgvalue:
            nodevvbgvalue = noderestorevvbg_group.nodes.get(name)
            if nodevvbgvalue:
                datavvbgvalue_font = bpy.data.fonts["Open Sans Extrabold"]
                nodevvbgvalue.font = datavvbgvalue_font     
        
        nodevvbgrangenumbers = ['String to Curves.011', 'String to Curves.013', 'String to Curves.014', 'String to Curves.015', 'String to Curves.016']
        for name in nodevvbgrangenumbers:
            nodevvbgrangenumbers = noderestorevvbg_group.nodes.get(name)
            if nodevvbgrangenumbers:
                datavvbgrangenumbers_font = bpy.data.fonts["Open Sans Light"]
                nodevvbgrangenumbers.font = datavvbgrangenumbers_font  

        nodevvbgpointtext = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010']
        for name in nodevvbgpointtext:
            nodevvbgpointtext = noderestorevvbg_group.nodes.get(name)
            if nodevvbgpointtext:
                datavvbgpointtext_font = bpy.data.fonts["Open Sans Regular"]
                nodevvbgpointtext.font = datavvbgpointtext_font  

        nodevvbgtexttotal = ['String to Curves.004']
        for name in nodevvbgtexttotal:
            nodevvbgtexttotal = noderestorevvbg_group.nodes.get(name)
            if nodevvbgtexttotal:
                datavvbgtexttotal_font = bpy.data.fonts["Open Sans Extrabold"]
                nodevvbgtexttotal.font = datavvbgtexttotal_font  

        nodevvbgvaluetotal = ['String to Curves.012']
        for name in nodevvbgvaluetotal:
            nodevvbgvaluetotal = noderestorevvbg_group.nodes.get(name)
            if nodevvbgvaluetotal:
                datavvbgvaluetotal_font = bpy.data.fonts["Open Sans Extrabold"]
                nodevvbgvaluetotal.font = datavvbgvaluetotal_font 
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontchangeVBGC(bpy.types.Operator):
    bl_label = "Apply All Fonts"
    bl_idname = "addonname.myop_operatorvbgcfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        nodevvbgc_group = modifier.node_group
        
        nodevvbgctitle = nodevvbgc_group.nodes['String to Curves.005']
        datavvbgctitle_font = bpy.data.fonts.load(mytool.my_pathfontvbgc_title)
        nodevvbgctitle.font = datavvbgctitle_font
        
        nodevvbgcsubtitle = nodevvbgc_group.nodes['String to Curves.006']
        datavvbgcsubtitle_font = bpy.data.fonts.load(mytool.my_pathfontvbgc_subtitle)
        nodevvbgcsubtitle.font = datavvbgcsubtitle_font

        nodevvbgcvaluea = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.022', 'String to Curves.023']
        for name in nodevvbgcvaluea:
            nodevvbgcvaluea = nodevvbgc_group.nodes.get(name)
            if nodevvbgcvaluea:
                datavvbgcvaluea_font = bpy.data.fonts.load(mytool.my_pathfontvbgc_barvaluea)
                nodevvbgcvaluea.font = datavvbgcvaluea_font

        nodevvbgcvalueb = ['String to Curves.025', 'String to Curves.026', 'String to Curves.027', 'String to Curves.028', 'String to Curves.029', 'String to Curves.030', 'String to Curves.031', 'String to Curves.032']
        for name in nodevvbgcvalueb:
            nodevvbgcvalueb = nodevvbgc_group.nodes.get(name)
            if nodevvbgcvalueb:
                datavvbgcvalueb_font = bpy.data.fonts.load(mytool.my_pathfontvbgc_barvalueb)
                nodevvbgcvalueb.font = datavvbgcvalueb_font

        nodevvbgcrangenumbers = ['String to Curves.011', 'String to Curves.012', 'String to Curves.013', 'String to Curves.014', 'String to Curves.015']
        for name in nodevvbgcrangenumbers:
            nodevvbgcrangenumbers = nodevvbgc_group.nodes.get(name)
            if nodevvbgcrangenumbers:
                datavvbgcrangenumbers_font = bpy.data.fonts.load(mytool.my_pathfontvbgc_rangenumbers)
                nodevvbgcrangenumbers.font = datavvbgcrangenumbers_font    
        
        nodevvbgcpointtext = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010']
        for name in nodevvbgcpointtext:
            nodevvbgcpointtext = nodevvbgc_group.nodes.get(name)
            if nodevvbgcpointtext:
                datavvbgcpointtext_font = bpy.data.fonts.load(mytool.my_pathfontvbgc_bartext)
                nodevvbgcpointtext.font = datavvbgcpointtext_font

        nodevvbgclegend = ['String to Curves.033', 'String to Curves.034']
        for name in nodevvbgclegend:
            nodevvbgclegend = nodevvbgc_group.nodes.get(name)
            if nodevvbgclegend:
                datavvbgclegend_font = bpy.data.fonts.load(mytool.my_pathfontvbgc_legend)
                nodevvbgclegend.font = datavvbgclegend_font     
        
        bpy.ops.file.pack_all()    
        
        return {'FINISHED'}
    
class FontrestoreVBGC(bpy.types.Operator):
    bl_label = "Restore OpenSans"
    bl_idname = "addonname.myop_operatorvbgcresfont"
        
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        obj = bpy.context.view_layer.objects.active
        modifier = obj.modifiers["GeometryNodes"]
        noderestorevvbgc_group = modifier.node_group
        
        noderestorevvbgctitle = noderestorevvbgc_group.nodes['String to Curves.005']
        datarestorevvbgctitle_font = bpy.data.fonts["Open Sans Extrabold"]
        noderestorevvbgctitle.font = datarestorevvbgctitle_font
        
        noderestorevvbgcsubtitle = noderestorevvbgc_group.nodes['String to Curves.006']
        datarestorevvbgcsubtitle_font = bpy.data.fonts["Open Sans Light"]
        noderestorevvbgcsubtitle.font = datarestorevvbgcsubtitle_font

        nodevvbgcvaluea = ['String to Curves.016', 'String to Curves.017', 'String to Curves.018', 'String to Curves.019', 'String to Curves.020', 'String to Curves.021', 'String to Curves.022', 'String to Curves.023']
        for name in nodevvbgcvaluea:
            nodevvbgcvaluea = noderestorevvbgc_group.nodes.get(name)
            if nodevvbgcvaluea:
                datavvbgcvaluea_font = bpy.data.fonts["Open Sans Extrabold"]
                nodevvbgcvaluea.font = datavvbgcvaluea_font   

        nodevvbgcvalueb = ['String to Curves.025', 'String to Curves.026', 'String to Curves.027', 'String to Curves.028', 'String to Curves.029', 'String to Curves.030', 'String to Curves.031', 'String to Curves.032']
        for name in nodevvbgcvalueb:
            nodevvbgcvalueb = noderestorevvbgc_group.nodes.get(name)
            if nodevvbgcvalueb:
                datavvbgcvalueb_font = bpy.data.fonts["Open Sans Extrabold"]
                nodevvbgcvalueb.font = datavvbgcvalueb_font    
        
        nodevvbgcrangenumbers = ['String to Curves.011', 'String to Curves.012', 'String to Curves.013', 'String to Curves.014', 'String to Curves.015']
        for name in nodevvbgcrangenumbers:
            nodevvbgcrangenumbers = noderestorevvbgc_group.nodes.get(name)
            if nodevvbgcrangenumbers:
                datavvbgcrangenumbers_font = bpy.data.fonts["Open Sans Regular"]
                nodevvbgcrangenumbers.font = datavvbgcrangenumbers_font  

        nodevvbgcpointtext = ['String to Curves', 'String to Curves.001', 'String to Curves.002', 'String to Curves.003', 'String to Curves.007', 'String to Curves.008', 'String to Curves.009', 'String to Curves.010']
        for name in nodevvbgcpointtext:
            nodevvbgcpointtext = noderestorevvbgc_group.nodes.get(name)
            if nodevvbgcpointtext:
                datavvbgcpointtext_font = bpy.data.fonts["Open Sans Regular"]
                nodevvbgcpointtext.font = datavvbgcpointtext_font  

        nodevvbgclegend = ['String to Curves.033', 'String to Curves.034']
        for name in nodevvbgclegend:
            nodevvbgclegend = noderestorevvbgc_group.nodes.get(name)
            if nodevvbgclegend:
                datavvbgclegend_font = bpy.data.fonts["Open Sans Regular"]
                nodevvbgclegend.font = datavvbgclegend_font  
        
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

classes = [MyProperties, MyoperatorCGsql, MyoperatorPGsql, Myoperator23CGsql, Myoperatorcandlesql, Myoperator23PGsql, MyoperatorHBGsql, MyoperatorHBGCsql, MyoperatorMCGsql, MyoperatorMPGsql, MyoperatorLGsql, MyoperatorMGsql, MyoperatorLGCsql, MyoperatorMGCsql, Myoperatorusmapsql, MyoperatorVBGsql, MyoperatorVBGCsql, MyoperatorCGcsv, MyoperatorCGCcsv, MyoperatorCANDLEcsv, MyoperatorPGCcsv, MyoperatorPGcsv, MyoperatorLGcsv, MyoperatorLGCcsv, 
MyoperatorHBcsv, MyoperatorHBCcsv, MyoperatorMCcsv, MyoperatorMPcsv, MyoperatorMGcsv, MyoperatorMGCcsv, MyoperatorUSMcsv, MyoperatorVBcsv, 
MyoperatorVBCcsv, RenderRender2, ADDONNAME_OT_my_opc, ADDONNAME_OT_my_op23cAL, ADDONNAME_OT_my_op23cBL, ADDONNAME_OT_my_op23cCL, 
ADDONNAME_OT_my_op23pAL, ADDONNAME_OT_my_op23pBL, ADDONNAME_OT_my_op23pCL, ADDONNAME_OT_my_opHBGAL, ADDONNAME_OT_my_opHBGBL, 
ADDONNAME_OT_my_opHBGCL, ADDONNAME_OT_my_opHBGDL, ADDONNAME_OT_my_opHBGEL, ADDONNAME_OT_my_opHBGFL, ADDONNAME_OT_my_opHBGGL, ADDONNAME_OT_my_opHBGHL, ADDONNAME_OT_my_opHBGIL, ADDONNAME_OT_my_opHBGJL, ADDONNAME_OT_my_opVBGAL, ADDONNAME_OT_my_opVBGBL, ADDONNAME_OT_my_opVBGCL, 
ADDONNAME_OT_my_opVBGDL, ADDONNAME_OT_my_opVBGEL, ADDONNAME_OT_my_opVBGFL, ADDONNAME_OT_my_opVBGGL, ADDONNAME_OT_my_opVBGHL,  
ADDONNAME_23C, ADDONNAME_23P, ADDONNAME_LGC, ADDONNAME_HBC, ADDONNAME_MG, ADDONNAME_MGC, ADDONNAME_USM, ADDONNAME_VB, ADDONNAME_VBC, ADDONNAME_OT_my_opggpie, 
ADDONNAME_OT_my_op, ADDONNAME_OT_my_op2, ADDONNAME_OT_my_op2pie, ADDONNAME_OT_my_oplgpie, ADDONNAME_OT_my_ophbpie, ADDONNAME_OT_my_opmcpie, 
ADDONNAME_OT_my_opmppie, ADDONNAME_OT_my_op3, FontchangeCG, FontchangePG, Fontchange23CG, Fontchange23PG, FontchangeCANDLEG, FontchangeLINEG, FontchangeMOUNTAING, FontchangeLINEGC, FontchangeMOUNTAINGC, FontchangeHBG, FontchangeMCG, FontchangeMPG, FontchangeUSM, FontrestoreUSM, FontchangeVBG, FontchangeVBGC, FontrestoreVBGC, FontrestoreVBG, FontrestoreMPG, FontrestoreMCG, FontrestoreHBG, FontchangeHBGC, FontrestoreHBGC, FontrestoreLINEGC, FontrestoreMOUNTAING, FontrestoreMOUNTAINGC, Fontrestore23CG, FontrestoreLINEG, Fontrestore23PG, FontrestoreCG, FontrestorePG, FontrestoreCANDLEG,
NG_PT_QuickRenderPresets_1, NG_PT_QuickRenderPresets_2, CIRCLE_GRAPH_PT_panel_1, CIRCLE_GRAPH_PT_panel_2, CIRCLE_GRAPH_PT_panel_3, CIRCLE_GRAPH_PT_panel_4, CIRCLE_GRAPH_PT_panel_5, CIRCLE_GRAPH_23_PT_panel_1, CIRCLE_GRAPH_23_PT_panel_2, CIRCLE_GRAPH_23_PT_panel_3, CIRCLE_GRAPH_23_PT_panel_4, CIRCLE_GRAPH_23_PT_panel_5, CANDLESTICK_GRAPH_PT_panel_1, CANDLESTICK_GRAPH_PT_panel_2, CANDLESTICK_GRAPH_PT_panel_3, CANDLESTICK_GRAPH_PT_panel_4, CANDLESTICK_GRAPH_PT_panel_5, PIE_GRAPH_PT_panel_1, PIE_GRAPH_PT_panel_2, PIE_GRAPH_PT_panel_3, PIE_GRAPH_PT_panel_4, PIE_GRAPH_PT_panel_5, PIE_GRAPH_23_PT_panel_1, 
PIE_GRAPH_23_PT_panel_2, PIE_GRAPH_23_PT_panel_3, PIE_GRAPH_23_PT_panel_4, PIE_GRAPH_23_PT_panel_5, LINE_GRAPH_PT_panel_1, LINE_GRAPH_PT_panel_2, LINE_GRAPH_PT_panel_3, LINE_GRAPH_PT_panel_4, LINE_GRAPH_PT_panel_5, COMPARISON_LINE_GRAPH_PT_panel_1, COMPARISON_LINE_GRAPH_PT_panel_2, COMPARISON_LINE_GRAPH_PT_panel_3, COMPARISON_LINE_GRAPH_PT_panel_4, COMPARISON_LINE_GRAPH_PT_panel_5,  HORIZONTAL_BAR_GRAPH_PT_panel_1, HORIZONTAL_BAR_GRAPH_PT_panel_2, HORIZONTAL_BAR_GRAPH_PT_panel_3, HORIZONTAL_BAR_GRAPH_PT_panel_4, HORIZONTAL_BAR_GRAPH_PT_panel_5, 
COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_1, COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_2, COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_3, COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_4, COMPARISON_HORIZONTAL_BAR_GRAPH_PT_panel_5, MULTIPLE_CIRCLE_GRAPH_PT_panel_1, MULTIPLE_CIRCLE_GRAPH_PT_panel_2, MULTIPLE_CIRCLE_GRAPH_PT_panel_3, MULTIPLE_CIRCLE_GRAPH_PT_panel_4, MULTIPLE_CIRCLE_GRAPH_PT_panel_5, MULTIPLE_PIE_GRAPH_PT_panel_1, MULTIPLE_PIE_GRAPH_PT_panel_2, MULTIPLE_PIE_GRAPH_PT_panel_3, MULTIPLE_PIE_GRAPH_PT_panel_4, MULTIPLE_PIE_GRAPH_PT_panel_5, MOUNTAIN_GRAPH_PT_panel_1, MOUNTAIN_GRAPH_PT_panel_2, MOUNTAIN_GRAPH_PT_panel_3, MOUNTAIN_GRAPH_PT_panel_4, MOUNTAIN_GRAPH_PT_panel_5,
COMPARISON_MOUNTAIN_GRAPH_PT_panel_1, COMPARISON_MOUNTAIN_GRAPH_PT_panel_2, COMPARISON_MOUNTAIN_GRAPH_PT_panel_3, COMPARISON_MOUNTAIN_GRAPH_PT_panel_4, COMPARISON_MOUNTAIN_GRAPH_PT_panel_5, Locationchange, US_MAP_PT_panel_1, US_MAP_PT_panel_2, US_MAP_PT_panel_3, US_MAP_PT_panel_4, US_MAP_PT_panel_5, VERTICAL_BAR_GRAPH_PT_panel_1, VERTICAL_BAR_GRAPH_PT_panel_2, VERTICAL_BAR_GRAPH_PT_panel_3, VERTICAL_BAR_GRAPH_PT_panel_4, VERTICAL_BAR_GRAPH_PT_panel_5, COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_1, COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_2, COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_3, COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_4, COMPARISON_VERTICAL_BAR_GRAPH_PT_panel_5, ADDONNAME_OT_my_opLGAL, 
ADDONNAME_OT_my_opLGBL, ADDONNAME_OT_my_opLGCL, ADDONNAME_OT_my_opLGDL, ADDONNAME_OT_my_opLGEL, ADDONNAME_OT_my_opLGFL,ADDONNAME_OT_my_opLGGL, ADDONNAME_OT_my_opLGHL, ADDONNAME_OT_my_opMGAL, ADDONNAME_OT_my_opMGBL, ADDONNAME_OT_my_opMGCL, ADDONNAME_OT_my_opMGDL, ADDONNAME_OT_my_opMGEL, ADDONNAME_OT_my_opMGFL, ADDONNAME_OT_my_opMGGL, ADDONNAME_OT_my_opMGHL, ADDONNAME_OT_my_opMCGAL, ADDONNAME_OT_my_opMCGBL, ADDONNAME_OT_my_opMCGCL, ADDONNAME_OT_my_opMCGDL, ADDONNAME_OT_my_opMCGEL, ADDONNAME_OT_my_opMCGFL, ADDONNAME_OT_my_opMCGGL, ADDONNAME_OT_my_opMCGHL, ADDONNAME_OT_my_opMPGAL, ADDONNAME_OT_my_opMPGBL, ADDONNAME_OT_my_opMPGCL, ADDONNAME_OT_my_opMPGDL, ADDONNAME_OT_my_opMPGEL, ADDONNAME_OT_my_opMPGFL, ADDONNAME_OT_my_opMPGGL, ADDONNAME_OT_my_opMPGHL, 
ADDONNAME_OT_my_opCOMPARISONAHBARAL, ADDONNAME_OT_my_opCOMPARISONAHBARBL, ADDONNAME_OT_my_opCOMPARISONAHBARCL, ADDONNAME_OT_my_opCOMPARISONAHBARD, ADDONNAME_OT_my_opCOMPARISONAHBARE, ADDONNAME_OT_my_opCOMPARISONAHBARF, ADDONNAME_OT_my_opCOMPARISONAHBARG, ADDONNAME_OT_my_opCOMPARISONAHBARH, ADDONNAME_OT_my_opCOMPARISONAHBARI, ADDONNAME_OT_my_opCOMPARISONBHBARAL, ADDONNAME_OT_my_opCOMPARISONBHBARBL, ADDONNAME_OT_my_opCOMPARISONBHBARCL, ADDONNAME_OT_my_opCOMPARISONBHBARD, ADDONNAME_OT_my_opCOMPARISONBHBARE, ADDONNAME_OT_my_opCOMPARISONBHBARF, ADDONNAME_OT_my_opCOMPARISONBHBARG, ADDONNAME_OT_my_opCOMPARISONBHBARH, ADDONNAME_OT_my_opCOMPARISONBHBARI, ADDONNAME_OT_my_opCOMPARISONALINEAL, ADDONNAME_OT_my_opCOMPARISONALINEB, ADDONNAME_OT_my_opCOMPARISONALINEC, ADDONNAME_OT_my_opCOMPARISONALINED, ADDONNAME_OT_my_opCOMPARISONALINEE, ADDONNAME_OT_my_opCOMPARISONALINEF, ADDONNAME_OT_my_opCOMPARISONALINEH, ADDONNAME_OT_my_opCOMPARISONALINEG, ADDONNAME_OT_my_opCOMPARISONBLINEA, 
ADDONNAME_OT_my_opCOMPARISONBLINEB, ADDONNAME_OT_my_opCOMPARISONBLINEC, ADDONNAME_OT_my_opCOMPARISONBLINED, ADDONNAME_OT_my_opCOMPARISONBLINEE, ADDONNAME_OT_my_opCOMPARISONBLINEF, ADDONNAME_OT_my_opCOMPARISONBLINEG, ADDONNAME_OT_my_opCOMPARISONBLINEH, ADDONNAME_OT_my_opCOMPARISONAMOUNTA, ADDONNAME_OT_my_opCOMPARISONAMOUNTB, ADDONNAME_OT_my_opCOMPARISONAMOUNTC, ADDONNAME_OT_my_opCOMPARISONAMOUNTD, ADDONNAME_OT_my_opCOMPARISONAMOUNTE, ADDONNAME_OT_my_opCOMPARISONAMOUNTF, ADDONNAME_OT_my_opCOMPARISONAMOUNTG, ADDONNAME_OT_my_opCOMPARISONAMOUNTH, ADDONNAME_OT_my_opCOMPARISONBMOUNTA, ADDONNAME_OT_my_opCOMPARISONBMOUNTB, 
ADDONNAME_OT_my_opCOMPARISONBMOUNTC, ADDONNAME_OT_my_opCOMPARISONBMOUNTD, ADDONNAME_OT_my_opCOMPARISONBMOUNTE, ADDONNAME_OT_my_opCOMPARISONBMOUNTF, ADDONNAME_OT_my_opCOMPARISONBMOUNTG, ADDONNAME_OT_my_opCOMPARISONBMOUNTH, ADDONNAME_OT_my_opCOMPARISONABARVA, ADDONNAME_OT_my_opCOMPARISONABARVB, ADDONNAME_OT_my_opCOMPARISONABARVC, ADDONNAME_OT_my_opCOMPARISONABARVD, ADDONNAME_OT_my_opCOMPARISONABARVE, ADDONNAME_OT_my_opCOMPARISONABARVF, ADDONNAME_OT_my_opCOMPARISONABARVG, ADDONNAME_OT_my_opCOMPARISONABARVH, ADDONNAME_OT_my_opCOMPARISONBBARVA, ADDONNAME_OT_my_opCOMPARISONBBARVB, ADDONNAME_OT_my_opCOMPARISONBBARVC, 
ADDONNAME_OT_my_opCOMPARISONBBARVD, ADDONNAME_OT_my_opCOMPARISONBBARVE, ADDONNAME_OT_my_opCOMPARISONBBARVF, ADDONNAME_OT_my_opCOMPARISONBBARVG, ADDONNAME_OT_my_opCOMPARISONBBARVH]
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type= MyProperties)
        
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    
if __name__ == "__main__":
    register()


