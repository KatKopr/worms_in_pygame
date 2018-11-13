#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Frame:
    
    def __init__(self, control):
        self.control=control
        self.player=[]
        self.timer=self.control.timer
        self.weapons=self.control.rocket_types
        #self.weapons=["Shotgun","Bazooka"]
    def draw(self):
        self.player=self.control.world.gamers[self.control.worm_no]
        health=self.control.worm.health/0.008
        #x=self.control.win.get_width
        #y=self.control.win.get_height
        x=200
        y=700
        if sum(self.control.alive_worms) > 1: 
            text="PLAYER: "+ self.player +", HEALTH: %.2f" % health
            self.write(text, x, y, 30)
            text2="Time remaining: "+ str(self.control.timer.time_remaining)
            self.write(text2, x, y+40, 30)
            text3="Weapon: " + str(self.weapons[self.control.worm.rocket_type])
            self.write(text3, x, y-40, 30)
        else:
            self.winner()
            self.control.game.over()
    def write(self, text, x, y, size):
        self.control.write(text, (0,255,0), x, y, size)
    
    def winner(self):
        x=400
        y=600
        a=self.control.alive_worms
        if sum(self.control.alive_worms) > 0:
            winner_number=[i for i, v in enumerate(a) if v==1]
            text="WINNER: "+ str(self.control.world.gamers[winner_number[0]])
        else:
            text="WINNER: NONE"
        text2="GAME OVER"
        #text3="PRESS A TO START AGAIN"
        self.write(text2, x, y+50, 30)
        self.write(text, x, y, 30)
        #self.write(text3, x, y-50, 30)
        
    
    
    
    
            
        

