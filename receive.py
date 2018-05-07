#Wade King implemented this!
from kivy.app           import App
from kivy.uix.button    import Button
from kivy.uix.label     import Label
from kivy.uix.boxlayout import BoxLayout

# Import kivy osc library
from kivy.lib.osc         import oscAPI 
# Import clock (required by osc listener)
from kivy.clock           import Clock

#Wade King implemented this!
from kivy.app           import App
from kivy.uix.button    import Button
from kivy.uix.label     import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image      import Image
from kivy.uix.scatter    import Scatter
from kivy.properties     import *
# Import kivy osc library
from kivy.lib.osc         import oscAPI 
# Import clock (required by osc listener)
from kivy.clock           import Clock
from kivy.config import Config
from kivy.core.window import Window


import VideoPlayer

class receiver(App):

    # Set ip and port to listen to
    ip = '0.0.0.0' # listens to any sender IP
    port = 5000    # listens only to this port
    play = VideoPlayer.VideoPlayer()

    def build(self):
        Window.size = (1366, 768)
        Window.borderless = True
        Window.fullscreen = True
        scat = Scatter()
        # Starts OSC
        oscAPI.init()  
        # Instanciates OSC listener
        oscid = oscAPI.listen(ipAddr=self.ip, port= self.port) 
        # listens for osc messages every screen refresh
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)
        # binds messages - this listens to messages if prefix /1/tok
        oscAPI.bind(oscid, self.token_on, '0')

        # add a label to the screen
        root = FloatLayout(size=(2950,1650), orientation='vertical')
        #self.label = Label(text="This is our vertical sceen!", font_size='50sp')
        #root.add_widget(self.label)

        root_image = Image(source='PauseScreen.png', size_hint_x=None, width=1366,
                                              size_hint_y=None, height=768,
                                              allow_stretch = True,
                                              keep_ratio = True)
        root.add_widget(root_image)
        # console message - ready!
        print "Ready to receive!"
        #self.receivedegrees(0,0)
        #self.receivedegrees(90,1)
     #   self.receivedegrees(180)
     #   self.receivedegrees(270)
        # return root
        return root
#if __name__ == "__main__":
    def token_on(self, vidnum, instance):
        print "received data from sender"
        print "%s" % vidnum[2]
        vid_num = int(vidnum[2]) #int(degrees[3])
        current_angle = 61
        #time = float(degrees[2]) / 360;
        print "vidnum = %d" % vid_num
        #play = VideoPlayer.VideoPlayer()
        self.play.chooseVideo(vid_num)
         
        return self.play

    def token_turned(self, data, instance):
        vid_num = self.play.currentVid
        current_angle = 61 #data[3]
        videotime = self.play.get_time(current_angle, vid_num)
        self.play.scrubVideo(videotime)

receiver().run()
