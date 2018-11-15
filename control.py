#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
from world import World
from frame import Frame
from timer import Timer

class Control:
    
    def __init__(self, window):
        self.worm_no=0
        self.worm=[]
        self.worms=[]
        self.weapon=1
        self.win=window
        self.world=[]
        self.events=[]
        self.rocket_types=["LASER","BAZOOKA"]
        self.timer=Timer(self)
        self.frame=Frame(self)
        self.alive_worms=[]
        self.game=[]
        self.music_control=[]
        
    def add_game(self,game):
        self.game=game
    
    def add_music_control(self, music_control):
        self.music_control=music_control
    
    def start_world(self,gamers):
        self.world = World(self.win, gamers)
        self.world.add_control(self)
        self.worm_no=0
        self.worms=self.world.worms
        self.worm=self.worms[self.worm_no]
        self.weapon=1
        self.alive_worms=[1]*len(gamers)
        for worm in self.worms:
            worm.add_control(self)
        #self.worm.color=(150,50,0)
        return self.world
    
    def change_worm(self):
        if self.timer.time_remaining==0:
            if self.worm.health>0:
                self.worm.color=(255,0,0)
            self.worm_no=(self.worm_no+1)%len(self.worms)
            self.worm=(self.worms[self.worm_no])
            if self.worm.health>0:
                self.worm.color=(150,50,0)
                self.worm.can_shoot=True
                self.worm.draw(self.win)
                self.worm.speed=100
                self.timer.set_timer(15)
        
    def change_weapon(self):
        self.worm.rocket_type=(self.worm.rocket_type+1)%2
            
    def change_coordinates(self, x,y):
        return (x, self.win.get_height()-y)
        
    def write(self, text, color, x, y, size):
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, color)
        self.win.blit(text, self.change_coordinates(x,y))
    
    def end_of_turn(self):
        if self.timer.time_remaining==0:
            self.worm.speed=0
            self.worm.can_shoot=False
            
    #def over(self):
        #self.frame.winner()
    
    def process_events(self, time_delta, events, worm):
        self.worms[worm].process_events(time_delta, events, self.world, self.world.terrain)
        

    def draw_pointer(self):
        x=self.change_coordinates(self.worm.x,self.worm.y)[0]
        y=self.change_coordinates(self.worm.x,self.worm.y)[1]
        points=[[x, y-40], [x-20, y-60], [x+20, y-60]]
        color=(247,240,25)
        pygame.draw.polygon(self.win,color,points,0)

