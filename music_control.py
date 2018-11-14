#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

class Music_Control:
    
    def __init__(self):
        self.playing=True
        pygame.mixer.music.load("music.ogg")
    
    def play(self):
        pygame.mixer.music.play(loops=-1)
    
    def stop(self):
        pygame.mixer.music.stop()

        
    