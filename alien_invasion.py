import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():

    pygame.init()

    ai_setting = Settings()

    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_setting, screen)
    bullets = Group()

    alien = Alien(ai_setting, screen)

    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting, screen, ship, alien, bullets)
        
run_game()  