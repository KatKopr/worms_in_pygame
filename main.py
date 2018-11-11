# -*- coding: utf-8 -*-
 
import pygame
import time

from world import World
from control import Control
from game import Game

pygame.init()

win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("The game")
prev_time = time.time()
#world = World(win)

#worm=0
#rocket=1
control=Control(win)
game=Game(control)
gamers=("Kasia", "Piob")
game.start(gamers)
while game.running:
    game.run(prev_time)
    prev_time=game.time

pygame.quit()
