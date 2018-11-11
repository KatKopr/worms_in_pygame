#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Control:
    def __init__(self, worms, worm, weapon, window):
        self.worm=worm
        self.weapon=weapon
        self.worms=worms
        self.win=window
        worms[worm].color=(150,50,0)
        #self.weapon_types=(1: "rocket", 2: "bazooka", 3: "granade")
    def change_worm(self):
        self.worms[self.worm].color=(255,0,0)
        self.worm=(self.worm+1)%len(self.worms)
        self.worms[self.worm].color=(150,50,0)
        self.worms[self.worm].draw(self.win)
    def change_weapon(self):
        if self.worms[self.worm].rocket_type==1:
            self.worms[self.worm].rocket_type=2
        else:
            self.worms[self.worm].rocket_type=1

