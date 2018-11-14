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
        self.rockets.append(r)
        
    def remove_rocket(self,r):
        self.rockets = []
    
    def rocket_sound(self):
        if self.rocket_type==0:
            fire = pygame.mixer.Sound("fire1.wav")
        elif self.rocket_type==1:
            fire = pygame.mixer.Sound("fire2.wav")
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
                self.rocket_sound()
        for r in self.rockets:
            r.process_events(self, time_delta, world, terrain)
            
    def explode(self, x, y, terrain, world):
        p = max(0, 40 - abs(self.x-x) - abs(self.y-y))
        p = 0.5*p
        self.health = max(0, self.health - p / 100.0)
        if self.health==0:
            #self.control.add_events("dead")
            self.dead()
        self.fall(terrain)

    def draw(self, window):
        #pygame.draw.circle(window, self.color, (self.x, window.get_height() - self.y), 5)
        self.control.win.blit(self.graphic, (self.x-10, window.get_height() - self.y - 30))
        pygame.draw.rect(window, (255,0,0), (self.x-15, window.get_height() - self.y-30, 30, 5))
        pygame.draw.rect(window, (0,255,0), (self.x-15, window.get_height() - self.y-30, int(30*self.health), 5))
        for r in self.rockets:
            r.draw(window)
        #pygame.draw.line(window, (255,0,255), (self.x, window.get_height() - self.y), (self.x + self.orientation * 20, window.get_height() - self.y - 20))
    
    def fall(self, terrain):
        self.y=int(terrain.get_level(self.x))
        
    def dead(self):
        self.color=(255,255,255)
        self.speed=0
        self.can_shoot=False
        self.control.alive_worms[self.number]=0
        #print(sum(self.control.alive_worms))
        #if sum(self.control.alive_worms)<2:
            #self.control.over()
        #self.write("You are dead", (0,255,0))
        
    def write(self, text, color):
        self.control.write(text, color, self.x, self.y)
    
        

