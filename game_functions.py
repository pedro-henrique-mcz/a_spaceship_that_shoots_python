import sys 

import pygame 

def check_events():
    '''Responde to press keys and mouse events'''
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
