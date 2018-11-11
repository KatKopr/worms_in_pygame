# -*- coding: utf-8 -*-

import pygame

from worm import Worm
from terrain import Terrain
from rocket import Rocket

class World:
    def __init__(self, window):
        self.terrain = Terrain(1200)
        self.worms = [Worm(300, self.terrain.get_level(300))]
        self.worms += [Worm(500, self.terrain.get_level(500))]
        self.worms += [Worm(700, self.terrain.get_level(700))]
        self.worms += [Worm(900, self.terrain.get_level(900),)]
        self.rockets = []
        self.window=window
        
    def add_rocket(self, r):
        self.rockets.append(r)
        
    def remove_rocket(self, r):
        self.rockets = []

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
    def dead(self, worm):
        worm.color=(255,255,255)
        worm.speed=0
        #self.write("You are dead!", (255,0,0), worm.x-30, self.window.get_height-worm.y-30)
        #self.write("You are dead!", (0,255,0), 100,100)
    def write(self, text, color, x, y):
        font = pygame.font.Font(None, 15)
        text = font.render(text, 1, color)
        self.window.blit(text, (x, y))