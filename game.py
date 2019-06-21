import sys
import pygame
from settings import Settings as set
from ship import Ship
from pygame.sprite import Group
import game_function as gf
from alien import Alien

def run_game():
    pygame.init()
    ai_settings=set()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()
    gf.create_fleet(ai_settings,screen,aliens)
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        

run_game()
