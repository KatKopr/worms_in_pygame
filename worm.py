# -*- coding: utf-8 -*-

import pygame
from rocket import Rocket


class Worm:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 0.8
        self.orientation = 1
        self.color=(255,0,0)
        self.rocket_type=1
        self.speed=100
        
    def process_events(self, time_delta, events, world, terrain):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.orientation = -1
            self.x -= int(time_delta * self.speed)
        if keys[pygame.K_RIGHT]:
            self.orientation = 1
            self.x += int(time_delta * self.speed)
        self.y = int(terrain.get_level(self.x))
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == ord("r"):
                world.add_rocket(Rocket(self.x, self.y, self.orientation, self.rocket_type))

    def explode(self, x, y, terrain, world):
        p = max(0, 40 - abs(self.x-x) - abs(self.y-y))
        self.health = max(0, self.health - p / 100.0)
        if self.health==0:
            world.dead(self)
        self.fall(terrain)

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, window.get_height() - self.y), 5)
        pygame.draw.rect(window, (255,0,0), (self.x-15, window.get_height() - self.y-20, 30, 5))
        pygame.draw.rect(window, (0,255,0), (self.x-15, window.get_height() - self.y-20, int(30*self.health), 5))
        #pygame.draw.line(window, (255,0,255), (self.x, window.get_height() - self.y), (self.x + self.orientation * 20, window.get_height() - self.y - 20))
    
    def fall(self, terrain):
        self.y=int(terrain.get_level(self.x))
    
        

