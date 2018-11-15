# -*- coding: utf-8 -*-

import pygame

class Rocket:
    SPEED = 80
    
    def __init__(self, x, y, o, type):
        self.x = x
        self.y = y
        self.t = 0
        self.orientation = o
        self.type=type
        
    def get_pos(self):
        t = self.t * (Rocket.SPEED + 20*self.type)
        x = self.x + self.orientation * t
        if self.type==0:
            y = self.y+2
        else:
            y = self.y - 0.005*t*t + t
        return (x, y)
        
    def process_events(self, worm, time_delta, world, terrain):
        self.t += time_delta - self.type*time_delta*0.5;
        (x, y) = self.get_pos()
        if terrain.get_level(int(x)) > y:
            worm.remove_rocket(self)
            world.explode(x, y, self.type)

    def draw(self, window):
        #(x, y) = self.get_pos()
        (x,y)=(int(self.get_pos()[0]),window.get_height() - int(self.get_pos()[1]))
        if self.type==0:
            #pygame.draw.circle(window, (255,0,0), (int(x), window.get_height() - int(y)), 2)
            pygame.draw.line(window, (0,255,0), (x,y), (x+2,y))
        elif self.type==1:
            pygame.draw.circle(window, (255,0,0), (x,y), 4)