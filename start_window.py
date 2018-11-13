#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import time

from option import Option

class Start_Window:
    
    def __init__(self, high_scores, window, control):
        self.gamers=[]
        self.sound=True
        self.running=True
        self.high_scores=high_scores
        self.window=window
        self.options=[]
        self.options.append(Option("START", 0 , 520))
        self.options.append(Option("SET NICKNAMES", 1, 480)) 
        self.options.append(Option("SOUND ON/OFF", 2, 440))
        self.options.append(Option("HIGH SCORES", 3, 400))
        self.option_no=0
        self.y_start=100
        self.x_start=200
        self.control=control
        
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
        self.display_options()
        self.draw_pointer()
        pygame.display.update()
    
    def process_events(self, time_delta, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.process_option()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.change_option("next")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.change_option("previous")
    
    def display_options(self):
        color=(0,255,0)
        x=self.x_start
        for option in self.options:
            self.write(option.name ,color, x, option.y, 30)
            
    def change_option(self, type):
        a=len(self.options)
        if type=="next":
            self.option_no = (self.option_no+1)%a
        else:
            self.option_no = (self.option_no-1)%a
        #y=self.y_start+100+40*self.option_no
        self.draw_pointer()
    
    def process_option(self):
        a=self.options[self.option_no].name
        if a == "START":
            self.quit()
        elif a == "SET NICKNAMES":
            pass
            #self.gamers.append(self.translate_input())
        elif a == "SOUND ON/OFF":
            self.sound_control()
        elif a == "HIGH SCORES":
            self.see_high_scores()
        
    def add_gamer(self, gamer):
        self.gamers+=gamer
    
    def sound_control(self):
        self.sound=not self.sound
    
    #def start_game(self):
    def quit(self):
        self.running=False
    
    def translate_input(events):
        name=""
        for event in events:
            if event.type == pygame.KEYDOWN and event.key != pygame.K_SPACE:
                name+=pygame.key.name(event.key)
        return name
    
    def see_high_scores(self):
        pass
    
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
        x=100
        y=self.options[self.option_no].y
        y=self.control.change_coordinates(x,y)[1]
        points=[[x-10, y], [x-30, y+20], [x-30, y-20]]
        color=(247,240,25)
        pygame.draw.polygon(self.window,color,points,0)