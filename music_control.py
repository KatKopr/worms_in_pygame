#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

class Music_Control:
    
    def __init__(self):
        self.playing=True
        pygame.mixer.music.load("music.ogg")
        pygame.mixer.music.set_volume(0.3)
    
    def play(self):
        pygame.mixer.music.play(loops=-1)
        self.playing=True
    
    def stop(self):
        pygame.mixer.music.pause()
        self.playing=False

        
    