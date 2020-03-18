import pygame
import sys

from classes import *
from functions import *

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
grey = (230, 230, 230)

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

screen_dict = {
    'width' : screen_width,
    'height' : screen_height,
    'surface' : screen,
    'bg_color' : (230, 230, 230),
    }

pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()

player_ship = Ship(screen_dict)
enemy = Alien()
enemy.generate_aliens(screen_dict)

while True:

    key = check_event()

    player_ship.move(key, screen_dict)
    enemy.move(screen_dict)

    player_ship.bullet.bullets = enemy.check_bullet(player_ship.bullet.bullets)

    draw_game_window(screen_dict, player_ship, enemy)
    clock.tick(30)
