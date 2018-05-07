from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivy.lib.osc import oscAPI 
from kivy.uix.actionbar import ActionBar
from kivy.core.window import Window
import time
from kivy.config import Config
#from kivy.lib.gstplayer import GstPlayer
from kivy.uix.image      import Image

#This class def. done by Joshua Moore
class VideoPlayer(App):
    currentVid = -1	

    currentVidCounter = 0
    currentVidObj = None
    Vlayout =  BoxLayout(orientation='vertical')
    video1 = Video(source='transition1-1.m4v')
    video2 = Video(source='transition2-1.m4v') 
    video3 = Video(source='transition3-1.m4v') 
    video4 = Video(source='transition4-1.m4v')    
    #time-related functions done by Wade King
    vidtimeList = [6, 2, 5, 3]
    root_image = Image(source='PauseScreen.png', size_hint_x=None, width=1366,
                                              size_hint_y=None, height=768,
                                              allow_stretch = True,
                                              keep_ratio = True)
    
    #This function done by Joshua Moore
    def build(self):

        Window.size = (1366, 768)
       # Window.borderless = True
        #Window.fullscreen = True


        return self.Vlayout
    #This function done by Joshua Moore
    def chooseVideo(self, vidNum):
  
        # Currently pauses video upon token removal and plays from  
          # previously paused spot
        # Later: Ideally want a static image to display upon removal
          # and for video to start from beginning upon replacement
        videolist = []
           
        if vidNum == self.currentVid:
            if self.currentVidCounter % 2 == 1:
                self.Vlayout.clear_widgets(videolist)
                #videolist.clear()
                del videolist[:]
                self.Vlayout.add_widget(self.currentVidObj)
                self.currentVidObj.state = 'play'
            else:
                self.currentVidObj.state = 'pause'
                self.Vlayout.clear_widgets(videolist)
                #videolist.clear()
                del videolist[:]
                self.Vlayout.add_widget(self.root_image)
                
            self.currentVidCounter += 1
        else:
            self.Vlayout.clear_widgets(videolist)
            #videolist.clear()
            del videolist[:]
            if self.currentVid != -1:
                self.video1.play = False
                self.video2.play = False
                self.video3.play = False
                self.video4.play = False

            #This will be simplified -jm
            if vidNum == 0:
                videolist.insert(0,self.video1)
                self.Vlayout.add_widget(self.video1)
                self.currentVidObj = self.video1
                self.video1.state = 'play'
                print ("Playing Video: 1-1")
            elif vidNum == 1:
                videolist.insert(0,self.video2)
                self.Vlayout.add_widget(self.video2)
                self.currentVidObj = self.video2
                self.video2.state = 'play'
                print ("Playing Video: 2-1")
            elif vidNum == 2:
                videolist.insert(0,self.video3)
                self.Vlayout.add_widget(self.video3)
                self.currentVidObj = self.video3
                self.video3.state = 'play'
                print ("Playing Video: 3-1")
            elif vidNum == 3:
                videolist.insert(0, self.video4)
                self.Vlayout.add_widget(self.video4)
                self.currentVidObj = self.video4
                self.video4.state = 'play'
                print ("Playing Video: 4-1")
            self.currentVid = vidNum
            self.currentVidCounter = 0
            self.run()
           
         
            
            
    #This function written by Wade King
    def scrubVideo(self, timestamp):
        print("hello")

    #this function written by Wade King
    def get_time(self, angle, vidnum):
        print("angle of knob = " + str(angle))
        print("chosen video = " + str(vidnum))
        totaltime = float(self.vidtimeList[vidnum])
        print("Length of Video = " + str(totaltime))
        minutes = int(totaltime / 60)
        timepersixdegrees = float(totaltime / 60)
        print("time for every 6 degrees turned = " + str(timepersixdegrees))
        newangle = angle - (angle % 6)
        print("new angle of knob = " + str(newangle))
        timestamp = timepersixdegrees * (newangle / 6)
        print("timestamp calculated = " + str(timestamp))
        return timestamp

    def closeVid(self):
        self.Vlayout.remove_widget(self.video)
