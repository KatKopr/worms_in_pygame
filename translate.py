#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Translate:
    def __init__(self, window):
        self.window=window
    
    def coordinates(self, x, y):
        return (x, self.window.get_height()-y)
