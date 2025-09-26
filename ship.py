'''Ship Class Module'''
import pygame

class Ship():
    '''Ship Class'''
    def __init__(self, screen):
        '''Starts the spaceship 
        in a different initial position'''
        self.screen = screen

        #Loads the sapceship image and gets it's rect
        self.image = pygame.image.load('img/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new spaceship in the center 
        #of the bottom part of the screen

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''Draws the spaceship in the new position'''
        self.screen.blit(self.image, self.rect)