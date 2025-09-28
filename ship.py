'''Ship Class Module'''
import pygame

class Ship():
    '''Ship Class'''
    def __init__(self, ai_settings, screen):
        '''Starts the spaceship 
        in a different initial position'''
        self.screen = screen
        self.ai_settings = ai_settings

        #Loads the sapceship image and gets it's rect
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Flags 
        self.moving_right = False
        self.moving_left = False

        #Start each new spaceship in the center 
        #of the bottom part of the screen

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

    def update(self):
        '''Att the ship's moviment'''
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_dactor
        if self.moving_left:
            self.center-= self.ai_settings.ship_speed_dactor

        self.rect.centerx = self.center
        
    def blitme(self):
        '''Draws the spaceship in the new position'''
        self.screen.blit(self.image, self.rect)