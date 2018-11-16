# -*- coding: utf-8 -*-

import pygame
from rocket import Rocket
class Worm:
    
    def __init__(self, x, y, name, number):
        self.x = x
        self.y = y
        self.health = 0.8
        self.orientation = 1
        self.color=(255,0,0)
        self.rocket_type=0
        self.rockets=[]
        self.speed=100
        self.control=[]
        self.name=name
        self.can_shoot=True
        self.number=number
        self.graphic_right=pygame.image.load("cat_right.png")
        self.graphic_left=pygame.image.load("cat_left.png")
        self.graphic=self.graphic_right
        
    def add_control(self, control):
        self.control=control
    
    def add_rocket(self, r):
        if len(self.rockets) < 5:
            self.rockets.append(r)
        
    def remove_rocket(self,r):
        self.rockets.remove(r)
    
    def rocket_sound(self):
        if self.rocket_type==0:
            fire = pygame.mixer.Sound("fire1.wav")
        if self.rocket_type==1:
            fire = pygame.mixer.Sound("fire2.wav")
        if self.rocket_type==2:
            fire = pygame.mixer.Sound("fire3.wav")
        pygame.mixer.Sound.play(fire,loops=0, maxtime=500)
        
    def process_events(self, time_delta, events, world, terrain):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.orientation = -1
            self.x -= int(time_delta * self.speed)
            self.graphic=self.graphic_left
        if keys[pygame.K_RIGHT]:
            self.orientation = 1
            self.x += int(time_delta * self.speed)
            self.graphic=self.graphic_right
        self.y = int(terrain.get_level(self.x))
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == ord("r") and self.can_shoot:
                self.add_rocket(Rocket(self.x, self.y, self.orientation, self.rocket_type))
                if self.control.music_control.playing:
                    self.rocket_sound()
        for r in self.rockets:
            r.process_events(self, time_delta, world, terrain)
            
    def explode(self, x, y, terrain, world):
        p = max(0, 40 - abs(self.x-x) - abs(self.y-y))
        p = 0.5*p
        self.health = max(0, self.health - p / 100.0)
        if self.health==0:
            self.dead()
        self.fall(terrain)

    def draw(self, window):
        self.control.win.blit(self.graphic, (self.x-10, window.get_height() - self.y - 30))
        pygame.draw.rect(window, (255,0,0), (self.x-15, window.get_height() - self.y-30, 30, 5))
        pygame.draw.rect(window, (0,255,0), (self.x-15, window.get_height() - self.y-30, int(30*self.health), 5))
        for r in self.rockets:
            r.draw(window)
    
    def fall(self, terrain):
        a=0
        if self.control.worm_no!=self.number:
            print(self.number)
            a=1
        self.y=int(terrain.get_level(self.x))+5*a
        
    def dead(self):
        self.color=(255,255,255)
        self.speed=0
        self.can_shoot=False
        self.control.alive_worms[self.number]=0
        
    def write(self, text, color):
        self.control.write(text, color, self.x, self.y)
    
        

