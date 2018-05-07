### This file was adapted from the original example file
###This file is for the horizontal screen

import sys
import os
sys.path.append(os.getcwd() + "/lib/garden.tei_knob/")

import kivy
from kivy.app import App
from kivy.properties     import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter    import Scatter
from kivy.uix.image      import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config

from tei_knob import  Knob

import kivy
from kivy.lib.osc         import oscAPI 
from kivy.app import App
# Import clock (required by osc listener)
from kivy.clock           import Clock
#Wade made all changes related to resolution
from win32api import GetSystemMetrics

class sender(App):

    def build(self):
        oscAPI.init()

    def sendMessage(self, tokenNum):
        # ip = '198.21.242.1'
        #ip = '192.168.43.151'
        ip = '198.21.199.110'

        port = 5000
        print("Sending Message! " + tokenNum)
        oscAPI.sendMsg( '0', [tokenNum], ipAddr= ip, port= port)
        
    pass

sender().run()


class MyKnob(Knob):
    # Object property that receives the image
    obj = ObjectProperty()
    send = sender();
    # on_knob is called if value, token_id or token_placed chage
    def on_knob(self, value, pattern_id):
        angle = value
        self.obj.rotation = angle
        # sender.sendMessage(self, str(int(self.obj.rotation)))
        # print("Token #: " + str(self.knobimg_source) + "\nRotation Value: " + str(self.obj.rotation))

    # on_token_place is called when the token is detected, sends the message
    def on_token_placed(self, instance, value):
        videoNum = 0

        if self.knobimg_source == "knob1.png":
            videoNum = 0
        elif self.knobimg_source == "knob2.png":
            videoNum = 1
        elif self.knobimg_source == "knob3.png":
            videoNum = 2
        else:
            videoNum = 3
        
        #self.remove_widget(self.arrows1)
        #self.remove_widget(self.arrows2)
        #self.remove_widget(self.arrows3)
        #self.remove_widget(self.arrows4)
        # sends the number of the knob to the verticle screen so it knows
        # what video to play
        sender.sendMessage(self.send, str(videoNum))
        print("Token Number: " + str(videoNum))

#done by wade
resolution = [GetSystemMetrics(0), GetSystemMetrics(1)]
def scale_to_res(val, i, j):
        
        return (int(float(val) / float(i) * float(resolution[j])))

class TeiKnobApp(App): 
    count = 0
    def build(self):

        Config.set('graphics', 'width', str(resolution[0]))
        Config.set('graphics', 'height', str(resolution[1]))
        Config.set('graphics', 'borderless', 1)
        Config.set('graphics', 'fullscreen', 1)
        # creates a float layout
        root = FloatLayout(size=(resolution[0],resolution[1]), pos = (0,0))
        # Creates a scatter widget
        scatter = Scatter()
       
        # Creates an image widget
        root_image = Image(source='Bottom_Screen1.jpeg', size_hint_x=None, width=resolution[0],
                                              size_hint_y=None, height=resolution[1],
                                              allow_stretch = True,
                                              keep_ratio = True)
        root.add_widget(root_image)

        # Creates the knob objects - creates first knob
        knob1 = MyKnob(size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob1.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter) # Passes the object to the knob

        # Creates second knob object
        knob2 = MyKnob(size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob2.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter) # Passes the object to the knob

        # Creates third knob
        knob3 = MyKnob(size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob3.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter) # Passes the object to the knob

        # Creates fourth knob
        knob4 = MyKnob(size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                         min = 0, max = 360,
                         step = 1,
                         show_marker = True,
                         knobimg_source = "knob4.png",
                         marker_img = "img/bline.png",
                         markeroff_color = (0.3, 0.3, .3, 1),
                         pattern_id= 99, #(ids 1 to 8, or 99 for no id)
                         debug = False,
                         obj = scatter) # Passes the object to the knob

        # These functions place the konbs on the screen in the right position
        widget1 = RelativeLayout(size_hint = (None, None), 
                                 size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                                 pos = (scale_to_res(96, 1980, 0), scale_to_res(40, 1080, 1))) #152
        widget1.add_widget(knob1)


        widget2 = RelativeLayout(size_hint = (None, None), 
                                 size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                                 pos = (scale_to_res(585, 1980, 0), scale_to_res(40, 1080, 1))) #880
        widget2.add_widget(knob2)


        widget3 = RelativeLayout(size_hint = (None, None), 
                                 size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                                 pos = (scale_to_res(1080, 1980, 0), scale_to_res(40, 1080, 1))) #1610
        widget3.add_widget(knob3)


        widget4 = RelativeLayout(size_hint = (None, None), 
                                 size = (scale_to_res(315, 1980, 0),scale_to_res(315, 1980, 0)),
                                 pos = (scale_to_res(1574, 1980, 0), scale_to_res(40, 1080, 1))) #2340
        widget4.add_widget(knob4)
        
        
        # Adds knob to the root
        root.add_widget(widget1)

        root.add_widget(widget2)

        root.add_widget(widget3)

        root.add_widget(widget4)

        #done by wade
        arrows1 = Image(source='arrows.png', size_hint_x=None, width=425,
                                              size_hint_y=None, height=425,
                                              pos = (scale_to_res(-10, 1980, 0), scale_to_res(-65, 1080, 1)),
                                              allow_stretch = True,
                                              keep_ratio = True)
        #scatter1 = Scatter()
        #scatter1.add_widget(arrows1)
        root.add_widget(arrows1)        
        arrows2 = Image(source='arrows.png', size_hint_x=None, width=425,
                                              size_hint_y=None, height=425,
                                              pos = (scale_to_res(470, 1980, 0), scale_to_res(-65, 1080, 1)),
                                              allow_stretch = True,
                                              keep_ratio = True) 
        #scatter2 = Scatter().add_widget(arrows2)
        root.add_widget(arrows2) 
        arrows3 = Image(source='arrows.png', size_hint_x=None, width=425,
                                              size_hint_y=None, height=425,
                                              pos = (scale_to_res(965, 1980, 0), scale_to_res(-65, 1080, 1)),
                                              allow_stretch = True,
                                              keep_ratio = True)
        #scatter3 = Scatter().add_widget(arrows3)
        root.add_widget(arrows3)  
        arrows4 = Image(source='arrows.png', size_hint_x=None, width=425,
                                              size_hint_y=None, height=425,
                                              pos = (scale_to_res(1465, 1980, 0), scale_to_res(-65, 1080, 1)),
                                              allow_stretch = True,
                                              keep_ratio = True)
        #scatter4 = Scatter().add_widget(arrows4)
        root.add_widget(arrows4)  

        #anim = Animation(center = scatter1.pos, rotation = 360)
        #anim.start(scatter1);
        return root

TeiKnobApp().run()
