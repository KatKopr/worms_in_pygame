# -*- coding: utf-8 -*-

import pygame

from worm import Worm
from terrain import Terrain
from rocket import Rocket

class World:
    def __init__(self, window, gamers):
        self.terrain = Terrain(1200)
        self.worms=[]
        self.gamers=gamers
        for i in range(len(gamers)):
            self.worms += [Worm(300+i*200, self.terrain.get_level(300+i*200), gamers[i])]
        self.rockets = []
        self.window=window
        self.control = []
        
    def add_rocket(self, r):
        self.rockets.append(r)
        
    def remove_rocket(self, r):
        self.rockets = []
    
    def add_control(self, control):
        self.control=control

    def process_events(self, time_delta, events, worm):
        self.worms[worm].process_events(time_delta, events, self, self.terrain)
        for r in self.rockets:
            r.process_events(time_delta, self, self.terrain)
        
    def explode(self, x, y):
        self.terrain.explode(x, y)
        for w in self.worms:
            w.explode(x, y, self.terrain, self)
        
    def draw(self, window):
        self.terrain.draw(window)
        for w in self.worms:
            w.draw(window)
        for r in self.rockets:
            r.draw(window)
        #self.write("Test!", (0,255,0), 100,100)
        #self.write("You are dead!", (255,0,0), worm.x-30, self.window.get_height-worm.y-30)
        #self.write("You are dead!", (0,255,0), 100,100)