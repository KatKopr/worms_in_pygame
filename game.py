#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import time

class Game:
    
    def __init__(self, control):
        self.control=control
        self.world=[]
        self.running=[]
        self.time=[]
    
    def start(self, gamers):
        self.world=self.control.start_world(gamers)
        self.running=True
    
    def run(self, prev_time):
        pygame.time.delay(20)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                self.control.change_worm()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.control.change_weapon()
        next_time = time.time()            
        self.world.process_events(next_time - prev_time, events, self.control.worm_no)
        self.time = next_time

        self.control.win.fill((0,0,0))
        self.world.draw(self.control.win)
        #control.process_events()
        pygame.display.update()
        
    def quit(self):
        self.running=False
        

