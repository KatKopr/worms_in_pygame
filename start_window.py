#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Start_Window:
    
    def __init__(self):
        self.gamers=[]
        self.sound=True
        self.game_running=False
        
    def add_gamer(self, gamer):
        self.gamers+=gamer
    
    def sound_control(self):
        self.sound=not self.sound
    
    def start_game(self):
        self.game_running=True
