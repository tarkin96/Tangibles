#Wade King implemented this!
from kivy.app           import App
from kivy.uix.button    import Button
from kivy.uix.label     import Label
from kivy.uix.boxlayout import BoxLayout

# Import kivy osc library
from kivy.lib.osc         import oscAPI 
# Import clock (required by osc listener)
from kivy.clock           import Clock

class TestApp(App):
    # Set ip and port to listen to
    ip = '0.0.0.0' # listens to any sender IP
    port = 5000    # listens only to this port

    def build(self):
        # Starts OSC
        oscAPI.init()  
        # Instanciates OSC listener
        oscid = oscAPI.listen(ipAddr=self.ip, port= self.port) 
        # listens for osc messages every screen refresh
        Clock.schedule_interval(lambda *x: oscAPI.readQueue(oscid), 0)

        # binds messages - this listens to messages if prefix /1/tok
        oscAPI.bind(oscid, self.receivedegrees, 0)

        # add a label to the screen
        root = BoxLayout(orientation='vertical')
        self.label = Label(text="This is our vertical sceen!", font_size='50sp')
        root.add_widget(self.label)

        # console message - ready!
        print "Ready to receive!"
        self.receivedegrees(0)
        self.receivedegrees(90)
        self.receivedegrees(180)
        self.receivedegrees(270)
        # return root
        return root
    def receivedegrees(self, degrees):
        print "received data from sender"
        print "%d" % degrees

        time = float(degrees) / 360;
        print "percent of way through video: %f" % time
        #print "opening video at timestamp"
        #scrubvideo(0, time)
    #OSC callback function
   # def cb_tok(self, value, instance): 
        # print message received to console
       # print "Message received: "
      #  print value
        #self.label.text = "Messages received: " + str(value[2])

TestApp().run()