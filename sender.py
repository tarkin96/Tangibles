import kivy
from kivy.lib.osc         import oscAPI 
from kivy.app import App
# Import clock (required by osc listener)
from kivy.clock           import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class sender(App):
    ip = '127.0.0.1'
    port = 5000

    def build(self):
        oscAPI.init()
        layout = BoxLayout(orientation='horizontal') 
        button =  Button(text='Touch me!', font_size=120)        
        button.bind(on_press=self.pressBtn)
        button.bind(on_release=self.releaseBtn)

        self.label = Label(text="------------", font_size=50)
        layout.add_widget(button)
        layout.add_widget(self.label)
        return layout
    
    def pressBtn(self, event):
        print("button touched")  
        self.label.text = "------------"

        #Adding 1 to counter
        #self.counter += 1 
        # Send OSC message
        oscAPI.sendMsg( '0', [90], ipAddr= self.ip, port= self.port)
        oscAPI.sendMsg( '0', [360], ipAddr= self.ip, port= self.port)
        oscAPI.sendMsg( '0', [127], ipAddr= self.ip, port= self.port) 
        
    def releaseBtn(self, event):
        print("Osc message sent")  
        print("button released") 
        self.label.text = "Osc message sent"

    pass

sender().run()


