# -*- coding: utf-8 -*-

import pygame

class Rocket:
    SPEED = 100
    
    def __init__(self, x, y, o,type):
        self.x = x
        self.y = y
        self.t = 0
        self.orientation = o
        self.type=type
        
    def get_pos(self):
        t = self.t * Rocket.SPEED
        x = self.x + self.orientation * t
        y = self.y - 0.005*t*t + t
        return (x, y)
        
    def process_events(self, time_delta, world, terrain):
        self.t += time_delta;
        (x, y) = self.get_pos()
        if terrain.get_level(int(x)) > y:
            world.remove_rocket(self)
            world.explode(x, y)

    def draw(self, window):
        (x, y) = self.get_pos()
        if self.type==1:
            pygame.draw.circle(window, (255,0,0), (int(x), window.get_height() - int(y)), 2)
        elif self.type==2:
            pygame.draw.circle(window, (0,255,0), (int(x), window.get_height() - int(y)), 2)