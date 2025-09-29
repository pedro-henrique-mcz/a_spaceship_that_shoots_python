import sys 

import pygame 
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    '''Responde to press keys and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                sys.exit()     

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''React to the pressin on the key'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Create a new bullets object and add to a array
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    '''React to the pressin on the key'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False    
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False   

def update_bullets(bullets):
    '''Att the bullets position to get rid old bullets'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings, screen, ship, alien,  bullets):
    '''Att images on the screen and altern to the new screen'''
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()

    pygame.display.flip()