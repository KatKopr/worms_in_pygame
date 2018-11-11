#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
from world import World
from frame import Frame

class Control:
    
    def __init__(self, window):
        self.worm_no=0
        self.worm=[]
        self.worms=[]
        self.weapon=1
        self.win=window
        self.world=[]
        self.events=[]
        self.frame=Frame(self)
    def start_world(self,gamers):
            self.world = World(self.win, gamers)
            self.world.add_control(self)
            self.worm_no=0
            self.worm=self.world.worms[self.worm_no]
            self.weapon=1
            self.worms=self.world.worms
            for worm in self.worms:
                worm.add_control(self)
            self.worm.color=(150,50,0)
            return self.world
    def change_worm(self):
        if self.worm.health>0:
            self.worm.color=(255,0,0)
        self.worm_no=(self.worm_no+1)%len(self.worms)
        self.worm=(self.worms[self.worm_no])
        self.worm.color=(150,50,0)
        self.worm.draw(self.win)
    def change_weapon(self):
        if self.worm.rocket_type==1:
            self.worm.rocket_type=2
        else:
            self.worm.rocket_type=1
            
    def change_coordinates(self, x,y):
        return (x, self.win.get_height()-y)
        
    def write(self, text, color, x, y, size):
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, color)
        self.win.blit(text, self.change_coordinates(x,y))
        

                
