#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Frame:
    
    def __init__(self, control):
        self.control=control
        self.player=[]
        self.timer=self.control.timer
        self.weapons=self.control.rocket_types
        self.any_key=True
    def draw(self):
        self.player=self.control.world.gamers[self.control.worm_no]
        health=self.control.worm.health/0.008
        x=700
        y=700
        if sum(self.control.alive_worms) > 1: 
            text="PLAYER: "+ self.player +", HEALTH: %.2f" % health
            text2="TIME REMAINING: "+ str(self.control.timer.time_remaining)
            text3="WEAPON: " + str(self.weapons[self.control.worm.rocket_type])
            te=[text3, text, text2]
            for t in te:
                self.write(t, x, y+40*te.index(t), 30)
            x2=x-500
            te=["WEAPON CHANGE: SPACE","PLAYER CHANGE: TAB", "SHOOT: R", "MOVE: ARROWS"]
            for t in te:
                self.write(t, x2, y+40*te.index(t), 30)
        else:
            self.winner()
            self.control.game.over()
        
        if self.any_key:
            t="PRESS ANY KEY (OTHER THAN SPACE) TO START THE GAME"
            self.write(t, x-350, y-200, 30)
        
    def write(self, text, x, y, size):
        self.control.write(text, (0,255,0), x, y, size)
    
    def key(self):
        self.any_key=False
    
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
        self.write(text2, x, y+50, 30)
        self.write(text, x, y, 30)
        
    
    
    
    
            
        

