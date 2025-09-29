import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A class which manager the bullets fired 
    by the ship'''

    def __init__(self, ai_setting, screen, ship):
        '''Create a object for the actual bullet fired
        by the ship'''

        super().__init__()
        self.screen = screen

        #Creating a rect for the bullet at (0,0) and, and then
        #define the correct position

        self.rect = pygame.Rect(0,0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top


        #Storage the bullet's position with a decimal value
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor


    def update(self):
        '''Move the bullet to the upper side of the screen'''
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        '''Draw the bullet in the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)