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
        self.gamers=[]
        self.start_again=False
    
    def start(self, gamers):
        self.world=self.control.start_world(gamers)
        self.gamers=gamers
        self.running=True
        self.control.add_game(self)
    
    def run(self, prev_time):
        self.start_again=False
        pygame.time.delay(20)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                self.control.change_worm()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.control.change_weapon()
            elif event.type == pygame.KEYDOWN:
            #and event.key == pygame.K_p:
                self.control.timer.change_state()
            if event.type == self.control.timer.COUNTDOWN:
                self.control.timer.countdown()
            #self.control.winner=self.control.alive_worms[0].name
            #self.quit
        next_time = time.time()            
        self.control.process_events(next_time - prev_time, events, self.control.worm_no)
        self.time = next_time
        self.control.win.fill((0,0,0))
        self.world.draw(self.control.win)
        #control.process_events()
        pygame.display.update()
        
    def quit(self):
        self.running=False
    
    def over(self):
        events=pygame.event.get()
        for event in events:
            #print("prawie koniec1")
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                self.start_again=True
                #print("prawie koniec")
                self.quit()
            
        

