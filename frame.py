#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Frame:
    
    def __init__(self, control):
        self.control=control
        self.player=[]
        self.time_remaining=[]
    
    def draw(self):
        self.player=self.control.world.gamers[self.control.worm_no]
        health=self.control.worm.health/0.008
        #x=self.control.win.get_width
        #y=self.control.win.get_height
        x=200
        y=700
        text="PLAYER: "+ self.player +", HEALTH: %.2f" % health
        self.write(text, x, y, 30)
    
    def write(self, text, x, y, size):
        self.control.write(text, (0,255,0), x, y, size)
    
    
    
    
            
        

