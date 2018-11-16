#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import time

from options_control import Options_Control

class Start_Window:
    
    def __init__(self, window, control):
        self.gamers=[]
        self.gamers2=[]
        self.sound=True
        self.running=True
        self.window=window
        self.options=[]
        self.option_no=0
        self.y_start=100
        self.x_start=200
        self.control=control
        self.music_control=self.control.music_control
        self.options_control=Options_Control(self.options, self.control, self)
        self.options_control.starting_kit()
    
    def run(self, prev_time):
        pygame.time.delay(20)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.quit()
        next_time = time.time()            
        self.process_events(next_time - prev_time, events)
        self.time = next_time
        self.window.fill((0,0,0))
        self.set_frame()
        self.options_control.display_options()
        self.draw_pointer()
        pygame.display.update()
    
    def process_events(self, time_delta, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.options_control.process_option()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.options_control.change_option("next")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.options_control.change_option("previous")
    
    def quit(self):
        self.running=False
    
    
    def set_frame(self):
        text="WELCOME TO THE GAME"
        text2="PRESS SPACE TO CHOOSE OPTION"
        color=(0,255,0)
        x=300
        y=self.control.change_coordinates(x,self.y_start)[1]
        self.write(text,color, x, y, 30)
        self.write(text2, color, x, y-50, 30)
    
    def write(self, text, color, x, y, size):
        font = pygame.font.Font(None, size)
        text = font.render(text, 1, color)
        self.window.blit(text, self.control.change_coordinates(x,y))
        
    def draw_pointer(self):
        x=self.x_start
        y=self.options[self.option_no].y-5
        y=self.control.change_coordinates(x,y)[1]
        points=[[x-10, y], [x-30, y+20], [x-30, y-20]]
        color=(247,240,25)
        pygame.draw.polygon(self.window,color,points,0)

