import sys 

import pygame 
from ship import Ship

def check_events(ship:Ship):
    '''Responde to press keys and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()      
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    '''React to the pressin on the key'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    '''React to the pressin on the key'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False    
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False   

def update_screen(ai_settings, screen, ship):
    '''Att images on the screen and altern to the new screen'''
    screen.fill(ai_settings.bg_color)
    ship.blitme()


    pygame.display.flip()