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
        self.timer=Timer(self)
        self.frame=Frame(self)
        self.alive_worms=[]
        self.game=[]
        
    def add_game(self,game):
        self.game=game
    
    def start_world(self,gamers):
        self.world = World(self.win, gamers)
        self.world.add_control(self)
        self.worm_no=0
        self.worm=self.world.worms[self.worm_no]
        self.weapon=1
        self.worms=self.world.worms
        self.alive_worms=[1]*len(gamers)
        for worm in self.worms:
            worm.add_control(self)
        self.worm.color=(150,50,0)
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
    
    def end_of_turn(self):
        if self.timer.time_remaining==0:
            self.worm.speed=0
            self.worm.can_shoot=False
            
    def over(self):
        self.frame.winner()
        pygame.time.delay(1000)
        self.game.quit()

                
