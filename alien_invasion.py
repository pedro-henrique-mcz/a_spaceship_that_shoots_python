import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf

def run_game():

    pygame.init()

    ai_setting = Settings()

    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_setting)

    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_setting, screen, ship, aliens)

    while True:
        gf.check_events(ai_setting, screen, ship, bullets)

        if stats.game_activate:
            ship.update()
            gf.update_bullets(ai_setting, screen, ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_setting, screen, ship, aliens, bullets)
        
        
run_game()  