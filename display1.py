#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Display:
    def __init__(self, control):
        self.control=control
        self.curr_window=[]
    
    def display_start(self):
        self.curr_window=Window(0)
