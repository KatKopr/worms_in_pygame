# -*- coding: utf-8 -*-
import pygame
import random

class Terrain():
    def __init__(self, width):
        self.level = []
        self.last=250
        self.sign=1;
        for i in range(width):
            if self.last<400 and self.last>100:
                if i%50!=0:
                    lvl=self.last+2*self.sign
                else:
                    lvl=self.last+2*self.sign
                    #lvl=random.randint(self.last-5,self.last+5)
                    self.sign=random.choice((-1,1))
            else:
                self.sign=-self.sign
                lvl=self.last+2*self.sign
            self.level.append(lvl)
            self.last=lvl
    
    def draw(self, window):
        for i in range(len(self.level)):
            pygame.draw.line(window, (0,0,255), (i, window.get_height()), (i, window.get_height() - self.level[i]))
        
    def explode(self, x, y, type):
        z=20*type
        for i in range(len(self.level)):
            p = max(0, 20+z - abs(x-i))
            self.level[i] -= max(0, min(2*p, self.level[i]-(y-p)))
       
        
    def get_level(self, x):
        if x < len(self.level):
            return self.level[x]
        else:
            return self.level[len(self.level)-1]
    
    