# -*- coding: utf-8 -*-
 
import pygame
import time

from control import Control
from game import Game
from start_window import Start_Window

pygame.init()

win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("The game")

prev_time = time.time()

control=Control(win)
game=Game(control)
gamers=("Kasia", "Piotr")
high_scores=[]
start_window=Start_Window(high_scores, win, control)

while start_window.running:
    start_window.run(prev_time)
    prev_time=start_window.time

game.start(gamers)

while game.running:
    game.run(prev_time)
    prev_time=game.time

pygame.quit()
