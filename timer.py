#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

class Timer:
    COUNTDOWN=pygame.USEREVENT + 1
    def __init__(self, control):
        self.control=control
        self.player_no=self.control.worm_no
        self.time_remaining=15
        self.stop=True
    
    def set_timer(self, time):
        self.time_remaining=time
    
    def start_timer(self):
        self.stop=False
        pygame.time.set_timer(self.COUNTDOWN,1000)
    
    def stop_timer(self):
        self.stop=True
    
    def change_state(self):
        if self.stop==True:
            self.start_timer()
        else:
            self.stop_timer
            
    def countdown(self):
        if self.time_remaining>0:
            self.time_remaining-=1
        else:
            self.stop=True
            self.control.end_of_turn()
        

