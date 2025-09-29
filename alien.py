import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class taht represent only one alien of the trop'''

    def __init__(self, ai_settings, screen):
        '''Start a alien and define his initial position'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('img/alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        '''Draw a alien in his initial position'''
        self.screen.blit(self.image, self.rect)

    