# -*- coding: utf-8 -*-
 
import pygame
import time
from world import World
from control import Control

pygame.init()

win = pygame.display.set_mode((1200,800))

pygame.display.set_caption("The game")

world = World(win)
world.write("Test!", (0,255,0), 100,100)
prev_time = time.time()
worm=0
rocket=1
control=Control(world.worms, worm, rocket,win)
run=True
while run:
    pygame.time.delay(20)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            control.change_worm()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            control.change_weapon()
    next_time = time.time()            
    world.process_events(next_time - prev_time, events, control.worm)
    prev_time = next_time

    win.fill((0,0,0))
    world.draw(win)
    pygame.display.update()

pygame.quit()
