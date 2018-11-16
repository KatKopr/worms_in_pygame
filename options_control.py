#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from option import Option
#from inputbox import InputBox

class Options_Control:
    
    def __init__(self, options, control, start_window):
        self.options=options
        self.control=control
        self.window=start_window
        self.sound=True
        
    def starting_kit(self):
        self.add_option(Option("START", 0 , 520))
        self.add_option(Option("SOUND ON/OFF", 1, 480))
    
    def add_option(self,option):
        self.options.append(option)
    
    def display_options(self):
        color=(0,255,0)
        x=self.window.x_start
        for option in self.options:
            self.window.write(option.name ,color, x, option.y, 30)
            
    def change_option(self, type):
        a=len(self.options)
        if type=="next":
            self.window.option_no = (self.window.option_no+1)%a
        else:
            self.window.option_no = (self.window.option_no-1)%a
        self.window.draw_pointer()
    
    def process_option(self):
        a=self.options[self.window.option_no]
        if a.name == "START":
            self.control.game.start_again=True
            self.window.quit()
        elif a.name == "SOUND ON/OFF":
            self.sound_control()
        
    def add_gamer(self, gamer):
        self.window.gamers+=gamer
    
    def sound_control(self):
        self.sound=not self.sound
        if self.sound:
            self.control.music_control.play()
        else:
            self.control.music_control.stop()
        

