# -*- coding: utf-8 -*-

import pygame

from worm import Worm
from terrain import Terrain
#from rocket import Rocket

class World:
    def __init__(self, window, gamers):
        self.terrain = Terrain(1200)
        self.worms=[]
        self.gamers=gamers
        for i in range(len(gamers)):
            self.worms += [Worm(300+i*200, self.terrain.get_level(300+i*200)+5, gamers[i],i)]
        self.rockets = []
        self.window=window
        self.control = []
    
    def add_control(self, control):
        self.control=control
        
    def explode(self, x, y, type):
        self.terrain.explode(x, y, type)
        if self.control.music_control.playing:
            self.explosion_sound(type)
        for w in self.worms:
            w.explode(x, y, self.terrain, self)
        
    def draw(self, window):
        self.terrain.draw(window)
        for w in self.worms:
            w.draw(window)
        self.control.frame.draw()
        self.control.draw_pointer()

    def explosion_sound(self, type):
        if type==0:
            fire = pygame.mixer.Sound("explosion1.wav")
        if type==1:
            fire = pygame.mixer.Sound("explosion2.wav")
        if type==2:
            fire = pygame.mixer.Sound("explosion3.wav")
        pygame.mixer.Sound.play(fire,loops=0)