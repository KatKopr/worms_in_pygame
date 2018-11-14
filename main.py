# -*- coding: utf-8 -*-
 
import pygame
import time

from control import Control
from music_control import Music_Control
from game import Game
from start_window import Start_Window

pygame.init()

win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Cats")

prev_time = time.time()

control=Control(win)
game=Game(control)
control.add_game(game)
gamers=("Kasia", "Piotr")
high_scores=[]
start_window=Start_Window(high_scores, win, control)
music_control=Music_Control()
start_window.add_music_control(music_control)
music_control.play()

while start_window.running:
    start_window.run(prev_time)
    prev_time=start_window.time

while game.start_again:
    game.start(gamers)
    while game.running:
        game.run(prev_time)
        prev_time=game.time
    #print("koniec")
    #start_window.run(prev_time)
    

pygame.quit()
